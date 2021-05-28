print('In your Best Interest: \n\nZenith Bank Plc\n\n')
ussd = input('Please type in your bank USSD code: ')
def menu():
    option = int(input('1. Check your balance\n2. Transfer\n3. Airtime\n4. Transaction History\n\nPlease select an option: '))
    if(option == 1):
        print('Your account balance is 36,000.00 naira')
        main = int(input('ENTER 1 TO RETURN TO MENU\nENTER 2 TO END: \n\n'))
        if(main == 1):
            menu()
        elif(main == 2):
            exit()
        else:
            print('input error!')
    elif(option == 2):
        num = input('Enter the Account number you want to tranfer the money to: ')
        amount = input('Enter amount: ')
        pin = input('Enter four digits pin: ')
        compilation = 'Do you want to send '+amount+' to this account number: '+ num+'?\n1. Yes\n2. No\n'
        assure = input(compilation)
        if(assure == '1'):
            print('Transaction successful')
            main = int(input('ENTER 1 TO RETURN TO MENU\nENTER 2 TO END: \n\n'))
            if(main == 1):
                menu()
            elif(main == 2):
                exit()
            else:
                print('input error!')            
        elif(assure == '2'):
            print('Transanction cancelled')
            main = int(input('ENTER 1 TO RETURN TO MENU\nENTER 2 TO END: \n\n'))
            if(main == 1):
                menu()
            elif(main == 2):
                exit()
            else:
                print('input error!')
    elif(option == 3):
        choice = int(input('1. For self\n2. For others\n'))
        if(choice == 1):
            amount = (input('Enter amount: '))
            print('Transaction successful')
            main = int(input('ENTER 1 TO RETURN TO MENU\nENTER 2 TO END: \n\n'))
            if(main == 1):
                menu()
            elif(main == 2):
                exit()
            else:
                print('input error!')
        elif(choice == 2):
            amount=(input('Enter amount: '))
            number = input('Enter the phone number you want to buy airtime for: ')
            compilation = 'Do you want to buy '+ amount+ ' naira worth of airtime for '+ number+'?: \n1. Yes\n2. No\n'
            assure = int(input(compilation))
            if(assure == 1):
                print('Transaction successful')
                main = int(input('ENTER 1 TO RETURN TO MENU\nENTER 2 TO END: \n\n'))
                if(main == 1):
                    menu()
                elif(main == 2):
                    exit()
                else:
                    print('input error!')
            elif(assure == 2):
                print('Transaction cancelled')
                main = int(input('ENTER 1 TO RETURN TO MENU\nENTER 2 TO END: \n\n'))
                if(main == 1):
                    menu()
                elif(main == 2):
                    exit()
                else:
                    print('input error!')
            else:
                print('invalid input')
    elif(option == 4):
        print('An sms would be sent to you shortly')
if(ussd == '*966#'):
    menu()
else:
    print('Wrong input')