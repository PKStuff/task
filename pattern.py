def triangle(n):

    k= 2*n - n

    for i in range(1,n+1):

        for j in range(0,k):
            print(end=" ")

        k=k-1

        print((" "+"*")*i,end="\n")

triangle(29)

''' o/p

                             *
                             * *
                            * * *
                           * * * *
                          * * * * *
                         * * * * * *
                        * * * * * * *
                       * * * * * * * *
                      * * * * * * * * *
                     * * * * * * * * * *
                    * * * * * * * * * * *
                   * * * * * * * * * * * *
                  * * * * * * * * * * * * *
                 * * * * * * * * * * * * * *
                * * * * * * * * * * * * * * *
               * * * * * * * * * * * * * * * *
              * * * * * * * * * * * * * * * * *
             * * * * * * * * * * * * * * * * * *
            * * * * * * * * * * * * * * * * * * *
           * * * * * * * * * * * * * * * * * * * *
          * * * * * * * * * * * * * * * * * * * * *
         * * * * * * * * * * * * * * * * * * * * * *
        * * * * * * * * * * * * * * * * * * * * * * *
       * * * * * * * * * * * * * * * * * * * * * * * *
      * * * * * * * * * * * * * * * * * * * * * * * * *
     * * * * * * * * * * * * * * * * * * * * * * * * * *
    * * * * * * * * * * * * * * * * * * * * * * * * * * *
   * * * * * * * * * * * * * * * * * * * * * * * * * * * *
  * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
  
'''
  
  
  
  
  def triangle(n):

    k= 2*n - n

    for i in range(1,n+1):

        for j in range(0,k):
            print(end=" ")

        k=k-1

        print(("*")*i,end="\n")

triangle(29)


'''
                             *
                            **
                           ***
                          ****
                         *****
                        ******
                       *******
                      ********
                     *********
                    **********
                   ***********
                  ************
                 *************
                **************
               ***************
              ****************
             *****************
            ******************
           *******************
          ********************
         *********************
        **********************
       ***********************
      ************************
     *************************
    **************************
   ***************************
  ****************************
 *****************************
'''

def Pattern(n):
    for i in range(1,n):
        k=n-i
        for j in range(0,k):
            print(end=" ")
        for a in range(0,i):
            print("*",end=" ")
        for j in range(0,k):
            print(end=" ")
        print()
    

Pattern(20)

'''
PS C:\Projects\Python> python .\sample.py
                   *
                  * *
                 * * *
                * * * *
               * * * * *
              * * * * * *
             * * * * * * *
            * * * * * * * *
           * * * * * * * * *
          * * * * * * * * * *
         * * * * * * * * * * *
        * * * * * * * * * * * *
       * * * * * * * * * * * * *
      * * * * * * * * * * * * * *
     * * * * * * * * * * * * * * *
    * * * * * * * * * * * * * * * *
   * * * * * * * * * * * * * * * * *
  * * * * * * * * * * * * * * * * * *
 * * * * * * * * * * * * * * * * * * *
PS C:\Projects\Python>
'''
def pattern(n):
    for i in range(1,n+1):
        k = n - i
        for j in range(k):
            print(end="  ")
        for a in range(1,i+1):
            print(a,end=" ")
        for b in range(i,1,-1):
            print(b-1,end=" ")
#         for j in range(k):
#             print(end="  ")
        print()

if __name__ == '__main__':
    pattern(10)

'''
O/P:
PS C:\Projects\Python> python .\sample.py
                  1
                1 2 1
              1 2 3 2 1
            1 2 3 4 3 2 1
          1 2 3 4 5 4 3 2 1
        1 2 3 4 5 6 5 4 3 2 1
      1 2 3 4 5 6 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
  1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8 9 10 9 8 7 6 5 4 3 2 1
'''
def pattern(n):
    for i in range(1,n):
        k = n - i
        for j in range(1,k):
            print(end=" ")
        for a in range(1,i):
            print(a,end=" ")
        print()
    for i in range(n-1,1,-1):
        k = n - i
        for j in range(1,k):
            print(end=" ")
        for a in range(1,i):
            print(a,end=" ")
        print()

pattern(10)
'''
lenovo@lenovo-Lenovo-ideapad-330-15IKB:/media/lenovo/New Volume/Stuff/Python/task$ python3 Sample.py 
        
       1 
      1 2 
     1 2 3 
    1 2 3 4 
   1 2 3 4 5 
  1 2 3 4 5 6 
 1 2 3 4 5 6 7 
1 2 3 4 5 6 7 8 
1 2 3 4 5 6 7 8 
 1 2 3 4 5 6 7 
  1 2 3 4 5 6 
   1 2 3 4 5 
    1 2 3 4 
     1 2 3 
      1 2 
       1 
lenovo@lenovo-Lenovo-ideapad-330-15IKB:/media/lenovo/New Volume/Stuff/Python/task
'''
