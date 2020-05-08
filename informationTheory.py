import math

p = 0.5
entropy = p * (math.log2(1/p))
shinf = math.log2(1/p)

print(entropy, shinf)