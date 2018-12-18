from .Airport import Airport
from .Flight import Flight
from typing import List
from datetime import datetime
from datetime import time
from TdP_collections.queue.array_queue import ArrayQueue
from .utils import *


def backtracking_prune(arrival: time, departure: time, coincidence: int, time_spent: int, total: int) -> bool:
    """
    Verifica le condizioni di backtracking relative al costo del viaggio e alle coincidenze da
    rispettare
    :param arrival: orario di arrivo di un volo
    :param departure: orario di partenza di un volo
    :param coincidence: tempo minimo di coincidenza in un aeroporto
    :param time_spent: tempo di viaggio speso finora
    :param total: tempo totale di viaggio ammesso
    :return: True se la condizione di pruning è valida, False altrimenti
    """
    if time_spent <= total and arrival + coincidence <= departure:
        return True
    else:
        return False


def list_routes(schedule: List[Flight], source: Airport, dest: Airport, t: time, T: int):
    """
    La funzione restituisce tutte le rotte che consentono di andare da a a b con un durata
    complessiva del viaggio non superiore a T e con orario di partenza successivo a t.
    Una rotta è costituita da una sequenza di voli e la sua durata è data dalla somma delle
    durate di tutti i voli più i tempi di attesa negli scali per le coincidenze. Ad ogni
    scalo bisogna considerare che non è possibile effettuare una coincidenza se tra l’orario
    di atterraggio di un volo ed il tempo di decollo del volo successivo intercorre un tempo
    inferiore a c(a).
    :param schedule: orario della compagnia, nella forma di insieme di voli
    :param source: areoporto di partenza
    :param dest: areoporto di arrivo
    :param t: orario di partenza
    :param T: intervallo di tempo
    :return: tutte le rotte che rispettano i vincoli imposti come (quale tipo di dato?)
    """

    queue = ArrayQueue()
    paths = {}

    # costruisce un dizionario che associa ad ogni aeroporto la lista dei voli che
    # partono da tale aeroporto. Operazione con costo O(f) dove f è il numero di voli
    # che può essere ottimizzata mantenendo i voli in una struttura dati più efficiente.
    # scopo di queste righe è fare in modo da mantenere per l'aeroporto di partenza della
    # funzione l'insieme di voli partenti possibili
    flights_tmp = dict()
    for f in schedule:
        if s(f) in flights_tmp:
            flights_tmp[s(f)].append(f)
        else:
            flights_tmp[s(f)] = [f]

    # questa sezione di codice inizializza i possibili path che partono dall'aeroporto richiesto.
    # Ha costo lineare O(f_source), dove f_source è il numero di voli che partono dalla sorgente.
    i = 0
    # scorri l'insieme di voli che partono dalla sorgente desiderata
    for f in flights_tmp[source]:
        # il costo del volo è la somma del tempo di coincidenza in aeroporto e della durata effettiva
        # del volo
        cost = (c(source) + a(f) - l(f))
        # verifica che il volo soddisfi i requisiti di durata e tempo di partenza
        # COINCIDENZA ZERO ATTENZIONE
        if backtracking_prune(t, l(f), 0, cost, T):
            # mantieni un riferimento al volo e alle sue informazioni
            queue.enqueue((i, f, cost))
            # inizializza un path vuoto possibile da questo volo
            paths[i] = []
            # print(str(i), str(flight), cost)
            i += 1

    while not queue.is_empty():
        # prendi il primo volo in coda
        start_airport, current_flight, time_elapsed = queue.dequeue()
        paths[start_airport].append(current_flight)
        # print("ITERATION "+str(time_elapsed))
        # se non sono arrivato a destinazione
        if d(current_flight) != dest:
            # prende il primo path in lista
            item = paths.pop(start_airport)
            j = len(paths)
            for flight in flights_tmp[d(current_flight)]:
                cost = time_elapsed + (l(flight) - a(current_flight) + a(flight) - l(flight)) # finora + attesa + volo
                if backtracking_prune(a(current_flight), l(flight), c(d(current_flight)), cost, T):
                    queue.enqueue((j, flight, cost))
                    paths[j] = item.copy()
                    # print(str(j), str(flight), cost)
                    # print("DURATA VOLO - ", a(flight) - l(flight))
                    # print("DURATA ATTESA - ", l(flight) - a(my_flight))
                    j += 1

    return paths


if __name__ == "__main__":

    airports,flights=read_from_file("test1")

    """for airport in airports:
        print(airport)

    for flight in flights:
        print(flight)"""

    start = airports[0]
    end = airports[3]
    starting_time = datetime.strptime("12:00", "%H:%M").time()
    total_time = datetime.strptime("12:00", "%H:%M").time()

    start_time_minutes = starting_time.hour*60 + starting_time.minute
    total_time_minutes = total_time.hour*60 + total_time.minute

    paths = list_routes(flights,start,end,start_time_minutes,total_time_minutes)

    print("\n\nPercorsi da "+str(start)+" a "+str(end)+" in "+str(total_time_minutes)+" minuti ")
    print("Partenza alle "+str(starting_time))

    for path in paths.keys():
        print("--------------PATH----------- "+str(path))
        for flight in paths[path]:
            print(str(flight))
