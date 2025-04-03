#!/usr/bin/env python3
from mylib.logistics import (
    calculate_distance,
    calculate_time,
    calculate_logistics,
    find_coordinates,
)
import click
import sys

@click.group()
def cli():
    """Logistics calculator CLI."""
    pass
    """
    This module is part of the mylib package.
    This is a simple logistics calculator CLI that calculates the distance and time
    taken to travel between two coordinates.
    - calculate_distance
    - calculate_time
    - calculate_logistics
    - find_coordinates
    """

