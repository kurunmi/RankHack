def isPalindrome(s):
    start = 0
    end = len(s) -1
    new_word = s.lower()
    print(new_word)
    while start < end:
        if not str(new_word[start]).isalnum():
            start += 1
        elif not str(new_word[end]).isalnum():
            end -= 1
        elif new_word[start] == new_word[end]:
            start += 1
            end -= 1
        else:
            print(new_word[start], new_word[end])
            return False
    return True


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    s1 = ""
    print(isPalindrome(s1))