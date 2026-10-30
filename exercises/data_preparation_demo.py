"""Invented-only Module 2 demo. No input files, network or anonymisation claim.
Run: python3 data_preparation_demo.py
All values are constructed here, not sampled/fitted from real records.
"""


def invented_rows():
    """A shareable toy schema, missing score, and deliberately unusual score."""
    return [
        {'name': 'Alex Example', 'age': 43, 'group': 'A', 'score': 2},
        {'name': 'Blair Example', 'age': 31, 'group': 'A', 'score': None},
        {'name': 'Casey Example', 'age': 52, 'group': 'A', 'score': 6},
        {'name': 'Drew Example', 'age': 24, 'group': 'B', 'score': 10},
        {'name': 'Ellis Example', 'age': 67, 'group': 'B', 'score': 14},
        {'name': 'Fran Example', 'age': 89, 'group': 'C', 'score': 100},
    ]


def minimise(rows):
    """Keep only fields needed for group means and missing counts."""
    return [{'group': row['group'], 'score': row['score']} for row in rows]


def summarise(rows):
    """Return group -> (all rows, observed, missing, mean or None)."""
    groups = {}
    for row in rows:
        if not isinstance(row['group'], str):
            raise ValueError('group must be text')
        score = row['score']
        if score is not None and type(score) not in (int, float):
            raise ValueError('score must be numeric or None')
        groups.setdefault(row['group'], []).append(score)
    result = {}
    for group, values in sorted(groups.items()):
        observed = [value for value in values if value is not None]
        result[group] = (len(values), len(observed), len(values) - len(observed),
                         sum(observed) / len(observed) if observed else None)
    return result


def main():
    before = invented_rows()
    after = minimise(before)
    assert all(set(row) == {'group', 'score'} for row in after)
    assert summarise(before) == summarise(after)
    assert sum(row['score'] is None for row in before) == sum(row['score'] is None for row in after)
    print('INVENTED ONLY; no privacy certification')
    for label, rows in [('before', before), ('after', after)]:
        missing = sum(row['score'] is None for row in rows)
        print(f'{label}: rows={len(rows)} missing={missing} numeric={len(rows)-missing}')
        for group, (n, observed, absent, mean) in summarise(rows).items():
            value = 'NA' if mean is None else f'{mean:g}'
            print(f'{label} {group}: n={n} observed={observed} missing={absent} mean={value}')
    print('checks: columns, types, missingness, question preserved')
    print('release: NOT ASSESSED; C reveals one value')


if __name__ == '__main__':
    main()
