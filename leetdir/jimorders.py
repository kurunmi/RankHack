def jimorders(orders):
    servetime = []
    servedict = {}
    cust = 1
    for order in orders:
        ordtime = order[0] + order[1]
        servetime.append(ordtime)
        if ordtime not in servedict:
            servedict[ordtime] = []
        servedict[ordtime].append(cust)
        cust += 1
    final = sorted(servetime)
    myline = []
    for mytime in final:
        myline.append(servedict[mytime].pop(0))
    print(myline)
    return myline

if __name__ == '__main__':
    orders = [[1, 3], [2, 3], [3, 3]]
    orders1 = [[8, 1], [4, 2], [5, 6], [3, 1], [4, 3]]
    orders2 = [[8, 3], [5, 6], [6, 2], [2, 3], [4, 3]]
    jimorders(orders)



