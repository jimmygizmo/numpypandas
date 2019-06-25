#! /usr/bin/env python3
        
import pandas
import colorama

csvfile = "data/AppleStore.csv"


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


# phead("DATA CLEANING OF KNOWN BAD RECORDS")
# df.replace({r"Varies\swith\sdevice": ""}, regex=True, inplace=True)
# pblue("Replaced all occurances of 'Varies with device' from all rows and all "
#       "columns. Compare with previous output of last 10 rows.")
# pwhite(df.tail(10))
# phead("DATA CLEANING OF KNOWN BAD RECORDS")
# CANNOT DO IT THIS WAY: ValueError: The truth value of a Series is ambiguous.
# df[df.id not in [
#                  1182265441, 1183709176, 1185428381, 1185731859, 1185777521,
#                  1186108496, 1187128255
#                 ]
#   ]
# Individually - Very inefficient since we recreate the entire df each time:
# THIS DOES NOT WORK
# df[df.id != "1182265441"]
# df[df.id != "1183709176"]
# df[df.id != "1185428381"]
# df[df.id != "1185731859"]
# NOR DOES THIS
# df = df[df.id != "1185777521"]
# df = df[df.id != "1186108496"]
# df = df[df.id != "1187128255"]


# DISABLED: This only prints a 20 item head and tail with lousy formatting of
# the column names. The preceding head and tail are much better for this.
# phead("PANDAS AUTO-GENERATED SUMMARY OF THIS DATA FILE")
# pwhite(df.describe)


# Search specific fields and print occurances as entire record.
phead("- - - - FLAPPY SEARCH. ALL APP TITLES CONTAINING 'lappy'")
for index, row in df.iterrows():
    app_title = row["track_name"]
    if "lappy" in app_title:
        pwhite(row)
        pdiv()




##
#
