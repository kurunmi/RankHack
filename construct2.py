def canConstruct(ransomNote, magazine):
    for letter in ransomNote:
        if letter not in magazine:
            return False
        magazine = magazine.replace(letter, '', 1)
    return True

if __name__ == '__main__':
    ransomNote = "alakobnab"
    magazine = "alakobabonitide"
    print(canConstruct(ransomNote, magazine))
    print("rapp")