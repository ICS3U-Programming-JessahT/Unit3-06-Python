#!/usr/bin/env python3

# Created By: Jessah
# Date: Oct 11, 2022
# This program generates a random number and makes the user guess
# if its correct with if,then,else statements

import random


def main():

    str_num = input("Guess a number between 0 to 9: ")

    random_variable = random.randint(0, 9)

    try:
        int_num = int(str_num)
        if int_num == random_variable:
            print("")
            print("Right!")

        elif int_num > 9 or int_num < 0:
            print("That number isn't in the range of 0 - 9")

        else:
            print("")
            print("Wrong!")
            print("")
            print("The right number is")
            print(random_variable)

    except Exception:
        print("")
        print("That is not an integer")
    finally:
        print("Try again?")


if __name__ == "__main__":
    main()
