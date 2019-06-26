#! /usr/local/bin python3

import pandas as pd
import happyprint as hp



df = pd.DataFrame({
    'STNAME':list('abscscbcdbcsscae'),
    'CTYNAME':[4,5,6,5,6,2,3,4,5,6,4,5,4,3,6,5]
    })

hp.pblue(df)
#    STNAME  CTYNAME
# 0       a        4
# 1       b        5
# 2       s        6
# 3       c        5
# 4       s        6
# 5       c        2
# 6       b        3
# 7       c        4
# 8       d        5
# 9       b        6
# 10      c        4
# 11      s        5
# 12      s        4
# 13      c        3
# 14      a        6
# 15      e        5

df = df[['STNAME','CTYNAME']].groupby(['STNAME'])['CTYNAME'] \
                             .count() \
                             .reset_index(name='count') \
                             .sort_values(['count'], ascending=False) \
                             .head(5)

hp.pwhite(df)
#   STNAME  count
# 2      c      5
# 5      s      4
# 1      b      3
# 0      a      2
# 3      d      1
