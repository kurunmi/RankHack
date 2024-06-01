import math


def isPalindrome(s):
    newstr = ""
    for letter in s:
        if str.isalnum(letter):
            newstr += letter.lower()
    if not newstr or len(newstr) < 2:
        return False
    mid = math.floor(len(newstr)/2)
    if len(newstr) % 2 == 0:
        return newstr[:mid] == newstr[mid:][::-1]
    return newstr[:mid] == newstr[mid+1:][::-1]