'''
Created on 19 Dec 2020

@author: jesperboberg
'''


from BettingCalculators.Overround import powerMethod, multiplicativeMethod, additiveMethod


def combination(odds,comb,overroundFunction):
    # odds is a list with n odds, comb is a list with the choices [1,3,2], overroundFunction can be e.g. powerMethod
    result = 1
    for indx,match in enumerate(odds):
        trueOdds = overroundFunction(match)
        result = result*trueOdds[comb[indx]]
    return result

methods = [additiveMethod,multiplicativeMethod,powerMethod]
for meth in methods:
    print(combination([[3.39,3.39,2.27],[3.63,3.23,2.25]],[2,2],meth))



