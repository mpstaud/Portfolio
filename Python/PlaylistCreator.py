import pandas as pd
import time


df = pd.DataFrame({'Title':['Fergalicious', "Hip's Don't Lie", "Say it right", "Clumsy", "Boom Boom Pow",
                            "Dani California", "SOS", "The Sweet Escape"],
                   'Artist':['Fergie feat will.i.am', 'Shakira feat. Wyclef Jean', 'Nelly Furtado', 'Fergie',
                             'Black Eyed Peas', 'Red Hot Chili Peppers', 'Rihanna', 'Gwen Stefani']})
print(df)


def add_song(title, artist):
    df.loc[len(df.index)] = [str(title),str(artist)]
    print(df)


def selection():
    sel = input('Press A to add, R to remove, and S to see the whole playlist--> ')
    if sel == 'A' or 'a':
        song_title = input('Song Name: ')
        time.sleep(0.5)
        song_artist = input('Artist Name: ')
        time.sleep(1)
        add_song(song_title, song_artist)
    else:
        'All Done!'


def main():
    start = input('Press P to start: ')
    for i in range(0, 5):
        selection()


if __name__ == '__main__':
    # Run main method
    main()


else:
    print("The end")