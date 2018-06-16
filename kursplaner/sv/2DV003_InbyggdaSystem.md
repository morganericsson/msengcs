# 2DV003 - Inbyggda system (5 hp)

|     |     |
| --- | --- | 
| *Huvudområde*: | Datavetenskap | 
| *Fördjupning*: | G2F | 

## Förkunskaper

- 1DV004 - Objektorienterad programmering
- 1DV005 - Jämnlöpande program
- 2DV001 - Datorns uppbyggnad
- 1FY001 - Mekanik
- 1FY002 - Ellära och magnetism

## Lärandemål

Efter slutförd kurs skall studenten kunna:

1. *Kunskap och förståelse*
    1. Beskriva de huvudsakliga applikationerna och referensarkitekturerna (CPU, buss, gränssnitt etc.) för inbyggda system och realtidshantering,
    2. definiera gränssnittet mellan hårdvara och programvara och påvisa relaterade begränsningar och potentiella risker,
    3. sammanfatta hur inbyggda operativsystem är strukturerat och arbetar, särskilt när det gäller avbrott, processer, trådar och schemaläggare, samt
    4. förklara anomalier vid schemaläggning, deras orsaker och hur man hanterar dem.
2. *Färdighet och förmåga*
    1. Använda olika metoder för att bestämma möjligheten att schemalägga en uppsättning periodiska uppgifter,
    2. använda effektiva språk och designmiljöer för inbyggda system,
    3. formge och implementera inbyggda program för att styra hårdvaruenheter, sensorer och manöverdon, samt
    4. implementera undantags- och avbrottsrutiner.
3. *Värderingsförmåga och förhållningssätt*
    1. Bedöma för- och nackdelar för olika schemaläggningsmetoder, samt
    2. bedöma för- och nackdelar för olika synkroniseringsmetoder.

## Kursinnehåll

Kursen ger en introduktion till inbyggda system, sensorer och manöverdon, samt hur dessa nås från mjukvara. Kursen ger sedan en fördjupning i schemaläggning för realtidssystem och vilka krav som olika algoritmer kan uppfylla. Konsekvenser av att missa deadline diskuteras också.

Följande moment behandlas:

- Introduktion till inbyggda system samt fysiska och simulerade miljöer.
- Sensorer och manöverdon i inbyggda system.
- Begreppen tid och tidshantering, monoton och icke-monoton tid samt fördröjningar.
- Realtidsoperativsystem och schemaläggning av uppgifter.
- Metoder för avbrottsstyrd schemaläggning.
- Synkronisering av uppgifter, omkastad prioritet, prioritetsarv, begränsad prioritet.
- Hantering av undantag och avbrott.

## Undervisnings- och arbetsformer

Undervisningen sker i form av föreläsningar och lärarledda laborationer. Laborationer är dels individuella, dels i form av grupparbeten. 

Obligatorisk närvaro kan förekomma på vissa moment.

## Examination

Examinationen av kursen delas in i följande moment:

| Kod  | Benämning               | Betyg | Poäng | 
| :--- | :--------------------   | :---: | :---: |
|`LAB1`| Programmeringsuppgifter | A-F   | 1,5   |
|`PRJ1`| Projekt                 | A-F   | 2     |
|`HEM1`| Hemtentamen                | A-F   | 1,5   |

För godkänt betyg på kursen krävs minst betyg E på samtliga moment. Slutbetyget bestäms från:`LAB1`(25%),`PRJ1`(35%) och`HEM1`(40%).

## Måluppfyllelse

Examinationsmomenten på kursen kopplas till lärandemålen enligt följande:

| Lärandemål |`LAB1` |`PRJ1` |`HEM1` |
| :--------- | :---: | :---: | :---: |
| 1.1        |       |       | **X** |
| 1.2        |       |       | **X** |
| 1.3        |       |       | **X** |
| 1.4        |       |       | **X** |
| 2.1        | **X** |       | **X** |
| 2.2        | **X** | **X** |       |
| 2.3        | **X** | **X** |       |
| 2.4        | **X** |       |       |
| 3.1        |       | **X** | **X** |
| 3.2        |       | **X** | **X** |

## Kurslitteratur

Obligatorisk litteratur:

- Buttazzo, G., *Hard real-time computing systems - predictable scheduling algorithms and applications*, Springer, 2011. Antal sidor: 400 av 485.
- Kopetz, H., *Real-time systems: Design principles for distributed embedded applications*. Springer, 2011. Antal sidor: 300 av 339. 

## Övrigt

Kursen genomförs på ett sådant sätt att kursdeltagarnas erfarenheter och kunskap görs synlig och utvecklas. Det innebär till exempel att vi har ett inkluderande förhållningssätt och strävar efter att ingen ska känna sig exkluderad. Detta kan yttra sig på olika sätt i en kurs, till exempel genom att som läraren använder sig utav könsneutrala exempel.