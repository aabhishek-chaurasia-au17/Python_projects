# from food_ordering_system import *
from RajinderDaDhaba import *
from PindBalluchi import *
from DharamGaram import *
from payment import *


class getSingleOrder_Selection(RajinderDaDhaba, PindBalluchi, DharamGaram):

    def getSingleOrder(self, R, A, D):
        self.order_list = {}

        for key in R.menu_A:
            print(key, ':', R.menu_A[key])

        for key in A.menu_B:
            print(key, ':', A.menu_B[key])

        for key in D.menu_C:
            print(key, ':', D.menu_C[key])

        # print("TODAY's MENU FOR SINGLE ORDER: ",self.list_of_items )
        # print()

         # approach1 restaurant selection strategy as lowest price offer

        self.item_name = input("Enter the food you wish to order: ")
        print()

        if self.item_name in R.menu_A:
            self.price_A = R.menu_A[self.item_name]

        else:
            self.price_A = '9999'

        if self.item_name in A.menu_B:
            self.price_B = A.menu_B[self.item_name]

        else:
            self.price_B = '9999'

        if self.item_name in D.menu_C:
            self.price_C = D.menu_C[self.item_name]

        else:
            self.price_C = '9999'

        self.min_price = min(self.price_A, self.price_B, self.price_C)

        # here we checking that item input is in the given restaurant or not and second we check that if item is
        #  present then we check the price of that item is equal to min price or not
        if self.item_name in R.menu_A and self.min_price in R.menu_A[self.item_name]:
            print(self.item_name,
                  "is from RajinderDaDhaba which offer you a lowest price at Rs", self.min_price)
            print()
            self.order_list[self.item_name] = self.min_price

            Payment.order_payment(self.order_list)

        if self.item_name in A.menu_B and self.min_price in A.menu_B[self.item_name]:
            print(self.item_name,
                  "is from PindBalluchi which offer you a lowest price at Rs", self.min_price)
            print()
            self.order_list[self.item_name] = self.min_price

            Payment.order_payment(self.order_list)

        if self.item_name in D.menu_C and self.min_price in D.menu_C[self.item_name]:
            print(self.item_name,
                  "is from DharamGaram which offer you a lowest price at Rs", self.min_price)
            print()
            self.order_list[self.item_name] = self.min_price

            Payment.order_payment(self.order_list)
