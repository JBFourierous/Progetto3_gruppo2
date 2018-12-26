from pkg_1.exercise_1 import *
from pprint import pprint
"""
Un volo consuma 60kg di gasolio per ogni ora di volo e prima del decollo la compagnia deve 
acquistare dal gestore dell’areoporto il gasolio necessario per il volo. Si assuma che ogni kg di 
gasolio costa 1€ e che la compagnia ha a disposizione un budget complessivo uguale a B per pagare 
il gasolio e che questo budget non consente di coprire tutti i voli previsti nell’orario. Gli 
amministratori della compagnia devono decidere quali voli far partire e quali cancellare.
"""


# La funzione seleziona quali voli far decollare in modo da massimizzare il numero complessivo di
#posti disponibili. Inoltre, la funzione deve restituire per ogni areoporto a quanti soldi devono
#essere assegnati al responsabile dello scalo per pagare il gasolio necessario per tutti i voli
#in partenza da a.
#:param s: orario della compagnia
#:param B: budget del carburante
#:return: dict (?) contenente {aereoporto: soldi assegnati per il carburante}

def compute_time(time):
    tmp = time.split(":")
    hour = int(tmp[0])
    min = int(tmp[1])
    return hour, min

def get_cost(time_departeur, time_arrive):
    hour_departeur, min_depaurteur = compute_time(time_departeur)
    hour_arrive, min_arrive = compute_time(time_arrive)
    cost = ((hour_arrive - hour_departeur) % 24) * 60 + (min_arrive - min_depaurteur) % 60
    return cost

def select_flight(airports: dict, flights, B:int):
    table = [[0 for w in range(B + 1)] for j in range(len(flights) + 1)]
    money = {}
    for airport in airports.keys():
        money[airport] = 0

    for j in range(1, len(flights) + 1):
        for w in range(1, B + 1):
            departeur, arrive, time_departeur, time_arrive, places = flight[j-1]
            cost = get_cost(time_departeur, time_arrive)
            if cost > w:
                table[j][w] = table[j - 1][w]
            else:
                table[j][w] = max(table[j - 1][w],
                                  table[j - 1][w - cost] + int(places))

    print('\n'.join([''.join(['{:7}'.format(item) for item in row])
                     for row in table]))
    result = []
    w = B
    j = len(flights)

    while j > 0 and w > 0:
        was_added = table[j][w] != table[j - 1][w]

        if was_added:
            departeur, arrive, time_departeur, time_arrive, places = flight[j-1]
            cost = get_cost(time_departeur, time_arrive)
            result.append(flight[j - 1])
            w -= cost
        j -= 1
    for elem in result:
        departeur, arrive, time_departeur, time_arrive, places = elem
        cost = get_cost(time_departeur, time_arrive)
        if money[departeur] == 0:
            money[departeur] = cost
        else:
            money[departeur] += cost

    return result,money

keys = []
value = []
flight = []
try:
    file = open('airports.txt')
    file_2 = open('flight.txt')
except FileNotFoundError:
    print("File not found")
for line in file:
    tmp = line.strip().split(" ")
    keys.append(tmp[0])
    value.append(tmp[1])
airport = dict(zip(keys, value))

for line in file_2:
    tmp = line.strip().split(" ")
    flight.append(tmp)

result, money = select_flight(airport,flight,600)
for e in result:
    print(e)
for e in money.values():
    print(e)