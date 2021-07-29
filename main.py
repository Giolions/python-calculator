while True:
    print(
        '1) Addiction'
        '\n2) Subtraction'
        '\n3) Multiplication'
        '\n4) Division'
        '\nexit) Quits the application'
    )

    choose = input('>> ')


    if choose == '1':
        print('You choose addiction ')
        print('The result is ' + str(float(input('First number > ')) + float(input('Second number > '))))


    elif choose == '2':
        print('You choose subtraction')
        print('The result is ' + str(float(input('First number > ')) - float(input('Second number > '))))

    elif choose == '3':
        print('You choose multiplication')
        a = float(input('First number > '))
        b = float(input('Second number > '))
        print('il risultato è ' + str(a * b))

    elif choose == '4':
        print('You choose division')
        a = float(input('First number > '))
        b = float(input('Second number > '))
        print('The result is ' + str(a / b))
    elif choose == 'exit':
        break