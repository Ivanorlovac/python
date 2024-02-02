import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Funktion för att ladda väderdata från "väder.csv"
def ladda_vaderdata():
    # Läser in CSV-filen med Pandas
    data = pd.read_csv('väder.csv')
    return data


# Funktion för att analysera temperaturdata
def analysera_data(data, plats1, plats2):
    data_plats1 = data[data['Plats'] == plats1] # Skapar en ny DataFrame  från den ursprungliga data DataFrame.
    data_plats2 = data[data['Plats'] == plats2] # På samma sätt som ovan, skapar denna rad en ny DataFrame data_plats2
    medel_temp_plats1 = np.mean(data_plats1['Temperatur']) # Berä. med.vär. av tem. för pl.1 np.mean-fun. fr. NumPy-bib.
    medel_temp_plats2 = np.mean(data_plats2['Temperatur']) # På ett liknande sätt som ovan, berä.medeltemp. för pl.2
    return medel_temp_plats1, medel_temp_plats2 # Slutligen returnerar denna rad de beräknade
    # genomsnittstemperaturerna för både plats1 och plats2 som ett par värden.


# Funktion för att jämföra nederbörd och vindstyrka mellan två platser
def analysera_nederbord_vind(data, plats1, plats2):
    data_plats1 = data[data['Plats'] == plats1] # Denna rad skapar en ny DataFrame data_plats1 som innehåller endast
    # rader från den ursprungliga data DataFrame där värdena i kolumnen 'Plats' matchar plats1.
    data_plats2 = data[data['Plats'] == plats2] # På liknande sätt filtrerar denna rad data DataFrame för att skapa
    # en ny DataFrame data_plats2 som endast innehåller rader där värdet i kolumnen 'Plats' är lika med plats2.
    medel_nederbord_plats1 = np.mean(data_plats1['Nederbörd'])
    medel_nederbord_plats2 = np.mean(data_plats2['Nederbörd'])
    medel_vindstyrka_plats1 = np.mean(data_plats1['Vindstyrka'])
    medel_vindstyrka_plats2 = np.mean(data_plats2['Vindstyrka'])
    return (medel_nederbord_plats1, medel_nederbord_plats2, medel_vindstyrka_plats1, medel_vindstyrka_plats2)


# Uppdaterad visualiseringsfunktion
def visualisera_data(medel_temp_plats1, medel_temp_plats2, medel_nederbord_plats1, medel_nederbord_plats2,
                     medel_vindstyrka_plats1, medel_vindstyrka_plats2, plats1, plats2):
    # Skapar flera barplots för att jämföra olika parametrar
    fig, ax = plt.subplots(3, 1, figsize=(8, 12))

    # Temperatur
    ax[0].bar([plats1, plats2], [medel_temp_plats1, medel_temp_plats2], color=['blue', 'lightblue'])
    ax[0].set_ylabel('Medeltemperatur')
    ax[0].set_title('Temperaturjämförelse')

    # Nederbörd
    ax[1].bar([plats1, plats2], [medel_nederbord_plats1, medel_nederbord_plats2], color=['green', 'lightgreen'])
    ax[1].set_ylabel('Medelnederbörd')
    ax[1].set_title('Nederbördsjämförelse')

    # Vindstyrka
    ax[2].bar([plats1, plats2], [medel_vindstyrka_plats1, medel_vindstyrka_plats2], color=['red', 'pink'])
    ax[2].set_ylabel('Medelvindstyrka')
    ax[2].set_title('Vindstyrkejämförelse')

    plt.tight_layout()
    plt.show()


# Huvudfunktionen för applikationen
def huvudfunktion():
    plats1 = input("Ange första platsen för jämförelse: ")
    plats2 = input("Ange andra platsen för jämförelse: ")

    data = ladda_vaderdata()
    medel_temp_plats1, medel_temp_plats2 = analysera_data(data, plats1, plats2)
    (medel_nederbörd_plats1, medel_nederbörd_plats2, medel_vindstyrka_plats1,
     medel_vindstyrka_plats2) = analysera_nederbord_vind(data, plats1, plats2)

    visualisera_data(medel_temp_plats1, medel_temp_plats2, medel_nederbörd_plats1, medel_nederbörd_plats2,
                     medel_vindstyrka_plats1, medel_vindstyrka_plats2, plats1, plats2)


# Kör huvudfunktionen
if __name__ == "__main__":
    huvudfunktion()
