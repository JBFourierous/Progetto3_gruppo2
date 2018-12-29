from pkg_1.utils import initialize_schedule, init_schedule_with_date
from datetime import timedelta, datetime
from pkg_1.exercise_1 import list_routes
from pkg_1.utils import l, a


def test_paths_available():
    # airports, schedule = initialize_schedule("../airports.txt", "../flights.txt")
    airports, schedule = init_schedule_with_date("../airports.txt", "../fli.txt")

    start = airports[0]
    end = airports[1]

    shift = datetime.strptime(
        "29-12-2018", "%d-%m-%Y") - datetime.strptime(
        "1-1-2018", "%d-%m-%Y")
    start_time = timedelta(hours=12, minutes=00) + shift
    total_time = timedelta(hours=8)

    paths = list_routes(schedule, start, end, start_time, total_time)

    list_costs = list()
    if len(paths) != 0:
        for path in paths:
            cost = timedelta(0)
            arrive_time = start_time
            for f in path:
                curr_cost = l(f) - arrive_time + a(f) - l(f)
                cost = curr_cost + cost
                arrive_time = a(f)
            if cost > total_time:
                print("Test test_paths_available failed")
                return
            list_costs.append(cost)
        if len(paths) == 5 and len(list_costs) == 5 and all(i <= total_time for i in list_costs):
            print("Test test_paths_available passed")
        else:
            print("Test test_paths_available failed")
    else:
        print("Test test_paths_available failed")


def test_other_paths_available():
    # airports, schedule = initialize_schedule("../airports.txt", "../flights.txt")
    airports, schedule = init_schedule_with_date("../airports.txt", "../fli.txt")

    start = airports[6]  # FCO
    end = airports[0]    # LHR

    shift = datetime.strptime(
        "29-12-2018", "%d-%m-%Y") - datetime.strptime(
        "1-1-2018", "%d-%m-%Y")
    start_time = timedelta(hours=6, minutes=00) + shift
    total_time = timedelta(hours=10)
    paths = list_routes(schedule, start, end, start_time, total_time)

    list_costs = list()
    if len(paths) != 0:
        for path in paths:
            cost = timedelta(0)
            arrive_time = start_time
            for f in path:
                curr_cost = l(f) - arrive_time + a(f) - l(f)
                cost = curr_cost + cost
                arrive_time = a(f)
            if cost > total_time:
                print("Test test_paths_available failed")
                return
            list_costs.append(cost)
        if len(paths) == 9 and len(list_costs) == 9 and all(i <= total_time for i in list_costs):
            print("Test test_other_paths_available passed")
        else:
            print("Test test_other_paths_available failed")
    else:
        print("Test test_other_paths_available failed")


def test_no_flight_available():
    # airports, schedule = initialize_schedule("../airports.txt", "../flights.txt")
    airports, schedule = init_schedule_with_date("../airports.txt", "../fli.txt")

    start = airports[0]
    end = airports[1]

    shift = datetime.strptime(
        "29-12-2018", "%d-%m-%Y") - datetime.strptime(
        "1-1-2018", "%d-%m-%Y")
    start_time = timedelta(hours=6, minutes=00) + shift
    total_time = timedelta(hours=1)

    paths = list_routes(schedule, start, end, start_time, total_time)
    if len(paths) != 0:
        print("Test test_no_flight_available failed")
    else:
        print("Test test_no_flight_available passed")


def execute_tests():
    test_paths_available()
    test_other_paths_available()
    test_no_flight_available()


if __name__ == "__main__":
    execute_tests()
