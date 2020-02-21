recipientName=input('Enter nameof recipient')
recipientPhone=input('Enter phone No.')
if '254' not in recipientPhone:
    print('Enter the number in the format 254xxxxxxxxxx')
amount = int(input('Enter amount'))
confirm = int(input("press'1' to proceed"))
if(confirm==1):
    balance=50000
    newBal=50000-(amount +(amount*0.01))
print('confirmed Kes {} amount sent to {} of {}. Balance is{}'.format(amount,recipientName,recipientPhone,newBal))   
