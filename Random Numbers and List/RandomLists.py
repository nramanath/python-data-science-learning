import random

def printHorizontalLine(style="-", length=30):
    for _ in xrange(length):
        print style,
    print ""

print "random.shuffle is used to shuffle the elements of a list"
upToTen = range(10)
print "\nbefore shuffling, list =", upToTen
random.shuffle(upToTen)
print "after shuffling, list =", upToTen
print "\nNOTE: random.shuffle MODIFIES THE ORIGINAL list !"
printHorizontalLine()

print "random.choice is used to pick a random element from a list"
planets = ["Earth", "Neptune", "Pluto", "Jupiter"]
print random.choice(planets)
printHorizontalLine()

print "Generating a list with random numbers WITHOUT duplicates"
randomListWithoutDuplicates = random.sample(xrange(20,40), 5) # generates 5 numbers
print randomListWithoutDuplicates
printHorizontalLine()

print "Generating a list with random numbers WITH duplicates"
randomListWithDuplicates = [random.choice(range(10)) for _ in range(10)]
print randomListWithDuplicates
printHorizontalLine()
