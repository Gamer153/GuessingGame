import pickle
import os
from random import randint
import sys

options = {}
number = 0
tries = 0

def save_options():
    with open("options.dat", "wb") as f:
        pickle.dump(options, f)

def int_input(prompt: str) -> int:
    inpt = "§163§&/(!!§"
    while not inpt.isnumeric():
        if inpt != "§163§&/(!!§":
            print("Not a valid number, please try again!")
        inpt = input(prompt)
    return int(inpt)

def show_menu():
    global number, options
    mnu_open = True
    while mnu_open:
        print()
        print("[1] Set lower bound")
        print("[2] Set upper bound")
        print("[?] Cheat")
        print("[x] Quit game\n")
        print("[0] Back to game")
        selection = input("> ")
        if selection == "1":
            lower = int_input("Input new lower bound: ")
            options["limits"]["lower"] = lower
            save_options()
            sel = input("Should I generate a new number [Yes/no]? ").lower().strip()
            if sel in ["y", "yes", ""]:
                gen_number()
                print("Generated new number.")
        elif selection == "2":
            upper = int_input("Input new upper bound: ")
            options["limits"]["upper"] = upper
            save_options()
            sel = input("Should I generate a new number [Yes/no]? ").lower().strip()
            if sel in ["y", "yes", ""]:
                gen_number()
                print("Generated new number.")
        elif selection == "?":
            if input("Are you sure [yes/no]? ").lower().strip() in ["y", "yes", ""]:
                print("The number is:", number)
            else:
                print("Ok.")
        elif selection == "x":
            print("Bye.")
            sys.exit(0)
        elif selection == "0":
            mnu_open = False


def gen_number():
    global number
    lower = options["limits"]["lower"]
    upper = options["limits"]["upper"]
    while number == 0:
        number = randint(lower, upper)

if __name__ == "__main__":
    if os.path.exists("options.dat"):
        with open("options.dat", "rb") as f:
            options = pickle.load(f)
    else:
        options = {"limits":{"lower": 1, "upper":1000}}

    lower = options["limits"]["lower"]
    upper = options["limits"]["upper"]
    gen_number()
    guess = int(input(f"Guess the number between {lower} and {upper} [1. try, 0 = open menu]: "))
    tries += 1
    while guess != number:
        if guess == 0:
            show_menu()
            print()
            lower = options["limits"]["lower"]
            upper = options["limits"]["upper"]
            guess = int(input(f"Guess the number between {lower} and {upper} [{tries}. try, 0 = open menu]: "))
            continue
        if guess < number:
            print("Too small!")
        else:
            print("Too big!")
        tries += 1
        guess = int(input(f"Guess the number between {lower} and {upper} [{tries}. try, 0 = open menu]: "))
    print("Yay! You got it in", tries, "tries!")
