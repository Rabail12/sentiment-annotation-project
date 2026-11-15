import pandas as pd
import os

INPUT = "data/raw_texts.csv"
OUTPUT = "data/labeled_data.csv"
LABELS = {"p": "Positive", "n": "Negative"}

df = pd.read_csv(INPUT)

if os.path.exists(OUTPUT):
    rows = pd.read_csv(OUTPUT).to_dict("records")
else:
    rows = []

for i in range(len(rows), len(df)):
    print(f"\n[{i+1}/{len(df)}]\n{df.loc[i, 'text']}")
    choice = ""
    while choice not in LABELS and choice != "q":
        choice = input("p = Positive, n = Negative, q = quit: ").lower()
    if choice == "q":
        break
    rows.append({"text": df.loc[i, "text"], "label": LABELS[choice]})
    pd.DataFrame(rows).to_csv(OUTPUT, index=False)

print("Done. Labeled", len(rows), "reviews.")