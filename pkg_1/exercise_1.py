
from typing import List
from typing import Dict
from pkg_1.utils import a, l, d, c, Airport, Flight
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
    if arrival is None or departure is None or time_spent is None or coincidence is None or total is None:
        print('Time is None')
        exit(1)
    elif time_spent <= total and arrival + coincidence <= departure:
        return False
    else:
        return True


def recursive_visit(schedule: Dict, source: Airport, sink: Airport,
                    arrival_time: timedelta, T: timedelta, solution: List, paths: List):
    # se ho raggiunto la destinazione posso salvare il percorso seguito
    if source == sink:
        # paths.append(solution[1].copy())
        paths.append(list((solution[1])))
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
                recursive_visit(schedule, d(flight), sink, a(flight), T, solution, paths)
                # pulisci i dati sulla visita al ritorno dalle chiamate
                solution[1].remove(flight)
                solution[0] -= curr_cost


def list_routes(schedule: Dict[Airport, list], source: Airport, dest: Airport, t: timedelta, T: timedelta) -> list:
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
    :return: tutte le rotte che rispettano i vincoli imposti come lista
    """

    solution = [timedelta(minutes=0), []]              # mantengo come soluzione locale la coppia (costo, insieme di voli)
    paths = []                                         # insieme dei path possibili tra gli aeroporti

    # chiama la visita ricorsiva per valutare tutti i path possibili
    recursive_visit(schedule, source, dest, t, T, solution, paths)
    return paths
