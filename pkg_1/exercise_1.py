import datetime


class Schedule:
    def __init__(self):
        self.airports = dict()  # airports[a] = c(a)
        self.flights = dict()  # flights[f] = s(f), d(f), l(f), a(f), p(f)


class Route:
    def __init__(self):
        self.flights = list()
        self.duration = datetime.time()


def list_routes(s: Schedule, a: str, b: str, t: datetime.time, T: datetime.timedelta) -> list:
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
    visited = {}
    act_nodes = []
    act_edges = []
    paths = []
    return get_all_paths(s, a, b, visited, act_nodes, act_edges, paths, t, T)

def get_all_paths(schedule, source, dest, visited, act_nodes, act_edges, paths, t, T) -> list:
    """
    Questa funzione implementa una versione modificata di una visita DFS di un grafo salvando tutti i
    possibili path (in termini di archi attraversati) da una sorgente a una destinazione. Si tratta di
    una soluzione di ricerca esaustiva che per mantenere accettabili le prestazioni applica le seguenti
    condizioni di bounding per il backtracking:
    - se il volo di partenza ha start > t non segue l'arco
    - se la durata della tratta parziale creata nella visita dei nodi è superiore a T scarta la soluzione
      parizale
    - se il tempo di coincidenza a un certo nodo della soluzione parziale è maggiore della differenza tra
      tempo di arrivo e di partenza del nuovo volo scarta la soluzione parziale
    :param schedule: orario della compagnia aerea
    :param source: nodo di partenza della visita
    :param dest: nodo destinazione da raggiungere
    :param visited: dizionario dei nodi già visitati dato il path attuale
    :param act_nodes: lista dei nodi nel path attuale
    :param act_edges: lista degli archi nel path attuale
    :param paths: lista dei possibili path che soddisfano le condizioni di ricerca
    :param t: orario di partenza
    :param T: intervallo di Tempo
    :return: lista dei possibili path che soddisfano le condizioni di ricerca
    """
    visited[source] = True                  # segna il nodo come visitato
    act_nodes.append(source)                # aggiungi al path il nodo sorgente

    if source == dest:                      # se hai raggiunto la destinazione salva il path locale trovato
        paths.append(act_edges)
    else:
        # se non hai raggiunto la destinazione, per ogni nodo adiacente a quello che stai vistando cerca un path
        # verso la destinazione ricorsivamente
        for flight in schedule.incident_edges(source):
            # verifica che il volo non parta dopo t, solo per il primo nodo
            if len(act_edges) == 0:
                if not (flight.getStart() > t):
                    if not (source.getCoincidence() > flight.getLeaveTime() - act_edges[-1].getArrivalTime()):
                        if not (act_edges[1] + source.getCoicidence() + flight.getDuration()) > T:
                            act_edges.append(flight)
                else:
                    return
            else:
                if not (source.getCoincidence() > flight.getLeaveTime() - act_edges[-1].getArrivalTime()):
                    if not (act_edges[1] + source.getCoicidence() + flight.getDuration()) > T:
                        act_edges.append(flight)
                else:
                    return
            if visited[flight.opposite(source)] is False:      # continua la ricerca solo se il nodo non è stato già visitato
                get_all_paths(schedule, flight.opposite(source), dest, visited, act_nodes, act_edges, paths)
        act_nodes.pop()                      # rimuovi il nodo e segnalo non visitato per evitare cicli
        visited[source] = False
    return paths

if __name__ == "__main__":
    s = Schedule()
    s.airports = {"MXP": datetime.time(1, 30)}
    s.flights = {4151: ("MXP", "CDG", datetime.time(6, 30), datetime.time(8, 5), 40)}

    # list_routes(s, "MXP", "BGY", datetime.time(6, 30), datetime.timedelta(minutes=30))
