from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from mylib.logistics import (
    calculate_distance,
    calculate_time,
    find_coordinates,
    list_cities_with_coordinates,
)

from mylib.wiki import wiki_full_text, wiki_search, wiki_summary


app = FastAPI()


class City(BaseModel):
    name: str


@app.get("/")
async def root():
    """Home Page with GET HTTP Method"""

    return {"message": "Hello Logistics INC"}


@app.get("/cities")
async def cities():
    """List cities with GET HTTP Method

    Returns back a list of cities that are available to get further information about
    """

    return {"cities": list_cities_with_coordinates()}


# build a post method to calculate the travel time between two cities by car
@app.post("/travel")
async def travel(city1: City, city2: City):
    """Estimate travel time between two cities by car with POST HTTP Method

    Returns back the travel time between two cities by car.
    """
    print(f"city1: {city1}")
    print(f"city2: {city2}")
    # import ipdb; ipdb.set_trace() #found bug using this!
    # calculate the distance between the two cities
    travel_distance = calculate_distance(
        find_coordinates(city1.name), find_coordinates(city2.name)
    )
    # calculate the speed of the car
    travel_speed = 60
    # calculate the time taken to travel the distance
    # using the speed
    hours = calculate_time(travel_distance, travel_speed)
    print(f"hours: {hours}")
    return {"travel_time": f"{hours} hours"}


@app.post("/distance")
async def distance(city1: City, city2: City):
    """Calculate distance between two cities with POST HTTP Method

    Returns back the distance between two cities in miles
    """

    return {
        "distance": calculate_distance(
            find_coordinates(city1.name), find_coordinates(city2.name)
        )
    }


@app.post("/keywords")
async def keywords(city: City):
    """Get the top 10 keywords from the content of a page with POST HTTP Method
    Returns back the top 10 keywords from the content of a pagesss
    """

    return {
        "keywords": wiki_search(city.name),
        "summary": wiki_summary(city.name),
        "full_text": wiki_full_text(city.name),
    }


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
