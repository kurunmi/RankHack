def factcheck(n):
    counter = 0
    while n > 0:
        n //= 5
        counter += n
    return counter



if __name__ == '__main__':
    print(factcheck(10))