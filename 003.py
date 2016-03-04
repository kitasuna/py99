# https://sites.google.com/site/prologsite/prolog-problems/1
# 1.03 (*) Find the K'th element of a list.


def elem_at(mylist, index):
    return mylist[index - 1]

def main():
    mylist = ['a', 11, 'b', 'c', 'd', 1, 4]
    print(mylist)

    print(elem_at(mylist, 3))




if __name__ == '__main__':
    main()
