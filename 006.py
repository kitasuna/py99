# https://sites.google.com/site/prologsite/prolog-problems/1
# 1.06 (*) Find out whether a list is a palindrome.



def main():
    mylist = [['a', 11, 'b', 'c', 'd', 1, 4],
            ['t','a','c','o','c','a','t']]
    print(mylist)

    mylistr = []
    for i in mylist:
        mylistr.append(list(reversed(i)))

    print(mylistr)

    for i,j in zip(mylist, mylistr):
       if i == j:
           print('list is a palindrome')
       else:
           print('list is not a palindrome')



if __name__ == '__main__':
    main()
