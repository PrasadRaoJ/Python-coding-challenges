import random
from random import randint
choice =input('DO you want OTP: (y/n)')
if choice == 'y':
    otp = random.randint(10000,99999)
    print('Your OTP is: '+str(otp))
    inp1 = int(input('Enter your OTP: '))
    if otp == inp1:
        print('Transaction is successful..!')

    else:
        i=0
        print('Incorrect OTP.Please try again..! you have only 2 Attemps.')
        while i<2:
            inp2 = int(input('Enter your OTP: '))
            i+=1
            if otp == inp2:
                print('Transaction is successful..!')
                break;

            else:
                print('Wrong OTP..Please Try again..')

            if i==2 and otp!=inp2:
                print('you reached  maximum inputs.please Renerate your OTP..')
else:
     print('Thank you for Attempting..!')
