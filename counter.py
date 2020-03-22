# Get the words that we want to exclude.
with open("exclude.txt", "r") as f_exclude:
    exclude = f_exclude.read()
    exclude = exclude.split("\n")

# Split the tweets into words and count them

special_characters = """!"#$%&'()*+,-./:;<=>?[]^_}{~|"""
f = open("tweets.txt", encoding="utf-8")
words = {}
for line in f:
    line = line.strip()
    line = line.lower()
    line = line.split()

    for word in line:
        # Delete special characters
        if word[0] in special_characters:
            word = word[1:-1]
        if word[-1] in special_characters:
            word = word[:-2]

        # Count the words
        words[word] = words.get(word, 0) + 1


# Sort the words from most used

count = 1
num = sorted(words, key=words.get, reverse=True)
for k in num:
    if k in exclude:
        continue
    else:
        if count <= 50:
            print(k, words[k])
            count += 1
        else:
            break
