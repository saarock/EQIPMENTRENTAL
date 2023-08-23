import sys, os


def clear():
    try:
                
        y_n = os.path.exists('fine.txt')
        if(y_n):
            with open('fine.txt', 'r') as file:
                           pass 
            os.remove('fine.txt')
    except Exception as e:
         print(e)

def clss():
    try:
        print('Do you want to pay fine type 1 for Yes and 2 for No')
        a = input(':: ')
        if(int(a) ==1 ):
            with open('fine.txt', 'r') as file:
                a = file.readlines()
                b_ = a[4].split('=')
                b__ = b_[1].replace('$', '')
                print('I am trying')
                b = b__.strip()
                a = input(f'Pay {b}:  ')
                print(a,b)
                if(int(a) == int(b)):
                    print('Thank you.')
                    file.close()
                    clear()
                    sys.exit()
                else:
                    clss()
        elif(int(a) == 2):
            sys.exit()
        else:
            print('Try again')
            clss()
    except Exception as e:
        print(e)