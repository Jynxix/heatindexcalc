import statistics


# The following extra credit steps were made: program returns error if temperature is above 300 or below -200,
# and if humidity is below 0 or over 100

def main():
    print("*** Heat Index Calculator ***")
    # Name of each location given by user
    locations = []
    # Value of each temperature given by user
    Temperatures = []
    # Value of each relative humidity given by user
    Humidity = []
    # Each Heat Index calculated using the values of Temperature and Humidity given by the user
    Hindex = []
    locationnum = int(input("Select the number of locations: "))
    if locationnum < 1:
        print(f"Error: {locationnum} is not a valid input.")
        exit(-1)
    decimal = int(input("Select decimal precision for the calculations [1--4]: "))
    if decimal > 4:
        print(f"Error: {decimal} is not in the range [1—4].")
        exit(-1)
    if decimal < 1:
        print(f"Error: {decimal} is not in the range [1—4].")
        exit(-1)
    for i in range(locationnum):
        location = input(f"Enter the name of Location {i + 1}: ")
        T = float(input(f"\tEnter air temperature [in deg F]: "))
        if T > 300 or T < -200:
            print(f"Error: Please enter a realistic temperature.")
            exit(-1)
        R = float(input("\tEnter relative humidity [in percentage]: "))
        if R < 0:
            print(f"Error: Relative humidity cannot be negative!")
            exit(-1)
        if R > 100:
            print(f"Error: Relative humidity cannot exceed 100!")
            exit(-1)

        Temperatures.append(T)
        Humidity.append(R)
        locations.append(location)
        HI = -42.379 + 2.04901523 * T + 10.14333127 * R - 0.22475541 * T * R - 0.00683783 * T * T - 0.05481717 * R * R + 0.00122874 * T * T * R + \
             0.00085282 * T * R * R - 0.00000199 * T * T * R * R
        print(f"\tHI is {round(HI, decimal)} deg F. ")
        Hindex.append(HI)
    print("*** Summary ***")
    print("HI:")
    print(f"\tAvg recorded HI: {round(statistics.mean(Hindex), decimal)} deg F")
    print(f"\tLocation with lowest HI: {locations[Hindex.index(min(Hindex))]} ({round(min(Hindex), decimal)} deg F) ")
    print("Air Temperature:")
    print(f"\tAvg recorded air temperature: {round(statistics.mean(Temperatures), decimal)} deg F")
    print(
        f"\tLocation with lowest air temperature: {locations[Temperatures.index(int(min(Temperatures)))]} ({int(min(Temperatures))} deg F) ")
    print("Relative Humidity:")
    print(f"\tAvg recorded recorded relative humidity: ({int(statistics.mean(Humidity))}%)")
    print(
        f"\tLocation with highest relative humidity: {locations[Humidity.index(int(max(Humidity)))]} ({int(max(Humidity))}%) ")


main()
