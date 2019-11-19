# Model for predictions

## Usage:
```
from joblib import load
model = load('model.joblib')

prediction = model.predict(['neighbourhood_group', 
                            'neighbourhood', 
                            'room_type', 
                            'minimum_nights', 
                            'calculated_host_listings_count', 
                            'availability_365', 
                            'bathrooms', 
                            'bedrooms'])
```

## Mapping for `room_type`, `neighbourhood_group`, and `neighbourhood`:

### Room_type:
```
Entire home/apt    1
Private room       2
Shared room        3
```

### Neighbourhood_group:
```
Mitte                        1
Pankow                       2
Tempelhof - Schöneberg       3
Friedrichshain-Kreuzberg     4
Charlottenburg-Wilm.         5
Neukölln                     6
Treptow - Köpenick           7
Steglitz - Zehlendorf        8
Reinickendorf                9
Lichtenberg                 10
Marzahn - Hellersdorf       11
Spandau                     12
```

### Neighbourhood:
```
Brunnenstr. Süd                                1
Prenzlauer Berg Nordwest                       2
Prenzlauer Berg Südwest                        3
Schöneberg-Nord                                4
Helmholtzplatz                                 5
Frankfurter Allee Süd FK                       6
nördliche Luisenstadt                          7
südliche Luisenstadt                           8
Tempelhofer Vorstadt                           9
Prenzlauer Berg Süd                           10
Moabit Ost                                    11
Prenzlauer Berg Nord                          12
Otto-Suhr-Allee                               13
Schillerpromenade                             14
Alt  Treptow                                  15
Alexanderplatz                                16
Neue Kantstraße                               17
Ostpreußendamm                                18
Schmöckwitz/Karolinenhof/Rauchfangswerder     19
Neuköllner Mitte/Zentrum                      20
Frankfurter Allee Nord                        21
Kantstraße                                    22
Schmargendorf                                 23
Regierungsviertel                             24
Reuterstraße                                  25
Schöneberg-Süd                                26
Blankenfelde/Niederschönhausen                27
Friedrichshagen                               28
Südliche Friedrichstadt                       29
Moabit West                                   30
Wiesbadener Straße                            31
West 3                                        32
Blankenburg/Heinersdorf/Märchenland           33
Rummelsburger Bucht                           34
Friedenau                                     35
Brunnenstr. Nord                              36
Ost 2                                         37
Volkspark Wilmersdorf                         38
Pankow Zentrum                                39
Pankow Süd                                    40
Osloer Straße                                 41
Drakestr.                                     42
West 1                                        43
Prenzlauer Berg Ost                           44
Buckow Nord                                   45
Karlshorst                                    46
Karl-Marx-Allee-Nord                          47
Alt-Lichtenberg                               48
Düsseldorfer Straße                           49
Zehlendorf  Nord                              50
Tiergarten Süd                                51
Neu Lichtenberg                               52
Rudow                                         53
Mierendorffplatz                              54
Wedding Zentrum                               55
Karl-Marx-Allee-Süd                           56
Altglienicke                                  57
Lichtenrade                                   58
Westend                                       59
Mahlsdorf                                     60
West 5                                        61
Rixdorf                                       62
Biesdorf                                      63
Zehlendorf  Südwest                           64
Johannisthal                                  65
Barstraße                                     66
Marienfelde                                   67
Heerstraße Nord                               68
Albrechtstr.                                  69
Buckow                                        70
Baumschulenweg                                71
Halensee                                      72
Schloß Charlottenburg                         73
Kurfürstendamm                                74
Schloßstr.                                    75
Nord 1                                        76
Karow                                         77
Nord 2                                        78
Rahnsdorf/Hessenwinkel                        79
Gatow / Kladow                                80
Lankwitz                                      81
Parkviertel                                   82
Alt-Hohenschönhausen Süd                      83
Weißensee                                     84
Schönholz/Wilhelmsruh/Rosenthal               85
Weißensee Ost                                 86
Alt-Hohenschönhausen Nord                     87
Gropiusstadt                                  88
Britz                                         89
Tempelhof                                     90
Ost 1                                         91
Kaulsdorf                                     92
Hellersdorf-Nord                              93
Marzahn-Mitte                                 94
MV 1                                          95
Adlershof                                     96
Heerstrasse                                   97
Teltower Damm                                 98
Köllnische Heide                              99
Friedrichsfelde Nord                         100
Grunewald                                    101
Plänterwald                                  102
Buchholz                                     103
Wilhelmstadt                                 104
West 4                                       105
Fennpfuhl                                    106
Köpenick-Nord                                107
Bohnsdorf                                    108
Mariendorf                                   109
Frankfurter Allee Süd                        110
MV 2                                         111
Marzahn-Süd                                  112
Siemensstadt                                 113
Müggelheim                                   114
Charlottenburg Nord                          115
Oberschöneweide                              116
Buch                                         117
Niederschöneweide                            118
Spandau Mitte                                119
Dammvorstadt                                 120
Brunsbütteler Damm                           121
Hakenfelde                                   122
Köpenick-Süd                                 123
Neu-Hohenschönhausen Nord                    124
Hellersdorf-Süd                              125
Grünau                                       126
Falkenhagener Feld                           127
Haselhorst                                   128
West 2                                       129
Altstadt-Kietz                               130
Friedrichsfelde Süd                          131
Neu-Hohenschönhausen Süd                     132
Malchow, Wartenberg und Falkenberg           133
Kölln. Vorstadt/Spindlersf.                  134
Hellersdorf-Ost                              135
Allende-Viertel                              136
```
