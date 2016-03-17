# https://sites.google.com/site/prologsite/prolog-problems/1
# 1.07 (**) Flatten a nested list structure.

import collections

def flatten(l):
    for el in l:
        # That extra check for str keeps it from recursion hell
        if isinstance(el, collections.Iterable) and not isinstance(el,
                str):
            for sub in flatten(el):
                yield sub
        else:
            yield el

def main():
    mylist = [['a', 11, 'b', 'c', [1, 2, 3], 1, 4],
            ['t','a','c','o','c','a','t'], "stringvar"]

    print(mylist)

    merged = flatten(mylist)

    print(list(merged))


if __name__ == '__main__':
    main()
