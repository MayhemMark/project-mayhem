# mandatory checker
awesome_list = ["weyland","weyland404","wybe", "wvbe","erik"]

def mand_check(name):
    print(f"You have entered {name}")
    print("comparing your name...")
    name = str(name.lower())
    if name in awesome_list:
        print("You are quite awesome, however not mandatory")
    elif name == "mark":
        print("Your name is Mark, you are mandatory")
    else:
        print("You suck ass!")

mand_check(input("What is your name?: "))
