#!/usr/bin/env python3

# Created by: Joey Marcotte
# Created on: October 2019
# This program shows if an integer is positive or negative


def main():
    # input
    random_number = int(input("pick a number:"))

    # process
    if random_number > 0:
        # output
        print("the number is +")
    elif random_number < 0:
        print("the number is -")
    else:
        print("number is 0")


if __name__ == "__main__":
    main()
