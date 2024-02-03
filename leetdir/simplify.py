def simplify(path):
    mypath = path.split('/')
    dir_arr = []
    for item in mypath:
        if item == '..' and dir_arr:
            dir_arr.pop()
        elif item not in ('.', '..', ''):
            dir_arr.append(item)
    return '/' + '/'.join(dir_arr)


if __name__ == '__main__':
    path = "/home/"
    path1 = './home/bona/../bena/babylon/.../barack'
    print(simplify(path1))