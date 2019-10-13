
# The Collatz Sequence
# the simplest impossible math problem.

number = 0
selection = 0

def collatz(number):
        if number % 2 == 0:
            number = number // 2
            return number
        if number % 2 != 0:
            number = 3 * number + 1
            return number

while selection == 0:
    print('Enter number: ')
    try :
        number = int(input())
        if number == 1:
            print('Number Already 1')
        else :
            while number != 1:
                print(collatz(number))
                number = collatz(number) 
    except TypeError:
        print('Must Enter Integer')
    except ValueError:
        print('Must Enter Integer')
    print()
    print('Enter the number 0 if you would like to try again')
    selection = int(input())



    




