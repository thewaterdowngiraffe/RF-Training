import pytest
from vehicles import car, motorcycle, plane


def test_car():
    mycar = car()
    assert mycar.top_speed == 140
    assert mycar.passengers == 3
    assert mycar.vehicle_type == "car"


def test_motorcycle():
    mymotorcycle = motorcycle()
    assert mymotorcycle.top_speed == 200
    assert mymotorcycle.passengers == 1
    assert mymotorcycle.vehicle_type == "motorcycle"


def test_plane():
    myplane = plane()
    assert myplane.top_speed == 700
    assert myplane.passengers == 50
    assert myplane.vehicle_type == "plane"
