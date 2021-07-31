from RajinderDaDhaba import *
from PindBalluchi import *
from DharamGaram import *
from payment import *


class Multiple_Order_Selection(RajinderDaDhaba, PindBalluchi, DharamGaram):

    def multiple_order(self, R, A, D):

        self.mul_order_list = {}
        self.max_order = 3

        print("!!! We have the following restaurants !!!")
        print()

        print("1.Rajinder Da Dhaba", "2.Pind Balluchi", "3.Dharam Garam")
        print()

        self.res_name = input("Choose the restaurant by number: ")
        print()

        if self.res_name == '1':  # RajinderDaDhaba

            for key in R.menu_A:
                print(key, ':', R.menu_A[key])
            for i in range(self.max_order):
                self.choice = input("Enter the item name you wish to order: ")
                print()
                # x = int(input("enter the quantity of",self.choice,": ")
                self.mul_order_list[self.choice] = R.menu_A[self.choice]

                if i == 1:
                    self.choice = input(
                        "Do you wish to add more food . Press Y for YES & N for NO: ")
                    print()
                    if self.choice == 'Y' or self.choice == 'y':
                        print(
                            "This is the last item you will select as your cart is about to full")
                        print()
                        self.choice = input(
                            "Enter the last item name you wish to add: ")
                        print()
                        self.mul_order_list[self.choice] = R.menu_A[self.choice]
                        break
                    elif self.choice == 'N' or self.choice == 'n':
                        break
                self.choice = input(
                    "Do you wish to add more food. Press Y for YES & N for NO: ")
                print()
                if self.choice == 'Y' or self.choice == 'y':
                    continue
                elif self.choice == 'N' or self.choice == 'n':
                    break
            print()
            print(
                "***********************************************************************")
            self.py_choice = input(
                "Do you wish to continue for PAYMENT.Press 'Y' for YES & 'N' for NO: ")
            print()

            if self.py_choice == 'Y' or self.py_choice == 'y':
                Payment.order_payment(self.mul_order_list)

            elif self.py_choice == 'N' or self.py_choice == 'n':
                return

        elif self.res_name == '2':  # PindBalluchi

            for key in A.menu_B:
                print(key, ':', A.menu_B[key])
            for i in range(self.max_order):
                self.choice = input("Enter the item name you wish to order: ")
                print()
                self.mul_order_list[self.choice] = A.menu_B[self.choice]
                if i == 1:
                    self.choice = input(
                        "Do you wish to add more food. Press Y for YES & N for NO: ")
                    print()
                    if self.choice == 'Y' or self.choice == 'y':
                        print(
                            "This is the last item you will select as your cart is about to full")
                        print()
                        self.choice = input(
                            "Enter the item name you wish to order: ")
                        print()
                        self.mul_order_list[self.choice] = A.menu_B[self.choice]
                        break
                    elif self.choice == 'N' or self.choice == 'n':
                        break
                self.choice = input(
                    "Do you wish to add more food. Press Y for YES & N for NO: ")
                print()
                if self.choice == 'Y' or self.choice == 'y':
                    continue
                elif self.choice == 'N' or self.choice == 'n':
                    break
            print(
                "***********************************************************************")
            self.py_choice = input(
                "Do you wish to continue for payment.Press 'Y' for YES & 'N' for NO: ")
            print()

            if self.py_choice == 'Y' or self.py_choice == 'y':
                Payment.order_payment(self.mul_order_list)

            elif self.py_choice == 'N' or self.py_choice == 'n':
                return

        elif self.res_name == '3':  # DharamGaram

            for key in D.menu_C:
                print(key, ':', D.menu_C[key])
            max_order = 3
            for i in range(max_order):
                self.choice = input("Enter the item name you wish to order: ")
                print()

                self.mul_order_list[self.choice] = D.menu_C[self.choice]
                if i == 1:
                    self.choice = input(
                        "Do you wish to add more food. Press Y for YES & N for NO: ")
                    print()
                    if self.choice == 'Y' or self.choice == 'y':
                        print(
                            "This is the last item you will select as your cart is about to full")
                        print()
                        self.choice = input(
                            "Enter the item name you wish to order: ")
                        print()
                        self.mul_order_list[self.choice] = D.menu_C[self.choice]
                        break
                    elif self.choice == 'N' or self.choice == 'n':
                        break
                self.choice = input(
                    "Do you wish to add more food. Press Y for YES & N for NO: ")
                print()
                if self.choice == 'Y' or self.choice == 'y':
                    continue
                elif self.choice == 'N' or self.choice == 'n':
                    break
            print(
                "***********************************************************************")
            self.py_choice = input(
                "Do you wish to continue for payment.      Press 'Y' for YES & 'N' for NO: ")
            print()

            if self.py_choice == 'Y' or self.py_choice == 'y':
                Payment.order_payment(self.mul_order_list)

            elif self.py_choice == 'N' or self.py_choice == 'n':
                return
