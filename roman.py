#1/usr/bin/python3


romans = {'I': 1,
         'V': 5,
         'X': 10,
         'L': 50,
         'C': 100,
         'D': 500,
         'M': 1000}

special_cases = ['I', 'C', 'X']

def roman(s):
    current = False
    previous = False
    bucket = 0
    for i in range(len(s)-1, -1, -1):
        val = s[i]
        current = romans[val]
        if previous and current < previous and val in special_cases:
            bucket -= current
        else:
            bucket += current
        previous = current
    return bucket





if __name__ == '__main__':
    print(roman("MCMXCIV"))
