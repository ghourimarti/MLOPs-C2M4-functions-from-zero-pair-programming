#!/usr/bin/env python3
"""
This module deals with logistics and calculates the distance between two points
and the time taken to travel between them and logistics-related calculations.
for a given speed.
"""

import math
import geopy
from geopy.distance import geodesic

# build  a list of 100 cities with their coordinates in united states
# Example coordinates for 10 cities in the United States
# Coordinates are in degrees and direction like North, south, east, west
cities_coordinates = {
    "New York": (40.7128, -74.0060),
    "Los Angeles": (34.0522, -118.2437),
    "Chicago": (41.8781, -87.6298),
    "Houston": (29.7604, -95.3698),
    "Phoenix": (33.4484, -112.0740),
    "Philadelphia": (39.9526, -75.1652),
    "San Antonio": (29.4241, -98.4936),
    "San Diego": (32.7157, -117.1611),
    "Dallas": (32.7767, -96.7970),
    "San Jose": (37.3382, -121.8863)
}


# build a function to calculate the distance between two coordinates
def calculate_distance(coord1, coord2):
    """
    Calculate the distance between two coordinates using geopy.
    :param coord1: Tuple of (latitude, longitude) for point 1
    :param coord2: Tuple of (latitude, longitude) for point 2
    :return: Distance in kilometers
    """
    print(f"Calculating distance between {coord1} and {coord2}")
    print(geodesic(coord1, coord2).kilometers)
    return geodesic(coord1, coord2).kilometers

def calculate_time(distance, speed):
    """
    Calculate the time taken to travel a distance at a given speed.
    :param distance: Distance in kilometers
    :param speed: Speed in kilometers per hour
    :return: Time in hours
    """
    if speed <= 0:
        raise ValueError("Speed must be greater than zero.")
    return distance / speed

# build a function to find co ordinates of city
def find_coordinates(city):
    """
    Find the coordinates of a city.
    :param city: Name of the city
    :return: Tuple of (latitude, longitude)
    """
    if city in cities_coordinates:
        return cities_coordinates[city]
    else:
        raise ValueError(f"City '{city}' not found in the list.")

# build list of cities with their coordinates
def list_cities_with_coordinates():
    """
    List all cities with their coordinates.
    :return: Dictionary of cities and their coordinates
    """
    return cities_coordinates

# call all the functions to check if they are working
if __name__ == "__main__":
    # Example usage
    city1 = "New York"
    city2 = "Los Angeles"
    speed = 60  # Speed in kilometers per hour

    coord1 = find_coordinates(city1)
    coord2 = find_coordinates(city2)

    distance = calculate_distance(coord1, coord2)
    time = calculate_time(distance, speed)

    print(f"Distance between {city1} and {city2}:       {distance:.2f} km")
    print(f"Time taken to travel at {speed} km/h:       {time:.2f} hours")
    print(f"Coordinates of {city1}:                     {coord1}")
    print(f"Coordinates of {city2}:                     {coord2}")
    print("\n\nList of cities with coordinates:")
    for city, coord in list_cities_with_coordinates().items():
        print(f"{city}: {coord}")