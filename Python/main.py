from random import randint

if __name__ == "__main__":
    number = randint(1, 1000)
    guess = int(input("Guess the number between 1 and 1000: "))
    tries = 0
    while guess != number:
        if guess < number:
            print("Too small!")
        else:
            print("Too big!")
        tries += 1
        guess = int(input("Guess the number between 1 and 1000: "))
    print("Yay! You got it in", tries, "tries!")
