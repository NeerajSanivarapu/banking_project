user_pass={'dinga':1234,'dingi':4567}
user_pin={'dinga':1111,'dingi':2222}
user_bal={'dinga':1000,'dingi':500}
name=input('enter your name:')
def deposit(user_name):
    pin=int(input('enter the pin:'))

    if pin==user_pin[user_name]:
        amount=int(input('enter the amount:'))
        if amount>0:
            user_bal[user_name] = amount + user_bal[user_name]
            print(user_bal[user_name])
        else:
            print('amount should be positive..')
    else:
        print('pin not matched...')


def withdraw(user_name):
    pin = int(input('enter the pin:'))
    if pin == user_pin[user_name]:
        amount=int(input('enter the amount:'))
        if amount >0:
            if amount <= user_bal[user_name]:
                user_bal[user_name] = user_bal[user_name] - amount
                print(f'{amount} got debited from your account sucesfully available balance is '
                      f'{user_bal[user_name]}')
            else:
                print('insufficient balance')

        else:
            print('amount should be positive')


def balance_check(user_name):
    pin=int(input('enter the pin'))
    if pin ==user_pin[user_name]:
        print(f' available balance is {user_bal[user_name]}')
    else:
        print('invalid pin..')
def signup():
    print('****** creating the account ******')
    new_user_name = input('enter the user_name:')
    password = int(input('enter the password'))
    con_password = int(input('enter the conform password'))
    pin = int(input('enter the pin'))
    con_pin = int(input('enter the conform pin :'))
    amount = int(input('enter the amount'))
    if new_user_name not in user_pass:
        if password == con_password:
            if pin == con_pin:
                if amount > 0:
                    user_pass[new_user_name]=password
                    print(user_pass)
                    user_pin[new_user_name]=pin
                    print(user_pin)
                    user_bal[new_user_name]=amount
                    print(user_bal)
                else:
                    print('amount should be positive..')
            else:
                print('pin not  matched..')
        else:
            print('password not matched..')
    else:
        print('user name already exist..')
print(f'\t\t\t\t\twelcome {name}')
print(f'\t\t\t\t{'*'*20}')
print('choose any one of the option:\n1.login\n2.signup')
option=input('enter the option').lower()
# if option is login

if option=='login':
    user_name=input('enter the user_name:')
    if user_name in user_pass :
        password = int(input('enter the password'))
        if password==user_pass[user_name]:
            while True:
                print('choose any one of the option:\n1.deposit\n2.withdraw\n3.balance check\n4.exit')
                op=int(input('enter the option:'))
                if op==1:
                    deposit(user_name)
                elif op==2:
                    withdraw(user_name)
                elif op==3:
                    balance_check(user_name)
                else:
                    print('thank you for using our application..')
                    break
        else:
                print('password not matching')
    else:
         print('user_name does not exist please create the account ')
elif option=='signup':
    signup()
else:
    print('invalid option..')
















