#!/usr/bin/python
#-*- coding: utf-8 -*-
"""
This module contains a lot of abbreviations for the program. 

**Source abbreviations**:

    * AHJ:Ahjos et al. 1984-88 1988-89 1990 FINLAND
    * AMB:Ambraseys 1985ab NORWAY
    * ANA:Ananin and Panasenko 1982 NW RUSSIA
    * APA:Kola Science Centre Apatity Russia NW RUSSIA
    * ARV:Arvidsson et al. 1992 SWEDEN
    * BER:Univ. BERGEN Norway NORWAY
    * BGS:British Geological Survey UK NORTH SEA
    * BKH:NORSAR Kjeller Norway 1980 1984 NORTH SEA
    * BAT:Båth 1956 1979 SWEDEN
    * COP:Kort og Matrikkelstyrelsen COPENHAGEN Denmark 1962- 1985  DENMARK
    * DOS:Doss 1910 NW RUSSIA
    * DNK:Geological Survey of Denmark and Greenland DENMARK
    * DSI:Nikonov and Sildvee referring to Doss 1988 NW RUSSIA
    * ERW:Wahlström referring to Erdmann 1990 SWEDEN
    * EKS:Ekström 1939 FINLAND
    * FOA:Slunga et al. 1984 SWEDEN
    * GRE:Gregersen 1979 DENMARK
    * GUW:Wahlström referring to Gumaelius 1990 SWEDEN
    * HJE:Hjelme personal communication DENMARK
    * HEL:Inst. Seismology Univ. HELSINKI 1971- 
    * HOL:Holmquist 1987; Holmquist and Wahlström 1987 SWEDEN
    * IGS:Inst. Geological Sciences Edinburg UK NORTH SEA 
    * ISC:International Seismological Center 1964- 
    * IVO:Saari 1990 FINLAND
    * KAR:Karjalainen 1936 FINLAND
    * KAT:Kataja see Penttilä 1978 FINLAND
    * KIM:Kim et al. 1988 1989 SWEDEN
    * KJE:Kjellen 1910 SWEDEN
    * KJW:Wahlström referring to Kjellen 1990 SWEDEN
    * KOL:Kolderup 1899-1936 1913 NORWAY
    * KON:Kondorskaya et al. 1988 NW RUSSIA
    * KOR:Korhonen 1978; Korhonen and Ahjos 1979 FINLAND
    * KSI:Nikonov and Sildvee 1988 NW RUSSIA 
    * KVA:Kvale 1952-59 1960 NORWAY
    * LEH:Lehman 1956 DENMARK
    * LIW:Wahlström referring to Linnarsson 1990 SWEDEN
    * MOS:World Data Center B Moscow Russia NW RUSSIA 
    * MUW:Muir Wood and Woo 1987 NORWAY
    * MUI:Muir Wood et al. 1988 NORWAY
    * NAO:NORSAR Kjeller Norway 1971- NORWAY
    * NOW:Wahlström referring to Nordenström 1990 SWEDEN
    * NSW:Wahlström referring to Nya Södertälje Tidning 1990 SWEDEN
    * OPT:Optun 1988 NORWAY
    * PAN:Panasenko 1977 1979 NW RUSSIA
    * PEN:Penttilä 1978 FINLAND
    * POR:Porkka see Penttilä 1978 FINLAND
    * REB:Båth referring to Renqvist 1956 SWEDEN FINLAND
    * REN:Renqvist 1930 FINLAND
    * REW:Wahlström referring to Renqvist 1990 SWEDEN
    * SEL:Sellevol et al. 1980 NORWAY
    * SIL:Nikonov and Sildvee 1988 NW RUSSIA 
    * SIW:Wahlström referring to Sidenbladh 1990 SWEDEN
    * SK :Siren and Korollef see Penttilä 1978 FINLAND
    * SLU:Slunga 1982 1985 1989a SWEDEN
    * SVW:Wahlström referring to Svedmark 1990 SWEDEN
    * TOW:Wahlström referring to Törnebohm 1990 SWEDEN
    * UPP:Univ. UPPSALA Sweden 1906- SWEDEN
    * USG:U.S. Geological Survey USA 1981- 
    * VES:Vesanen see Penttilä 1978 FINLAND
    * WAH:Wahlström and Ahjos 1982 Wahlström et al. 1987 SWEDEN FINLAND}

**Magnitude Scale abbreviations**:

    * M:macroseismic magnitude
    * I:magnitude based solely on intensity
    * R:magnitude based solely on radius of perceptibility
    * L:local magnitude by source reference
    * LB:B}th et al 1976
    * LW:Wahlstr|m and Ahjos 1982
    * LN:Norsar (B}th et al. 1976)
    * LU:UPP (Wahlstr|m and Ahjos 1982)
    * LH:HEL (Wahlstr|m and Ahjos 1982)
    * LA:HEL (Wahlstr|m and Ahjos 1982)
    * LF:FOA (Slunga 1982) 
    * LK:Kim et al. 1988 1989
    * C:magnitude based on signal coda duration
    * CB:BER (Bergen 1985-1991)
    * CH:HEL (Wahlstr|m and Ahjos 1982)
    * CP:Ananin and Panasenko 1982
    * PA:Ananin and Panasenko 1982
    * S:surface wave magnitude (Karnik 1969 Muir Wood and Woo 1987)
    * B:body wave magnitude
    * BI:ISC 1964-1991}

**Region Code abbreviations**:

    * A: GERMANY
    * B: BARENTS SEA
    * C: BALTIC SEA
    * D: DENMARK
    * E: GREAT BRITAIN
    * F: FINLAND
    * G: GREENLAND SEA
    * I: ICELAND REGION
    * J: JAN MAYEN
    * N: NORWAY
    * O: NORWEGIAN SEA
    * P: POLAND
    * R: NORTH SEA
    * S: SWEDEN
    * U: RUSSIA
    * V: ESTONIA

**Macroseismic Reference abbreviations**:

    * ARH: Arhe personal communication
    * HAV: Havskov and Optun 1984
    * KUL: Kulhanek and Wahlström 1981 1985
    * MOB: Moberg 1855 1891 1894 1900-01
    * ROS: Rosberg 1903-04 1912
    * TAL: Talvitie see Penttilä 1978
    * YLI: Yliniemi personal communication}

"""

