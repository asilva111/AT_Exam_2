Perfect Squares

8.1 - For this problem we can take our integer n and try to arrive at it using a defined list of
available perfect squares. For something like n = 4 the only available perfect squares we can work
with are [0,1,4] although 0 will never be used. For something like n = 12 the list is [1,4,9].

We can identify the recursive nature of the solution by understanding that we will "chip" from the
given integer one of the avaiable numbers, which themselves are composed of possible perfect squares
all the way down. This is where we can identify overlapig work.

8.2 - We can store the solution to smaller subproblems in a dictionary or list, where we have a number
and it's value in the entry is the minimum number of squares required to compose it. This way we don't have
to calculate all of the possible squares over and over.