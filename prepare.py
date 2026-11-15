import pandas as pd

N = 100

df = pd.read_csv("data/imdb_sample.csv")
sample = df.sample(N, random_state=42).reset_index(drop=True)

sample.to_csv("data/ground_truth.csv", index=False)
sample[["review"]].rename(columns={"review": "text"}).to_csv("data/raw_texts.csv", index=False)
print("Prepared", N, "reviews")