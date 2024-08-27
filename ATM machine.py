import time

#asking user to insert there card in ATM machine
print("Please insert your card")
#now machine will take some time to process
time.sleep(5)
#setting the password 
password=1234
#asking user to enter the atm card pin
pin=int(input("Enter your ATM pin : "))
#entering the total amount of balance
balance = 5000

if pin == password:
    while True:

        print("""
            1 == balance enquiry
            2 == withdraw cash
            3 == deposit cash
            4 == PIN change
            5 == exit 
        """)
        #asking user to enter number according to their choice
        try:
            option=int(input("Please enter your choice = "))
        #if they enter choice another than the given choices
        except:
            print("Please enter valid option")

        if option == 1:
            print("Your current balance is ",balance)
            print("_____________________________________________")     #just for net work using this line
        if option == 2:
            withdraw_amount = int(input("Please enter withdraw amount = "))
            balance = balance - withdraw_amount
            print( withdraw_amount ," is debited from your account")
            print("Your current balance is ",balance)
            print("_____________________________________________")
        if option == 3:
            deposit_amount = int(input("Please enter deposit amount = "))
            balance = balance + deposit_amount
            print( deposit_amount, " is credited to your account")
            print("Your current balance is ",balance)
            print("_____________________________________________")
        if option == 4:
           
           op = int(input("Enter your old password: "))
           np1 = int(input("Enter your new password: "))
           np2 = int(input("Re-enter your new password: "))
           if op == pin & np1 == np2:
               {
                  print("Your new password is set.") 
               }
           else:
               {
                   print("Wrong password")
               }
           print("_____________________________________________")
        if option == 5:
            break

else:
    print("Wrong pin inserted please try again.")