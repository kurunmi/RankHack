def justify(words, maxWidth):
    final = []
    current = ""
    trailing = 0
    curlen = 0
    firstdex = 0
    for i in range(len(words)):
        trailing += 1
        curlen += (len(words[i]))
        if i == len(words) - 1 or ((curlen + (trailing - 1) + len(words[i + 1])) >= maxWidth):
            if i == firstdex:
                extra_spc = maxWidth - len(words[i])
                bits = 0
                current += words[i] + extra_spc * " "
            else:
                tmp_len = len(words[firstdex:i+1]) - 1
                extra_spc = (maxWidth - curlen) // tmp_len
                bits = (maxWidth - curlen) % tmp_len
                for inword in words[firstdex:i]:
                    current += inword + (" " * (extra_spc))
                    if bits > 0:
                        current += " "
                        bits -= 1
                current += words[i]
            final.append(current)
            current = ""
            curlen = 0
            trailing = 0
            firstdex = i + 1
    return final



if __name__ == '__main__':
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    words1 = ["What", "must", "be", "acknowledgment", "shall", "be"]
    maxWidth1 = 16
    words2 = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
              "Art", "is", "everything", "else", "we", "do"]
    maxWidth2 = 20
    print(justify(words, maxWidth))

