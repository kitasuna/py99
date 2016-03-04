# https://sites.google.com/site/prologsite/prolog-problems/1
# 1.05 (*) Reverse a list.



def main():
    mylist = ['a', 11, 'b', 'c', 'd', 1, 4]
    print(mylist)

    mylistr = list(reversed(mylist))

    print(mylistr)



if __name__ == '__main__':
    main()
