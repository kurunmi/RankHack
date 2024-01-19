def canConstruct(randomNote, magazine):
    if len(magazine) < 1:
        return False
    if sorted(randomNote) == sorted(magazine):
        return True
    mag_dict = {}
    for x in magazine:
        mag_dict[x] = (1 + mag_dict.get(x, 0))
    for letter in randomNote:
        if letter not in mag_dict:
            return False
        if letter in mag_dict:
            mag_dict[letter] -= 1
            if mag_dict[letter] == 0:
                del mag_dict[letter]
    return True



if __name__ == '__main__':
    ransomNote = "alakobnabn"
    magazine = "alakobabonitide"
    print(canConstruct(ransomNote, magazine))