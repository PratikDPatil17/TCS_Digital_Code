import pandas as pd

df = pd.read_html("http://scrape-table.surge.sh/",header = 0)

dfs = df[0]
dfs.to_csv('data.csv', index=False)

