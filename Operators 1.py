number=int(input('Guess a number between 1 to 10:'))
while True:
    if number==3:
        print('Your number is correct')
        break
    elif number<3:
        print('Your number is to low')
        number=int(input('Guess a number between 1 to 10'))
    elif number>10:
        print('Write number between 1 to 10')
        number=int(input('Guess a number between 1 to 10'))
    else:
        print('Your guessing to high')
        number=int(input('Guess a number between 1 to 10'))
