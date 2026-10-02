class InvalidRentalDaysError(Exception):
    """Raised when rental days are zero or negative."""
    pass


class InvalidRentalPriceError(Exception):
    """Raised when rental price is zero or negative."""
    pass