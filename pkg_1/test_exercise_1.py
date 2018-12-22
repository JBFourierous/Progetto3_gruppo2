from pkg_1.utils import initialize_schedule
from datetime import timedelta
from pkg_1.exercise_1 import list_routes
from pkg_1.utils import l, a


def test_paths_available():
    airports, schedule = initialize_schedule("../airports.txt", "../flights.txt")

    # for airport in airports:
    #     print(airport)
    # for airport, listofflights in schedule.items():
    #     for flight in listofflights:
    #         print(airport, "flight: ", flight)

    start = airports[0]
    end = airports[1]

    start_time = timedelta(hours=12, minutes=00)
    total_time = timedelta(hours=8)

    paths = list_routes(schedule, start, end, start_time, total_time)

    # the result is correct if
    # time the flight start - time you arrive + length of the flight < total_time

    # print("\nI want to go from " + str(start.getName()) + " to " + str(end.getName()) +
    #       " starting at " + str(start_time) + " in max " + str(total_time))
    cost = None
    if len(paths) != 0:
        for path in paths:
            cost = timedelta(0)
            arrive_time = start_time
            for f in path:
                curr_cost = l(f) - arrive_time + a(f) - l(f)
                # print(curr_cost)
                cost = curr_cost + cost
                arrive_time = a(f)
                # print(f)
            # print(cost)
            if cost > total_time:
                print("Test test_paths_available failed")
                return
        if len(paths) == 5 and cost < total_time:
            print("Test test_paths_available passed")
    else:
        print("Test test_paths_available failed")


def test_no_flight_available():
    airports, schedule = initialize_schedule("../airports.txt", "../flights.txt")
    start = airports[0]
    end = airports[1]

    start_time = timedelta(hours=6, minutes=00)
    total_time = timedelta(hours=1)

    paths = list_routes(schedule, start, end, start_time, total_time)
    if len(paths) != 0:
        print("Test test_no_flight_available failed")
    else:
        print("Test test_no_flight_available passed")


def execute_tests():
    test_paths_available()
    test_no_flight_available()


if __name__ == "__main__":
    execute_tests()
