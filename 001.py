# https://sites.google.com/site/prologsite/prolog-problems/1
# 1.01 (*) Find the last element of a list.

def main():
    mylist = ['a','b','c']
    print(mylist)

    # This way works
    print(mylist[len(mylist) - 1 ])

    # This way is a bit prettier
    print(mylist[-1])

if __name__ == '__main__':
    main()
