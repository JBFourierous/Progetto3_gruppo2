class Airport:
    """
    Classe che definisce un aeroporto, di cui si conservano le seguenti informazioni:
    name: nome dell'aeroporto
    coincidence: tempo minimo di coincidenza da spendere nell'aeroporto
    """
    __slots__ = "name", "coincidence"

    def __init__(self, name: str, coincidence: int):
        self.name = name
        self.coincidence = coincidence

    def __eq__(self, other) -> bool:
        return self.name == other.getName()

    def getName(self) -> str:
        return self.name

    def getCoincidence(self) -> int:
        return self.coincidence

