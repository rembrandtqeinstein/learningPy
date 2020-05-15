# Use tuples to navigate through a dict that made a histogram and find out the most used words

fname = input('Enter a text file to use: ')

try:
    fhandler = open(fname)
except:
    print('Bad text file, try romeo.txt')
    quit()

hist = dict()

for line in fhandler:
    line = line.rstrip()
    words = line.split()
    for w in words:
        hist[w] = hist.get(w,0) + 1

# Here I'm going to loop throguh the dictionary and create a reversed order tupple so that I can sort and show the 10 most used words
lis = list()
for k,v in hist.items(): # Iterates through Key and Value of the Dict resulting from the previous for loop
    tup = (v,k) # Creates a new tuple with the Value first and the Key Second
    lis.append(tup) # Appends to the list created outside this for the new tupple with the value first and the key second

lis = sorted(lis, reverse=True) # This sorts the new list with tuples based on the highest Value, since that is the First Key, if they are the same then by the Key (Alphabetical or numerical)

for v,k in lis[:10]: # This loops the list up to the 10th position 0 to 9
    print(k,v) # This prints the Key first and the value after

# We can do the same as the last two for loops with LIST COMPREHENSION as follows
ord = sorted([(v,k) for k,v in hist.items()], reverse=True)
# The [ ] Part creates a new tuple, the first part (v,k) from the loop that follows that iterates through the whole dictionary as the for loop that enters each key and value. Then we apply the sort directly to the resulting tupple, with reversed order and that gives us a list of Values and Keys
print(ord)