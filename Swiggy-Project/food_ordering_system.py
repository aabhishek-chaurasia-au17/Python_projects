from getSingleOrder import *
from multiple_order import *
from RajinderDaDhaba import *
from PindBalluchi import *
from DharamGaram import *
from update_menu import *
from art import logo1

single = getSingleOrder_Selection()
multi = Multiple_Order_Selection()
up = Update_Menu()
R = RajinderDaDhaba()
A = PindBalluchi()
D = DharamGaram()
R.food_item()
A.food_item()
D.food_item()

print(logo1)

print("*** Hello! FOODY ***")
print("Press 1 to Get into App ")
print("press 2 to QUIT the App ")
o = input("Enter your choice : ")
print()

if o == '1':
    print("Hello! are you a CUSTOMER OR ADMIN. \n 1.CUSTOMER \n 2.ADMIN ")
    op = input("Enter your choice :")
    print()
    if op == '1':
        print("***********************************")
        print("Dear Customer Order your food here ")
        print("***********************************")
        time.sleep(5)
        print()
        print("Press 1.FOR SINGLE FOOD ORDER \nPress 2.TO CHOOSE RESTAURANT FOR MULTIPLE ORDER: ")
        print()
        op = input("Enter your choice : ")

        if op == '1':
            single.getSingleOrder(R, A, D)
        elif op == '2':
            multi.multiple_order(R, A, D)
    elif op == '2':
        up.add_item(R, A, D)


else:
    print("You chose to quit ")
    print()
    print("Bye Bye FOODY ")
