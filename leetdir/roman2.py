def rotoint(roman):
    stoint={'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}

    roman.replace('IV', 'IIII').replace('VIII', 'IX')
    roman.replace('XL', 'XXXX').replace('XC', 'LXXX')
    roman.replace('CD', 'CCCC').replace('CM', 'DCCC')

    final = 0
    for s in roman:
        final += stoint[s]
    return final

if __name__ == '__main__':
    roman = 'XIV'
    print(rotoint(roman))

