from leetdir.coinbase_app import mydict
import re
import xml.etree.ElementTree as ET


def natsum(myarr, mydict):
    total = 0
    if not myarr:
        print(0)
        return
    print(total, mydict, myarr)
    for loc in range(sorted(myarr)[-1] + 1):
        if loc in mydict:
            myarr[mydict[loc]] = total
        if loc % 3 == 0 or loc % 5 == 0:
            total += loc
    print(total, mydict, myarr)
    for i in myarr:
        print(i)


def natsum1(n):
    x = n-1
    print(int(((3 * (x//3) * (1 + x//3))/2) + ((5 * (x//5) * (1+ x//5))/2) - ((15 * (x//15) * (1+x//15))/2)))


def numer(string):
    for a, b in enumerate(string):
        print(a, b)

def merge_tools(string, k):
    klen = len(string) // k
    for x in range(k):
        seen = set()
        word = ""
        for y in string[(x * klen):((x+1) * klen)]:
            if y not in seen:
                word += y
                seen.add(y)
        print(word)




if __name__ == '__main__':
    xml = """<?xml version="1.0"?>
            <data>
                <country name="Liechtenstein">
                    <rank>1</rank>
                    <year>2008</year>
                    <gdppc>141100</gdppc>
                    <neighbor name="Austria" direction="E"/>
                    <neighbor name="Switzerland" direction="W"/>
                </country>
            <country name="Singapore">
                <rank>4</rank>
                <year>2011</year>
                <gdppc>59900</gdppc>
                <neighbor name="Malaysia" direction="N"/>
            </country>
            <country name="Panama">
                <rank>68</rank>
                <year>2011</year>
                <gdppc>13600</gdppc>
                <neighbor name="Costa Rica" direction="W"/>
                <neighbor name="Colombia" direction="E"/>
            </country>
            </data>"""
    tree = ET.fromstring(xml)
    for elem in tree.iter():
        print(elem, len(elem))

    myarr = [500, 400, 300, 200, 100, 55555, 555, 666, 12432]
    mystr = "BonaBanana"
    #print(mystr[0:0])
    #merge_tools(mystr, 2)
    #mystr = '<link meshak="t1"</updated><link meshak="t1"</updated>'
    #print(re.split(r"</*>", mystr))
    #numer(mystr)
    index = 7
    for x in myarr:
        mydict[x] = index
        #index += 1
    #natsum(myarr, mydict)
        #natsum1(x)

