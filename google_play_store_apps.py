#! /usr/bin/env python3
        
import pandas as pd
import happyprint as hp

csvfile = "data/googleplaystore.csv"

# Load the csv file into a pandas dataframe
df = pd.read_csv(csvfile)


hp.phead("- - - - OVERVIEW OF RAW, UNFILTERED DATA")
hp.pblue("First 10 rows of data:")
hp.pwhite(df.head(10))

hp.pblue("Last 10 rows of data:")
hp.pwhite(df.tail(10))


hp.phead("DATA CLEANING")
df.replace({r"Varies\swith\sdevice": ""}, regex=True, inplace=True)
hp.pblue("Replaced all occurances of 'Varies with device' from all rows and all "
      "columns. Compare with previous output of last 10 rows.")
hp.pwhite(df.tail(10))


# DISABLED: This only prints a 20 item head and tail with lousy formatting of
# the column names. The preceding head and tail are much better for this.
#phead("PANDAS AUTO-GENERATED SUMMARY OF THIS DATA FILE")
#pwhite(df.describe)


# Search specific fields and print occurances as entire record.
hp.phead("- - - - FLAPPY SEARCH. ALL APP TITLES CONTAINING 'lappy'")
for index, row in df.iterrows():
    app_title = row["App"]
    if "lappy" in app_title:
        hp.pwhite(row)
        hp.pdiv()

hp.phead("- - - - TEXT HISTOGRAM (VALUE COUNT) OF GENRES")
#pwhite(df.groupby('Genres')***NEED A REFERENCE TO INTERNAL INTEGER INDEX OR SOME UNIQUE ID TO COUNT HERE**.nunique())
# The Apple data set has a unique id column which we successfully use and refer to by name here.
# TODO: Now sort by count.

