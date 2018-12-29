from datetime import timedelta, datetime
from pkg_1.Airport import Airport


class Flight:
    """
    Classe che definisce un volo, di cui si conservano i seguenti attributi:
    start: Airport di partenza
    destination: Airport di arrivo
    left: orario di partenza
    arrival: orario di arrivo
    places: numero di posti disponibili sul volo
    """
    __slots__ = "start", "destination", "date", "leave", "arrival", "places"

    def __init__(self, start: Airport, destination: Airport, date: datetime, leave: timedelta, arrival: timedelta, places: int):
        self.start = start
        self.destination = destination
        self.date = date
        self.leave = leave
        self.arrival = arrival
        self.places = places

    def __eq__(self, o: object) -> bool:
        return self.start == o.getStart() and self.destination == o.getDestination() and self.leave == o.getLeaveTime() \
                        and self.arrival == o.getArrivalTime() and self.places == o.getPlaces()

    def __hash__(self) -> int:
        return hash((self.start, self.destination, self.leave, self.arrival, self.places))

    def __str__(self) -> str:
        return self.start.getName() + " " + self.getDestination().getName() + " " +\
               str(datetime.strftime(self.getDate(), "%Y/%m/%d")) + " " + str(self.leave) + " " + \
               str(self.arrival) + " " + str(self.getPlaces())

    def getDate(self) -> datetime:
        return self.date

    def getLeaveTime(self) -> timedelta:
        evaluate_date = self.getDate() - datetime.strptime(
            "1-1-"+str(self.getDate().year),
            "%d-%m-%Y")
        # print(isinstance(self.leave + evaluate_date, timedelta))
        return self.leave + evaluate_date

    def getArrivalTime(self) -> timedelta:
        evaluate_date = self.getDate() - datetime.strptime(
            "1-1-" + str(self.getDate().year),
            "%d-%m-%Y")
        if self.leave > self.arrival:
            evaluate_date += timedelta(days=1)
        return self.arrival + evaluate_date

    def getStart(self) -> Airport:
        return self.start

    def getDestination(self) -> Airport:
        return self.destination

    def getPlaces(self) -> int:
        return self.places

