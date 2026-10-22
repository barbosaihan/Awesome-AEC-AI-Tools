#!/usr/bin/env python3
"""Validate *new regressions* in the two Markdown catalogs against Git refs."""

import argparse
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import urlsplit

FILES = ('README.md', 'README.pt-BR.md')
LINK = re.compile(r'^\[([^]]+)\]\(([^)]+)\)')
SEPARATOR = re.compile(r'^:?-{3,}:?$')


@dataclass(frozen=True)
class Entry:
    category: str
    name: str
    url: str
    line: int


def cells(line):
    """Split a Markdown table row, ignoring escaped pipes and inline code pipes."""
    text = line.strip()
    if not text.startswith('|'):
        return None
    result, part, ticks = [], '', 0
    for index, char in enumerate(text):
        if char == '`' and (index == 0 or text[index - 1] != '\\'):
            ticks ^= 1
        if char == '|' and not ticks and (index == 0 or text[index - 1] != '\\'):
            result.append(part.strip())
            part = ''
        else:
            part += char
    result.append(part.strip())
    if result[0] != '' or result[-1] != '':
        return None
    return result[1:-1]


def valid_url(url):
    if re.search(r'\s|[<>\\]', url):
        return False
    try:
        parsed = urlsplit(url)
        _ = parsed.port  # Access rejects non-numeric and out-of-range ports.
        return (parsed.scheme in ('http', 'https') and bool(parsed.hostname)
                and parsed.username is None and parsed.password is None)
    except ValueError:
        return False


def scan(text):
    """Return issue signatures and catalog entries; signatures omit line numbers."""
    issues = Counter()
    entries = []
    lines = text.splitlines()
    if not lines or not re.match(r'^# [^#\s].*$', lines[0]):
        issues[('H1', 'primeira linha sem H1 íntegro')] += 1
    category, fenced, width, header = '', False, None, None
    for number, line in enumerate(lines, 1):
        if re.match(r'^\s*(`{3,}|~{3,})', line):
            fenced = not fenced
            continue
        if fenced:
            continue
        if line.startswith(('## ', '### ')):
            category = line.lstrip('#').strip()
            width, header = None, None
            continue
        row = cells(line)
        if row is None:
            if not line.strip():
                width, header = None, None
            continue
        if width is None:
            width, header = len(row), row
            continue
        if all(SEPARATOR.fullmatch(cell) for cell in row) and len(row) == width:
            continue
        if number > 1 and cells(lines[number - 2]) == header and not all(SEPARATOR.fullmatch(cell) for cell in row):
            issues[('tabela', category, line.strip())] += 1
            continue
        if len(row) != width:
            issues[('tabela', category, line.strip())] += 1
            continue
        if not row:
            continue
        match = LINK.match(row[0])
        if not match:
            if row[0].startswith('['):
                issues[('entrada', category, line.strip())] += 1
            continue
        name, url = match.groups()
        entries.append(Entry(category, name, url, number))
        if not valid_url(url):
            issues[('URL', category, name, url)] += 1
        if len(row) < 2 or not row[1].strip():
            issues[('descrição', category, name, url)] += 1
    duplicates = Counter((entry.category, entry.url) for entry in entries)
    for (section, url), count in duplicates.items():
        if count > 1:
            issues[('duplicada', section, url)] += count - 1
    return issues, entries


def validate(base, head):
    """Report new defects only; compare added URLs and adjacent order per language."""
    findings, additions, url_counts = [], {}, {}
    for filename in FILES:
        old_issues, old_entries = scan(base[filename])
        new_issues, new_entries = scan(head[filename])
        for issue, count in (new_issues - old_issues).items():
            findings.append(f'{filename}: {issue[0]}: {issue[1:]} ({count})')
        old_urls = Counter(item.url for item in old_entries)
        new_urls = Counter(item.url for item in new_entries)
        url_counts[filename] = (old_urls, new_urls)
        additions[filename] = new_urls - old_urls
        # Preserve legacy inversions: only an adjacency involving a new URL can fail.
        for left, right in zip(new_entries, new_entries[1:]):
            if left.category != right.category:
                continue
            if not (additions[filename][left.url] or additions[filename][right.url]):
                continue
            if left.name.casefold() > right.name.casefold():
                findings.append(f'{filename}:{right.line}: ordem: {left.name} antes de {right.name}')
    old_en, new_en = url_counts[FILES[0]]
    old_pt, new_pt = url_counts[FILES[1]]
    for url in (old_en | old_pt | new_en | new_pt):
        before = old_en[url] - old_pt[url]
        after = new_en[url] - new_pt[url]
        if after and (abs(after) > abs(before) or (before and (after > 0) != (before > 0))):
            findings.append(f'paridade: {url} desequilíbrio EN-PT {before:+d} → {after:+d}')
    return findings


def git_file(ref, filename):
    # No shell; filename is a constant and refs come from trusted workflow inputs.
    return subprocess.check_output(['git', 'show', f'{ref}:{filename}'], text=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-ref', required=True, help='Git base commit/ref for differential checks')
    parser.add_argument('--head-ref', help='Git head commit/ref; defaults to local working tree')
    args = parser.parse_args()
    try:
        head = {f: git_file(args.head_ref, f) if args.head_ref else Path(f).read_text(encoding='utf-8') for f in FILES}
        base = {f: git_file(args.base_ref, f) for f in FILES}
        problems = validate(base, head)
    except (OSError, subprocess.CalledProcessError, UnicodeError) as exc:
        print(f'Erro ao ler catálogos: {exc}', file=sys.stderr)
        return 2
    if problems:
        for problem in problems:
            print(problem, file=sys.stderr)
        return 1
    print('Catálogos: sem regressões mecânicas detectadas.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
