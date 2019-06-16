# even and odd
# even /2
#odd =! /2

print('welcome to odd-even game. \ by:me \ twitter:@yaqubalrubiaan \n ----------- \n x = exit')
while True:
    number = input("Enter The Number: ")
    if number == 'x':
        print('exit the game.')
        break
    try:
        number = int(number)
        if number % 2 == 0:
            print("Even!")

        else:
            print("Odd!")

    except ValueError:
        print("please enter valid number.")