#! /usr/local/bin python3

import pandas as pd

df = pd.DataFrame({
    'STNAME':list('abscscbcdbcsscae'),
    'CTYNAME':[4,5,6,5,6,2,3,4,5,6,4,5,4,3,6,5]
    })

print (df)
#     CTYNAME STNAME
# 0         4      a
# 1         5      b
# 2         6      s
# 3         5      c
# 4         6      s
# 5         2      c
# 6         3      b
# 7         4      c
# 8         5      d
# 9         6      b
# 10        4      c
# 11        5      s
# 12        4      s
# 13        3      c
# 14        6      a
# 15        5      e

df = df[['STNAME','CTYNAME']].groupby(['STNAME'])['CTYNAME'] \
                             .count() \
                             .reset_index(name='count') \
                             .sort_values(['count'], ascending=False) \
                             .head(5)

print(df)

