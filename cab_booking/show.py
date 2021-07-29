from car import c


class show:
    def __init__(self):
        pass

    def DisplayTitleBar(self):
        print("*______________ ******************************** ______________*")
        print("*______________ WELCOME TO My CAB BOOKING SYSTEM ______________*")
        print("*______________ ******************************** ______________*")

    def DisplayMenuOptions(self):
        print("Please Select any Option")
        print("1. Register a rider")
        print("2. Register a driver/cab")
        print("3. Update a cab's location")
        print("4. A driver switch availability")
        print("5. A rider can book a cab")
        print("6. Fetch history of all rides")
        print("7. End the Trip")
        print("8. EXIT Programe")

    def WorkExecuteOperation(self):
        menuvalue = int(input("Please Enter The Option: "))
        if(menuvalue == 1):
            c.addRider()
        elif(menuvalue == 2):
            c.addCab_Driver()
        elif(menuvalue == 3):
            c.UpdateCabLocation()
        elif(menuvalue == 4):
            c.update_cab_switch()
        elif(menuvalue == 5):
            c.book_cab()
        elif(menuvalue == 6):
            c.update_fetch_history()
        elif(menuvalue == 7):
            c.update_trip_end()
        elif(menuvalue == 8):
            exit()


# a = show()
