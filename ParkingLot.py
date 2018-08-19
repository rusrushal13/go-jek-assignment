#!/usr/bin/env python3

import sys
from Constants import *
from Utilities import (ParkingLot, createParkingLot, parkCar, carDeparture,
                       lotStatus, carByColour, slotByCarNumber, slotByColour)


def executeCommand(parkingLot, command):
    if command[0] == CREATE_PARKING_LOT:
        parkingLot = createParkingLot(int(command[1]))
    elif command[0] == PARK_CAR:
        parkCar(parkingLot, command[1], command[2])
    elif command[0] == CAR_DEPARTURE:
        carDeparture(parkingLot, command[1])
    elif command[0] == LOT_STATUS:
        lotStatus(parkingLot)
    elif command[0] == SEARCH_SLOT_BY_CAR_NUMBER:
        slotByCarNumber(parkingLot, command[1])
    elif command[0] == SEARCH_CAR_BY_COLOUR:
        carByColour(parkingLot, command[1])
    elif command[0] == SEARCH_SLOT_BY_COLOUR:
        slotByColour(parkingLot, command[1])
    else:
        print('Command is not applicable')
    return parkingLot


def commandMode(parkingLot):
    try:
        command = input().split()
        while command[0] != EXIT:
            parkingLot = executeCommand(parkingLot, command)
            command = input().split()
    except Exception as e:
        print(e)


def fileReaderMode(parkingLot, fileName):
    try:
        with open(fileName) as file:
            commands = file.readlines()
            for command in commands:
                parkingLot = executeCommand(
                    parkingLot, command.replace('\n', '').split())
    except Exception as e:
        print(e)


def main():
    parkingLot = None
    if len(sys.argv) > 1:
        fileReaderMode(parkingLot, sys.argv[1])
    else:
        commandMode(parkingLot)


if __name__ == '__main__':
    main()
