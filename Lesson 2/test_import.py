import pytest


def test_vehicles():
    try:
        import vehicles
        return None
    except ImportError:
        raise ImportError("Failed to see the vehicles.py file")


def test_car():
    try:
        from vehicles import car
        return None
    except ImportError:
        raise ImportError("failed to create the car class")


def test_motorcycle():
    try:
        from vehicles import motorcycle
        return None
    except ImportError:
        raise ImportError("failed to create the motorcycle class")


def test_plane():
    try:
        from vehicles import plane
        return None
    except ImportError:
        raise ImportError("failed to create the plane class")
