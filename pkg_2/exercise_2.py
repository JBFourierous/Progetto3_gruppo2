from TdP_collections.priority_queue.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue
from typing import List
from typing import Dict
from Progetto3_gruppo2.pkg_1.Airport import Airport
from Progetto3_gruppo2.pkg_1.utils import *
from datetime import time


def find_route(schedule: Dict, airports: List, start: Airport, dest: Airport, t: time) -> List:
    """
    La funzione trova la rotta che permette di arrivare da a a b nel minor tempo
    possibile, partendo ad un orario non precedente a t. (Come per l’esercizio
    precedente, bisogna tener conto del tempo minimo di coincidenza di ogni
    scalo).
    :param schedule: orario della compagnia
    :param airports: lista degli aeroporti
    :param start: areoporto di partenza
    :param dest: areoporto di arrivo
    :param t: orario di partenza
    :return: la rotta che rispetta i vincoli imposti
    """
    path = list()                           # insieme dei voli che costituiscono il percorso più breve
    q = AdaptableHeapPriorityQueue()        # coda a priorità per Dijkstra
    cloud = dict()                          # insieme di nodi visitati da Dijkstra con loro costo
    costs = dict()                          # dizionario dei costi ottimi valutati da Dijkstra
    locators = dict()                       # dizionario dei locator per la coda q

    # fase di inizializzazione dei costi per ogni aeroporto, cioè i nodi del grafo delle rotte aeree
    for airport in airports:
        if airport == start:
            costs[airport] = 0
        else:
            costs[airport] = float('inf')
        # nella coda mantengo il riferimento ad aeroporto sorgente e destinazione, e all'istrante temporale di arrivo
        locators[airport] = q.add(costs[airport], (airport, None, t))

    while not q.is_empty():
        # prendi l'elemento a costo minore nella coda (aeroporto che si raggiunge con tempo minore)
        cost, (source, flight_taken, time) = q.remove_min()
        # salva l'ultimo volo preso per ragggiungere questo aeroporto
        cloud[source] = flight_taken
        # per ogni volo che parte da questo aeroporto (per ogni arco uscente dal nodo)
        for flight in schedule[source]:
            # se non ho già raggiunto l'aeroporto di destinazione del volo
            if d(flight) not in cloud:
                # se il volo è ammissibile
                if time + c(source) <= l(flight):
                    # se il costo per arrivarci è minore di quello noto fino ad ora, aggiornalo
                    if costs[source] + l(flight) - time + a(flight) - l(flight) < costs[d(flight)]:
                        costs[d(flight)] = costs[source] + l(flight) - time + a(flight) - l(flight)
                        # nella coda mantieni ora in corrispondenza di questo aeroporto il volo per raggiungerlo e
                        # l'ora in cui ci arrivi
                        q.update(locators[d(flight)], costs[d(flight)], (d(flight), flight, a(flight)))

    # ripercorro all'indietro i voli che mi portano a destinazione
    flight_to_take = cloud[dest]
    while flight_to_take is not None:
        # costruisco la rotta della soluzione
        path.insert(0, flight_to_take)
        flight_to_take = cloud[s(flight_to_take)]
    return path


