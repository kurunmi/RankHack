def get_hexcode(line):
    myline = line.strip(';').strip(')').split()
    for mystr in myline:
        newstr = mystr.split(',')
        for each in newstr:
            if each:
                eachstr = each.split(')')
                for rec in eachstr:
                    if rec and check_hex_str(rec[1:]):
                        print(rec)


def check_hex_str(mystr):
    if len(mystr) != 3 and len(mystr) != 6:
        return False
    hex_letters = set(['A', 'B', 'C', 'D', 'E', 'F'])
    for x in mystr:
        if (not x.isnumeric() and (x.upper() not in hex_letters)):
            return False
    return True


hex_letters = {'A', 'B', 'C', 'D', 'E', 'F'}
def get_word(hextr):
    hextr = hextr.split(':')
    for word in hextr:
        for item in word.split():
            if '#' in item:
                for let in range(len(item)):
                    if item[let] == '#':
                        j = let + 1
                        while j < len(item) and (item[j].isnumeric() or item[j].upper() in hex_letters):
                            j += 1
                        if len(item[let:j]) ==  4 or len(item[let:j]) == 7:
                            print(item[let:j])
                        







if __name__ == '__main__':
    data = f"24\n"
    data = "  visibility: hidden;\n"
    data += "}\n"
    data += ".custom-file-input::before {\n"
    data += "  content: 'Select some files';\n"
    data += "  display: inline-block;\n"
    data += "  background: -webkit-linear-gradient(top, #f9f9f9, #e3e3e3);\n"
    data += "  border: 1px solid #999;\n"
    data += "  border-radius: 3px;\n"
    data += "  padding: 5px 8px;\n"
    data += "  outline: none;\n"
    data += "  white-space: nowrap;\n"
    data += "  -webkit-user-select: none;\n"
    data += "  cursor: pointer;\n"
    data += "  text-shadow: 1px 1px #fff;\n"
    data += "  font-weight: 700;\n"
    data += "  font-size: 10pt;\n"
    data += "}\n"
    data += ".custom-file-input:hover::before {\n"
    data += "  border-color: black;\n"
    data += "}\n"
    data += ".custom-file-input:active::before {\n"
    data += "  background: -webkit-linear-gradient(top, #e3e3e3, #f9f9f9);\n"
    data += "}\n"

    data1 = """#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}   """
    for line in data.split('\n'):
        if '#' in line and ':' in line:
            get_word(line)