source_reference = {"AHJ":["Ahjos et al., 1984-88, 1988-89, 1990", "FINLAND"],
                    "AMB":["Ambraseys, 1985a,b", "NORWAY"],
                    "ANA":["Ananin and Panasenko, 1982", "NW RUSSIA"],
                    "APA":["Kola Science Centre, Apatity, Russia", "NW RUSSIA"],
                    "ARV":["Arvidsson et al., 1992", "SWEDEN"],
                    "BER":["Univ. BERGEN, Norway", "NORWAY"],
                    "BGS":["British Geological Survey, UK", "NORTH SEA"],
                    "BKH":["NORSAR, Kjeller, Norway, 1980, 1984", "NORTH SEA"],
                    "BAT":["Båth, 1956, 1979", "SWEDEN"],
                    "COP":["Kort og Matrikkelstyrelsen, COPENHAGEN, Denmark, 1962-, 1985",  "DENMARK"],
                    "DOS":["Doss, 1910", "NW RUSSIA"],
                    "DNK":["Geological Survey of Denmark and Greenland", "DENMARK"],
                    "DSI":["Nikonov and Sildvee, referring to Doss, 1988", "NW RUSSIA"],
                    "ERW":["Wahlström, referring to Erdmann, 1990", "SWEDEN"],
                    "EKS":["Ekström, 1939", "FINLAND"],
                    "FOA":["Slunga et al., 1984", "SWEDEN"],
                    "GRE":["Gregersen, 1979", "DENMARK"],
                    "GUW":["Wahlström, referring to Gumaelius, 1990", "SWEDEN"],
                    "HJE":["Hjelme, personal communication", "DENMARK"],
                    "HEL":["Inst. Seismology, Univ. HELSINKI, 1971-", ""],
                    "HOL":["Holmquist, 1987; Holmquist and Wahlström, 1987", "SWEDEN"],
                    "IGS":["Inst. Geological Sciences, Edinburg, UK", "NORTH SEA"] ,
                    "ISC":["International Seismological Center, 1964-", ""],
                    "IVO":["Saari, 1990", "FINLAND"],
                    "KAR":["Karjalainen, 1936", "FINLAND"],
                    "KAT":["Kataja, see Penttilä, 1978", "FINLAND"],
                    "KIM":["Kim et al., 1988, 1989", "SWEDEN"],
                    "KJE":["Kjellen, 1910", "SWEDEN"],
                    "KJW":["Wahlström, referring to Kjellen, 1990", "SWEDEN"],
                    "KOL":["Kolderup, 1899-1936, 1913", "NORWAY"],
                    "KON":["Kondorskaya et al., 1988", "NW RUSSIA"],
                    "KOR":["Korhonen, 1978; Korhonen and Ahjos, 1979", "FINLAND"],
                    "KSI":["Nikonov and Sildvee, 1988", "NW RUSSIA"] ,
                    "KVA":["Kvale, 1952-59, 1960", "NORWAY"],
                    "LEH":["Lehman, 1956", "DENMARK"],
                    "LIW":["Wahlström, referring to Linnarsson, 1990", "SWEDEN"],
                    "MOS":["World Data Center B, Moscow, Russia", "NW RUSSIA"] ,
                    "MUW":["Muir Wood and Woo, 1987", "NORWAY"],
                    "MUI":["Muir Wood et al., 1988", "NORWAY"],
                    "NAO":["NORSAR, Kjeller, Norway, 1971-", "NORWAY"],
                    "NOW":["Wahlström, referring to Nordenström, 1990", "SWEDEN"],
                    "NSW":["Wahlström, referring to Nya Södertälje Tidning, 1990", "SWEDEN"],
                    "OPT":["Optun, 1988", "NORWAY"],
                    "PAN":["Panasenko, 1977, 1979", "NW RUSSIA"],
                    "PEN":["Penttilä, 1978", "FINLAND"],
                    "POR":["Porkka, see Penttilä, 1978", "FINLAND"],
                    "REB":["Båth, referring to Renqvist, 1956", "SWEDEN, FINLAND"],
                    "REN":["Renqvist, 1930", "FINLAND"],
                    "REW":["Wahlström, referring to Renqvist, 1990", "SWEDEN"],
                    "SEL":["Sellevol et al., 1980", "NORWAY"],
                    "SIL":["Nikonov and Sildvee, 1988", "NW RUSSIA"] ,
                    "SIW":["Wahlström, referring to Sidenbladh, 1990", "SWEDEN"],
                    "SK ":["Siren and Korollef, see Penttilä, 1978", "FINLAND"],
                    "SLU":["Slunga, 1982, 1985, 1989a", "SWEDEN"],
                    "SVW":["Wahlström, referring to Svedmark, 1990", "SWEDEN"],
                    "TOW":["Wahlström, referring to Törnebohm, 1990", "SWEDEN"],
                    "UPP":["Univ. UPPSALA, Sweden, 1906-", "SWEDEN"],
                    "USG":["U.S. Geological Survey, USA, 1981-", ""],
                    "VES":["Vesanen, see Penttilä, 1978", "FINLAND"],
                    "WAH":["Wahlström and Ahjos, 1982, Wahlström et al., 1987", "SWEDEN, FINLAND"]}

