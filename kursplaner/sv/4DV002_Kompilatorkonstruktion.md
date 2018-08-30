# 4DV002 - Kompilatorkonstruktion (5 hp)

|     |     |
| --- | --- | 
| *Huvudområde*: | Datavetenskap | 
| *Fördjupning*: | A1N | 

## Förkunskaper

- 1DV004 - Objektorienterad programmering  
- 1DV006 - Algoritmer
- 1MA001 - Diskret matematik
- 2DV001 - Datorns uppbyggnad 
- 2DV002 - Mjukvaruarkitektur

## Lärandemål

Efter slutförd kurs skall studenten kunna:

1. *Kunskap och förståelse*
    1. Beskriva en kompilators olika faser,
    2. förklara olika parsningstekniker,
    3. förklara vad sker i den semantiska analysen, 
    4. förklara hur typsystem fungerar för några vanliga programspråk, samt
    5. förklara hur en stackmaskin fungerar.
2. *Färdighet och förmåga*
    1. Definiera en finit tillståndsmaskin och en LL(1)-kontextfri grammatik för enkla programspråk,
    2. designa och implementera en semantisk analys med felhantering, typinterferens och som dekorerar syntaxträdet med typinformation, 
    3. implementera en parser med hjälp av ett givet parsergeneratorverktyg, samt
    4. designa och implementera en stackmaskinbaserad virtuell maskin.
3. *Värderingsförmåga och förhållningssätt*
    1. Värdera svårigheten i att hantera olika programkonstruktioner, samt
    2. välja och reflektera över lämplig formell notation för att beskriva ett givet formellt språk.

## Kursinnehåll

Kursen presenterar tekniker, teorier och verktyg som används då man utvecklar en kompilator. Kursen diskuterar också hur dessa idéer kan användas för att definiera, hantera och interpretera domänspecifika språk inom modelldriven programvaruutveckling. Ett fokus blir därför kompilatorns frontend, generering av mellannivå-representationer, och hur dessa representationer kan exekveras. 

Följande moment behandlas:

- Kompilatorns olika faser.
- Objekt­-orienterad kompilatordesign.
- Lexikalanalys med hjälp av finita automater och reguljära uttryck.
- Kontextfria grammatiker och språk.
- Olika parsningtekniker för kontextfria språk.
- Typsystem och typinterferens.
- Attribuerade grammatiker.
- Semantisk analys.
- Mellannivå-representationer.
- Kodgenerering.
- Stackmaskiner.

## Undervisnings- och arbetsformer

Undervisningen består av föreläsningar och lärarhandledd hantering av inlämnings- och programmeringsuppgifter. Inlämningsuppgifterna är individuella, programmeringsuppgifterna sker i par.  

## Examination

Examinationen av kursen delas in i följande moment:

| Kod  | Benämning             | Betyg | Poäng | 
| :--- | :-------------------- | :---: | :---: |
|`UPG1`| Inlämningsuppgifter   | A-F   | 1     |
|`LAB1`| Programmeringsuppgifter | A-F   | 2     |
|`TEN1`| Skriftlig tentamen    | A-F   | 2     |

För godkänt betyg på kursen krävs minst betyg E på samtliga moment. Slutbetyget bestäms från:`UPG1`(20%),`LAB1`(40%) och`TEN1`(40%).

## Måluppfyllelse

Examinationsmomenten på kursen kopplas till lärandemålen enligt följande:

| Lärandemål |`UPG1` |`LAB1` |`TEN1` | 
| :--------- | :---: | :---: | :---: |
| 1.1        |       |       | **X** |
| 1.2        |       |       | **X** |
| 1.3        |       |       | **X** |
| 1.4        |       |       | **X** |
| 1.5        |       |       | **X** |
| 2.1        | **X** |       |       |
| 2.2        | **X** | **X** |       |
| 2.3        |       | **X** |       |
| 2.4        |       | **X** |       |
| 3.1        |       |       | **X** |
| 3.2        |       |       | **X** |

## Kurslitteratur

Obligatorisk litteratur:

- Aho, A. V., Lam, M. S., Sethi, R. och Ullman, J. D., *Compilers: Principles, Techniques, and Tools*, Pearson Education, 2006. Antal sidor: 510 av 986.

## Övrigt

Kursen genomförs på ett sådant sätt att kursdeltagarnas erfarenheter och kunskap görs synlig och utvecklas. Det innebär till exempel att vi har ett inkluderande förhållningssätt och strävar efter att ingen ska känna sig exkluderad. Detta kan yttra sig på olika sätt i en kurs, till exempel genom att som läraren använder sig utav könsneutrala exempel.
