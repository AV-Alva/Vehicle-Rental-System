from .vehicle import Vehicle
from .logger_config import logger


class Bike(Vehicle):
    """Child class representing a bike."""

    def __init__(
        self,
        vehicle_number,
        brand,
        model,
        rental_price_per_day,
        engine_capacity
    ):
        super().__init__(
            vehicle_number,
            brand,
            model,
            rental_price_per_day
        )

        self.engine_capacity = engine_capacity

        logger.info(
            f"Bike created: {vehicle_number}, "
            f"Engine: {engine_capacity}cc"
        )

    def display_details(self):
        super().display_details()
        print(f"Engine Capacity: {self.engine_capacity}cc")