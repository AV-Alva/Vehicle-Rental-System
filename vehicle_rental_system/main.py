from vehicle_rental import (
    Car,
    Bike,
    InvalidRentalDaysError,
    InvalidRentalPriceError
)

from vehicle_rental.logger_config import logger


def rent_vehicle(vehicle, days):
    """Display vehicle details and calculate rental cost."""

    try:
        print("\n" + "=" * 45)

        vehicle.display_details()

        print(f"Rental Days    : {days}")

        total_rent = vehicle.calculate_rent(days)

        print(f"Total Rent     : ₹{total_rent}")

        print("=" * 45)

    except InvalidRentalDaysError as error:
        print(f"Rental Error: {error}")
        logger.error(f"Rental failed: {error}")

    except Exception as error:
        print(f"Unexpected Error: {error}")
        logger.exception("Unexpected error occurred")


def main():

    try:
        # Create 2 Cars
        car1 = Car(
            "KA01AB1234",
            "Toyota",
            "Innova",
            3500,
            7
        )

        car2 = Car(
            "KA02CD5678",
            "Hyundai",
            "Creta",
            2800,
            5
        )

        # Create 2 Bikes
        bike1 = Bike(
            "KA03EF1111",
            "Royal Enfield",
            "Classic 350",
            1200,
            350
        )

        bike2 = Bike(
            "KA04GH2222",
            "Honda",
            "Activa",
            600,
            110
        )

        # Demonstrate rentals
        rent_vehicle(car1, 3)
        rent_vehicle(car2, 5)
        rent_vehicle(bike1, 2)
        rent_vehicle(bike2, 4)

        # Demonstrate exception handling
        print("\nTesting invalid rental duration...")

        rent_vehicle(car1, 0)

    except InvalidRentalPriceError as error:
        print(f"Vehicle Creation Error: {error}")
        logger.error(f"Vehicle creation failed: {error}")

    except Exception as error:
        print(f"Unexpected Application Error: {error}")
        logger.exception("Critical application error")


if __name__ == "__main__":
    main()