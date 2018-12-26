from datetime import timedelta


class Airport:
    """
    Classe che definisce un aeroporto, di cui si conservano le seguenti informazioni:
    name: nome dell'aeroporto
    coincidence: tempo minimo di coincidenza da spendere nell'aeroporto
    """
    __slots__ = "name", "coincidence"

    def __init__(self, name: str, coincidence: timedelta):
        self.name = name
        self.coincidence = coincidence

    def __hash__(self) -> int:
        return hash((self.name, self.coincidence))

    def __eq__(self, other) -> bool:
        return self.name == other.getName()

    def __contains__(self, item):
        return self.name == item.name

    def __str__(self) -> str:
        return self.name + " " + str(self.coincidence)

    def getName(self) -> str:
        return self.name

    def getCoincidence(self) -> timedelta:
        return self.coincidence

