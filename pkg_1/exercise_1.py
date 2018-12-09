import datetime


class Schedule:
    def __init__(self):
        self.airports = dict()  # airports[a] = c(a)
        self.flights = dict()  # flights[f] = s(f), d(f), l(f), a(f), p(f)


class Route:
    def __init__(self):
        self.flights = list()
        self.duration = datetime.time()


def list_routes(s: Schedule, a: str, b: str, t: datetime.time, T: datetime.timedelta) -> Route:
    """
    La funzione restituisce tutte le rotte che consentono di andare da a a b con un durata
    complessiva del viaggio non superiore a T e con orario di partenza successivo a t.
    Una rotta è costituita da una sequenza di voli e la sua durata è data dalla somma delle
    durate di tutti i voli più i tempi di attesa negli scali per le coincidenze. Ad ogni
    scalo bisogna considerare che non è possibile effettuare una coincidenza se tra l’orario
    di atterraggio di un volo ed il tempo di decollo del volo successivo intercorre un tempo
    inferiore a c(a).
    :param s: orario della compagnia
    :param a: areoporto di partenza
    :param b: areoporto di arrivo
    :param t: orario di partenza
    :param T: intervallo di tempo
    :return: tutte le rotte che rispettano i vincoli imposti come (quale tipo di dato?)
    """
    pass


if __name__ == "__main__":
    s = Schedule()
    s.airports = {"MXP": datetime.time(1, 30)}
    s.flights = {4151: ("MXP", "CDG", datetime.time(6, 30), datetime.time(8, 5), 40)}

    # list_routes(s, "MXP", "BGY", datetime.time(6, 30), datetime.timedelta(minutes=30))
