# Ohm's law V = IR
resistors = []


def voltage(i, r):
    volt = i * r
    return print('Your Voltage is ' + str(volt) + ' Volts')


def series():
    res_num_series = int(input('How many resistors do you have? '))
    for i in range(0, res_num_series):
        resistance = int(input("Enter the resistance in Ohms for this resistor"))
        resistors.append(resistance)
    total_resistance = 1 / sum(resistors)
    current = int(input('How much current is flowing through your circuit? '))
    voltage(current, float(total_resistance))


def main():
    circuit_type = input('Press S for Series, P for Parallel, C for a combination of the 2: ')
    if circuit_type == 'S':
        series()


if __name__ == '__main__':
    main()
