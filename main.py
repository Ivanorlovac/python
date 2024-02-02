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
    return medel_temp_plats1, medel_temp_plats2 # Slutligen returnerar denna rad de beräknaden genomsnittstemperaturerna för både plats1 och plats2 som ett par värden.


# Funktion för att jämföra nederbörd och vindstyrka mellan två platser
def analysera_nederbord_vind(data, plats1, plats2):
    data_plats1 = data[data['Plats'] == plats1] # Denna rad skapar en ny DataFrame data_plats1 som innehåller endast rader från den ursprungliga data DataFrame där värdena i kolumnen 'Plats' matchar plats1.
    data_plats2 = data[data['Plats'] == plats2] # På liknande sätt filtrerar denna rad data DataFrame för att skapa en ny DataFrame data_plats2 som endast innehåller rader där värdet i kolumnen 'Plats' är lika med plats2.
    medel_nederbord_plats1 = np.mean(data_plats1['Nederbörd']) # Denna rad beräknar genomsnittet av nederbördsmängden  för plats1. Genom att använda np.mean funktionen från NumPy-biblioteket, räknar den ut medelvärdet av alla  värden i kolumnen 'Nederbörd' i data_plats1
    medel_nederbord_plats2 = np.mean(data_plats2['Nederbörd']) # På samma sätt som ovan, beräknar denna rad genomsnittet av nederbördsmängden för plats2 genom att ta medelvärdet av alla värden i kolumnen 'Nederbörd' i data_plats2. medel_nederbörd_plats2 blir således den genomsnittliga nederbördsmängden för den andra platsen.
    medel_vindstyrka_plats1 = np.mean(data_plats1['Vindstyrka']) # Denna rad beräknar medelvindstyrkan för plats1. Precis som tidigare används np.mean för att beräkna genomsnittet av värdena i kolumnen 'Vindstyrka' i data_plats1. Resultatet, medel_vindstyrka_plats1, representerar den genomsnittliga vindstyrkan för den första platsen.
    medel_vindstyrka_plats2 = np.mean(data_plats2['Vindstyrka']) # Liksom de tidigare raderna beräknar denna rad medelvindstyrkan för plats2 genom att ta medelvärdet av värdena i kolumnen 'Vindstyrka' i data_plats2. medel_vindstyrka_plats2 indikerar den genomsnittliga vindstyrkan för den andra platsen.
    return (medel_nederbord_plats1, medel_nederbord_plats2, medel_vindstyrka_plats1, medel_vindstyrka_plats2) # Slutligen returnerar denna rad en tuple med de beräknade medelvärdena för nederbörd och vindstyrka för de två valda platserna. Dessa värden kan sedan användas för ytterligare analys eller visualisering i andra delar av programmet.


# Uppdaterad visualiseringsfunktion
def visualisera_data(medel_temp_plats1, medel_temp_plats2, medel_nederbord_plats1, medel_nederbord_plats2,
                     medel_vindstyrka_plats1, medel_vindstyrka_plats2, plats1, plats2):
    # Skapar flera barplots för att jämföra olika parametrar
    fig, ax = plt.subplots(3, 1, figsize=(8, 12)) # skapar en figur (fig) och ett array av axlar (ax) för att rymma tre subplots (grafiska områden). Argumentet 3, 1 anger att det ska finnas tre rader och en kolumn av grafer, vilket innebär att graferna ordnas vertikalt.Figsize=(8, 12) definierar storleken på hela figuren i tum (bredd, höjd).

    # Temperatur
    ax[0].bar([plats1, plats2], [medel_temp_plats1, medel_temp_plats2], color=['blue', 'lightblue']) # Denna rad skapar en stapeldiagram (bar plot) på den första axeln (ax[0]). Den jämför medeltemperaturen (medel_temp_plats1 och medel_temp_plats2) för de två valda platserna. Färgerna för staplarna definieras som blå och ljusblå.
    ax[0].set_ylabel('Medeltemperatur') #  Dessa rader sätter en etikett för y-axeln och en titel för den första subploten, vilket specificerar att det handlar om jämförelse av medeltemperatur.
    ax[0].set_title('Temperaturjämförelse') # Dessa rader sätter en etikett för y-axeln och en titel för den första subploten, vilket specificerar att det handlar om jämförelse av medeltemperatur.

    # Nederbörd
    ax[1].bar([plats1, plats2], [medel_nederbord_plats1, medel_nederbord_plats2], color=['green', 'lightgreen']) # Skapar en andra stapeldiagram på den andra axeln (ax[1]) för att visa jämförelse av medelnederbörd. Färgerna är här gröna och ljusgröna.
    ax[1].set_ylabel('Medelnederbörd') # Sätter etiketten för y-axeln och titeln för den andra subploten, indikerande att det är en jämförelse av nederbörd.
    ax[1].set_title('Nederbördsjämförelse') # Sätter etiketten för y-axeln och titeln för den andra subploten, indikerande att det är en jämförelse av nederbörd.

    # Vindstyrka
    ax[2].bar([plats1, plats2], [medel_vindstyrka_plats1, medel_vindstyrka_plats2], color=['red', 'pink']) # Skapar en tredje stapeldiagram på den tredje axeln (ax[2]) för att visa jämförelse av medelvindstyrka. Staplarna är färgade i rött och rosa.
    ax[2].set_ylabel('Medelvindstyrka') # Sätter etiketten för y-axeln och titeln för den tredje subploten, vilket indikerar att det är en jämförelse av vindstyrka.
    ax[2].set_title('Vindstyrkejämförelse') # Sätter etiketten för y-axeln och titeln för den tredje subploten, vilket indikerar att det är en jämförelse av vindstyrka.

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
