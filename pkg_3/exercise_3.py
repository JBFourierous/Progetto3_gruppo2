from pkg_1.exercise_1 import *
from pkg_1.utils import initialize_schedule, p, s

"""
Un volo consuma 60kg di gasolio per ogni ora di volo e prima del decollo la compagnia deve 
acquistare dal gestore dell’areoporto il gasolio necessario per il volo. Si assuma che ogni kg di 
gasolio costa 1€ e che la compagnia ha a disposizione un budget complessivo uguale a B per pagare 
il gasolio e che questo budget non consente di coprire tutti i voli previsti nell’orario. Gli 
amministratori della compagnia devono decidere quali voli far partire e quali cancellare.
"""


# La funzione seleziona quali voli far decollare in modo da massimizzare il numero complessivo di
# posti disponibili. Inoltre, la funzione deve restituire per ogni areoporto a quanti soldi devono
# essere assegnati al responsabile dello scalo per pagare il gasolio necessario per tutti i voli
# in partenza da a.
# :param s: orario della compagnia
# :param B: budget del carburante
# :return: dict (?) contenente {aereoporto: soldi assegnati per il carburante}


def get_cost(time_departeur, time_arrive):
    days, seconds = time_arrive.days, time_arrive.seconds
    hour_arrive = days * 24 + seconds // 3600
    min_arrive = (seconds % 3600) // 60
    days, seconds = time_departeur.days, time_departeur.seconds
    hour_departeur = days * 24 + seconds // 3600
    min_depaurteur = (seconds % 3600) // 60
    cost = ((hour_arrive - hour_departeur) % 24) * 60 + (min_arrive - min_depaurteur) % 60
    return cost


def select_flight(airports, flights, B: int):
    lista = []
    for air, c in flights.items():
        for pippo in c:
            lista.append(pippo)  # mi creo la lista di voli

    table = [[0 for w in range(B + 1)] for j in
             range(len(lista) + 1)]  # inizializzo la tabella dove devono essere memorizzati i valori
    money = {}  # dizionario in cui per ogni areoporto verrà riportato il costo in euro da spendere
    for airport in airports:
        money[airport] = 0

    for j in range(1, len(lista) + 1):
        for w in range(1, B + 1):
            time_departeur = l(lista[j - 1])
            time_arrive = a(lista[j - 1])
            places = p(lista[j - 1])
            cost = get_cost(time_departeur, time_arrive)
            if cost > w:
                table[j][w] = table[j - 1][w]
            else:
                table[j][w] = max(table[j - 1][w],
                                  table[j - 1][w - cost] + int(places))

    # print('\n'.join([''.join(['{:7}'.format(item) for item in row])
    #                  for row in table]))
    result = []
    w = B
    j = len(lista)
    total_cost = 0

    while j > 0 and w > 0:
        was_added = table[j][w] != table[j - 1][w]

        if was_added:
            time_departeur = l(lista[j - 1])
            time_arrive = a(lista[j - 1])
            cost = get_cost(time_departeur, time_arrive)
            result.append(lista[j - 1])
            w -= cost
        j -= 1
    for elem in result:
        departeur = s(elem)
        time_departeur = l(elem)
        time_arrive = a(elem)
        cost = get_cost(time_departeur, time_arrive)
        total_cost += cost
        if money[departeur] == 0:
            money[departeur] = cost
        else:
            money[departeur] += cost

    return result, money, total_cost


airports, flights = initialize_schedule("../airports.txt", "../flights.txt")
result, money, total_cost = select_flight(airports, flights, 750)
print("lista dei voli che devono partire")
for e in result:
    print(e)
print("totale dei soldi per ogni aeroporto")
for e in money.values():
    print(e)
print("costo totale")
print(total_cost)
