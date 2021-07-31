from RajinderDaDhaba import *
from PindBalluchi import *
from DharamGaram import *


class Update_Menu(RajinderDaDhaba, PindBalluchi, DharamGaram):

    def add_item(self, R, A, D):

        print("!!! We have the following restaurants !!!")
        print()

        print("1.Rajinder Da Dhaba", "2.Pind Balluchi", "3.Dharam Garam")
        print()
        self.res_name = input(
            "Please select the Restaurant you want to Update: ")
        print()

        if self.res_name == '1':
            print("Your menu are: ")
            for key in R.menu_A:
                print(key, ':', R.menu_A[key])
            self.op = input(
                "Press 1 for ADD ITEM & 2 for REMOVE ITEM & 3 for RETURN: ")
            print()
            if self.op == '1':
                self.item = input("Add the name of item: ")
                self.price = input("Add the price: ")
                print()
                R.menu_A[self.item] = self.price
                print("Your updated menu are: ")
                for key in R.menu_A:
                    print(key, ':', R.menu_A[key])

            elif self.op == '2':
                self.item = input("Type the item you want to remove: ")
                print()
                del R.menu_A[self.item]
                print("Your updated menu are: ")
                for key in R.menu_A:
                    print(key, ':', R.menu_A[key])

            elif self.op == '3':
                return

        elif self.res_name == '2':
            print("Your menu are: ")
            for key in A.menu_B:
                print(key, ':', A.menu_B[key])
            self.op = input(
                "Press 1 for ADD ITEM & 2 for REMOVE ITEM & 3 for RETURN: ")
            print()
            if self.op == '1':
                self.item = input("Add the name of item: ")
                self.price = input("Add the price: ")
                print()
                A.menu_B[self.item] = self.price
                print("Your updated menu are: ")
                for key in A.menu_B:
                    print(key, ':', A.menu_B[key])

            elif self.op == '2':
                self.item = input("Type the item you want to remove: ")
                print()
                del A.menu_B[self.item]
                print("Your updated menu are: ")
                for key in A.menu_B:
                    print(key, ':', A.menu_B[key])

            elif self.op == '3':
                return

        elif self.res_name == '3':
            print("Your menu are: ")
            for key in D.menu_C:
                print(key, ':', D.menu_C[key])
            self.op = input(
                "Press 1 for ADD ITEM & 2 for REMOVE ITEM & 3 for RETURN: ")
            print()
            if self.op == '1':
                self.item = input("Add the name of item: ")
                self.price = input("Add the price: ")
                print()
                D.menu_C[self.item] = self.price
                print("Your updated menu are: ")
                for key in D.menu_C:
                    print(key, ':', D.menu_C[key])

            elif self.op == '2':
                self.item = input("Type the item you want to remove: ")
                print()
                del D.menu_C[self.item]
                print("Your updated menu are: ")
                for key in D.menu_C:
                    print(key, ':', D.menu_C[key])

            elif self.op == '3':
                return
