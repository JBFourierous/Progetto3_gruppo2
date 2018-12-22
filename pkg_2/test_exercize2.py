from pkg_1.utils import initialize_schedule
from datetime import timedelta
from pkg_2.exercise_2 import find_route

if __name__ == "__main__":
    airports, schedule = initialize_schedule("../airports.txt", "../flights.txt")

    # for airport in airports:
    #     print(airport)
    # for airport, list_of_flights in schedule.items():
    #     for flight in list_of_flights:
    #         print(airport, "flight: ", flight)

    start = airports[0]
    end = airports[1]

    start_time = timedelta(hours=6, minutes=40)
    total_time = timedelta(hours=10)

    paths = find_route(schedule=schedule,
                       airports=airports,
                       start=start,
                       dest=end,
                       t=start_time)
    print("\nI want to go from " + str(start.getName()) + " to " + str(end.getName()) +
          " starting at " + str(start_time) + " in the shortest time possible ")
    if len(paths) != 0:
        for path in paths:
            print("--------------PATH----------- ")
            print(path)
    else:
        print("No flight available")

