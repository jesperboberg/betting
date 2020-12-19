'''
Created on 15 Dec 2020

@author: jesperboberg
'''
import BettingFirstAttempt.functions as functions

# Load data from a season, print out the data available
plData = functions.getData('PL19:20.csv')
dataIndexing = plData[0]
# Find the index of some statistic
findIndex = plData[0].index("B365<2.5")


# Calculate points for a team during a season
totalAwayPointsWH,totalHomePointsWH = functions.calculatePointsSeason('West Ham',plData)
totalPointsWH = totalAwayPointsWH+totalHomePointsWH
