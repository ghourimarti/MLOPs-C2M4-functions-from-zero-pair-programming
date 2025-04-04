#!/usr/bin/env python3
from mylib.logistics import (
    calculate_distance,
    calculate_time,
    find_coordinates,
    list_cities_with_coordinates,
    calculate_logistics,
)
import click


@click.group()
def cli():
    """Logistics calculator CLI."""


# calculate distance between two points
@cli.command("distance")
@click.argument("city1")
@click.argument("city2")
@click.argument("speed", type=float)
def distance_command(city1, city2, speed):
    """Calculate the distance between two cities and the time taken to travel between them.
    :param city1: Name of the first city
    :param city2: Name of the second city
    :param speed: Speed in kilometers per hour
    :return: Distance in kilometers and time in hours
    """
    coord1 = find_coordinates(city1)
    coord2 = find_coordinates(city2)

    distance = calculate_distance(coord1, coord2)
    time = calculate_time(distance, speed)

    click.echo(f"Distance between {city1} and {city2}: {distance:.2f} km")
    click.echo(f"Time taken to travel at {speed} km/h: {time:.2f} hours")


# calculate time taken to travel a distance at a given speed
@cli.command("time")
@click.argument("distance", type=float)
@click.argument("speed", type=float)
def time_command(distance, speed):
    """Calculate the time taken to travel a distance at a given speed.
    :param distance: Distance in kilometers
    :param speed: Speed in kilometers per hour
    :return: Time in hours
    """
    time = calculate_time(distance, speed)
    click.echo(f"Time taken to travel {distance} km at {speed} km/h: {time:.2f} hours")


# calculate logistics for a given distance and speed
@cli.command("logistics")
@click.argument("distance", type=float)
@click.argument("speed", type=float)
@click.argument("city1")
@click.argument("city2")
def logistics_command(distance, speed, city1, city2):
    """Calculate the logistics for a given distance and speed.
    :param distance: Distance in kilometers
    :param speed: Speed in kilometers per hour
    :param city1: Name of the first city
    :param city2: Name of the second city
    :return: Logistics information
    """
    coord1 = find_coordinates(city1)
    coord2 = find_coordinates(city2)

    logistics_info = calculate_logistics(distance, speed, coord1, coord2)

    click.echo(f"Logistics information for {city1} and {city2}: {logistics_info}")


# find coordinates of a city
@cli.command("coordinates")
@click.argument("city")
def coordinates_command(city):
    """Find the coordinates of a city.
    :param city: Name of the city
    :return: Coordinates of the city
    """
    coord = find_coordinates(city)
    click.echo(f"Coordinates of {city}: {coord}")


# list all cities with their coordinates
@cli.command("list_cities")
def list_cities_command():
    """List all cities with their coordinates.
    :return: List of cities and their coordinates
    """
    cities = list_cities_with_coordinates()
    click.echo("Cities and their coordinates:")
    for city, coord in cities.items():
        click.echo(f"{city}: {coord}")
    click.echo("\n\n")


if __name__ == "__main__":
    cli()
