import random, string

def simple_word_list():
    fname = "romeo.txt"

    try:
        fhandler = open(fname)
    except:
        quit()

    words = list()

    for line in fhandler:
        line = line.rstrip()
        line = line.split()
        for word in line:
            if word not in words:
                words.append(word)
            else:
                continue
    return words

def password(*args):
    if strength == 'low':
        words = simple_word_list()
        nums = random.sample(range(1, len(words)), 2)
        paswrd = words[nums[0]] + words[nums[1]]
        return paswrd
    else:
        paswrd = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation) for _ in range(chars))
        return paswrd

while True:
    strength = input("Select your password strength (low) or just hit enter (done to exit): ")
    if strength == 'done':
        break
    elif strength != "low":
        chars = input("Select the amount of characters for the password: ")
        try:
            chars = int(chars)
        except:
            print("Not a number")
        ps = password(strength,chars)
        print(ps)
    else:
        ps = password(strength)
        print(ps)



