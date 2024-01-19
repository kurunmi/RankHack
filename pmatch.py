#!/usr/bin/python3

def checkMatch(str1, str2):
    if str1 == str2:
        return True
    return False

def matchingStrings(strings, queries):
    result = []
    for myquery in queries:
        query_count = 0
        for mystring in strings:
            if checkMatch(myquery, mystring):
                query_count += 1
        result.append(query_count)
    return result

if __name__ == '__main__':
    strings = ['ab', 'ab', 'abc']
    queries = ['ab', 'abc', 'bc']
    tst = matchingStrings(strings, queries)
    print(tst)