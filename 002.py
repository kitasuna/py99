# https://sites.google.com/site/prologsite/prolog-problems/1
# 1.02 (*) Find the last but one element of a list.

def main():
    mylist = ['a','b','c']
    print(mylist)

    # This way works
    print(mylist[len(mylist) - 2 ])

    # This way is a bit prettier
    print(mylist[-2])

    # Let's try to break the list's bounds
    mylist2 = ['a']
    print(mylist2)

    # This will execute; it evals to
    # mylist2[-1], which is 'a'
    print(mylist2[len(mylist2) - 2 ])

    # This one throws an error
    # print(mylist2[-2])

    # ... so let's wrap it in a try block
    try:
        print(mylist2[-2])
    except:
        print('Index out of range')

if __name__ == '__main__':
    main()
