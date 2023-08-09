"""
Strategy:   Consider object oriented programming as graph
            traversal problem.
Example:    Kaprekar Function

The strategy is base on the object model figure './media/OOP-graph-traversal.png'

Raymond Hettinger's notion of object-oriented programming is that you
should not write classes, why not? Because a lot of classes have
already been pre-written for you.

Nor do you need to write for-loops, or if-statements and what not, why?

Because the science of object oriented programming in a rich
eco-system language such as python, can be considered as a graph
traversal problem. Take a bunch of classes; int, str, lists, etc., each
with the capabillites you want, and figure out a way to traverse to them.

Sample classes and their known capabilites:
    int     =   good at add, subtract, multiply and divide operations
    str     =   good at uppercase, lowercase and other text operations
    file    =   good at read and write  from a file
    list    =   good at mutating, appending and sorting
    dict    =   good at looking things up, searching operations
    set     =   good at union, intersection and differences of data

Each class has their own speciality. The object model for traversing
the oob graph follows:
    step 1:     figure out which class you are currently using
    step 2:     figure out which class have the capabilities you need
                to solve your problem.
    step 3:     figure out the traversal path to get from the current
                class to the one  that will solve your problem

Problem:    The Kaprekar constant involves sotring four digits in
            ascending and descending order and subtracting them. This
            repeats itself until the result of subtraction end up with
            number 6174.

            To solve the problem, we need to convert the 4 digits into
            string and later into lists in order to sort them. The
            ascending and descending sorted digits need to be converted
            back into int to finish of the subtraction.

Example:    3542 -> 5432 - 2345 -> 3087
            3087 -> 8730 - 0378 -> 8352
            8352 -> 8532 - 2358 -> 6174
            6174 -> 7641 - 1467 -> 6174
             ^-----------------------o

Steps:      There is no direct connection between int and list, so you
            haver to traverse to list through str.

            int -> str = use str()
            str -> list = use split()
            list = use sort()

            Subtract the sorted ascending and descending lists with the
            each other. To do that you need to traverse back to inti.
            Since there is no direct connection between list and int you
            to makte use of str again.

            list -> str = use join()
            str -> int = use int()
            int = use -
"""


"""
# Compressed function
def kap(n):
    s = format(n, '04')
    big = int('',join(sorted(s, reverse=True)))
    small = int(''.join(sorted(s)))
    return big - small
"""


def kap(n):
    s = '%04d' % n
    t = list(s)
    t.sort(reverse=True)
    big = int(''.join(t))
    t.sort()
    small = int(''.join(t))
    return big - small


def main():
    n = 1000

    while (n != 6174):
        n = kap(n)
        print(n)


# The below example shows the non-object-model approach in python.
# Source: https://www.geeksforgeeks.org/kaprekar-constant/
# Credit: mits
def kaprekarRec(n, prev):
    if (n == 0):
        return 0;
    prev = n;

    digits = [0] * 4;
    for i in range(4):
        digits[i] = n % 10;
        n = int(n / 10);

    digits.sort();
    asc = 0;
    for i in range(4):
        asc = asc * 10 + digits[i];

    digits.sort();
    desc = 0;
    for i in range(3, -1, -1):
        desc = desc * 10 + digits[i];

    diff = abs(asc - desc);

    if (diff == prev):
        return diff;

    return kaprekarRec(diff, prev);

# A wrapper over kaprekarRec()
def kaprekar(n):
    rev = 0;
    return kaprekarRec(n, rev);

#print(kaprekar(1000));
#print(kaprekar(1112));
#print(kaprekar(9812));


if __name__ == "__main__":
    main()
