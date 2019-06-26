import colorama

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

    