from TdP_collections.priority_queue.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue
from typing import Dict
from pkg_1.utils import Airport, List, d, l, a, c, s
from datetime import timedelta
from collections import deque


def find_route(schedule: Dict, airports: List, start: Airport, dest: Airport, t: timedelta) -> List:
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
    Complessità computazionale O((n+m) log n), ma si può ragionevolmente assumere che
    m >> n, per cui O(m log n), in cui n è il numero di aerporti ed m il numero di voli
    """
    path = deque()                          # insieme dei voli che costituiscono il percorso più breve
    q = AdaptableHeapPriorityQueue()        # coda a priorità per Dijkstra
    cloud = dict()                          # insieme di nodi visitati da Dijkstra con loro costo
    costs = dict()                          # dizionario dei costi ottimi valutati da Dijkstra
    locators = dict()                       # dizionario dei locators per la coda q

    # fase di inizializzazione dei costi per ogni aeroporto nella lista
    # n inserimenti => O(nlogn)
    for airport in airports:
        if airport == start:
            costs[airport] = timedelta(0)
        else:
            costs[airport] = timedelta(hours=1000)  # sintassi per +∞
        # nella coda mantengo il riferimento ad aeroporto sorgente, aeroporto destinazione e tempo di arrivo
        # salvo il locator per futuri aggiornamenti
        # ogni inserimento nella coda al più O(log n)
        locators[airport] = q.add(costs[airport], (airport, None, t))

    # la valutazione della lista vuota prende tempo 0(1), gli elementi nella lista sono n
    while not q.is_empty():
        # prendi l'elemento a costo minore nella coda (aeroporto che si raggiunge con tempo minore)
        # ogni remove_min al più O(log n)
        cost, (source, flight_taken, t_temp) = q.remove_min()
        # salva l'ultimo volo preso per raggiungere questo aeroporto
        cloud[source] = flight_taken
        # se ho raggiunto la destinazione, Dijkstra mi assicura che questo è il percorso più breve
        # esco dal ciclo
        if source == dest:
            break
        # per ogni volo che parte da source (aeroporto corrente)
        # al più z, se z è il numero di voli che partono da source
        for flight in schedule[source]:
            # valuto se l'aeroporto di destinazione del volo è stato già aggiunto alla soluzione
            if d(flight) not in cloud:
                # valuto se il volo rientra nei vincoli temporali
                if t_temp + c(source) <= l(flight):
                    # se il costo per arrivare in d(f) è minore di quello noto fino ad ora, aggiornalo
                    if costs[source] + l(flight) - t_temp + a(flight) - l(flight) < costs[d(flight)]:
                        costs[d(flight)] = costs[source] + l(flight) - t_temp + a(flight) - l(flight)
                        # nella coda mantieni in corrispondenza di questo aeroporto (key) il volo per
                        # raggiungerlo e l'ora in cui ci arrivi, che è il relativo tempo di arrivo
                        # la modifica della key di un elemento richiede tempo O(log n)
                        q.update(locators[d(flight)], costs[d(flight)], (d(flight), flight, a(flight)))

    # ripercorro all'indietro i voli che mi portano a destinazione per costruire la rotta della soluzione
    # si utilizza una deque (double-ended queue) che è rappresentata internamente come una lista doppiamente linkata,
    # in modo da avere l'inserimento in testa più efficiente possibile e cioè O(1)
    # nel caso peggiore potrebbero essere inseriti m elementi, con complessità totale O(m)
    flight_to_take = cloud[dest]
    while flight_to_take is not None:
        path.appendleft(flight_to_take)
        flight_to_take = cloud[s(flight_to_take)]
    # cast a lista richiede O(n) con n numero di elementi nella collezione
    return list(path)

