fname = input('Enter file name and extension: ')

try:
    fhand = open(fname)
except:
    print('Bad file or Bad file Name')
    quit()

sum = 0
count = 0

for line in fhand:
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    else:
        pos = line.find(':')
        try:
            spamScore = float(line[pos+1:])
        except:
            print('Not Numbers')
        sum = sum + spamScore
        count = count + 1
        #print(line)
        #print(sum, count)

print('Sum of Spam Score:', sum, 'Count of Spam Scores:', count, 'Average Spam Score:', sum/count)