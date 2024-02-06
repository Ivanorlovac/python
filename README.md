Min applikation är designad för att analysera och visualisera väderdata. Den tillåter användarna att jämföra väderförhållandena mellan två valda platser baserat
på historiska data om temperatur, nederbörd, och vindstyrka. 
Applikationen är byggd i Python, och använder populära bibliotek som Pandas för datahantering, NumPy för numeriska beräkningar och Matplotlib för att skapa visuella representationer av data.

Funktioner och Processer

1. Applikationen börjar med att läsa in väderdata från en CSV-fil med hjälp av Pandas.
   Datan innehåller flera kolumner: Datum, Plats, Temperatur, Nederbörd, och Vindstyrka.

3. Genom terminalen frågar applikationen användaren att mata in två platser för jämförelse. Detta steg involverar direkt interaktion där användarens val avgör vilka datasegment som ska analyseras.

4. För varje angiven plats filtrerar applikationen ut relevant data från den totala datasetet.
   Den beräknar sedan medelvärden för temperatur, nederbörd, och vindstyrka för dessa platser. Detta görs med NumPy för att säkerställa effektiv och noggrann beräkning.

6. Med hjälp av Matplotlib skapar applikationen tre olika stapeldiagram för att visualisera jämförelser av de beräknade medelvärdena för temperatur, nederbörd, och vindstyrka mellan de två valda platserna.
   Varje grafik är unikt anpassad med färgkoder och etiketter för att förbättra läsbarheten och insikten från visualiseringarna.



Applikationen är strukturerad runt flera funktioner som var och en ansvarar för en specifik del av processen, från datainläsning till visualisering. Detta gör koden modulär, lättare att underhålla och utöka.
Användningen av `if __name__ == "__main__":` mönster säkerställer att applikationen kan köras som ett fristående skript samtidigt som den tillåter att dess delar kan importeras och återanvändas i andra Python-skript.


Lista över städer du kan jämföra:

Stockholm,
Göteborg,
Malmö,
Uppsala,
Linköping,
Karlstad,
Umeå,
Luleå,
Borås,
Helsingborg,
Lund,
Halmstad.

Programmet ber dig först ange namnet på den första staden och sedan namnet på den andra.

Alla kommentarer finns i main.py
