from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test for SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Silver service Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(f"${taxi.get_fare()}")


main()
