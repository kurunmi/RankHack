#!/usr/bin/python3
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def brecords(scores):
    init = scores.pop(0)
    most = init
    most_ct = 0
    least = init
    min_ct = 0
    print(most, least)
    for score in scores:
        if score > most:
            most = score
            most_ct +=1
        elif score < least:
            least = score
            min_ct += 1
        print(most, least, most_ct, min_ct)
    return [most, least]



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    scores = [12,24,10,24]
    myout = brecords(scores)
    print(myout)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
