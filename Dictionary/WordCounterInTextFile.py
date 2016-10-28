from collections import defaultdict


contents = open('/Users/ramanathan/Documents/sublime.txt', 'r')
wordCounter = defaultdict(int)

for line in contents:
    for word in line.split():
        wordCounter[word] += 1

print wordCounter
