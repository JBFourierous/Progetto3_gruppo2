from datetime import time
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

    def __init__(self, start: Airport, destination: Airport, leave: time, arrival: time, places: int):
        self.start = start
        self.destination = destination
        self.leave = leave
        self.arrival = arrival
        self.places = places

    def getLeaveTime(self) -> time:
        return self.leave

    def getArrivalTime(self) -> time:
        return self.arrival

    def getStart(self) -> Airport:
        return self.start

    def getDestination(self) -> Airport:
        return self.destination

    def getPlaces(self) -> int:
        return self.places

