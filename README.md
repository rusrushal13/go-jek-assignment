# Parking Lot

**Question** : Design a Parking lot which can hold `n` Cars. Every car been issued a ticket for a slot and the slot been assigned based on the nearest to the entry. The system should also return some queries such as:

- Registration numbers of all cars of a particular colour.
- Slot number in which a car with a given registration number is parked.
- Slot numbers of all slots where a car of a particular colour is parked.

**Approach**: A car consist of Registration number, slot number and it's colour. Likewise our Parking Lot consist slots. For not making it too complicated, I choose a python dictionary for storing cars on slots and implemented the functionalities as accordingly.

## Commands for application

- `create_parking_lot`
- `park`
- `leave`
- `status`
- `slot_numbers_for_cars_with_colour`
- `slot_number_for_registration_number`
- `registration_numbers_for_cars_with_colour`

## Running the application

Running the application in Interactive mode:

```python
./ParkingLot.py
```

Running the application in File mode:

```python
./ParkingLot.py input.txt
```

## Running the application in a Docker Container

Build the image:

```python
docker build -t parkinglot:1.0 .
```

Running the application in Interactive mode:

```python
docker run -it parkinglot:1.0 ./ParkingLot.py
```

Running the application in File mode:

```python
docker run -it parkinglot:1.0 ./ParkingLot.py input.txt
```

## Possible errors

When using running application in Docker, if it gives this error:

```bash
docker: Error response from daemon: OCI runtime create failed: container_linux.go:348: starting container process caused "exec: \"./ParkingLot.py\": permission denied": unknown.
```

just change the permissions by running

```bash
sudo chmod +x ./ParkingLot.py
```