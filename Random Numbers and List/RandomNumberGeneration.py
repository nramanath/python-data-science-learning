import random


def printHorizontalLine(style="-", length=30):
    for _ in xrange(length):
        print style,
    print ""


print "random.random() produces a random number from 0 to 1"
print random.random()
printHorizontalLine()

print "use random.seed() to produce reproducible results"
random.seed(1)
print "seed = 1  randomNumber =", random.random()
random.seed(3)
print "seed = 3  randomNumber =", random.random()
random.seed(1)
print "seed = 1  randomNumber =", random.random()
printHorizontalLine()

print "random.randrange() is used to generate random numbers in a particular range"
print "random.randrange() take either one or two arguments"
print random.randrange(10)  # choose randomly from [0,1, ... ,9]
print random.randrange(11, 15)  # chooses randomly from [11,12,13,14]
print printHorizontalLine()

