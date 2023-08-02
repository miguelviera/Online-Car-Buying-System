# /****************************************
# * Student Name: Miguel Viera Hernandez
# * Date Due: July 19, 2023
# * Date Submitted: July 13, 2023
# * Program Name: Online Car Buying System
# * Program Description: This is a simple Online Car Buying System program that allows administrators to keep track of cars and customers information. Customers can also buy cars using the program.
# ****************************************/


# Car section
print('Program: Online Car Buying System')

class Automobile:
    def __init__(self):
        self._make = ''
        self._model = ''
        self._type = ''
        self._year = 0
        self._mileage = 0
        self._color = ''
        self._price = 0
    def addVehicle(self):
        try:
            self._make = input('Enter vehicle make: ')
            self._model = input('Enter vehicle model: ')
            self._type = input('Enter vehicle body type: ')
            self._year = int(input('Enter vehicle year: '))
            self._mileage = int(input('Enter vehicle mileage: '))
            self._color = input('Enter vehicle color: ')
            self._price = int(input('Enter vehicle price: '))
            return True
        except ValueError:
            print('Please try entering vehicle information again using only whole numbers for mileage and year')
            return False
    def __str__(self):
        return '\t'.join(str(x) for x in [self._make, self._model, self._type, self._year, self._mileage, self._color, self._price])
    
# Inventory section
class Inventory:
    def __init__(self):
        self.vehicles = ['\t'.join(str(x) for x in ["Toyota", "Corolla", "Sedan", 2022, 20000, "White", 25000]), '\t'.join(str(x) for x in ["Toyota", "Camry", "Sedan", 2010, 10000, "Black", 5000]),
                         '\t'.join(str(x) for x in ["Honda", "Civic", "Sedan", 2011, 130000, "Blue", 6000]), '\t'.join(str(x) for x in ["Nissan", "Maxima", "Sedan", 2015, 80000, "Red", 14000])]
    def addVehicle(self):
        vehicle = Automobile()
        if vehicle.addVehicle() == True:
            self.vehicles.append(vehicle)
            print ("")
            print('This vehicle has been added, Thank you')
            # print ("")
    def viewInventory(self):
        print("Inventory List:")
        print('\t'.join(['Id', 'Make', 'Model', 'Type', 'Year', 'Mileage', 'Color', 'Price']))
        for idx, vehicle in enumerate(self.vehicles) :
            print(idx + 1, end='\t')
            print(vehicle)
        # print("")

inventory = Inventory()

# Customer section
class Customer:
    def __init__(self):
        self._name = ''
        self._address = ''
        self._email = 0
        self._phone = ''
        
    def addCustomer(self):
            self._name = input('Enter customer name: ')
            self._address = input('Enter customer address: ')
            self._email = input('Enter customer email: ')
            self._phone = input('Enter customer phone with format(XXX)-XXX-XXXX: ')
            return True
    def __str__(self):
        return '\t'.join(str(x) for x in ["Name: " + self._name, "Address: " + self._address, "Email: " + self._email, "Phone: " + self._phone])

class CustomerList:
    def __init__(self):
        self.customers = ['\t'.join(str(x) for x in ["Name: Miguel Viera", "Address: 300 Forrest, Nashville Tn, 37211", "Email: viera@gmail.com", "Phone: (615)-999-9874"]), 
                         '\t'.join(str(x) for x in ["Name: Miguel Hernandez", "Address: 200 Forrest, Nashville Tn, 37211", "Email: hernandez@gmail.com", "Phone: (615)-999-5474"]), 
                         '\t'.join(str(x) for x in ["Name: Luis Gonzalez", "Address: 300 Street, Nashville Tn, 37211", "Email: gonzalez@gmail.com", "Phone: (615)-459-9874"]),
                         '\t'.join(str(x) for x in ["Name: Carlos Iglesias", "Address: 800 Harding Place, Nashville Tn, 37211", "Email: carlos@gmail.com", "Phone: (645)-999-9874"])]
    def addCustomer(self):
        customer = Customer()
        if customer.addCustomer() == True:
            self.customers.append(customer)
            print ()
            print('This customer has been added, Thank you')
            # print ()
    def viewCustomerList(self):
        print("Customer List:")
        for idx, customer in enumerate(self.customers) :
            print("Id: " + str(idx + 1), end='\t')
            print(customer)
        # print ()

customerList = CustomerList()

