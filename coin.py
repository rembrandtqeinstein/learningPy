import numpy as np
def coinFlip(p):
    #perform the binomial distribution (returns 0 or 1)
    result = np.random.binomial(1,p)
#return flip to be added to numpy array
    return result
'''Main Area'''
#probability of heads vs. tails. This can be changed.
probability = .5
#num of flips required. This can be changed.
n = 10000000
#initiate array
fullResults = np.arange(n)
#perform desired numbered of flips at required probability set above
for i in range(0, n):
    fullResults[i] = coinFlip(probability)
    i+=1
#calculate the percentage result
ratio = np.count_nonzero(fullResults == 1)/(np.count_nonzero(fullResults == 1) + np.count_nonzero(fullResults == 0))
#print results
print("probability is set to ", probability)
print("Taxfix = 0, Bipi = 1: ", fullResults)
#Total up heads and tails for easy user experience
print("Bipi Count: ", np.count_nonzero(fullResults == 1))
print("Taxfix Count: ", np.count_nonzero(fullResults == 0))
#Print the percentage
print("Bipi Ratio: ", (ratio*100), "%")
print("Taxfix Ratio: ", ((1-ratio)*100), "%")