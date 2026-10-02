# 🚗 Vehicle Rental System — Python OOP

## 📌 Project Overview

The **Vehicle Rental System** is a mini Python application developed to demonstrate important **Object-Oriented Programming (OOP)** concepts such as:

- Classes and Objects
- Constructors
- Inheritance
- Parent and Child Classes
- Method Overriding
- Static Methods
- Packages and Modules
- Exception Handling
- Custom Exceptions
- Logging

The application models a simple vehicle rental platform where customers can rent different types of vehicles such as **Cars** and **Bikes**.

The rental amount is calculated based on the vehicle's **rental price per day** and the **number of rental days**.

---

# 🎯 Objective

The objective of this project is to understand how a real-world vehicle rental application can be designed using Python OOP.

The system contains:

- A parent `Vehicle` class
- A child `Car` class
- A child `Bike` class
- Rental price calculation
- Rental duration validation
- Custom exception handling
- Application logging
- Modular package structure

---

# 🏗️ Class Structure

```text
              Vehicle
             /       \
           Car       Bike
```

### Vehicle

The `Vehicle` class is the **parent/base class**.

It contains common vehicle information:

- Vehicle number
- Brand
- Model
- Rental price per day

### Car

`Car` inherits from `Vehicle`.

In addition to the common vehicle information, it contains:

- Number of seats

### Bike

`Bike` also inherits from `Vehicle`.

It contains:

- Engine capacity

This demonstrates **inheritance**, where common functionality is written once in the parent class and reused by child classes.

---

# 📁 Project Structure

```text
vehicle_rental_system/
│
├── main.py
├── README.md
│
├── vehicle_rental/
│   ├── __init__.py
│   ├── vehicle.py
│   ├── car.py
│   ├── bike.py
│   ├── exceptions.py
│   └── logger_config.py
│
└── logs/
    └── rental.log
```

---

# 📄 Module Description

## `main.py`

This is the **entry point** of the application.

It:

- Creates Car objects
- Creates Bike objects
- Displays vehicle information
- Calculates rental charges
- Tests invalid rental duration
- Handles exceptions
- Records errors in the log file

---

## `vehicle.py`

Contains the parent `Vehicle` class.

Main attributes:

```python
vehicle_number
brand
model
rental_price_per_day
```

Main methods:

```python
display_details()
calculate_rent(days)
is_valid_rental_duration(days)
```

The `calculate_rent()` method calculates:

```text
Total Rent = Rental Price Per Day × Number of Days
```

Example:

```text
Rental Price = ₹3500/day
Rental Days  = 3

Total Rent = 3500 × 3
           = ₹10500
```

---

## `car.py`

Contains the `Car` child class.

```python
class Car(Vehicle):
```

`Car` inherits the properties and methods of `Vehicle`.

It adds one additional attribute:

```python
number_of_seats
```

For example:

```text
Toyota Innova
Seats: 7
Rental Price: ₹3500/day
```

---

## `bike.py`

Contains the `Bike` child class.

```python
class Bike(Vehicle):
```

It inherits from `Vehicle` and adds:

```python
engine_capacity
```

For example:

```text
Royal Enfield Classic 350
Engine Capacity: 350cc
Rental Price: ₹1200/day
```

---

## `exceptions.py`

Contains custom exceptions used by the application.

```python
InvalidRentalDaysError
InvalidRentalPriceError
```

For example, rental days must be greater than zero.

If someone tries:

```python
calculate_rent(0)
```

the program raises:

```text
InvalidRentalDaysError
```

instead of allowing an invalid rental.

---

## `logger_config.py`

Configures Python's `logging` module.

Application events are stored inside:

```text
logs/rental.log
```

The log records events such as:

```text
INFO - Vehicle created
INFO - Rent calculated
ERROR - Invalid rental duration
ERROR - Vehicle creation failed
```

Logging helps developers understand what happened inside an application without relying only on `print()` statements.

---

## `__init__.py`

The `__init__.py` file tells Python that `vehicle_rental` should be treated as a **package**.

It also exposes important classes and exceptions so they can be imported easily.

For example:

```python
from vehicle_rental import Car, Bike
```

instead of importing every class from its individual module.

---

# 🧠 OOP Concepts Used

| Concept | Implementation |
|---|---|
| Class | `Vehicle`, `Car`, `Bike` |
| Objects | `car1`, `car2`, `bike1`, `bike2` |
| Constructor | `__init__()` |
| Parent Class | `Vehicle` |
| Child Classes | `Car`, `Bike` |
| Inheritance | `Car(Vehicle)`, `Bike(Vehicle)` |
| `super()` | Calls parent class functionality |
| Instance Method | `calculate_rent()` |
| Static Method | `is_valid_rental_duration()` |
| Method Overriding | `display_details()` |
| Package | `vehicle_rental` |
| Modules | `vehicle.py`, `car.py`, `bike.py`, etc. |
| Custom Exceptions | `InvalidRentalDaysError` |
| Exception Handling | `try` and `except` |
| Logging | `logger.info()`, `logger.error()` |

---

# 🔄 Program Flow

The application follows this flow:

```text
START
  │
  ▼
main.py
  │
  ▼
Create Vehicle Objects
  │
  ├──── Car Objects
  │
  └──── Bike Objects
  │
  ▼
Display Vehicle Details
  │
  ▼
Enter / Provide Rental Days
  │
  ▼
Validate Rental Duration
  │
  ├── Invalid ──► Raise Exception
  │                 │
  │                 ▼
  │              Log Error
  │
  └── Valid
       │
       ▼
Calculate Rent
       │
       ▼
Rental Price × Days
       │
       ▼
Display Total Rent
       │
       ▼
Log Successful Operation
       │
       ▼
END
```

