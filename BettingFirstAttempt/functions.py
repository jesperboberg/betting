import csv

def getData(filename):
    with open(filename, 'rt') as csvfile:
        data = []
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            data.append(row)
    return data

def getDataTeam(data,team,homeGames,awayGames):
    teamData = []
    for game in data:
        if game[3] == team and homeGames:
            teamData.append(game)
        if game[4] == team and awayGames:
            teamData.append(game)
    return teamData
    
def calculatePointsSeason(team,seasonData):
    games = getDataTeam(data=seasonData,homeGames=True,awayGames=True,team=team)
    homeGames = [game for game in games if game[3] == team]
    awayGames = [game for game in games if game[4] == team]

    totalHomePoints = sum([3 for game in homeGames if game[7] == 'H']) + sum([1 for game in homeGames if game[7] == 'D'])
    totalAwayPoints = sum([3 for game in awayGames if game[7] == 'A']) + sum([1 for game in awayGames if game[7] == 'D'])
    return totalHomePoints,totalAwayPoints