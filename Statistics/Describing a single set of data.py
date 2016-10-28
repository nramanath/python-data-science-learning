from __future__ import division
import random
from collections import Counter


def printHorizontalLine(style="-", length=50):
    for _ in xrange(length):
        print style,
    print ""


def median(v):
    """finds the 'middle-most' value of v"""
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2
    if n % 2 == 1:
        # if odd, return the middle value
        return sorted_v[midpoint]
    else:
        # if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2


"""
Clearly, the mean is simpler to compute, and it varies smoothly as our data changes. If
we have n data points and one of them increases by some small amount e, then necessarily
the mean will increase by e / n. (This makes the mean amenable to all sorts of
calculus tricks.)
"""


# this isn't right if you don't from __future__ import division
def mean(x):
    return sum(x) / len(x)


"""A generalization of the median is the quantile, which represents the value less than
which a certain percentile of the data lies. (The median represents the value less than
which 50% of the data lies.)"""


def quantile(x, p):
    """returns the pth-percentile value in x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]


def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems() if count == max_count]


""" this is used to create a list of elements
from a list without duplicates"""
# num_friends = random.sample(xrange(100),10)

""" this is used to create a list of elements
from a list with duplicates"""
num_friends = [random.choice(range(100)) for _ in range(100)]

print "Data Set for Number of Friends:"
print num_friends
printHorizontalLine()

print "\nSimple Stats:"
printHorizontalLine(length=15)

num_points = len(num_friends)
smallest_value = min(num_friends)
largest_value = max(num_friends)
sorted_num_friends = sorted(num_friends)

second_smallest_value = sorted_num_friends[1]
second_largest_value = sorted_num_friends[-2]

print "Number of Data Points :", num_points
print "Smallest value : ", smallest_value
print "Largest Value : ", largest_value
print "2nd Smallest value : ", second_smallest_value
print "2nd Largest Value : ", second_largest_value
print "\n"
printHorizontalLine()

print "\nCentral Tendencies:"
printHorizontalLine(length=15)
print "Mean = ", mean(num_friends)
print "Median = ", median(num_friends)
print "Quantile Q1 - 0.25 = ", quantile(num_friends, 0.25)
print "Quantile Q2 - 0.50 = ", quantile(num_friends, 0.5)
print "Quantile Q3 - 0.75 = ", quantile(num_friends, 0.75)
print "Mode = ", mode(num_friends)
printHorizontalLine()

print "\nDispersion:"
printHorizontalLine(length=15)
