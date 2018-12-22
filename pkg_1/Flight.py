from datetime import timedelta
from .Airport import Airport


class Flight:
    """
    Classe che definisce un volo, di cui si conservano i seguenti attributi:
    start: Airport di partenza
    destination: Airport di arrivo
    left: orario di partenza
    arrival: orario di arrivo
    places: numero di posti disponibili sul volo
    """
    __slots__ = "start", "destination", "leave", "arrival", "places"

    def __init__(self, start: Airport, destination: Airport, leave: timedelta, arrival: timedelta, places: int):
        self.start = start
        self.destination = destination
        self.leave = leave
        self.arrival = arrival
        self.places = places

    def __eq__(self, o: object) -> bool:
        return self.start == o.getStart() and self.destination == o.getDestination() and self.leave == o.getLeaveTime() \
                        and self.arrival == o.getArrivalTime() and self.places == o.getPlaces()

    def __hash__(self) -> int:
        return hash((self.start, self.destination, self.leave, self.arrival, self.places))

    def __str__(self) -> str:
        return self.start.getName() + " " + self.getDestination().getName() + " " + str(self.getLeaveTime()) + " " + \
               str(self.getArrivalTime()) + " " + str(self.getPlaces())

    def getLeaveTime(self) -> timedelta:
        return self.leave

    def getArrivalTime(self) -> timedelta:
        return self.arrival

    def getStart(self) -> Airport:
        return self.start

    def getDestination(self) -> Airport:
        return self.destination

    def getPlaces(self) -> int:
        return self.places

