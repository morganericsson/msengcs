# 4DV006 -  Parallelldatorprogrammering (5 hp)

|     |     |
| --- | --- | 
| *Huvudområde*: | Datavetenskap | 
| *Fördjupning*: | A1N | 

## Förkunskaper

- 1DV005 - Jämnlöpande program
- 1DV006 - Algoritmer
- 2DV001 - Datorns uppbyggnad
- 2DV004 - Datorgrafik

## Lärandemål

Efter slutförd kurs skall studenten kunna:

1. *Kunskap och förståelse*
    1. Förklara de huvudsakliga likheterna och skillnaderna mellan jämnlöpande och parallella program, 
    2. beskriva olika typer av parallella datorer och acceleratorer samt resonera kring vilken typ som bäst lämpar sig för ett givet problem, samt
    3. redogöra för de senaste rönen inom parallella datorer och acceleratorer, samt hur man programmerar dessa på lämpliga sätt.
2. *Färdighet och förmåga*
    1. Bryta ner problem, formulera parallella algoritmer för att lösa dessa, och implementera dessa för olika typer av parallella datorer och acceleratorer, t.ex. med hjälp av OpenMP, CUDA, eller MPI, 
    2. planera och driftsätta ett kluster och lämplig mjukvara (t.ex. MPI) för att lösa en viss typ av problem, samt
    3. givet ett problem och en implementation, resonera kring förväntad prestanda och olika sätt att öka denna.
3. *Värderingsförmåga och förhållningssätt*
    1. Reflektera kring kostnaden för att lösa vissa typer av problem, t.ex. med avseende på faktiska kostnader och energi/miljökostnader, samt hur dessa påverkas av val av arkitektur, algoritm, osv.,

## Kursinnehåll

Kursen ger en fördjupning i hur problem kan lösas med hjälp av parallelldatorer och acceleratorer, hur problem bryts ner, och hur program kan optimeras för olika dator- och accelerator-arkitekturer. 

Följande moment behandlas:

- Introduktion till homogena och heterogena parallella datorer.
- Introduktion till grafikprocessorer och acceleratorer.
- Fördjupning i hur problem kan brytas ned för parallell exekvering.
- OpenMP.
- Programmering av beräkningsklustrer med hjälp av t.ex. MPI.
- Programmering av grafikprocessorer med hjälp av t.ex. CUDA.
- Parallella mönster såsom prefixsumma, map-reduce, matrisberäkningar, merge-sortering och sökning i grafer.
- Exempel på hur parallellprogrammering kan användas inom olika domäner, t.ex. maskininlärning, bildbehandling och bildanalys.
- Planering och driftsättning av (virtuella) klustrar i molnet.
- Vanliga benchmarks och hur dessa används för att uppskatta prestanda.
- Enklare verktyg för att testa och felsöka parallella program.

## Undervisnings- och arbetsformer

Undervisningen består av föreläsningar, seminarier och lärarledda laborationer. Kursen innehåller även en serie gästföreläsningar där industrirepresentanter och forskare presenterar hur de använder parallelldatorer och acceleratorer samt vilken typ av problem de löser med hjälp av dessa.

## Examination

Examinationen av kursen delas in följande moment:

| Kod  | Benämning             | Betyg | Poäng |  
| :--- | :-------------------- | :---: | :---: |  
| TEN1 | Skriftlig tentamen    | A-F   | 1     |  
| LAB1 | Programmeringsuppgifter | A-F   | 4     |  

För godkänt betyg på kursen krävs minst betyg E på samtliga moment. Slutbetyget bestäms från: TEN1 (30%) och LAB1 (70%).

## Måluppfyllelse

Examinationsmomenten kopplas till lärandemålen enligt följande:

| Lärandemål | TEN1  | LAB1  |
| :--------- | :---: | :---: |
| 1.1        | **X** | **X** |
| 1.2        | **X** |       |
| 1.3        | **X** | **X** |
| 2.1        |       | **X** |
| 2.2        |       | **X** |
| 2.3        |       | **X** |
| 3.1        | **X** |       |

## Kurslitteratur

Obligatorisk litteratur:

- Kirk, D. och Hwu, W-M., *Programming Massively Parallel Processors - A Hands-on Approach*, tredje utgåvan, Morgan Kaufmann, 2016. Antal sidor: 500 / 576
- Kompendium med vetenskapliga artiklar.

## Övrigt

Kursen bedrivs på ett sådant sätt att både mäns och kvinnors erfarenhet och kunskaper synliggörs och utvecklas.
