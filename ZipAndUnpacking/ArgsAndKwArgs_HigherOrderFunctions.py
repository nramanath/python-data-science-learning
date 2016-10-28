"""
higher-order function - takes as input some function f
and returns a new function

"""


def square(f):
    def level1(*args, **kwargs):
        print 'args', args
        print 'kw args', kwargs
        return f(*args, **kwargs) ** 2

    return level1


def a_plus_b(x, y):
    return x + y


def a_plus_b_plus_c(x, y, z):
    return x + y + z


def a_minus_b(x, y):
    return x - y


a_plus_b_whole_square = square(a_plus_b)
print a_plus_b_whole_square(2, 3)

a_minus_b_whole_square = square(a_minus_b)
print a_minus_b_whole_square(2, 3)

a_minus_b_plus_c_whole_square = square(a_plus_b_plus_c)
print a_minus_b_plus_c_whole_square(2, 3, 4)
