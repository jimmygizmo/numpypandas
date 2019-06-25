#! /usr/bin/env python3

import pandas
import colorama

datafile = "data/googleplaystore.csv"


def pwht(msg):
        print(f"{colorama.Fore.WHITE}{msg}")

def pyel(msg):
        print(f"{colorama.Fore.YELLOW}{msg}")

def pblu(msg):
        print(f"{colorama.Fore.CYAN}{msg}")

def pred(msg):
        print(f"{colorama.Fore.RED}{msg}")

def pdiv():
        pblu("- - - - - - - - - - - - - - - - - - - -")


data = pandas.read_csv(datafile)

print()
pdiv()
pblu("First 10 rows of data:")
pwht(data.head(10))

pblu("Last 10 rows of data:")
pwht(data.tail(10))


##
#
