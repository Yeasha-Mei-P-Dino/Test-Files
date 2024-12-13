import random as ran
ran = ran.randint(1,10)

while True:
    print("="*100, "\n\t GUESSING GAME")
    guess = int(input("\n\t Enter a number from 1-10: "))
    if guess < ran:
        print("\n\t Higher")
    elif guess > ran:
        print("\n\t Lower")
    elif guess == ran:
        print("\n\t Congrats! You guessed it right!")
        want = input("\n\t Do you still want to play (y/n): ")
        if want.lower() == "y":
            print("\n\t Okiieee have fun ^W^")
            continue
        elif want.lower() == "n":
            print("\n\t Thanks for playing ^U^ until next time.")
            break
        else:
            print("\n\t Please read carefully and be clear with your answer.")