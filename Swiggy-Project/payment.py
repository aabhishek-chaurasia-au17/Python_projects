import time
from prettytable import PrettyTable


class Payment:
    @staticmethod
    # a list which is dictionary where all food items and price is stored.
    def order_payment(order):
        selected_items = []
        for item in order:
            selected_items.append(item)
        print("You have selected:\n")
        for key in selected_items:
            print(key)
        print()
        sum = 0

        for i in order:
            sum = sum + int(order[i])
            CGST = sum * (2.5/100)
            SGST = sum * (2.5/100)
            updated_sum = sum + CGST + SGST

        print(">> Your total amount of all items is ₹ : ", sum)
        # print("CGST is:                                 ",CGST)
        # print("SGST is:                                 ",SGST,"\n"*2)
        # print("Final amount to be paid after CGST and SGST is ₹ : ",updated_sum)

        x = PrettyTable()
        x.field_names = ["CGST", "SGST", "Total"]
        x.add_row([CGST, SGST, updated_sum])
        print(x)

        print("Please give your Contact Details")
        print()
        First_name = input("First Name :")
        Last_name = input("Last Name :")
        Phone_number = input("Phone Number :")
        Address = input("Address :")

        print()
        print("Please select the payment method : ")
        print()
        print(" 1.COD \n 2.UPI \n 3.Debit/Credit card ")
        print()
        n = input(" Selected Option : ")
        print()
        print("Your  Details  :")
        print("************************")
        print(f" First name : {First_name}")
        print(f" Last name : {Last_name}")
        print(f" Phone number : {Phone_number}")
        print(f" Delivary Address : {Address}")
        print()

        if n == '1':
            print("accepted your request for COD")
            print("You have to pay Rs:", sum)
            print()

        elif n == '2':
            n = input("Please enter your UPI ID: ")
            print()
            m = input("Enter pin :")
            print()
            print("Your payment is in progress.....")
            print()
            time.sleep(3)
            print("Payment has been accepted")
            print()
        elif n == '3':
            print("Please enter your Card Details: ")
            print()
            m = input("Enter Card Number :")
            z = input("Enter CVV :")
            time.sleep(3)
            y = input("Enter OTP :")
            print("Your payment is in progress.....")
            print()
            time.sleep(3)
            print("Payment has been accepted!!!!")
            print()
        print()

        print("Your Food is preparing......")
        print()

        time.sleep(5)

        print("Your food is ready to deliver. It will reach by you in 30 minutes :)")
        print()

        print(".....HAPPY ORDERING.....\n")
        print()
