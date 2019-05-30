DEFAULT_GAMES = ['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4']

def points(games):
    total = 0
    for gameString in games:
        total += getGameScore(gameString)
    return total

def getGameScore (game):
    splits = list(map(lambda goals: int(goals), game.split(":")))
    if splits[0] > splits[-1]:
        return 3 
    elif splits[-1] == splits[0]:
        return 1
    else:
        return 0

print(points(DEFAULT_GAMES))

print(points(['0:1']))


# if x>y - 3 points
# if x<y - 0 point
# if x=y - 1 point

# def points(a):
#     return sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in a))

# def points(games):
#     return sum([0,1,3][1+(g[0]>g[2])-(g[0]<g[2])] for g in games)

# def points(games):
#     count = 0
#     for match in games:
#         x = match.split(":")
#         if x[0] > x[1]:
#             count += 3
#         elif x[0] == x[1]:
#             count += 1
#     return count

# points=lambda Q:sum(3*(V[0]>V[2])+(V[0]==V[2])for V in Q)
