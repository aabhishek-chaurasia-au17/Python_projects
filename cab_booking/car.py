import csv
import math
from show import show

directory = "H:\\attainU\\python\\Python_projects\\cab_booking\\database\\"

a = show()


class car:
    def __init__(self):
        pass

    def addRider(self):
        # a = show()
        print("PLEASE ADD RIDER DETAILS")
        Name = input("Please Enter Your Name: ")
        Age = input("Please Enter Your Age: ")
        Gender = input("Please Enter Your Gender: ")
        Contact = input("Please Enter Your Contact: ")
        filename = directory+"Rider.csv"
        header = ("Name", "Age", "Gender", "Contact")
        data = [(Name, Age, Gender, Contact)]
        # writer(header, data, filename, "write")
        print("!!!Welcome", Name, "Have a Great Experience!!!")
        a.show()

    def addCab_Driver(self):
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
        a.show()

    def UpdateCabLocation(self):
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
        show()

    def update_cab_switch(self):
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
        show()

    def update_trip_end(self):
        print("PLEASE END THE TRIP")
        CabName = input("PLEASE ENTER THE CAB NUMBER FOR TRIP: ")
        filename = directory+"Booking.csv"
        with open(filename, newline="") as file:
            readData = [row for row in csv.DictReader(file)]

        for val in readData:
            if(val['CabNumber'] == CabName):
                readHeader = val.keys()
                val['TripEnd'] = "YES"
                writer(readHeader, readData, filename, "update")
        print("Trip Ended Successfully!!!")
        show()

    def update_fetch_history(self):
        print("PLEASE FETCH THE HISTORY")
        Name = input("PLEASE ENTER THE NAME FOR HISTORY: ")
        filename = directory+"Booking.csv"
        with open(filename, newline="") as file:
            readData = [row for row in csv.DictReader(file)]
        for val in readData:
            if(val['Name'] == Name):
                print(val)

        print("End Of History!!!")
        show()

    def book_cab(self):
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
        show()

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


c = car()
