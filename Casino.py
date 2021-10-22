from random import *

number1 = [1, 2, 3]
number2 = [1, 2, 3]
number3 = [1, 2, 3]
cash = int(input("Enter your deposit UAH :"))


def line1():
    shuffle(number1)
    shuffle(number2)
    shuffle(number3)
    print(number1)
    print(number2)
    print(number3)


while True:
    game = input("Spin? y/n :")
    if game == "y":
        line1()
        if number1 == number2:
            cash += 25
            print("Your win :", cash)
        elif number2 == number3:
            cash += 25
            print("Your win :", cash)
        elif number1 == number2 and number2 == number3:
            cash += 100
            print("Your win :", cash)
        else:
            cash -= 25
            print("Your loose :", cash)
            if cash <= 0:
                print("Game over :", cash)
                break
    else:
        print("Game over", cash)
        break
