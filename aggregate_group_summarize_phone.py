#! /usr/bin/env python3

# Inspired by:
# https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/

import dateutil
import pandas as pd
import happyprint as hp

csvfile = "data/phone_data.csv"

# Load the csv file into a pandas dataframe
df = pd.read_csv(csvfile)
# This is actually slightly different from the above:
# df = pd.DataFrame.from_csv(csvfile)

# DATA DESCRIPTION - 5 Months of Cell Phone Activity - 830 Records:
# 1. date: The date and time of the entry
# 2. duration: The duration (in seconds) for each call, the amount of data
#    (in MB) for each data entry, and the number of texts sent (usually 1) for
#    each sms entry.
# 3. item: A description of the event occurring – can be one of call, sms, or
#    data.
# 4. month: The billing month that each entry belongs to – of form ‘YYYY-MM’.
# 5. network: The mobile network that was called/texted for each entry.
# 6. network_type: Whether the number being called was a mobile, international
#    (‘world’), voicemail, landline, or other (‘special’) number.


# REGARDING pandas.read_csv() vs. pandas.DataFrame.from_csv()
# COMPARE:
# df = pd.read_csv(csvfile)
# TYPE: <class 'pandas.core.frame.DataFrame'>
# hp.pwhite(df.head(10))
#    index            date  duration  item    month    network network_type
# 0      0  15/10/14 06:58    34.429  data  2014-11       data         data
# VS:
#df = pd.DataFrame.from_csv(csvfile)
# TYPE: <class 'pandas.core.frame.DataFrame'>
# hp.pwhite(df.head(10))
#                  date  duration  item    month    network network_type
# index                                                                 
# 0      15/10/14 06:58    34.429  data  2014-11       data         data
# NOTICE THE LACK OF INTERNAL INDEX COLUMN WITH THE SECOND METHOD.
# See: https://stackoverflow.com/questions/26495408/pandas-pandas-dataframe-from-csv-vs-pandas-read-csv
# CONCLUSION:
# read_csv might be better to use. it is more versatile and the index column
# is useful.
# Will continue with from_csv to be consistent with tutorial linked at top.
# NOTE: DataFrame.from_csv is planned for deprecation.


hp.phead("- - - - OVERVIEW OF RAW, UNFILTERED DATA")
hp.pblue("First 10 rows of data:")
hp.pwhite(df.head(10))

hp.pblue("Last 10 rows of data:")
hp.pwhite(df.tail(10))

hp.phead("- - - - VARIOUS SUMMARIES")

hp.pblue("Count of 'item' column, hence total number of rows:")
hp.pwhite(df['item'].count())



hp.pdiv()