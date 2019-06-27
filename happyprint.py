import colorama

def pwhite(msg):
    print()
    print(f"{colorama.Fore.WHITE}{msg}")

def pyellow(msg):
    print()
    print(f"{colorama.Fore.YELLOW}{msg}")

def pblue(msg):
    print()
    print(f"{colorama.Fore.CYAN}{msg}")

def pred(msg):
    print()
    print(f"{colorama.Fore.RED}{msg}")

def pdiv():
    print()
    print(colorama.Fore.CYAN, end='')
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

def phead(msg):
    print()
    print(colorama.Fore.CYAN, end='')
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print(f"{colorama.Fore.YELLOW}{msg}")
    print(colorama.Fore.CYAN, end='')
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

    