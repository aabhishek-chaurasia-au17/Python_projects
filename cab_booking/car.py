import csv
import math

directory = "H:\\attainU\\python\\Python_projects\\cab_booking\\database\\"


class car:
    def __init__(Self):
        pass

    def DisplayTitleBar():
        print("*______________ ******************************** ______________*")
        print("*______________ WELCOME TO My CAB BOOKING SYSTEM ______________*")
        print("*______________ ******************************** ______________*")

    def DisplayMenuOptions():
        print("Please Select any Option")
        print("1. Register a rider")
        print("2. Register a driver/cab")
        print("3. Update a cab's location")
        print("4. A driver switch availability")
        print("5. A rider can book a cab")
        print("6. Fetch history of all rides")
        print("7. End the Trip")
        print("8. EXIT Programe")

    def addRider():
        print("PLEASE ADD RIDER DETAILS")
        Name = input("Please Enter Your Name: ")
        Age = input("Please Enter Your Age: ")
        Gender = input("Please Enter Your Gender: ")
        Contact = input("Please Enter Your Contact: ")
        filename = directory+"Rider.csv"
        header = ("Name", "Age", "Gender", "Contact")
        data = [(Name, Age, Gender, Contact)]
        writer(header, data, filename, "write")
        print("!!!Welcome", Name, "Have a Great Experience!!!")
        e.mainRun()

    def addCab_Driver():
        print("PLEASE ADD DRIVER/CAB DETAILS")
        Name = input("Please Enter Your Name: ")
        Age = input("Please Enter Your Age: ")
        Gender = input("Please Enter Your Gender: ")
        Location_X = input("Please Enter Your Location X: ")
        Location_Y = input("Please Enter Your Location Y: ")
        CabNumber = input("Please Enter Your Cab Number: ")
        CabName = input("Please Enter Your Cab Name: ")
        DLNumber = input("Please Enter Your DL Number: ")
        Switch = input("Please Enter Your Availability: ")
        Contact = input("Please Enter Your Contact: ")
        filename = directory+"Driver_Cab.csv"
        header = ("Name", "Age", "Gender", "Location_X",
                  "Location_Y", "CabNumber", "CabName", "DLNumber", "Switch", "Contact")
        data = [(Name, Age, Gender, Location_X, Location_Y,
                CabNumber, CabName, DLNumber, Switch, Contact)]
        writer(header, data, filename, "write")
        print("!!!Welcome", Name, "Have a Great Experience")
        mainRun()

    def UpdateCabLocation():
        print("PLEASE UPDATE CAB LOCATION")
        CabNumber = input("Please Enter Your Cab Number: ")
        Location_X = input("Please Enter Your Location X: ")
        Location_Y = input("Please Enter Your Location Y: ")
        filename = directory+"Driver_Cab.csv"
        with open(filename, newline="") as file:
            readData = [row for row in csv.DictReader(file)]

        for val in readData:
            if(val['CabNumber'] == CabNumber):
                readHeader = val.keys()
                val['Location_X'] = Location_X
                val['Location_Y'] = Location_Y
                writer(readHeader, readData, filename, "update")
        print("Location Updated Sucessfully!!!")
        mainRun()

    def update_cab_switch():
        print("PLEASE UPDATE CAB AVAILABILITY")
        Name = input("Please Enter Your Name: ")
        Switch = input("Please Enter Your DL Number: ")
        filename = directory+"Driver_Cab.csv"
        with open(filename, newline="") as file:
            readData = [row for row in csv.DictReader(file)]

        for val in readData:
            if(val['Name'] == Name):
                readHeader = val.keys()
                val['Switch'] = Switch
                writer(readHeader, readData, filename, "update")
        print("!!!Availability Updated Successfully!!!")
        mainRun()

    def update_trip_end():
        print("PLEASE END THE TRIP")
        CabName = input("Please Enter The Cab Number For Trip: ")
        filename = directory+"Booking.csv"
        with open(filename, newline="") as file:
            readData = [row for row in csv.DictReader(file)]

        for val in readData:
            if(val['CabNumber'] == CabName):
                readHeader = val.keys()
                val['TripEnd'] = "YES"
                writer(readHeader, readData, filename, "update")
        print("Trip Ended Successfully!!!")
        mainRun()

    def update_fetch_history():
        print("PLEASE FETCH THE HISTORY")
        Name = input("Please Enter The Name For History: ")
        filename = directory+"Booking.csv"
        with open(filename, newline="") as file:
            readData = [row for row in csv.DictReader(file)]

        for val in readData:
            if(val['Name'] == Name):
                print(val)

        print("End Of History!!!")
        mainRun()

    def book_cab():
        print("PLEASE BOOK CAB")
        Name = input("Please Enter Your Name: ")
        Location_X = input("Please Enter Your Location X: ")
        Location_Y = input("Please Enter Your Location Y: ")
        Date = input("Please Enter Date: ")
        Time = input("Please Enter Time: ")
        filename = directory+"Booking.csv"
        header = ("Name", "Location_X",
                  "Location_Y", "Date", "Time", "TripEnd", "CabNumber")

        with open(filename, newline="") as file:
            readData = [row for row in csv.DictReader(file)]

        filenameDrive = directory+"Driver_Cab.csv"
        with open(filenameDrive, newline="") as file:
            readDataDriver = [row for row in csv.DictReader(file)]

        outDict = []
        for val in readDataDriver:
            for valItem in readData:
                if(valItem['TripEnd'] == "NO"):
                    valueroot = math.sqrt((int(Location_X) - int(val['Location_X'])) ** 2 + (
                        int(Location_Y) - int(val['Location_Y'])) ** 2)
                    outDict.append(val['CabNumber'] + "|" + str(valueroot))

        Cabnumber = ''
        distance = 0.0
        for obj in outDict:
            if(distance < float(obj.split("|")[1])):
                distance = float(obj.split("|")[1])
                Cabnumber = obj.split("|")[0]

        data = [(Name,  Location_X, Location_Y, Date, Time, "NO", Cabnumber)]
        writer(header, data, filename, "write")
        print("Booking Added Successfully!!!")
        mainRun()

    def WorkExecuteOperation():
        menuvalue = int(input("Please Enter The Option: "))
        if(menuvalue == 1):
            addRider()
        elif(menuvalue == 2):
            addCab_Driver()
        elif(menuvalue == 3):
            UpdateCabLocation()
        elif(menuvalue == 4):
            update_cab_switch()
        elif(menuvalue == 5):
            book_cab()
        elif(menuvalue == 6):
            update_fetch_history()
        elif(menuvalue == 7):
            update_trip_end()
        elif(menuvalue == 8):
            exit()

    def writer(header, data, filename, option):
        with open(filename, "w", newline="") as csvfile:
            if option == "write":

                movies = csv.writer(csvfile)
                movies.writerow(header)
                for x in data:
                    movies.writerow(x)
            elif option == "update":
                writer = csv.DictWriter(csvfile, fieldnames=header)
                writer.writeheader()
                writer.writerows(data)
            else:
                print("Option is not known")

    def mainRun():
        
        DisplayTitleBar()
        DisplayMenuOptions()
        WorkExecuteOperation()


e = car()
