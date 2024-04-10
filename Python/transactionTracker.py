import pandas as pd


def transaction_data(price, item):
    # adds new record to the DataFrame
    df.loc[len(df.index)] = [price, item]
    return


def menu():
    print('******************************************')
    print()
    print('Welcome to the Pandas Transaction Tracker!\n')
    print('******************************************\n')
    print('Press A to add a transaction')
    print('Press D for done \n')


data = {'Amount': [1150.00, 483.86, 241.00, 300.00, 150.00, 100.00],
        'Description': ['Rent', 'Car Payment', 'Tuition', 'Groceries', 'Utilities', 'Gas']
        }

df = pd.DataFrame(data)


def main():
    done = False
    while not done:
        menu()
        option1 = input('Press a key to continue--> ')
        if option1 == 'D':
            done = True
        if option1 == 'A':
            pr = input('Enter the amount: ')
            desc = input('What was this for?: ')
            transaction_data(pr, desc)
            print(df)


if __name__ == '__main__':
    # Run main method
    main()
