# 1DV003 - Databaser och datamodellering (5 hp)

|     |     |
| --- | --- | 
| *Huvudområde*: | Datavetenskap | 
| *Fördjupning*: | G1F | 

## Förkunskaper

- 1DV001 - Programmering och datastrukturer
- 1DV002 - Introducerande projekt
- 1MA001 - Diskret matematik

## Lärandemål

Efter slutförd kurs skall studenten kunna:

1. *Kunskap och förståelse*
    1. Förklara de grundläggande begreppen relaterade till datorbaserade informationssystem samt förklara de viktigaste problemen och regelverken i samband med datahantering i stora organisationer och företag,
    2. översiktligt redogöra för olika databastyper, t.ex. relations-,  dokument- och objekt-baserade, 
    3. förklara de olika typerna av modeller (konceptuell, logisk och fysisk) som används för att ta fram och resonera kring en databas,
    4. förklara relationsmodellen, relationsalgebra, kopplingen till predikatlogik och normalformer, samt
    5. redogöra för hur data, t.ex. tabeller, kan lagras på block-enheter, t.ex. hårddiskar, inklusive att kunna beskriva de algoritmer och datastrukturer som behövs.
2. *Färdighet och förmåga*
    1. Utforma datamodeller på olika semantiska nivåer (begreppsmässig, logisk, fysisk) med hjälp av lämplig formalism, såsom Entity-Relationship och relationsmodeller,
    2. optimera en databasdesign genom att använda normalformer (1NF, 2NF, 3NF, BCNF), med beaktande av egenskaperna hos de fysiska medier som används för datalagring, samt
    3. implementera relationsdatamodeller i en databashanterare samt skapa, fråga och manipulera data med hjälp av SQL via klientprogram och program implementerade i Python.
3. *Värderingsförmåga och förhållningssätt*
    1. Analysera och värdera en domän och dess begränsningar som en datamodell samt muntligt och skriftligt diskutera fördelarna och nackdelarna med designen,
    2. reflektera över egenskaperna hos olika datamodeller och välja de som är mest lämpade för det problem som ska lösas, samt
    3. resonera om hur olika designalternativ påverkar databasens egenskaper, t.ex. prestanda och möjliga frågor.


## Kursinnehåll

Kursen ger en introduktion till databaser och informationshanteringssystem. Den utgår från grunderna i hur data kan lagras, t.ex. via relationsmodellen eller via nätverksmodeller och diskuterar hur frågespråk kan byggas ovanpå dessa. Bra design diskuteras på flera olika nivåer, från logiska datamodeller, till t.ex. relationsmodellen och normalformer och den faktiska fysiska lagringen. 

Följande moment behandlas:

- Introduktion till datorbaserade informationshanteringssystem 
- Vikten av databaser och informationshantering i samhället
- Vilken data kan, får och bör lagras. Vilka regelverk gäller, t.ex. GDPR
- Konceptuella, logiska och fysiska datamodeller
- Olika typer av databashanterare
- Diagram för att modellera data, t.ex. E/R
- Relationsmodeller och relationsalgebra
- Databasfrågor och databasmanipulation med SQL
- Funktionella beroenden och normalformer (1NF, 2NF, 3NF, BCNF)
- Installation och användning av vanliga databashanterare, t.ex. MySQL i labbmiljön.
- Utveckling av program som använder en databas
- Predikatlogik och dess relation till databaser
- Introduktion till samtidighet, låsning och hur transaktioner fungerar
- Filsystem och hur data lagras på blockenheter (t.ex. hårddiskar)

## Undervisnings- och arbetsformer

Undervisningen sker i form av föreläsningar, lärarledda laborationer och handledning av inlämningsuppgifter. Laborationer och inlämningsuppgifter sker i par. I vissa moment av kursen förväntas studenten att på egen hand söka den information som behövs för att lösa en uppgift.

## Examination

Examinationen av kursen delas in i följande moment:

| Kod  | Benämning               | Betyg | Poäng |  
| :--- | :--------------------   | :---: | :---: |  
| MUN1 | Muntlig tentamen        | A-F   | 2     |  
| LAB1 | Programmeringsuppgifter | A-F   | 2     |  
| UPG1 | Inlämningsuppgifter     | A-F   | 1     |  

För godkänt betyg på kursen krävs minst betyg E på samtliga moment. Slutbetyget bestäms från: MUN1 (40%), LAB1 (40%) och UPG1 (20%).

## Måluppfyllelse

Examinationsmomenten kopplas till lärandemålen enligt följande:

| Lärandemål | MUN1  | LAB1  | UPG1  |
| :--------- | :---: | :---: | :---: |
| 1.1        | **X** |       |       |
| 1.2        | **X** |       |       |
| 1.3        | **X** |       |       |
| 1.4        | **X** |       | **X** |
| 1.5        | **X** |       | **X** |
| 2.1        | **X** | **X** | **X** |
| 2.2        | **X** | **X** | **X** |
| 2.3        |       | **X** |       |
| 3.1        | **X** |       | **X** |
| 3.2        | **X** | **X** |       |
| 3.3        | **X** | **X** |       |


## Kurslitteratur

Obligatorisk litteratur:

- Garcia-Molina, H., Ullman, J. D. och Widom, J., *Database Systems: The Complete Book*, andra utgåvan, Pearson, 2013. Antal sidor: 700 av 1140.

## Övrigt

Kursen bedrivs på ett sådant sätt att både mäns och kvinnors erfarenhet och kunskaper synliggörs och utvecklas.