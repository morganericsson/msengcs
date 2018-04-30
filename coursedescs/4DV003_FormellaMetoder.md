# 4DV003 - Formella metoder (5 hp)

|     |     |
| --- | --- | 
| *Huvudområde*: | Datavetenskap | 
| *Fördjupning*: | A1F | 

## Förkunskaper

- 1DV003 - Databaser och datamodellering
- 1DV005 - Jämnlöpande program 
- 1DV006 - Algoritmer
- 2DV006 - Datorsäkerhet
- 1MA001 - Diskret matematik
- 4DV001 - Modellering och simulering av system

## Lärandemål

Efter slutförd kurs skall studenten kunna:

1. *Kunskap och förståelse*
    1. resonera kring vad säkerhet (security och safety) betyder för ett mjukvaruprogram eller system och vilka egenskaper som krävs.
    2. beskriva metoder för och svårigheter med att formellt verifiera egenskaper relaterade till säkerhet och korrekthet hos mjukvarusystem samt vilka begränsningar olika metoder har,
    3. redogöra för de senaste rönen inom formella metoder och verifikation, samt
    4. redogöra för hur runtime-övervakning kan användas för att genomdriva säkerhetskrav.
2. *Färdighet och förmåga*
    1. kunna uttrycka säkerhetsegenskaper hos (jämnlöpande) system och mjukvaruprogram formellt med hjälp av olika typer av logik,
    2. använda olika metoder för att verifiera korrekthet och säkerhet hos system under modellering och mjukvaruprogram, samt
    3. använda de vanligaste verktygen och programmen för att beskriva och verifiera system och mjukvaruprogram.
3. *Värderingsförmåga och förhållningssätt*
    1. Resonera kring vilka samhällskostnader (och konsekvenser) felaktig och osäker mjukvara medför samt hur formella metoder kan spela in för att t.ex. reglera mjukvara inom vissa domäner.

## Kursinnehåll

Kursen ger en introduktion till formell verifikation. Den bygger vidare på sats och predikatlogik och introducerar t.ex. logiker som tar hänsyn till tid. 

Följande moment behandlas:

- Introduktion till formell verifikation
- Klassifikation av olika verifikationstekniker
- Processalgebra (CCS), samt hur dessa kan utökas med tidsfördröjningar
- Tidstillståndsmaskin (timed automata)
- Fördjupning av sats- och predikatlogik, samt temporallogik (LTL och CTL).
- Programspråkssemantik
- Programverifikation med hjälp av Hoare-logik och separationslogik
- Modellkontroll med hjälp av LTL och CTL
- Runtime-övervakning

## Undervisnings- och arbetsformer

Undervisningen består av föreläsningar och lärarledda laborationer. Kursen innehåller även en serie gästföreläsningar där industrirepresentanter och forskare presenterar hur och varför de använder formell verifikation samt vilka metoder och verktyg de använder.

## Examination

Examinationen av kursen delas in i följande moment:

| Kod  | Benämning                                   | Betyg | Poäng |  
| :--- | :------------------------------------------ | :---: | :---: |  
| PRJ1 | Formell verifikation av ett mjukvaruprogram | A-F   | 1     |  
| PRJ2 | Formell verifikation av en systemmodell     | A-F   | 1     |  
| TEN1 | Skriftlig tentamen                          | A-F   | 3     |  

För godkänt betyg på kursen krävs minst betyg E på samtliga moment. Slutbetyget bestäms från: PRJ1 (20%), PRJ2 (20%) och TEN1 (60%).

## Måluppfyllelse

Examinationsmomenten kopplas till lärandemålen enligt följande:

| Lärandemål | PRJ1  | PRJ2  | TEN1  |
| :--------- | :---: | :---: | :---: |
| 1.1        | **X** | **X** | **X** |
| 1.2        |       |       | **X** |
| 1.3        | **X** | **X** | **X** |
| 1.4        |       |       | **X** |
| 2.1        | **X** | **X** | **X** |
| 2.2        | **X** | **X** |       |
| 2.3        | **X** | **X** |       |
| 3.1        |       |       | **X** |

## Kurslitteratur

Obligatorisk litteratur:

- Aceto, L., Ingólfsdóttir, A., Guldstrand Larsen, K. och Srba, J., *Reactive Systems: Modelling, Specification and Verification*, Cambridge University Press, 2014.  Antal sidor: 150 av 281.
- Huth, M. och Ryan, M., *Logic in Computer Science: Modelling and Reasoning about Systems*, andra utgåvan, Cambridge University Press, 2004. Antal sidor: 300 av 412.
- Kompendium med vetenskapliga artiklar
