def strconv(s, numRows):
    final = [""] * numRows
    step = 1
    index = 0

    if numRows == 1 or numRows >= len(s):
        return s

    for let in s:
        final[index] += let
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
        index += step

    return ''.join(final)

