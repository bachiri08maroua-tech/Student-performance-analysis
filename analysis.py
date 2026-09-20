import pandas as pd

data = pd.read_csv("data.csv")

print(data)

print("\nAverage:")
print(data.mean(numeric_only=True))

print("\nBest student:")
print(data.loc[data["previous_score"].idxmax()])
