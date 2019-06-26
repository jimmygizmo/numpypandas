#! /usr/bin/env python3
        
import pandas
import colorama

csvfile = "data/googleplaystore.csv"


def pwhite(msg):
    print(f"{colorama.Fore.WHITE}{msg}")

def pyellow(msg):
    print(f"{colorama.Fore.YELLOW}{msg}")

def pblue(msg):
    print(f"{colorama.Fore.CYAN}{msg}")

def pred(msg):
    print(f"{colorama.Fore.RED}{msg}")

def pdiv():
    pblue("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

def phead(msg):
    print()
    pdiv()
    pyellow(msg)
    pdiv()

# Load the csv file into a pandas dataframe
df = pandas.read_csv(csvfile)


phead("- - - - OVERVIEW OF RAW, UNFILTERED DATA")
pblue("First 10 rows of data:")
pwhite(df.head(10))

pblue("Last 10 rows of data:")
pwhite(df.tail(10))


phead("DATA CLEANING")
df.replace({r"Varies\swith\sdevice": ""}, regex=True, inplace=True)
pblue("Replaced all occurances of 'Varies with device' from all rows and all "
      "columns. Compare with previous output of last 10 rows.")
pwhite(df.tail(10))


# DISABLED: This only prints a 20 item head and tail with lousy formatting of
# the column names. The preceding head and tail are much better for this.
#phead("PANDAS AUTO-GENERATED SUMMARY OF THIS DATA FILE")
#pwhite(df.describe)


# Search specific fields and print occurances as entire record.
phead("- - - - FLAPPY SEARCH. ALL APP TITLES CONTAINING 'lappy'")
for index, row in df.iterrows():
    app_title = row["App"]
    if "lappy" in app_title:
        pwhite(row)
        pdiv()

phead("- - - - TEXT HISTOGRAM (VALUE COUNT) OF GENRES")
#pwhite(df.groupby('Genres')***NEED A REFERENCE TO INTERNAL INTEGER INDEX OR SOME UNIQUE ID TO COUNT HERE**.nunique())
# The Apple data set has a unique id column which we successfully use and refer to by name here.
# TODO: Now sort by count.

