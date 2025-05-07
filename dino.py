import csv
import math
from operator import itemgetter

def do_calc():
    dict1= {}
    result = []
    g = 9.8
    mycsv = csv.DictReader(open('/home/bona/apps/dataset1.csv', 'r'))
    for rows in mycsv:
        dict1[rows['NAME']] = rows
    csv1 = csv.DictReader(open('/home/bona/apps/dataset2.csv', 'r'))
    for rows in csv1:
        if rows['STANCE'] == 'bipedal' and rows['NAME'] in dict1 :
            leg = float(dict1[rows['NAME']]['LEG_LENGTH'])
            speed = ((float(rows['STRIDE_LENGTH']) * leg) * math.sqrt(leg * g))
            result.append((rows['NAME'], speed))
    result = sorted(result, key=itemgetter(1))
    for entry in result:
        print(entry[0], entry[1])






if __name__ == '__main__':
    do_calc()