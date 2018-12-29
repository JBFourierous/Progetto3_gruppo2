from pkg_1.utils import initialize_schedule
from pkg_3.exercise_3 import select_flight

def test_select_flight_result_is_the_expected_one():
    airports, flights = initialize_schedule("../airports.txt", "../flights_light.txt")
    result, money, total_cost = select_flight(airports, flights, 600)
    if str(result[0]) == "BCN FCO 2018/12/29 18:25:00 20:15:00 517"\
            and str(result[1]) == "BCN FCO 2018/12/29 16:40:00 18:25:00 625"\
            and str(result[2]) == "LHR FCO 2018/12/29 16:10:00 19:45:00 651"\
            and total_cost == 550:
        print("test passed")
    else:
        print("test failed")

def test_select_flight_result_is_the_expected_one_B_lessequal_zero():
    airports, flights = initialize_schedule("../airports.txt", "../flights_light.txt")
    result, money, total_cost = select_flight(airports, flights, 500)
    if result is None\
            or money is None\
            or total_cost <= 0:
        print("test failed")
    else:
        print("test passed")
def test_select_flight_result_is_the_expected_one_B_lessequal_zero_2():
    airports, flights = initialize_schedule("../airports.txt", "../flights_light.txt")
    result, money, total_cost = select_flight(airports, flights, 0)
    if result is None\
            and money is None\
            and total_cost <= 0:
        print("test passed")
    else:
        print("test failed")


def execute_test():
    test_select_flight_result_is_the_expected_one()
    test_select_flight_result_is_the_expected_one_B_lessequal_zero()
    test_select_flight_result_is_the_expected_one_B_lessequal_zero_2()

if __name__ == "__main__":
    execute_test()