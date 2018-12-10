class Airport:
    """
    Classe che definisce un aeroporto, di cui si conservano i seguenti attributi:
    name: nome dell'aeroporto
    coincidence: tempo minimo di scalo per le coincidenze
    """
    __slots__ = "name", "coincidence"

    def __eq__(self, other):
        return self.name == other.getName()

    def getName(self):
        return self.name

    def getCoincidence(self):
        return self.coincidence


class Flight:
    """
    Classe che definisce un volo, di cui si conservano i seguenti attributi:
    start: Airport di partenza
    destination: Airport di arrivo
    left: orario di partenza
    arrival: orario di arrivo
    places: numero di posti disponibili sul volo
    """
    __slots__ = "start", "destination", "left", "arrival", "places"

    def getLeaveTime(self):
        return self.left

    def getArrivalTime(self):
        return self.arrival

    def getDuration(self):
        return self.arrival - self.left