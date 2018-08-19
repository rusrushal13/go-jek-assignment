class Car:
    """
    Car class
    """

    def __init__(self, registrationNumber, colour):
        """
        Constructor for Car object

        ARGS:
            registrationNumber(str) - given registration number of the car
            colour(str) - given colour of the car
        """
        self.carRegistrationNumber = registrationNumber
        self.carColour = colour
        self.carSlot = None

    def setSlot(self, slot):
        """
        Setter for slot

        ARGS:
            slot(int) - the allocated slot for the car
        """
        self.carSlot = slot

    def getSlot(self):
        """
        Getter for slot
        """
        return self.carSlot

    def getColour(self):
        """
        Getter for colour
        """
        return self.carColour

    def getRegistrationNumber(self):
        """
        Getter for Registration Number
        """
        return self.carRegistrationNumber


class ParkingLot:
    def __init__(self, size):
        """
        Constructor for Parking Lot

        ARGS:
            size(int) - size of the parking lot
        """
        self.parkedCars = 0
        self.slots = dict.fromkeys([i for i in range(1, int(size)+1)])

    def incrementParkedCars(self):
        """
        will increment the number of parked cars
        """
        self.parkedCars += 1

    def decrementParkedCars(self):
        """
        will decrement the number of parked cars
        """
        self.parkedCars -= 1

    def getParkedCars(self):
        """
        getter for the number of parked cars
        """
        return self.parkedCars

    def getSlots(self):
        """
        getter for the parking slots
        """
        return self.slots

    def setSlots(self, slot, value):
        """
        setter for parking slots

        ARGS:
            slot(int) - where to place the incoming value
            value(Nonetype or Car object) - for setting the value on the given slot
        """
        self.slots[slot] = value


def createParkingLot(size):
    """
    creates a parking lot

    ARGS:
        size(int) - size of the parking lot
    """
    parkingLot = ParkingLot(size)
    print('Created a parking slot with ' + str(size) + ' slots')
    return parkingLot


def parkingLotIsFull(parkingLot):
    """
    checks whether parking lot is full or not

    ARGS:
        parkingLot(ParkingLot Object)
    """
    return str(len(parkingLot.getSlots())) <= str(parkingLot.getParkedCars())


def parkCar(parkingLot, registrationNumber, colour):
    """
    will park the car in the parking lot and prints the allocated slot in the parking lot

    ARGS:
        parkingLot(ParkingLot Object)
        registrationNumber(str) - given registration number for the car
        colour(str) - given colour for the car
    """
    if parkingLot:
        if not parkingLotIsFull(parkingLot):
            parkingSlot = parkingLot.getSlots()
            for slot in parkingSlot.keys():
                if parkingSlot[slot] is None:
                    car = Car(registrationNumber, colour)
                    parkingLot.setSlots(slot, car)
                    car.setSlot(slot)
                    parkingLot.incrementParkedCars()
                    print('Allocated slot number: ' + str(slot))
                    break
        else:
            print('Sorry, parking lot is full')
    else:
        print("Parking lot is not defined")


def carDeparture(parkingLot, inputSlot):
    """
    will leave the parking lot from desired slot and prints the leaving slot

    ARGS:
        parkingLot(ParkingLot Object)
        inputSlot(str) - given slot number
    """
    if parkingLot:
        if not parkingLot.getParkedCars():
            print('Sorry, parking lot is empty')
        elif int(inputSlot) >= 1 and int(inputSlot) < len(parkingLot.getSlots()):
            parkingSlot = parkingLot.getSlots()
            value = parkingSlot.get(int(inputSlot), None)
            if value is not None:
                parkingLot.setSlots(int(inputSlot), None)
                parkingLot.decrementParkedCars()
                print('Slot number ' + str(inputSlot) + ' is free')
            else:
                print('No car at Slot number ' + str(inputSlot))
        else:
            print('Cannot exit slot: ' + inputSlot + ' as no such exist!')
    else:
        print("Parking lot is not defined")


def lotStatus(parkingLot):
    """
    return the status of Parking Lot

    ARGS:
        parkingLot(ParkingLot Object)
    """
    if parkingLot:
        print('Slot No.\tRegistration No\tColour')
        parkingSlot = parkingLot.getSlots()
        for parkedCar in parkingSlot.values():
            if parkedCar is not None:
                print(str(parkedCar.getSlot()) + '\t' +
                      parkedCar.getRegistrationNumber() + '\t' +
                      parkedCar.getColour())
    else:
        print("Parking lot is not defined")


def carByColour(parkingLot, inputColour):
    """
    prints the registration number of the cars for the given colour

    ARGS:
        parkingLot(ParkingLot Object)
        inputColour(str) - given Colour
    """
    if parkingLot:
        if not parkingLot.getParkedCars():
            print('Sorry, parking lot is empty', end=' ')
        else:
            flag = False
            parkingSlot = parkingLot.getSlots()
            for parkedCar in parkingSlot.values():
                if parkedCar is not None:
                    if parkedCar.getColour() == inputColour:
                        flag = True
                        print(parkedCar.getRegistrationNumber(), end=', ')
            if not flag:
                print('Not found', end=' ')
        print('\b \b')
    else:
        print("Parking lot is not defined")


def slotByColour(parkingLot, inputColour):
    """
    prints the slot number of the cars for the given colour

    ARGS:
        parkingLot(ParkingLot Object)
        inputColour(str) - given colour
    """
    if parkingLot:
        if not parkingLot.getParkedCars():
            print('Sorry, parking lot is empty', end=' ')
        else:
            flag = False
            parkingSlot = parkingLot.getSlots()
            for parkedCar in parkingSlot.values():
                if parkedCar is not None:
                    if parkedCar.getColour() == inputColour:
                        flag = True
                        print(str(parkedCar.getSlot()), end=', ')
            if not flag:
                print('Not found', end=' ')
        print('\b \b')
    else:
        print("Parking lot is not defined")


def slotByCarNumber(parkingLot, number):
    """
    prints the slot number of the cars for the given number

    ARGS:
        parkingLot(ParkingLot Object)
        number(str) - given registration number
    """
    if parkingLot:
        if not parkingLot.getParkedCars():
            print('Sorry, parking lot is empty', end=' ')
        else:
            flag = False
            parkingSlot = parkingLot.getSlots()
            for parkedCar in parkingSlot.values():
                if parkedCar is not None:
                    if parkedCar.getRegistrationNumber() == number:
                        flag = True
                        print(str(parkedCar.getSlot()), end=', ')
                        # assuming that for the cars, there is one and only one registration number exits
                        break
            if not flag:
                print('Not found', end=' ')
        print('\b \b \b')
    else:
        print("Parking lot is not defined")
