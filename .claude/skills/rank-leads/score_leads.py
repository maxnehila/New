#!/usr/bin/env python3
"""Base-score sales leads out of 100 for Rippling fit.

Usage: python3 score_leads.py <input.csv> <output.csv>

Rubric: size fit (40) + industry fit (30) + CRM tier (20) + reachability (10).
Column names are matched fuzzily; adapt COLUMN_ALIASES for unusual exports.
"""
import sys
import pandas as pd

COLUMN_ALIASES = {
    'name':      ['account name', 'company', 'company name', 'account', 'name'],
    'employees': ['no. of employees', 'employees', 'employee count', 'headcount', 'size', '# employees'],
    'website':   ['website', 'domain', 'url', 'company website'],
    'industry':  ['industry', 'sector', 'vertical'],
    'tier':      ['core account fit tier', 'tier', 'fit tier', 'account tier'],
    'linkedin':  ['account linkedin url', 'linkedin url', 'linkedin', 'company linkedin'],
    'li_id':     ['linkedin company id', 'li company id'],
    'state':     ['billing state/province', 'state', 'state/province', 'billing state'],
}

HIGH_KEYWORDS = ['software', 'technology', 'it ', 'it service', 'internet', 'fintech',
                 'biotech', 'pharma', 'saas', 'data', 'security', 'consult', 'financial',
                 'staffing', 'venture', 'capital', 'investment', 'insurance', 'accounting',
                 'advertis', 'marketing', 'telecom', 'e-learning', 'research', 'design',
                 'media', 'aerospace', 'medical equipment', 'medical device', 'robotics']
LOW_KEYWORDS = ['education', 'school', 'religio', 'non-profit', 'nonprofit', 'government',
                'banking', 'civic', 'philanthropic', 'museum', 'librar', 'armed forces',
                'public policy']


def find_col(df, key):
    for alias in COLUMN_ALIASES[key]:
        for c in df.columns:
            if c.strip().lower() == alias:
                return c
    return None


def size_score(n):
    if pd.isna(n):
        return 0
    if 50 <= n <= 250:
        return 40
    if 25 <= n < 50:
        return 32
    if 250 < n <= 500:
        return 30
    if 10 <= n < 25:
        return 18
    if 500 < n <= 1000:
        return 15
    if n > 1000:
        return 5
    return 8


def industry_score(i):
    if pd.isna(i) or not str(i).strip():
        return 12
    il = str(i).lower()
    if any(k in il for k in LOW_KEYWORDS):
        return 8
    if any(k in il for k in HIGH_KEYWORDS):
        return 28
    return 18


def category(s):
    if s >= 85:
        return 'A - Hot (contact first)'
    if s >= 70:
        return 'B - Strong fit'
    if s >= 55:
        return 'C - Moderate / nurture'
    return 'D - Low priority'


def main(inp, outp):
    df = pd.read_csv(inp)
    cols = {k: find_col(df, k) for k in COLUMN_ALIASES}
    missing = [k for k, v in cols.items() if v is None]
    if missing:
        print(f"WARNING: unmapped columns (scored as 0/neutral): {missing}", file=sys.stderr)

    emp = pd.to_numeric(df[cols['employees']], errors='coerce') if cols['employees'] else pd.Series(float('nan'), index=df.index)
    df['score_size'] = emp.apply(size_score)
    df['score_industry'] = (df[cols['industry']].apply(industry_score)
                            if cols['industry'] else 12)

    if cols['tier']:
        tier_pts = {'Tier 1': 20, 'Tier 2': 14, 'Tier 3': 7, 'Tier 4': 0}
        df['score_tier'] = df[cols['tier']].map(tier_pts).fillna(7)
    else:
        # No tier column: redistribute weight onto size + industry
        df['score_tier'] = ((df['score_size'] / 40 + df['score_industry'] / 30) * 10).round()

    df['score_data'] = ((df[cols['linkedin']].notna().astype(int) * 6 if cols['linkedin'] else 0)
                        + (df[cols['website']].notna().astype(int) * 2 if cols['website'] else 0)
                        + (df[cols['li_id']].notna().astype(int) * 2 if cols['li_id'] else 0))

    df['lead_score'] = df[['score_size', 'score_industry', 'score_tier', 'score_data']].sum(axis=1)
    df['category'] = df['lead_score'].apply(category)
    df = df.sort_values('lead_score', ascending=False).reset_index(drop=True)
    df.insert(0, 'rank', df.index + 1)
    df.to_csv(outp, index=False)

    print(f"Scored {len(df)} leads -> {outp}")
    print(df['category'].value_counts().to_string())


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
