'''
Created on 15 Dec 2020

@author: jesperboberg
'''
import numpy as np

# Additive method, not very commonly used. Can give scewed odds for huge favorites or for huge underdogs.
def additiveMethod(odds):
    n = len(odds)
    oddsProb = 1/np.array(odds)
    trueProb = oddsProb - (sum(oddsProb)-1)/n
    trueOdds = 1/trueProb
    return trueOdds

# Multiplication or normalization method, commonly used because of its simplicity, does not 
# account for the favorite longshot bias.
def multiplicativeMethod(odds):
    oddsProb = 1/np.array(odds)
    trueProb = oddsProb/sum(oddsProb)
    trueOdds = 1/trueProb
    return trueOdds

# Power method iterates and calculates based on adjusting the odds by a constant power k.
def powerMethod(odds):
    iterationLimit = 1.001 # Slightly larger than 1.
    n = len(odds)
    impliedProbs = 1/np.array(odds)
    R = 1/sum(impliedProbs)
    k = np.log(n*R)/np.log(n)
    trueProbs = np.power(impliedProbs,1/k)
    trueOdds = 1/trueProbs
    if sum(trueProbs) > iterationLimit:
        trueProbs = powerMethod(1/trueProbs)
    return trueOdds

