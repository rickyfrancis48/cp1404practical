from prac_09.taxi import Taxi


def main():
    name = "Prius 1"
    fuel = 100

    my_taxi = Taxi(name, fuel)
    my_taxi.drive(40)
    print(my_taxi)
    print(f"Current fare is {my_taxi.get_fare()}")

    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print(f"Current fare is {my_taxi.get_fare()}")


main()
