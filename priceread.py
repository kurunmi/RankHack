import sys

class tradeObj:
    def __init__(self, OTime, Ctime, Symbol, Side, Price, Qty):
        self.Otime = OTime
        self.Ctime = Ctime
        self.Symbol = Symbol
        self.Side = Side
        self.Price = Price
        self.Quantity = Qty
        self.Position = ""

class tradeStocks:
    def __init__(self):
        self.holder = {}
        self.last_position = 0
    def read(self):
        for line in sys.stdin:
            time, symbol, side, price, quantity = line.split(',')
            obj = tradeObj(Ctime=time, Symbol=symbol, Price=price, Quantity=quantity, Side=side)

    def addTrade(self, obj):
        if obj.Symbol not in self.holder:
            obj.position = self.last_position
            self.last_position += 1
            self.holder[obj.Symbol] = []
            self.holder[obj.Symbol].append(obj)
        else:
            self.doMatching(obj)


    def doMatching(self, obj):
        previous = self.holder[obj.symbol][0]
        if obj.side == previous.side:
            obj.Position = self.last_position
            self.last_position += 1
            self.holder[obj.Symbol].append(obj)
        else:
            pnl, match = self.getPnl(previous, obj)
            print(previous.Otime, obj.Ctime, previous.Symbol, match, pnl, previous.Side, obj.Side, previous.Price,
                  obj.Price)
        if previous.Quantiy > obj.Quantity:
            previous.Quantity -= obj.Quantity
        elif previous.Quantity < obj.Quantity:
            obj.Quantity -= previous.Quantity
            self.holder[obj.Symbol].pop(0)
            self.doMatching(obj.Quantity)

    def getPnl(self, obj1, obj2):
        if obj1.Quantity > obj2.Quantity:
            match = obj2.Quantity
        else:
            match = obj1.Quantity
        pnl = (obj1.Price - obj2.Price) * match
        if obj1.Side == 'S':
            pnl = 1 - pnl
        return pnl, match





