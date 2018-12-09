from pkg_1.exercise_1 import Schedule
"""
Un volo consuma 60kg di gasolio per ogni ora di volo e prima del decollo la compagnia deve 
acquistare dal gestore dell’areoporto il gasolio necessario per il volo. Si assuma che ogni kg di 
gasolio costa 1€ e che la compagnia ha a disposizione un budget complessivo uguale a B per pagare 
il gasolio e che questo budget non consente di coprire tutti i voli previsti nell’orario. Gli 
amministratori della compagnia devono decidere quali voli far partire e quali cancellare.
"""


def select_flights(s: Schedule, B: int) -> dict:
    """
    La funzione seleziona quali voli far decollare in modo da massimizzare il numero complessivo di
    posti disponibili. Inoltre, la funzione deve restituire per ogni areoporto a quanti soldi devono
    essere assegnati al responsabile dello scalo per pagare il gasolio necessario per tutti i voli
    in partenza da a.
    :param s: orario della compagnia
    :param B: budget del carburante
    :return: dict (?) contenente {aereoporto: soldi assegnati per il carburante}
    """
    pass
