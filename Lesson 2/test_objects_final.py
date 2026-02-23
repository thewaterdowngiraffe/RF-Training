import pytest
from vehicles import car, motorcycle, plane


@pytest.mark.parametrize("top_speed", [0, 100, None])
@pytest.mark.parametrize("passengers", [2, 3, None])
@pytest.mark.parametrize("vehicle_type", ["sport", "coup", None])
def test_car(top_speed, passengers, vehicle_type):
    data = {
        "top_speed": top_speed,
        "passengers": passengers,
        "vehicle_type": vehicle_type
    }
    filtered_dict = {key: value for key,
                     value in data.items() if value is not None}
    mycar = car(**filtered_dict)
    assert mycar.top_speed == filtered_dict.get("top_speed", 140)
    assert mycar.passengers == filtered_dict.get("passengers", 3)
    assert mycar.vehicle_type == filtered_dict.get("vehicle_type", "car")


@pytest.mark.parametrize("top_speed", [205, 260, None])
@pytest.mark.parametrize("passengers", [0, 1, None])
@pytest.mark.parametrize("vehicle_type", ["sport", "harly", None])
def test_motorcycle(top_speed, passengers, vehicle_type):
    data = {
        "top_speed": top_speed,
        "passengers": passengers,
        "vehicle_type": vehicle_type
    }
    filtered_dict = {key: value for key,
                     value in data.items() if value is not None}

    mymotorcycle = motorcycle(**filtered_dict)
    assert mymotorcycle.top_speed == filtered_dict.get("top_speed", 200)
    assert mymotorcycle.passengers == filtered_dict.get("passengers", 1)
    assert mymotorcycle.vehicle_type == filtered_dict.get(
        "vehicle_type", "motorcycle")


@pytest.mark.parametrize("top_speed", [75, 2534, None])
@pytest.mark.parametrize("passengers", [1, 200, None])
@pytest.mark.parametrize("vehicle_type", ["high-wing", "fighter jet", None])
def test_plane(top_speed, passengers, vehicle_type):
    data = {
        "top_speed": top_speed,
        "passengers": passengers,
        "vehicle_type": vehicle_type
    }
    filtered_dict = {key: value for key,
                     value in data.items() if value is not None}

    myplane = plane(**filtered_dict)
    assert myplane.top_speed == filtered_dict.get("top_speed", 700)
    assert myplane.passengers == filtered_dict.get("passengers", 50)
    assert myplane.vehicle_type == filtered_dict.get("vehicle_type", "plane")
