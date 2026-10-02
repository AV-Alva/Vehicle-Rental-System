from .exceptions import InvalidRentalDaysError, InvalidRentalPriceError
from .logger_config import logger


class Vehicle:
    """Parent class representing a rental vehicle."""

    def __init__(self, vehicle_number, brand, model, rental_price_per_day):
        if rental_price_per_day <= 0:
            logger.error(
                f"Invalid rental price for vehicle {vehicle_number}: "
                f"{rental_price_per_day}"
            )
            raise InvalidRentalPriceError(
                "Rental price per day must be greater than zero."
            )

        self.vehicle_number = vehicle_number
        self.brand = brand
        self.model = model
        self.rental_price_per_day = rental_price_per_day

        logger.info(
            f"Vehicle created: {vehicle_number} - {brand} {model}"
        )

    def display_details(self):
        print(f"Vehicle Number : {self.vehicle_number}")
        print(f"Brand          : {self.brand}")
        print(f"Model          : {self.model}")
        print(f"Price/Day      : ₹{self.rental_price_per_day}")

    @staticmethod
    def is_valid_rental_duration(days):
        """Return True if rental duration is greater than zero."""
        return days > 0

    def calculate_rent(self, days):
        """Calculate rent based on number of rental days."""

        if not Vehicle.is_valid_rental_duration(days):
            logger.error(
                f"Invalid rental duration for {self.vehicle_number}: {days}"
            )
            raise InvalidRentalDaysError(
                "Rental days must be greater than zero."
            )

        total_rent = self.rental_price_per_day * days

        logger.info(
            f"Rent calculated for {self.vehicle_number}: "
            f"{days} days = ₹{total_rent}"
        )

        return total_rent