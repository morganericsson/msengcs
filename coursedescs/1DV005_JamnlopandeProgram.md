# 1DV005 - Jämnlöpande program (7,5 hp)

|     |     |
| --- | --- | 
| *Huvudområde*: | Datavetenskap | 
| *Fördjupning*: | G1F | 

## Förkunskaper

- 1DV003 - Databaser och datamodellering
- 1DV004 - Objekt-orienterad programmering

## Lärandemål

Efter slutförd kurs skall studenten kunna:

1. *Kunskap och förståelse*
    1. Förklara problem med delade resurser såsom låsningar, svält och race conditions,
    2. förklara några vanliga metoder för att hantera låsningar (t.ex. semaforer) samt deras egenskaper och begränsningar,
    3. förklara olika konsistensmodeller,
    4. resonera om olika egenskaper hos jämnlöpande program såsom korrekthet och avslutning,
    5. förklara skillnaden mellan delat minne och meddelande, samt
    6. förklara skillnaden mellan parallellism, samtidighet och asynkron exekvering.
2. *Färdighet och förmåga*
    1. Utveckla jämnlöpande program i Java för en dator med delat minne genom att använda trådar och låsning,
    2. implementera lås-fria datastrukturer i Java, 
    3. bevisa att (enkla) jämnlöpande program är korrekta, samt
    4. analysera ett problem och implementera en lämplig jämnlöpande lösning som är korrekt synkroniserad.
3. *Värderingsförmåga och förhållningssätt*
    1. Välja och föra ett resonemang om delat minne eller meddelanden är mest lämpligt vid ett givet problem.

## Kursinnehåll

Kursen introducerar hur jämnlöpande programmering och de problem detta medför, t.ex. låsningar och race-conditions. Olika sätt att hanteras dessa problem, t.ex. låsningsalgoritmer och meddelande-hantering diskuteras, samt vilka begränsningar dessa medför. Innehållet och algoritmerna exemplifieras med hjälp av trådar i Java.

Följande moment behandlas:

- Processer och synkronisering
- Schemaläggning 
- Delat minne och meddelanden
- Jämnlöpande programmering med trådar och delade variabler 
- Kritiska sektioner
- Lås, barriärer, semaforer och monitors
- Distribuerade/jämnlöpande algoritmer
- Konsistensmodeller
- Jämnlöpande och låsfria datastrukturer

## Undervisnings- och arbetsformer

Undervisningen består av föreläsningar och lärarhandledda laborationer. Programmeringsuppgifterna sker i par.  

## Examination

Examinationen av kursen delas in i följande moment:

| Kod  | Benämning               | Betyg | Poäng | 
| :--- | :-----------------------| :---: | :---: |
| TEN1 | Skriftlig tentamen      | A-F   | 4     |
| LAB1 | Programmeringsuppgifter | A-F   | 3,5   |

För godkänt betyg på kursen krävs minst betyg E på samtliga moment. Slutbetyget bestäms från: TEN1 (60%) och LAB1 (40%).

## Måluppfyllelse

Examinationsmomenten kopplas till lärandemålen enligt följande:

| Lärandemål | TEN1  | LAB1  |  
| :--------- | :---: | :---: |  
| 1.1        | **X** |       |  
| 1.2        | **X** | **X** |  
| 1.3        | **X** |       |  
| 1.4        | **X** | **X** |  
| 1.5        | **X** |       |  
| 1.6        | **X** |       |  
| 2.1        |       | **X** |  
| 2.2        |       | **X** |  
| 2.3        | **X** |       |  
| 2.4        | **X** | **X** |  
| 3.1        |       | **X** |  

## Kurslitteratur

Obligatorisk litteratur:

- Herlihy, M. och Shavit N., *The Art of Multiprocessor Programming*, Morgan Kaufmann, 2012. Antal sidor: 400 av 536.

## Övrigt

Kursen bedrivs på ett sådant sätt att både mäns och kvinnors erfarenhet och kunskaper synliggörs och utvecklas.