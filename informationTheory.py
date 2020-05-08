import math

p = input("Input a Probability between 0 and 100: ")
try:
    p = float(p)
except:
    print("Not a number between 0 and 100")
    quit()

p = p / 100

entropy = p * (math.log2(1/p))
shinf = math.log2(1/p)
eProb = 2**entropy

print(entropy, shinf, eProb)
larala