# Loop section
while True:
    print("")
    print("Options:")
    print('#1 Add Vehicle to Inventory')
    print('#2 Delete Vehicle from Inventory')
    print('#3 Update Vehicle in Inventory')
    print('#4 View Current Inventory')
    print('#5 Add customer to CustomerList')
    print('#6 Delete customer from CustomerList')
    print('#7 Update customer in CustomerList')
    print('#8 View Current CustomerList ')
    print('#9 Buy Car')
    print('#10 Quit')

    userInput=input('Please choose from one of the above options: ') 
    print("")
    if userInput=="1": 
        #add a vehicle
        inventory.addVehicle()
    elif userInput=='2':
        #delete a vehicle
        if len(inventory.vehicles) < 1:
            print('Sorry there are no vehicles currently in inventory')
            continue
        inventory.viewInventory()
        item = int(input('Please enter the number associated with the vehicle to be removed: '))
        if item - 1  > len(inventory.vehicles):
            print('This is an invalid number')
        else:
            inventory.vehicles.remove(inventory.vehicles[item - 1])
            print ()
            print('This vehicle has been removed')
    elif userInput == '3':
        #edit vehicle 
        if len(inventory.vehicles) < 1:
            print('Sorry there are no vehicles currently in inventory')
            continue
        inventory.viewInventory()
        item = int(input('Please enter the number associated with the vehicle to be updated: '))
        if item - 1  > len(inventory.vehicles):
            print('This is an invalid number')
        else:
            automobile = Automobile()
            if automobile.addVehicle() == True :
                inventory.vehicles.remove(inventory.vehicles[item - 1])
                inventory.vehicles.insert(item - 1, automobile)
                print ()
                print('This vehicle has been updated')

    elif userInput == '4':
        #list all the vehicles
        if len(inventory.vehicles) < 1:
            print('Sorry there are no vehicles currently in inventory')
            continue
        # print("")
        inventory.viewInventory()


    elif userInput=="5": 
        #add a customer
        customerList.addCustomer()
    elif userInput=='6':
        #delete a customer
        if len(customerList.customers) < 1:
            print('Sorry there are no customers currently in CustomerList')
            continue
        # print("")
        customerList.viewCustomerList()
        item = int(input('Please enter the number associated with the customer to be removed: '))
        if item - 1  > len(customerList.customers):
            print('This is an invalid number')
        else:
            customerList.customers.remove(customerList.customers[item - 1])
            print ()
            print('This customer has been removed')
    elif userInput == '7':
        #edit customer 
        if len(customerList.customers) < 1:
            print('Sorry there are no customers currently in CustomerList')
            continue
        customerList.viewCustomerList()
        item = int(input('Please enter the number associated with the customer to be updated: '))
        if item - 1  > len(customerList.customers):
            print('This is an invalid number')
        else:
            customer = Customer()
            if customer.addCustomer() == True :
                customerList.customers.remove(customerList.customers[item - 1])
                customerList.customers.insert(item - 1, customer)
                print ()
                print('This customer has been updated')

    elif userInput == '8':
        #list all the customers
        if len(customerList.customers) < 1:
            print('Sorry there are no customers currently in CustomerList')
            continue
        # print("")
        customerList.viewCustomerList()
     
    elif userInput == '9':
        if len(inventory.vehicles) < 1:
            print('Sorry there are no vehicles currently in inventory')
            continue
        
        customerList.viewCustomerList()
        print("")
        print("Who is buying the car?")
        customerRegistrationInput = input('Please enter "yes" if you are registered in the customer list above, or enter any other key to continue: ').lower()
        
        if customerRegistrationInput == "yes":
            customerIdInput = int(input("Please enter your Id number: ")) - 1
            print("Welcome: " + customerList.customers[customerIdInput].split()[1])
            print("")
            inventory.viewInventory()
            carInput = int(input('Please select the number of the car you want to buy: ')) - 1
            print("")
            print("Monthly payment calculator:")
            print("Car Price: " + inventory.vehicles[carInput].split()[-1])
            cardownpayment = float(input('Please input downpayment: ')) 
            Loanterms = float(input('Please input loan terms(months): ')) 
            monthlypayment = (float(inventory.vehicles[carInput].split()[-1]) - cardownpayment) / Loanterms
            print("Your monthly payment is: " + str(monthlypayment))
            print("")
            print("Congratulations " + customerList.customers[customerIdInput].split()[1] + " for buying the " + inventory.vehicles[carInput].split()[0] + " " + inventory.vehicles[carInput].split()[1] + "! Enjoy your new ride!")

            inventory.vehicles.remove(inventory.vehicles[carInput])
            print("The car has been sold and removed from the inventory")
        else:
            print("")
            print("Please first register into the system by selecting the option #5 and then proceed to buy the car")


    elif userInput == '10':
        #exit the loop
        print('Goodbye')
        break
    else:
        #invalid user input
        print('This is an invalid input. Please try again.')

