# https://sites.google.com/site/prologsite/prolog-problems/1
# 1.09 (**) Pack consecutive duplicates of list elements into sublists.

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
    mylist = ['q', 1, 2, 3, 3, 'a', 'd', 'd', 5, 3, 5, 1, 1]

    newlist = []
    tmplist = []
    for elem in mylist:
        try:
            if(tmplist[-1] == elem):
                tmplist.append(elem)
            else:
                if(len(tmplist) > 1):
                    newlist.append(tmplist)
                else:
                    print('last')
                    newlist.append(tmplist[-1])
                tmplist = []
        except IndexError:
            tmplist.append(elem)

    print(newlist)


if __name__ == '__main__':
    main()
