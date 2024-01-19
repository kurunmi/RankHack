#!/usr/bin/python3
def evenlyDivide(x, y):
    if x % y == 0:
        return True
    return False

def getNextPlayer(player):
    if player == 0:
        return 1
    return 0

def chooser(x):
    choices = []
    for newheight in range(1, x):
        #rint("h", newheight, evenlyDivide(x, newheight))
        if evenlyDivide(x, newheight):
            choices.append(newheight)
    if len(choices) >= 1:
        return (min(choices))
    return False

def generate_players(n):
    player_names =[]
    for x in range(1, n+1):
        player_names.append(str(x))
    return player_names


def towerBreakers(n, m):
    if m == 1:
        return 2
    if n % 2 == 0:
        return 2
    return 1
    towers = [m] * n
    player_names = ["1", "2"]
    print(player_names)
    print("towers", towers)
    choice = True
    index = 0
    while choice and choice != "False":
        for player in range(n):
            #print("Player " + str(player) + " " + player_names[index], towers[player])
            #print(choice)
            choice = chooser(towers[player])
            if not choice:
                print("returning")
                winner = getNextPlayer(index)
                return player_names[winner]
            towers[player] = choice
            index += 1
            if index ==2:
                index = 0
            #print("Player " + str(player) + " " + player_names[index], towers[player])


if __name__ == '__main__':
    mychoice = towerBreakers(20000,40000)
    print(mychoice)

