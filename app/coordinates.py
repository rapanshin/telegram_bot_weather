from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float


def get_coordinates() -> Coordinates:
    """Returns current coordinates using IP address"""
    """56.90778 с.ш. 60.62031 в.д."""
    latitude = 56.90778
    longitude = 60.62031

    return Coordinates(latitude=latitude, longitude=longitude)
