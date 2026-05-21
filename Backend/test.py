import pandas as pd

df = pd.read_csv("dataset.csv")

print("\nComplexity Score Stats:")
print("Min :", df["Complexity_Score"].min())
print("Max :", df["Complexity_Score"].max())
print("Mean:", df["Complexity_Score"].mean())
print("\nJoules Stats:")
print("Min :", df["Joules"].min())
print("Max :", df["Joules"].max())
print("Mean:", df["Joules"].mean())