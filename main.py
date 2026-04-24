#main run file for a atm simulator
'''
will break this into diff files such as
main
ops
database for easy development

'''
from database import *
import random #for adding ramdom amount of balance to new accounts


def create_account(): #function to create account
    print("welcome to the account creation creation section")
    a_num = int(input("enter your account number(starting from 100 to 200:)"))
    a_pin = int(input("enter your account pin(4 digit number)"))

    if a_num < 100 or a_num > 200:
        print("invalid account number, please try again")
        return
    else:
        if a_pin < 1000 or a_pin > 9999:
            print("invalid account pin, please try again")
            return
        else:
            if a_num in accounts:
                print("account number already exists, please try again")
                return
            else:
                accounts[a_num] = {"pin" : a_pin,
                                  "balance" : random.uniform(1, 10000000000),
                                  "transactions" : []
                                  }
                print(f"account number {a_num} created, you can now log in your new account to start using the ATM simulator")
        


def main_menu(): #main menu with login logic
    print("welcome to the ATM simulator")
    print("what would you like to do?")
    print("pls log in to your account")
    print("if you do not have an account, please create one, press 1 to create account")
    print("if you do have a account, please press 2 to proceed to log in")
    user_sep_input = input("enter your choice:")
    if user_sep_input == "1":
        create_account()
        main_menu() #after creating account, return to main menu to log in and use the ATM simulator
    elif user_sep_input == "2":
        pass #proceed to log in

        

    else:
        print("invalid choice, please try again")
        main_menu() #return to main menu if user input is invalid1


    a_num = int(input("enter your account number(starting from 100 to 200:)"))
    a_pin = int(input("enter your account pin(4 digit number):"))

    if a_num < 100 or a_num > 200:
        print("invalid account number, please try again")
        return
    
    else:
        if a_pin < 1000 or a_pin > 9999:
            print("invalid account pin, please try again")
            return
        
        else:
            if a_num in accounts and accounts[a_num]["pin"] == a_pin:
                print("login successful")
                print(f"welcome, account number {a_num}!")

                print("1.check balance")
                print("2.deposit")
                print("3.withdraw")
                print("4.view transactions")
                print("5.exit")
                
                while True:
                    
                    user_choice = input("enter your choice:")
                    
                    if user_choice == "1":
                        print("you chose to check balance")
                        print(f"your current account is {a_num}")
                        print(f"your current balance is {accounts[a_num]['balance']}")


                    elif user_choice == "2":
                        print("you chose to deposit")
                        print(f"your current account is {a_num}")
                        deposit_amount = float(input("enter the amount you want to deposit:"))
                        accounts[a_num]["balance"] += deposit_amount
                        accounts[a_num]["transactions"].append(f"deposit: {deposit_amount}")
                        print(f"your new balance is {accounts[a_num]['balance']}")

                    elif user_choice == "3":
                        print("you chose to withdraw")
                        print(f"your current account is {a_num}")
                        withdraw_amount= float(input("enter the amount you want to withdraw:"))
                        if withdraw_amount > accounts[a_num]["balance"]:
                            print("insufficient funds, please try again")

                        else:
                            accounts[a_num]["balance"] -= withdraw_amount
                            accounts[a_num]["transactions"].append(f"withdraw: {withdraw_amount}")
                            print(f"your new balance is {accounts[a_num]['balance']}")

                    

                    elif user_choice == "4":
                        print("you chose to view transactions")
                        print(f"your current account is {a_num}")
                        print("transaction history:")
                        for transaction in accounts[a_num]["transactions"]:
                            print(transaction)

                    elif user_choice == "5":
                        print("thank you for using the ATM simulator, goodbye!")
                        break

                    else:
                        print("invalid choicei , please try again")

                else:
                    print("invalid account number or pin, please try again")
                    return
                
            else:
                print("your account number or pin is incorrect, please try again")
                print("OR")
                print("you do not have an account, please create one")
                create_account()
                main_menu() #after creating account, return to main menu to log in and use the ATM simulator


main_menu()         
            






    


