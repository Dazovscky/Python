import random
from random import *

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def choice_number():
    shuffle(number)
    n = number.pop()
    yn = int(input("Choice number 1-10: "))
    if yn == n:
        print(n)
        print(yn)
        print("You Win!!!")
    else:
        print(n)
        print(yn)
        print("You Loose(((")


while True:
    game = input("Play game? y/n: ")
    if game == "y":
        choice_number()
    else:
        print("Game over")
        break
