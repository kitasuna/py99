# https://sites.google.com/site/prologsite/prolog-problems/1
# 1.08 (**) Eliminate consecutive duplicates of list elements.
# http://stackoverflow.com/questions/1011938/python-previous-and-next-values-inside-a-loop

from itertools import *

# I started using something like this,
# and then didn't end up needing it.
# Keeping it for posterity.
def prev_and_next(some_iterable):
    # Make three iterators from the original
    prevs, items, nexts = tee(some_iterable, 3)
    # Why do we need to use chain here if we're
    # chaining it with an empty list?
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(prevs, items, nexts)
    

def main():
    mylist = [1, 2, 3, 3, 'a', 'd', 'd', 5, 3, 5, 1, 1]

    ized = prev_and_next(mylist)
    # print(list(ized))

    newlist = []
    for elem in mylist:
        try:
            if newlist[-1] != elem:
                newlist.append(elem)
        except IndexError:
            newlist.append(elem)

    print(newlist)


if __name__ == '__main__':
    main()
