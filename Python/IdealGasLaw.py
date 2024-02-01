P = float(input('Enter the Pressure: '))
V = float(input('Enter the Volume: '))
T = float(input('Enter the Temperature: '))
n = float(input('Enter the number of moles: '))
R = 8.314  # Universal Gas Constant


def pressure():
    # Ignores P input & solves for Pressure
    result = (n * R * T) / V
    return result


def volume():
    # Ignores V input & solves for Volume
    result = (n * R * T) / P
    return result


def temperature():
    # Ignores T input & solves for Temperature
    result = (P * V) / (n * R)
    return result


def main():
    option = str(input('Which variable do you want to solve for? --> '))
    # User chooses which variable to solve for
    if option == 'P':
        P = int(pressure())
        print('Pressure: ' + str(P) + ' atm')
    elif option == 'V':
        V = float(volume())
        print('Volume: ' + str(V) + ' m^3')

    elif option == 'T':
        T = float(temperature())
        print('Temperature: ' + str(T) + ' K')

    else:
        print('Done')

    return


if __name__ == '__main__':
    # Run main method
    main()

else:
    print("The end")
