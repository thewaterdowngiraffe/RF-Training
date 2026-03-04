import pytest
from vehicles import car, motorcycle, plane


@pytest.mark.parametrize("item", [car(), motorcycle(), plane()])
def test_get_speed(item):
    for _ in range(10000):
        item.get_speed()
    assert item.top_speed == item.get_speed(
    ), "failed to reach top speed after 10000 steps"


@pytest.mark.parametrize("item", [car(), motorcycle(), plane()])
def test_get_speed_done(item):
    item.done = True
    for _ in range(10000):
        item.get_speed()
    assert 0 == item.get_speed(
    ), "failed to reach top speed after 10000 steps"