---

# 🧮 Static Method

The project contains a static method:

```python
@staticmethod
def is_valid_rental_duration(days):
    return days > 0
```

The method validates whether the rental duration is valid.

Examples:

```python
Vehicle.is_valid_rental_duration(5)
```

returns:

```text
True
```

while:

```python
Vehicle.is_valid_rental_duration(0)
```

returns:

```text
False
```

A static method is useful here because validating the number of rental days does not depend on the properties of a particular vehicle object.

---

# 🔗 Inheritance

Both `Car` and `Bike` inherit from `Vehicle`.

```python
class Car(Vehicle):
```

and

```python
class Bike(Vehicle):
```

Therefore, they automatically have access to functionality such as:

```python
calculate_rent()
```

without having to rewrite the same method in both child classes.

---

# ⬆️ Using `super()`

The child classes use:

```python
super().__init__()
```

to call the constructor of the parent `Vehicle` class.

They also use:

```python
super().display_details()
```

to reuse the parent's vehicle display functionality before displaying their own additional information.

This reduces duplicate code.

---

# ⚠️ Exception Handling

The project uses:

```python
try:
    # risky operation

except InvalidRentalDaysError:
    # handle invalid rental duration
```

For example, if the rental duration is:

```text
0 days
```

the application raises:

```text
InvalidRentalDaysError
```

with a message such as:

```text
Rental days must be greater than zero.
```

The error is handled gracefully instead of terminating the complete application unexpectedly.

---

# 📝 Logging

The project uses Python's built-in `logging` module.

Logs are stored inside:

```text
logs/rental.log
```

Example:

```text
INFO - Vehicle created: KA01AB1234 - Toyota Innova
INFO - Car created: KA01AB1234, Seats: 7
INFO - Rent calculated for KA01AB1234: 3 days = ₹10500
ERROR - Invalid rental duration for KA01AB1234: 0
```

Logging provides a history of important application activities and errors.

---

# 🚘 Vehicles Created

The demonstration creates at least **2 Cars and 2 Bikes**.

### Cars

```text
Toyota Innova
Hyundai Creta
```

### Bikes

```text
Royal Enfield Classic 350
Honda Activa
```

---

# ▶️ How to Run the Project

## Step 1 — Open the project

Open the following folder in VS Code:

```text
vehicle_rental_system
```

## Step 2 — Open Terminal

In VS Code:

```text
Terminal → New Terminal
```

## Step 3 — Run the program

Execute:

```bash
python main.py
```

---

# 💻 Sample Output

```text
=============================================
Vehicle Number : KA01AB1234
Brand          : Toyota
Model          : Innova
Price/Day      : ₹3500
Number of Seats: 7
Rental Days    : 3
Total Rent     : ₹10500
=============================================

=============================================
Vehicle Number : KA03EF1111
Brand          : Royal Enfield
Model          : Classic 350
Price/Day      : ₹1200
Engine Capacity: 350cc
Rental Days    : 2
Total Rent     : ₹2400
=============================================
```

---

# ❌ Invalid Rental Example

If the application attempts:

```python
rent_vehicle(car1, 0)
```

the static method detects that `0` is not a valid rental duration.

The application displays:

```text
Rental Error: Rental days must be greater than zero.
```

The error is also recorded in:

```text
logs/rental.log
```

---

# 🌍 Real-World Connection

This project represents the basic architecture behind vehicle rental platforms.

For example, a real system could contain:

```text
Vehicle
│
├── Car
├── Bike
├── Scooter
├── Truck
├── Van
└── ElectricVehicle
```

All vehicles could share common functionality such as:

```text
Vehicle Number
Brand
Model
Rental Price
Availability
Calculate Rent
```

while individual vehicle categories could contain their own specialized properties.

This is one of the major advantages of **inheritance**: common functionality can be reused while still allowing specialized child classes.

---

# 🚀 Possible Future Enhancements

The application can be extended with:

- Customer registration
- Vehicle availability checking
- Booking ID generation
- Rental start and end dates
- Discounts for longer rentals
- Security deposit calculation
- Vehicle return functionality
- Late return penalties
- Search vehicles by type
- Payment processing
- Database integration
- Menu-driven interface

---

# 📚 Learning Outcome

After completing this project, we understand how to:

1. Create parent and child classes.
2. Implement inheritance.
3. Use `super()`.
4. Override parent methods.
5. Create and use static methods.
6. Organize Python code using packages and modules.
7. Create custom exceptions.
8. Handle errors using `try` and `except`.
9. Record application activities using logging.
10. Model a real-world application using OOP.

---

## 🎓 Key Takeaway

Instead of writing separate and repetitive code for Cars and Bikes, we create a common `Vehicle` parent class.

```text
             VEHICLE
          Common Features
               │
        ┌──────┴──────┐
        ▼             ▼
       CAR           BIKE
      Seats      Engine Capacity
```

This makes the application **reusable, organized, maintainable, and easier to extend**.

---

**Project:** Vehicle Rental System  
**Language:** Python  
**Concept:** Object-Oriented Programming  
**Focus:** Inheritance, Static Methods, Packages, Modules, Exception Handling & Logging
