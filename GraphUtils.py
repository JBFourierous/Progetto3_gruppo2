class Airport:
    """
    Classe che definisce un aeroporto, di cui si conservano i seguenti attributi:
    name: nome dell'aeroporto
    coincidence: tempo minimo di scalo per le coincidenze
    """
    __slots__ = "name", "coincidence"


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