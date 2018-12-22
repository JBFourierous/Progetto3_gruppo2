from pkg_1.ex_1 import list_routes, Flight
from utilss import initialize_schedule
from datetime import timedelta

if __name__ == "__main__":
    airports, flights = initialize_schedule("air.txt", "fli.txt")

    # for airport in airports:
    #     print(airport)
    # for flight in flights:
    #     print(flight)

    start = airports[0]
    end = airports[1]
    # print(start)
    # print(end)
    schedule = dict()
    for el in airports:
        schedule[el] = list()
        for f in flights:
            if el == f.getStart():
                schedule[el].append(f)
    start_time = timedelta(hours=6, minutes=0)
    total_time = timedelta(hours=1)

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
