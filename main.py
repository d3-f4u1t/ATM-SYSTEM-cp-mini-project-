#main run file for a atm simulator
'''
will break this into diff files such as
main
ops
database for easy development

'''
from database import *

def main_menu():
    print("welcome to the ATM simulator")
    print("what would you like to do?")
    print("pls log in to your account")

    a_num = int(input("enter your account number(starting from 100 to 200:"))
    a_pin = int(input("enter your account pin(4 digit number):"))

    if a_num < 100 or a_num > 200:
        print("invalid account number, please try again")
        return
    
    else:
        if a_pin < 1000 or a_pin > 9999:
            print("invalid account pin, please try again")
            return
        
        else:
            if a_num in accounts and accounts[a_num][a_pin] == a_pin:
                print("login successful")
                print(f"welcome, account number {a_num}!")
                
                print("1.check balance")
                print("2.deposit")
                print("3.withdraw")
                print("4.exit")
                
                while True:
                    main_menu()
                    user_choice = input("enter your choice:")
                    
                    if user_choice == "1":
                        print("you chose to check balance")

                    elif user_choice == "2":
                        print("you chose to deposit")

                    elif user_choice == "3":
                        print("you chose to withdraw")

                    elif user_choice == "4":
                        print("thank you for using the ATM simulator, goodbye!")
                        break

                    else:
                        print("invalid choice, please try again")

                else:
                    print("invalid account number or pin, please try again")
                    return


                    
            






    


