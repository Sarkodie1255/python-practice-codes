from random import randint
while True:
    def dice():
        D=int(input('enter a random value from one 1 to 6'))
        if 1<= D<=6:
         print(f'this is the value you entered {D}')
         
        else:
           print('over the counter')
           exit()

        rand = randint(1,6)
        print(rand)

        if D == rand:
            print('you have won a 100,000 dollars')
        else:
            print('sorry bruh, you lost')

    dice()        