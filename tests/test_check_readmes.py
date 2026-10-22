import unittest
from pathlib import Path
import subprocess

from scripts.check_readmes import scan, validate


EN = 'README.md'
PT = 'README.pt-BR.md'


def page(rows='', h1='# Catalog', category='### Category'):
    return f'{h1}\n\n{category}\n\n| Tool | Description |\n|---|---|\n{rows}'


def row(name, url='https://example.org/tool', description='Useful tool'):
    return f'| [{name}]({url}) | {description} |\n'


def check(base_en, base_pt, head_en, head_pt):
    return validate({EN: base_en, PT: base_pt}, {EN: head_en, PT: head_pt})


class CatalogTests(unittest.TestCase):
    def test_clean_pair(self):
        base = page()
        self.assertEqual([], check(base, base, page(row('Alpha')), page(row('Alpha'))))

    def test_legacy_issues_not_rejected_without_new_regression(self):
        old = page(row('Zulu', 'file:///x', '') + row('Alpha', 'file:///x', ''))
        self.assertEqual([], check(old, old, old, old))

    def test_h1_inline_badge_without_space_is_valid(self):
        old = page()
        badge = page(h1='# Catalog![badge](https://example.org/badge)')
        self.assertEqual([], check(old, old, badge, old))

    def test_existing_spaced_badge_in_h1_is_valid(self):
        old = page(h1='# Catalog [![badge](https://example.org/badge.svg)](https://example.org)')
        self.assertNotIn('H1', [issue[0] for issue in scan(old)[0]])
        self.assertIn('H1', str(check(old, old, page(h1='<img src="x" />' + old.splitlines()[0]), old)))

    def test_missing_h1_first_line_rejected(self):
        old = page()
        self.assertIn('H1', str(check(old, old, '\n' + old, old)))

    def test_missing_portuguese_entry(self):
        old = page()
        self.assertIn('paridade', str(check(old, old, page(row('New')), old)))

    def test_changed_url_requires_both_languages(self):
        old = page(row('One', 'https://example.org/old'))
        changed = page(row('One', 'https://example.org/new'))
        self.assertIn('paridade', str(check(old, old, changed, old)))

    def test_removing_entry_from_only_one_language_breaks_parity(self):
        old = page(row('Alpha'))
        self.assertIn('paridade', str(check(old, old, page(), old)))

    def test_removing_entry_from_both_languages_keeps_parity(self):
        old = page(row('Alpha'))
        self.assertEqual([], check(old, old, page(), page()))

    def test_legacy_parity_debt_unchanged_is_not_new_error(self):
        en = page(row('Alpha'))
        pt = page()
        self.assertEqual([], check(en, pt, en, pt))

    def test_reducing_legacy_parity_debt_is_not_new_error(self):
        en = page(row('Alpha'))
        pt = page()
        self.assertEqual([], check(en, pt, page(), pt))

    def test_reversing_legacy_parity_debt_is_new_error(self):
        en = page(row('Alpha'))
        pt = page()
        self.assertIn('paridade', str(check(en, pt, page(), page(row('Alpha')))))

    def test_duplicate_within_category(self):
        old = page(row('Alpha'))
        head = page(row('Alpha') + row('Beta'))
        self.assertIn('duplicada', str(check(old, old, head, head)))

    def test_same_url_in_separate_categories_is_not_duplicate(self):
        old = page()
        head = old + '\n### Other\n\n| Tool | Description |\n|---|---|\n' + row('Beta')
        head = head.replace('|---|---|\n', '|---|---|\n' + row('Alpha'), 1)
        self.assertEqual([], check(old, old, head, head))

    def test_missing_description(self):
        old = page()
        head = page(row('Alpha', description='  '))
        self.assertIn('descrição', str(check(old, old, head, head)))

    def test_invalid_uri_schemes_and_empty_host(self):
        old = page()
        for url in ('javascript:alert', 'file:///tmp/x', 'https:///path', 'ftp://example.org'):
            with self.subTest(url=url):
                head = page(row('Alpha', url))
                self.assertIn('URL', str(check(old, old, head, head)))

    def test_invalid_port_and_userinfo(self):
        old = page()
        for url in ('https://example.org:bad/path', 'https://example.org:65536/',
                    'https://user:pass@example.org/', 'https://:password@example.org/'):
            with self.subTest(url=url):
                head = page(row('Alpha', url))
                self.assertIn('URL', str(check(old, old, head, head)))

    def test_cli_requires_base_ref(self):
        result = subprocess.run(['python3', 'scripts/check_readmes.py'],
                                capture_output=True, text=True, check=False)
        self.assertNotEqual(0, result.returncode)
        self.assertIn('--base-ref', result.stderr)

    def test_workflow_bootstraps_from_event_but_dispatch_uses_main(self):
        workflow = Path('.github/workflows/catalog-validation.yml').read_text()
        self.assertIn("ref: ${{ github.event_name == 'workflow_dispatch' && 'main' || github.sha }}", workflow)
        self.assertIn('persist-credentials: false', workflow)
        self.assertIn('contents: read', workflow)

    def test_new_item_out_of_order(self):
        old = page(row('Alpha') + row('Zulu', 'https://example.org/z'))
        head = page(row('Alpha') + row('Zulu', 'https://example.org/z') + row('Beta', 'https://example.org/b'))
        self.assertIn('ordem', str(check(old, old, head, head)))

    def test_legacy_out_of_order_allows_new_correctly_placed_item(self):
        old = page(row('Zulu', 'https://example.org/z') + row('Alpha'))
        head = page(row('Zulu', 'https://example.org/z') + row('Alpha') + row('Beta', 'https://example.org/b'))
        self.assertEqual([], check(old, old, head, head))

    def test_bad_table_column_count(self):
        old = page()
        bad = page('| [Alpha](https://example.org/tool) |\n')
        self.assertIn('tabela', str(check(old, old, bad, bad)))

    def test_bad_table_separator(self):
        old = page()
        bad = old.replace('|---|---|', '|---|broken|')
        self.assertIn('tabela', str(check(old, old, bad, bad)))

    def test_escaped_pipes_and_inline_code(self):
        old = page()
        head = page(row('Alpha', description=r'Pipe \| and `a|b` work'))
        self.assertEqual([], check(old, old, head, head))

    def test_fenced_examples_are_ignored(self):
        old = page()
        head = old + '\n```markdown\n| [Evil](file:///tmp/x) |\n```\n'
        self.assertEqual([], check(old, old, head, head))

    def test_table_with_three_columns(self):
        old = page()
        head = old + '\n### Three\n\n| Tool | Description | Language |\n|---|---|---|\n| [Beta](https://example.org/b) | Fine | Python |\n'
        self.assertEqual([], check(old, old, head, head))

    def test_new_fault_on_unchanged_legacy_is_caught(self):
        old = page(row('Old', 'file:///x'))
        head = old + row('New', 'javascript:evil')
        self.assertIn('URL', str(check(old, old, head, head)))


if __name__ == '__main__':
    unittest.main()
