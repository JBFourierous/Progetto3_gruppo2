from pkg_1.utils import initialize_schedule
from datetime import timedelta
from pkg_1.ex_1 import list_routes

if __name__ == "__main__":
    airports, schedule = initialize_schedule("airports.txt", "flight.txt")

    for airport in airports:
        print(airport)
    for airport, listofflights in schedule.items():
        for flight in listofflights:
            print(airport, "flight: ", flight)

    start = airports[0]
    end = airports[1]

    start_time = timedelta(hours=6, minutes=10)
    total_time = timedelta(hours=10)

    paths = list_routes(schedule, start, end, start_time, total_time)
    print("\nI want to go from " + str(start.getName()) + " to " + str(end.getName()) +
          " starting at " + str(start_time) + " in max " + str(total_time))
    if len(paths) != 0:
        for path in paths:
            print("--------------PATH----------- ")
            for f in path:
                print(f)
    else:
        print("No flight available")
