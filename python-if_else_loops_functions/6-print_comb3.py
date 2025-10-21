#!/usr/bin/python3
for i in range(10):  # loop for the first digit
    for j in range(i + 1, 10):  # loop for the second digit, always greater than first
        if i == 8 and j == 9:  # last combination
            print("{}{}".format(i, j))  # print without comma and space
        else:
            print("{}{}, ".format(i, j), end="")  # print with comma and space
