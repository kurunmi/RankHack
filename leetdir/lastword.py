def word(s):
    return len(s.split()[-1])

if __name__ == '__main__':
    s = "   fly me   to   the moon  "
    print(word(s))
