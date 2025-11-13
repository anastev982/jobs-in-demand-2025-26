import os, glob, re, pandas as pd

# 1) Nađi CSV (OneDrive može imati razna imena)
cands = []
for pat in [
    "/mnt/c/Users/steva/OneDrive*/Programiranje/**/*.csv",
    "/mnt/c/Users/steva/**/*.csv",
]:
    cands += glob.glob(pat, recursive=True)

def looks_ok(p):
    name = os.path.basename(p).lower()
    return any(k in name for k in ("posting","postings","linkedin","job","jobs"))

cands = [p for p in cands if looks_ok(p)]
cands = sorted(set(cands), key=os.path.getsize, reverse=True)

print("FOUND CSVs:", len(cands))
for i,p in enumerate(cands[:10]):
    print(f"{i:2d}  {os.path.getsize(p)//(1024*1024):4d} MB  {p}")

assert cands, "Nisam našla CSV. Ako znaš tačan put, stavi ga ručno u varijablu csv_path ispod."

csv_path = cands[0]
print("\nCSV:", csv_path)

# 2) Head i kolone
try:
    df = pd.read_csv(csv_path, nrows=5, engine="python", on_bad_lines="skip")
except Exception:
    df = pd.read_csv(csv_path, nrows=5, engine="python", on_bad_lines="skip", encoding="latin1")

print("\nColumns:", list(df.columns)[:30])
print("\nHEAD(5):")
print(df.to_string(index=False))

# 3) Analiza (title + description)
skills = ["kafka","bigquery","spark","dbt","airflow","snowflake","mlops","kubernetes","gcp","azure data factory","databricks"]
title_counts, skill_counts = {}, {s:0 for s in skills}
rows_seen = 0

for ch in pd.read_csv(csv_path, chunksize=50_000, dtype=str, engine="python", on_bad_lines="skip"):
    ch.columns = [c.lower().strip() for c in ch.columns]
    if "title" not in ch or "description" not in ch:
        print("\nMissing expected columns. Got:", list(ch.columns)[:30])
        break

    for k,v in ch["title"].dropna().str.strip().value_counts().items():
        title_counts[k] = title_counts.get(k,0) + int(v)

    s = ch["description"].fillna("").str.lower()
    for term in skills:
        skill_counts[term] += int(s.str.contains(re.escape(term)).sum())

    rows_seen += len(ch)
    if rows_seen >= 200_000:
        break

print("\nTop titles (sample):")
for k,v in sorted(title_counts.items(), key=lambda x: -x[1])[:15]:
    print(f"{v:6d}  {k}")

print("\nIn-demand skills (counts in descriptions):")
for k,v in sorted(skill_counts.items(), key=lambda x: -x[1]):
    print(f"{k:20s} {v}")
