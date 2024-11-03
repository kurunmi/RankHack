def largearr(myarr):
    return list(map(int, list(str(int("".join(map(str, myarr))) +1))))




if __name__ == '__main__':
    print(largearr([110]))