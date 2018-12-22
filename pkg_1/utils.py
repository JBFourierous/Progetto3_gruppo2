from Progetto3_gruppo2.pkg_1.Flight import Flight, Airport
from datetime import time
from typing import List
from typing import Dict

def c(a: Airport) -> int:
    """
    Restituisce il tempo minimo di coincidenza per un aeroporto
    :param a: Aeroporto di interesse
    :return: tempo di coincidenza minimo dell'aeroporto
    """
    return a.getCoincidence()


def s(f: Flight) -> Airport:
    """
    Restituisce l'aeroporto di partenza di un volo
    :param f: Volo di interesse
    :return: Aeroporto di partenza del volo
    """
    return f.getStart()


def d(f: Flight) -> Airport:
    """
    Restituisce l'aeroporto di arrivo di un volo
    :param f: Volo di interesse
    :return: Aeroporto di arrivo del volo
    """
    return f.getDestination()


def l(f: Flight) -> time:
    """
    Restituisce l'orario di partenza di un volo
    :param f: Volo di interesse
    :return: Orario di partenza del volo
    """
    return f.getLeaveTime()


def a(f: Flight) -> time:
    """
    Restituisce l'orario di arrivo di un volo
    :param f: Volo di interesse
    :return: Orario di arrivo del volo
    """
    return f.getArrivalTime()


def p(f: Flight) -> int:
    """
    Restituisce il numero di posti di un volo
    :param f: Volo di interesse
    :return: Numero di posti del volo
    """
    return f.getPlaces()


def initialize_schedule(airports_file: str, flights_file: str) -> (List[Airport], Dict[Airport, List[Flight]]):
    """
    Funzione che legge da file i dati riguardanti aeroporti e voli e inizializza l'orario della compagnia
    :param airports_file: file contenente i dati degli aeroporti
    :param flights_file: file contenente i dati dei voli
    :return: lista degli aeroporti, lista dei voli
    """
    airports = list()
    flights = list()
    schedule = dict()
    file1, file2 = None, None
    try:
        file1 = open(airports_file, "r")
        file2 = open(flights_file, "r")
    except FileNotFoundError:
        print("File " + airports_file + "or " + flights_file + " not found")
    for line in file1:
        tmp = line.split(" ")
        airport_name = tmp[0]
        airport_coincidence = tmp[1]
        new_airport = Airport(airport_name, int(airport_coincidence))
        airports.append(new_airport)
        schedule[new_airport] = list()

    for line in file2:
        tmp = line.split(" ")
        start = int(tmp[0])
        destination = int(tmp[1])
        left = tmp[2]
        arrival = tmp[3]
        places = tmp[4]
        new_flight = Flight(airports[start], airports[destination], time(int(left.split(":")[0]), int(left.split(":")[1])),
                              time(int(arrival.split(":")[0]), int(arrival.split(":")[1])), int(places))
        schedule[airports[start]].append(new_flight)
    return airports, schedule


if __name__ == "__main__":
    a, b = initialize_schedule("airports.txt", "flight.txt")
    for air in a:
        print(air)

    for air, f in b.items():
        print(air)
        for pippo in f:
            print(pippo)
