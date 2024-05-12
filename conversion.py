import pandas as pd

n = 150

df = pd.read_excel('data job posts.xlsx', sheet_name='Sheet1', usecols=["jobpost", "Title", "Company", "JobDescription","Location"],
        header=0, nrows=n)
df = df.dropna()
jsonl = df.to_json(orient="records", indent=0, lines=True)

with open("job-description.jsonl", "w") as f:
    f.write(jsonl)
