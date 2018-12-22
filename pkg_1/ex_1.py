from pkg_1.Flight import Flight, Airport
from typing import List
from typing import Dict
from TdP_collections.queue.array_queue import ArrayQueue
from .utils import *
from datetime import timedelta


def backtracking_prune(arrival: timedelta, departure: timedelta, coincidence: timedelta, time_spent: timedelta, total: timedelta) -> bool:
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
        return False
    else:
        return True


def recursive_visit(schedule: Dict, source: Airport, sink: Airport,
                    arrival_time: timedelta, T: timedelta, solution: List, paths: List):
    # se ho raggiunto la destinazione posso salvare il percorso seguito
    if source == sink:
        paths.append(solution[1])
    else:
        # per ogni volo in partenza dall'aeroporto in cui sono
        for flight in schedule[source]:
            # il costo del volo è la somma del tempo di attesa per il volo e della sua durata
            curr_cost = l(flight) - arrival_time + a(flight) - l(flight)
            # il nuovo costo totale di volo è la somma del precedente e di quello calcolato per il volo corrente
            total_cost = solution[0] + curr_cost
            # valuto tramite backtracking se il volo può essere preso
            if not backtracking_prune(arrival_time, l(flight), c(source), total_cost, T):
                # in caso positivo aggiungo al path corrente la soluzione e aggiorno il costo di volo
                solution[0] += curr_cost
                solution[1].append(flight)
                # valuto ricorsivamente i voli partenti dall'aeroporto appena aggiunto
                recursive_visit(schedule, d(flight), sink, a(flight), solution, paths)
                # pulisci i dati sulla visita al ritorno dalle chiamate
                solution[1].remove(flight)
                solution[0] -= curr_cost




def list_routes(schedule: List[Flight], source: Airport, dest: Airport, t: timedelta, T: timedelta):
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

    solution = [timedelta(minutes=0), []]              # mantengo come soluzione locale la coppia (costo, insieme di voli)
    paths = []                      # insieme dei path possibili tra gli aeroporti

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

    # chiama la visita ricorsiva per valutare tutti i path possibili
    recursive_visit(flights_tmp, source, dest, t, T, solution, paths)
    return paths

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