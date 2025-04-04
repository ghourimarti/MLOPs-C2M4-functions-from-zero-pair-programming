# write test cases for the logistics.py file
from mylib.logistics import (
    calculate_distance,
    calculate_time,
    find_coordinates,
    list_cities_with_coordinates,
)
import pytest

# Mock data for testing
cities_coordinates = {
    "New York": (40.7128, -74.0060),
    "Los Angeles": (34.0522, -118.2437),
    "Chicago": (41.8781, -87.6298),
}


def test_calculate_distance():
    # Test with known coordinates
    coord1 = (40.7128, -74.0060)  # New York
    coord2 = (34.0522, -118.2437)  # Los Angeles
    expected_distance = 2450.9503446683375  # Approximate distance in kilometers
    assert abs(calculate_distance(coord1, coord2) - expected_distance) < 1

    # Test with same coordinates (distance should be 0)
    coord1 = (40.7128, -74.0060)
    coord2 = (40.7128, -74.0060)
    assert calculate_distance(coord1, coord2) == 0


def test_calculate_time():
    # Test with known distance and speed
    distance = 100  # kilometers
    speed = 50  # kilometers per hour
    expected_time = 2.0  # hours
    assert calculate_time(distance, speed) == expected_time


#
def test_find_coordinates():
    # Test with known city
    city = "New York"
    expected_coordinates = (40.7128, -74.0060)
    assert find_coordinates(city) == expected_coordinates

    # Test with unknown city (should raise ValueError)
    with pytest.raises(ValueError):
        find_coordinates("Unknown City")
    # Test with empty city name (should raise ValueError)
    with pytest.raises(ValueError):
        find_coordinates("")
    # Test with city name containing special characters (should raise ValueError)
    with pytest.raises(ValueError):
        find_coordinates("New@York")
    # Test with city name containing numbers (should raise ValueError)
    with pytest.raises(ValueError):
        find_coordinates("New York 123")
    # Test with city name containing spaces (should raise ValueError)
    with pytest.raises(ValueError):
        find_coordinates("New York City")
    # Test with city name containing only spaces (should raise ValueError)
    with pytest.raises(ValueError):
        find_coordinates("   ")


# def test_list_cities_with_coordinates():
#     # Test if the function returns the correct dictionary
#     expected_coordinates = {
#         "New York": (40.7128, -74.0060),
#         "Los Angeles": (34.0522, -118.2437),
#         "Chicago": (41.8781, -87.6298),
#     }


#     assert expected_coordinates in list_cities_with_coordinates().items()

#     # Test if the function returns a dictionary
#     assert isinstance(list_cities_with_coordinates(), dict)
