from pkg_1.utils import initialize_schedule
from datetime import timedelta
from pkg_2.exercise_2 import find_route
from pkg_1.exercise_1 import list_routes
from pkg_1.utils import l, a


def test_path_available_check_it_is_the_shortest():
    airports, schedule = initialize_schedule("../airports.txt", "../flights.txt")

    start = airports[0]
    end = airports[1]

    start_time = timedelta(hours=12, minutes=00)

    path = find_route(schedule=schedule,
                      airports=airports,
                      start=start,
                      dest=end,
                      t=start_time)

    cost = None
    if len(path) != 0:
        cost = timedelta(0)
        arrive_time = start_time
        for f in path:
            curr_cost = l(f) - arrive_time + a(f) - l(f)
            cost = curr_cost + cost
            arrive_time = a(f)
    else:
        print("Test test_path_available_check_it_is_the_shortest failed")

    # Chiamando la list_routes() dell'esercizio 1 richiedendo come costo totale
    # il costo dello shortest path, la funzione deve restituire solo e soltando quel volo.
    paths = list_routes(schedule=schedule,
                        source=start,
                        dest=end,
                        t=start_time,
                        T=cost)
    if len(path) != 1:
        print("Test test_path_available_check_it_is_the_shortest failed")
    else:
        if str(paths[0][0]) == str(path[0]):
            print("Test test_path_available_check_it_is_the_shortest passed")
        else:
            print("Test test_path_available_check_it_is_the_shortest failed")


def test_another_path_available_check_it_is_the_shortest():
    airports, schedule = initialize_schedule("../airports.txt", "../flights.txt")

    start = airports[6]  # FCO
    end = airports[0]  # LHR

    start_time = timedelta(hours=6, minutes=00)

    path = find_route(schedule=schedule,
                      airports=airports,
                      start=start,
                      dest=end,
                      t=start_time)

    cost = None
    if len(path) != 0:
        cost = timedelta(0)
        arrive_time = start_time
        for f in path:
            curr_cost = l(f) - arrive_time + a(f) - l(f)
            cost = curr_cost + cost
            arrive_time = a(f)
    else:
        print("Test test_another_path_available_check_it_is_the_shortest failed")

    # Chiamando la list_routes() dell'esercizio 1 richiedendo come costo totale
    # il costo dello shortest path, la funzione deve restituire solo e soltando quel volo.
    paths = list_routes(schedule=schedule,
                        source=start,
                        dest=end,
                        t=start_time,
                        T=cost)
    if all(str(paths[0][i]) == str(path[i]) for i in range(len(path))) and \
            len(path) == len(paths[0]):
        print("Test test_another_path_available_check_it_is_the_shortest passed")
    else:
        print("Test test_another_path_available_check_it_is_the_shortest failed")


def test_no_flight_available():
    airports, schedule = initialize_schedule("../airports.txt", "../flights.txt")
    start = airports[8]  # OSL
    end = airports[7]    # SVO

    start_time = timedelta(hours=8, minutes=00)

    paths = find_route(schedule=schedule,
                       airports=airports,
                       start=start,
                       dest=end,
                       t=start_time)
    if len(paths) != 0:
        print("Test test_no_flight_available failed")
    else:
        print("Test test_no_flight_available passed")


def execute_test():
    test_path_available_check_it_is_the_shortest()
    test_another_path_available_check_it_is_the_shortest()
    test_no_flight_available()


if __name__ == "__main__":
    execute_test()
