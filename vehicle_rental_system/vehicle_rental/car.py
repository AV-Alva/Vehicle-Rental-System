from .vehicle import Vehicle
from .logger_config import logger


class Car(Vehicle):
    """Child class representing a car."""

    def __init__(
        self,
        vehicle_number,
        brand,
        model,
        rental_price_per_day,
        number_of_seats
    ):
        super().__init__(
            vehicle_number,
            brand,
            model,
            rental_price_per_day
        )

        self.number_of_seats = number_of_seats

        logger.info(
            f"Car created: {vehicle_number}, Seats: {number_of_seats}"
        )

    def display_details(self):
        super().display_details()
        print(f"Number of Seats: {self.number_of_seats}")