def intoro(num):
    mynums = [1000, 500, 100, 50, 10, 5, 1]
    numdict = {1000: 'M',
               500:  'D',
               100:  'C',
               50:   'L',
               10:   'X',
               5:    'V',
               1:    'I'}

    roman = ""
    for i in mynums:
        while num >= i:
            roman += numdict[i]
            num -= i

    roman = roman.replace('DCCCC', 'CM').replace('CCCC', 'CD')
    roman = roman.replace('LXXXX', 'XC').replace('XXXX', 'XL')
    roman = roman.replace('VIIII', 'IX').replace('IIII', 'IV')
    return roman


if __name__ == '__main__':
    num = 2994
    print(intoro(num))
