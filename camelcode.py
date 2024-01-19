#!/usr/bin/python3
import re
import fileinput

def stringSplit(mystr, mytype):
    #strarr = re.findall('[A-Z][^A-Z]*', mystr)
    if mytype == 'M':
        mystr = mystr.split('(')[0]
    outlist = []
    print(mystr)
    if mystr[-1] == ')':
        mystr = mystr.rstrip(mystr[-1])
    if mystr[-1] == '(':
        mystr = mystr.rstrip(mystr[-1])
    outstr = re.sub( r"([A-Z])", r" \1", mystr).split()
    for str_iter in outstr:
        pref = (str_iter[0:1].lower())
        postf = (str_iter[1:len(str_iter)])
        newsub = "%s%s" % (pref, postf)
        outlist.append(newsub)
    newstr = " ".join(outlist)
    print(newstr)

def stringJoin(mystr, mytype):
    mylist = mystr.split()
    outlist = []
    for str_iter in range(0, len(mylist)):
        newsub = mylist[str_iter]
        iter_start = 0
        if mytype == 'C':
            iter_start = -1
        if str_iter > iter_start:
            sub_str = mylist[str_iter]
            pref = (sub_str[0:1].upper())
            postf = (sub_str[1:len(sub_str)])
            newsub = "%s%s" % (pref, postf)
        outlist.append(newsub)
    newstr = "".join(outlist)
    if mytype == 'M':
        newstr += '()'
    print(newstr)

def str_helper(mystr, action, mytype):
    if action == 'C':
        stringJoin(mystr, mytype)
    if action == 'S':
        print('split')
        stringSplit(mystr, mytype)





    for myline in fileinput.input():
        myin = myline.split(';')
        mytype = myin[1]
        action = myin[0]
        data = myin[2]
        str_helper(data, action, mytype)
    #input1 = "mobile phone"
    #stringSplit(input)
    #stringJoin(input1)