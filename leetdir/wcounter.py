#!/usr/bin/python3

def counter(s):
    size = len(s)
    current_word = ""
    previous_word = ""
    for i in range(size):
        if s[i] != " ":
            current_word += s[i]
        if s[i] == " " and current_word:
            previous_word = current_word
            current_word = ""
    if current_word:
        previous_word = current_word
    print(previous_word)
    return len(previous_word)

if __name__ == '__main__':
    print(counter("abcd ab  abcdefg x   y   "))