magnitude_scale = { "M":"macroseismic magnitude",
                    "I":"magnitude based solely on intensity",
                    "R":"magnitude based solely on radius of perceptibility",
                    "L":"local magnitude by source reference",
                    "LB":"B}th et al, 1976",
                    "LW":"Wahlstr|m and Ahjos, 1982",
                    "LN":"Norsar (B}th et al., 1976)",
                    "LU":"UPP (Wahlstr|m and Ahjos, 1982)",
                    "LH":"HEL (Wahlstr|m and Ahjos, 1982)",
                    "LA":"HEL (Wahlstr|m and Ahjos, 1982)",
                    "LF":"FOA (Slunga, 1982)", 
                    "LK":"Kim et al., 1988 1989",
                    "C":"magnitude based on signal coda duration",
                    "CB":"BER (Bergen, 1985-1991)",
                    "CH":"HEL (Wahlstr|m and Ahjos, 1982)",
                    "CP":"Ananin and Panasenko, 1982",
                    "PA":"Ananin and Panasenko, 1982",
                    "S":"surface wave magnitude (Karnik, 1969, Muir Wood and Woo, 1987)",
                    "B":"body wave magnitude",
                    "BI":"ISC, 1964-1991"}

region_code = { "A": "GERMANY",
            "B": "BARENTS SEA",
            "C": "BALTIC SEA",
            "D": "DENMARK",
            "E": "GREAT BRITAIN",
            "F": "FINLAND",
            "G": "GREENLAND SEA",
            "I": "ICELAND REGION",
            "J": "JAN MAYEN",
            "N": "NORWAY",
            "O": "NORWEGIAN SEA",
            "P": "POLAND",
            "R": "NORTH SEA",
            "S": "SWEDEN",
            "U": "RUSSIA",
            "V": "ESTONIA"}

macroseismic_reference = {  "ARH": "Arhe, personal communication",
                            "HAV": "Havskov and Optun, 1984",
                            "KUL": "Kulhanek and Wahlström, 1981, 1985",
                            "MOB": "Moberg, 1855, 1891, 1894, 1900-01",
                            "ROS": "Rosberg, 1903-04, 1912",
                            "TAL": "Talvitie, see Penttilä, 1978",
                            "YLI": "Yliniemi, personal communication"}

