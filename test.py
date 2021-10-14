import pandas as pd
from igraph import *

df = pd.read_csv('./HW1/tvshow_edges.csv')
cnt = 0
for row in df.itertuples(index=False):
    cnt += 1
    if cnt < 10 or cnt > 17252:
        print(row)
print(cnt)
g = Graph.TupleList(df.itertuples(index=False), directed=True)

summary(g)