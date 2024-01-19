#!/usr/bin/python3
import string
import copy

lower_list = string.ascii_lowercase
upper_list = string.ascii_uppercase

def list_shift(lst, num):
    while num >= 1:
        print(lst)
        print(num)
        lst.append(lst.pop(0))
        print(lst)
        num -= 1
        print(lst)
    return lst

def lstDict(lst):
    dct = {}
    for x in range(len(lst)):
        dct[x] = lst[x]
    return dct


def lstDict1(lst):
    dct = {}
    for x in range(len(lst)):
        dct[lst[x]] = x
    return dct


def charflip(dict1, dict2, char):
    if not char.isalpha():
        return char
    print (dict1)
    print(dict2)
    print(dict1[char])
    return dict2[dict1[char]]

def switchstr(mystr, dict1, dict2):
    newstr = ""
    for char in mystr:
        newchar = charflip(dict1, dict2, char)
        newstr += newchar
    return newstr

def dictchooser(mystr, uinit, ushift, linit, lshift):
    newstr = ""
    for char in mystr:
        if char.isupper():
            newchar = charflip(uinit, ushift, char)
            print(char, newchar)
        elif char.islower():
            newchar = charflip(linit, lshift, char)
            print(char, newchar)
        else:
            newchar = char
        newstr += newchar
    print(mystr, newstr)
    return newstr




def cipher(s,k):
    dict1 = lstDict1(upper_list)
    dict2 = lstDict1(lower_list)
    upinit = copy.deepcopy(list(upper_list))
    lowinit = copy.deepcopy(list(lower_list))
    lower1 = list_shift(lowinit, k)
    lowerd = lstDict(lower1)
    upper1 = list_shift(upinit, k)
    upperd = lstDict(upper1)
    str2 = dictchooser(s, dict1, upperd, dict2, lowerd)
    return str2
#list1 = list_shift(list(lower_list), 5)



tst =  cipher("middle-Outz", 2)
print(tst)
