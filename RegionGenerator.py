#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#

import configparser
import uuid
import random
#import sys
#import os
#import tkinter as tk
#import tkinter.ttk as ttk
from tkinter.tix import * #Tooltips
from tkinter import messagebox
import random
import gettext


gettext.install('RegionsGen')
#lang1 = gettext.translation('RegionsGen', 'locale', languages=['de']) # Nur eine Sprache
#_ = lang1.gettext

langall = gettext.translation('RegionsGen', 'locale') # Automatische auswahl
_ = langall.gettext

# Uebersetzen geht so:
# ... _( )
# also ohne uebersetzung
# print('This is a not translatable string.')
# mit uebersetzung
# print(_('This is a translatable string.'))

# Extrahieren funktioniert in der Konsole im Programmpfad des Programmes so (Pfad anpassen):
# Pfad-zu\python.exe Pfad-zu\Tools\i18n\pygettext.py -d base -o Uebersetzungsdatei.pot Programmname.py
# C:\Python38\python.exe C:\Python38\Tools\i18n\pygettext.py -d base -o RegionsGen.pot RegionGenerator.py
# Diese POT Datei kann mit PoEdit dann in jede X Beliebige Sprache uebersetzt werden. Beispiel RegionsGen.po und RegionsGen.mo.
# Die Dateien kommen in das Verzeichnis Programmverzeichnis\locale\de\LC_MESSAGES Beipiel hier ist de fuer Deutsch.

# Unter Anzeigen -> Befehlspalette... -> Python: Select Interpreter kann man eine 
# der installierten Python Versionen auswählen die genutzt werden. Beispiel Python 2.7 oder 3.8.

# EXE Datei mit pyinstaller:
# pyinstaller muss mit pip installiert werden.
# pip install pyinstaller
# Alle Python Skripte hinten anhängen.
# pyinstaller --windowed --noconsole --onefile RegionGenerator.py

# random name
def randomname():
    name = random.choice(['Abod', 'Adalbeort', 'Adalgar', 'Adham', 'Adken', 'Adulfuns', 'Aelf', 'Aelfraid', 'Aelfric', 'Aelor', 'Aescby', 'Aethel', 'Aethelberht', 'Aethelisdun', 'Ahanor', 'Aherne', 'Ahrin', 'Aidan', 'Aidtun', 'Aifrid',
        'Ailean', 'Aimil', 'Aineislis', 'Arileas', 'Aislinn', 'Alain', 'Albhaois', 'Albion', 'Aldus', 'Aler', 'Algonthir', 'Alraed', 'Alhric', 'Alhwin', 'Alian', 'Allsun', 'Alviss', 'Amalasand', 'Amalien', 'Amario', 'Amber', 'Amhiunn',
        'Amhlaidh', 'Amires', 'Amlauril', 'Amon', 'Anant', 'Anaurathiel', 'Andariel', 'Andarius', 'Anfalas', 'Anhlaoigh', 'Anntoin', 'Anwyl', 'Aodh', 'Aodha', 'Aodhagan', 'Aodhan', 'Aoidh', 'Aoiffe', 'Aonghus', 'Aralian', 'Aralt', 'Arela',
        'Arheyu', 'Arndell', 'Arnhold', 'Arni', 'Arnwald', 'Arnwulf', 'Arombolosch', 'Arregaithel', 'Artair', 'Arthwr','Arthylomis', 'Artur', 'Asgault', 'Athàlùsa', 'Athdara', 'Athdara', 'Attewelle', 'Avis', 'Awurin', 'Aylen', 'Baehloew',
        'Bagon', 'Bain', 'Bairghith', 'Baldmar', 'Banain', 'Banbrigge', 'Bangan', 'Banlòr', 'Banurr', 'Bardawulf', 'Bardhardt', 'Bargash', 'Barghan', 'Barthr', 'Beadu', 'Beagan', 'Bearach', 'Beathag', 'Bebhinn', 'Becere', 'Beledene', 'Beonetleah',
        'Beorc', 'Beordtraed', 'Beorht', 'Beorhthram', 'Beormann', 'Beornet', 'Beorttun', 'Beorwalt', 'Berchtwald', 'Bercleah', 'Berdine', 'Berin', 'Berinhardt', 'Bhaird', 'Bhaltair', 'Bhaltair', 'Bhragas', 'Binge', 'Binok', 'Binokee', 'Blaecleah',
        'Blaed', 'Blar', 'Bliths', 'Bloddwyn', 'Blotsm', 'Bluainach', 'Boda', 'Bofind', 'Bofind', 'Bogohardt', 'Boltar', 'Born', 'Boron', 'Bothi', 'Boyne', 'Bradach', 'Brangwen', 'Brann', 'Breandan', 'Bret', 'Brian', 'Bridhid', 'Brock', 'Bronwyn',
        'Broth', 'Bryn', 'Brys', 'Buadhach', 'Buidhe', 'Burgal', 'Burr', 'Cadawig', 'Caddrairc', 'Cadel', 'Cadhla', 'Caellach', 'Caerau', 'Caerghallan', 'Cai', 'Cailean', 'Caileass', 'Cain', 'Caitlin', 'Calldwr', 'Cambeul', 'Cameron', 'Canshron',
        'Cant', 'Caoinleain', 'Caolabhuinn', 'Caolaidhe', 'Caomh', 'Caomhan', 'Caomhiun', 'Caradoc', 'Caramichil', 'Cariadland', 'Carleas', 'Carriag', 'Carridin', 'Casidhe', 'Cassimir', 'Cathan', 'Cathaoirmor', 'Cathasach', 'Cathmaol', 'Ceallach',
        'Ceannfhionn', 'Ceara', 'Cearbhallain', 'Cearnach', 'Cearrbhach', 'Ceileachan', 'Cein', 'Cellanir', 'Ceneric', 'Ceran', 'Chalice', 'Chandiris', 'Charea', 'Cianan', 'Ciarda', 'Cillcumhan', 'Cillin', 'Cinfhaolaidh', 'Cingesleah', 'Cinnard',
        'Cinneididh', 'Cinnfhail', 'Ciulthinn', 'Claefer', 'Elspe', 'Elsurion', 'Endover', 'Engelbergt', 'Engholm', 'Enit', 'Eodoaine', 'Eoghan', 'Eoin', 'Eorforwic', 'Eorl', 'Ingmar', 'Iniadea', 'Inis', 'Iosep', 'Isan', 'Isedria', 'Isenham', 'Itu', 'Ivhar', 'Jami',
        'Jander', 'Jaral', 'Jeffries', 'Claeg', 'Cleve', 'Clif', 'Clywd', 'Coal', 'Coalan', 'Coed', 'Coilin', 'Coille', 'Coinneach', 'Coire', 'Conaire', 'Conan', 'Conn', 'Conndchadh', 'Corbmac', 'Corcurachan', 'Corelja', 'Corondal', 'Corondhal', 'Corzar',
        'Craccas', 'Creag', 'Creaga', 'Creiddylad', 'Creya', 'Cristin', 'Cuinn', 'Curadhan', 'Cuthbeorht', 'Cwen', 'Cwladys', 'Cynbel', 'Cyne', 'Cyneburhleah', 'Cyneric', 'Cynesige', 'Cyrius', 'Cythranil', 'Daegelbeorht', 'Daegeseage', 'Dael', 'Daeltun', 'Daeran',
        'Daghat', 'Dagian', 'Dagomar', 'Dagr', 'Daimhin', 'Dalach', 'Dalr', 'Dalyell', 'Danr', 'Daregas', 'Darhan', 'Dariel', 'Darwyn', 'Dearan', 'Deardrui', 'Deasach', 'Deasmumhan', 'Debroun', 'Defyaio', 'Delair', 'Dellingr', 'Demandred', 'Demyavan', 'Dene', 'Denethor',
        'Denu', 'Deorward', 'Dercarat', 'Derenai', 'Derylynn', 'Dewi', 'Dewi', 'Diamar', 'Diarmaoid', 'Dikibyr', 'Diolmhain', 'Diomassach', 'Direa', 'Diss', 'Doghailen', 'Dogrim', 'Doire', 'Doireann', 'Domhnull', 'Dorminil', 'Draca', 'Drugiself', 'Dryw', 'Dseoran', 'Duria',
        'Duana', 'Dubh', 'Dubhgan', 'Dubhghall', 'Dubhglas', 'Dubhlachan', 'Dubhloach', 'Dubhthach', 'Duddaleah', 'Dufrhealh', 'Duhlasar', 'Dumond', 'Dunleah', 'Dunn', 'Dyddplentyn', 'Dylan', 'Dylan', 'Eachan', 'Eachthighearn', 'Eada', 'Eadbeorht', 'Eadgar', 'Eadmund',
        'Eadwulf', 'Ealadhach', 'Ealdraed', 'Ealhard', 'Ealhdun', 'Eamon', 'Eanruig', 'Earnest', 'Earric', 'Eathelin', 'Eatun', 'Eberk', 'Eburhardt', 'Ecgbeorth', 'Eferhard', 'Efrania', 'Ehren', 'Eibhlin', 'Eideann', 'Eilis', 'Einher', 'Einion', 'Eiric', '/', 'Eirik',
        'Eister', 'Elanear', 'Eldrias', 'Elemthain', 'Ellinar', 'Elram', 'Elrias', 'Eostre', 'Erinn', 'Erminric', 'Ertha', 'Estcot', 'Esthandir', 'Esyathol', 'Ethiyanil', 'Eyrekr', 'Eysellt', 'Faegan', 'Faeroth', 'Faerrleah', 'Faerven', 'Faerwald', 'Fairhinath', 'Famek', 'Faodhagan',
        'Fearbhirigh', 'Fearghal', 'Fearghus', 'Fearn', 'Feich', 'Felabeorht', 'Felizitas', 'Fender', 'Feoras', 'Fiamar', 'Filmaen', 'Fingolfin', 'Fionn', 'Fionnghalac', 'Fionnghuala', 'Fips', 'Firlionel', 'Flanna', 'Fleotig', 'Floinn', 'Flynt', 'Fridu', 'Friduric', 'Frimunt',
        'Fugentun', 'Gaelan', 'Gaelbhan', 'Galchobhar', 'Gallgaidheal', 'Gandalf', 'Garisin', 'Garivou', 'Garm', 'Garthr', 'Garwig', 'Geatan', 'Genji', 'Gerhwas', 'Gerrod', 'Gerwalt', 'Ghleanna', 'Gilolla', 'Gimli', 'Giollamhuire', 'Giollaruaidh', 'Gionnan', 'Giorsal', 'Gipcyan',
        'Gislbyr', 'Gled', 'Glenndun', 'Glynydd', 'Gnarf', 'Gnimsch', 'Gnosch', 'Goathaire', 'Goda', 'Godehard', 'Godgifu', 'Gondo', 'Goridh', 'Goridh', 'Gorman', 'Gorman', 'Goscelin', 'Gothfraidh', 'Grada', 'Graegleah', 'Griswald', 'Gruffudd', 'Gunnhar', 'Guthr', 'Gwalchmai',
        'Gwendolyn', 'Gwenhwyvar', 'Gwlsdys', 'Gyldan', 'Gyrwode', 'Gytha', 'Gyvron', 'Hacor', 'Hadu', 'Haele', 'Haesel', 'Haestibgas', 'Hafirinm', 'Hafleikr', 'Haga', 'Hakon', 'Halag', 'Halfdan', 'Halifrid', 'Halig', 'Haltor', 'Hammar', 'Hanraoi', 'Haorinas', 'Harad',
        'Haragraf', 'Harailt', 'Harpo', 'Harti', 'Haruald', 'Hearpere', 'Heathleah', 'Heimrik', 'Heort', 'Heriberaht', 'Herimann', 'Herwig', 'Hidlimar', 'Hilbrand', 'Hildhard', 'Hohberht', 'Hoibeard', 'Hoireabard', 'Holda', 'Honod', 'Howel', 'Howel', 'Hugiberaht', 'Hugiet',
        'Hunfrid', 'Hunig', 'Iaian', 'Ifig', 'Iltak', 'Imrahil', 'Jezer', 'Joreg', 'Jozan', 'Kaja', 'Kandorys', 'Kerwyn', 'Kiarr', 'Kief', 'Kiollsig', 'Kirkja', 'Kirkjabyr', 'Knut', 'Kort', 'Korulas', 'Krak', 'Krossbyr', 'Kuambyr', 'Kulbari', 'Kunagnos', 'Kuonraed', 'Kyan',
        'Kythauriel', 'Labhruinn', 'Ladhaoise', 'Laec', 'Lagan', 'Laghras', 'Laird', 'Landbercht', 'Langr', 'Laochailan', 'Laudrius', 'Leagorn', 'Leamhnach', 'Leander', 'Leannan', 'Leathlaghra', 'Lebennin', 'Lefael', 'Leif', 'Leoma', 'Leraneal', 'Leschko', 'Leskoh', 'Lethanon',
        'Leutpald', 'Lilias', 'Lind', 'Lindael', 'Lindberg', 'Lintflas', 'Lioslaith', 'Liusadh', 'Llwyd', 'Llyn', 'Llyweilun', 'Logmann', 'Lokti', 'Lomarin', 'Lonn', 'Lothar', 'Lotharingen', 'Lubig', 'Lughaidh', 'Lughaidh', 'Luighseacg', 'Toireasa', 'Torma', 'Torr', 'Torra', 'Truda',
        'Ula', 'Ura', 'Walda', 'Waldburga', 'Winifrid', 'Wulfila', 'Wulfrith', 'Wulfsige', 'Ladhaoise', 'Larissa', 'Lidda', 'Lilias', 'Liusadh', 'Luighseacg', 'Luisadh', 'Mab', 'Maertisa', 'Maeva', 'Magamhildi', 'Mahthildin', 'Maible', 'Maighdlin', 'Maire', 'Mairghread', 'Mairi',
        'Marcail', 'Maredud', 'Mathildi', 'Maura', 'Maureen', 'Meadhbh', 'Mearr', 'Mercia', 'Meredydd', 'Mhari', 'Mildraed', 'Minne', 'Miureall', 'Moibeal', 'Moire', 'Moireach', 'Monca', 'Morag', 'Morgant', 'Moya', 'Muire', 'Muirgheal', 'Muirne', 'Nadjala', 'Niall', 'Odharait',
        'Oona', 'Oonagh', 'Ordwime', 'Pianwig', 'Raginmund', 'Raoghnait', 'Rioghnach', 'Rois', 'Rozumund', 'Ruomhildr', 'Sadhbh', 'Sadhbha', 'Saidhghin', 'Salaidh', 'Sibeal', 'Sigilwig', 'Sigimund', 'Signi', 'Sine', 'Siobhan', 'Sion', 'Siubhan', 'Siusan', 'Sorcha', 'Sosanna',
        'Swynedd', 'Taithleach', 'Tanya', 'Thoridyss', 'Toirdealbach', 'Luisadh', 'Lundr', 'Luthais', 'Lyrandis', 'Lyrsil', 'Lysil', 'Lysira', 'Maarkan', 'Mab', 'Macothiel', 'Madelhari', 'Maegth', 'Maeva', 'Magafeld', 'Magnus', 'Maible', 'Maighdlin', 'Maire', 'Mairghread',
        'Mairi', 'Maithilis', 'Mandel', 'Mannfrith', 'Maodighomhnaigh', 'Maolmin', 'Maolmin', 'Maolmuire', 'Maoltuile', 'Marcail', 'Maredud', 'Mari', 'Maril', 'Marla', 'Maskol', 'Maura', 'Maureen', 'Meadhbh', 'Mearr', 'Meginhardt', 'Meliondor', 'Meredydd', 'Merehloew', 'Mersc',
        'Messkir', 'Metira', 'Metrios', 'Mhari', 'Mialee', 'Micheil', 'Minarvos', 'Minata', 'Mirtek', 'Miureall', 'Modread', 'Mog-Macha', 'Moibeal', 'Moineruadh', 'Moineruadh', 'Moire', 'Moireach', 'Moldrack', 'Monca', 'Morag', 'Morcan', 'Morfinn', 'Morgant', 'Morgen',
        'Morogh', 'Mortun', 'Moya', 'Muir', 'Muire', 'Muireadhaigh', 'Muirgheal', 'Muirne', 'Murchadh', 'Murthuile', 'Mylnburne', 'Naheniel', 'Nathondal', 'Naul', 'Neblehle', 'Nerviar', 'Newyddllyn', 'Niaeha', 'Niall', 'Nichus', 'Niewheall', 'Norberaht', 'Nuallan', 'Odbert',
        'Odharait', 'Odhrean', 'Odimorr', 'Odwulf', 'Oleifr', 'Ollaneg', 'Olvaerr', 'Omid', 'Oona', 'Oonagh', 'Ordalf', 'Orharikr', 'Osbeorht', 'Oskar', 'Osmaer', 'Osraed', 'Osric', 'Othomann', 'Owein', 'Owein', 'Padraig', 'Padriac', 'Paduicg', 'Parlan', 'Parlan', 'Peadair',
        'Peadar', 'Pennleah', 'Peppi', 'Perin', 'Permeyah', 'Preostleah', 'Quarz', 'Radagast', 'Rafmag', 'Allweg', 'Ragdal', 'El', 'Zoreh', 'Raghallach', 'Raghnall', 'Raginmund', 'Rahn', 'Raiola', 'Raja', 'Ramiris', 'Randwulf', 'Raoghnait', 'Raskogr', 'Rauthuellir', 'Raymir',
        'Readwulf', 'Regaf', 'Regdar', 'Reginberaht', 'Reidhachadh', 'Rhinfflew', 'Rhuk', 'Rhydag', 'Rhys', 'Riagan', 'Rian', 'Ridere', 'Rikar', 'Rille', 'Riocard', 'Riodhr', 'Rioghbhardan', 'Rioghnach', 'Rodhlann', 'Rognuald', 'Rois', 'Ronan', 'Rotland', 'Ruadhan', 'Ruarc',
        'Rudrik', 'Rudugeard', 'Rumenea', 'Ruodger', 'Ruodlant', 'Ruomhildr', 'Rurik', 'Sadhbh', 'Sadhbha', 'Saegar', 'Saelec', 'Saerfren', 'Saeweard', 'Saidhghin', 'Sailbheastar', 'Saitham', 'Sala', 'Salaidh', 'Salasu', 'San', 'Rhaal', 'Saphir', 'Saretus', 'Sargas', 'Saxon',
        'Scanlan', 'Sceaphierde', 'Scelfleah', 'Schiraljie', 'Scirwode', 'Scolaighe', 'Scrileadh', 'Seadaidh', 'Seain', 'Seanachan', 'Seanan', 'Seanlaoch', 'Seann', 'Secgleah', 'Seiradan', 'Selvagitas', 'Sentaia', 'Sgeulaiche', 'Sha', 'Rell', 'ShaRed', 'Shane', 'Shauir',
        'Sibeal', 'Siddael', 'Sigifrith', 'Sigilwig', 'Sigimund', 'Sigiwald', 'Signi', 'Sigurdhr', 'Silanay', 'Silmalinnon', 'Silmarilon', 'Silviara', 'Sim', 'Sindira', 'Sine', 'Siobhan', 'Siodhachan', 'Siolta', 'Siomonn', 'Sion', 'Sithethak', 'Siubhan', 'Siudhne',
        'Siusan', 'Skentha', 'Skereye', 'Skorag', 'Skypr', 'Slaedr', 'Slaghan', 'Sliaghin', 'Solamh', 'Somahirle', 'Sorcha', 'Sruthair', 'Sruthan', 'Stanach', 'Steorra', 'Stodhierde', 'Strom', 'Sucram', 'Suileabhan', 'Suthrland', 'Swynedd', 'Tabbert', 'Tad', 'Taffy',
        'Taithleach', 'Tamnais', 'Taran', 'Taurelias', 'Tearlach', 'Teimhnean', 'Temara', 'Tendrik', 'Tespius', 'Tewdwr', 'Thalion', 'Thamios', 'Tharimis', 'Thegn', 'Theuobald', 'Theuroik', 'Thoidgeirford', 'Thoraths', 'Thorbiartr', 'Thorbiorn', 'Thorfin', 'Thorir', 'Thoud',
        'Throaldr', 'Thruhleow', 'Thrythwig', 'Tiak', 'Tighearnach', 'Tioboid', 'Tiomoid', 'Tirell', 'Togtar', 'Toirdealbach', 'Toireasa', 'Tomas', 'Torc', 'Tordek', 'Torm', 'Tormaigh', 'Torr', 'Torra', 'Tosdramos', 'Trahayarn', 'Tramiel', 'Trea', 'Treabhar', 'Treasach',
        'Trekarraz', 'Trent', 'Trevelian', 'Trystan', 'Tsoladin', 'Tuathal', 'Turgal', 'Txorass', 'Tygr', 'Tyrion', 'Ualtar', 'Udo', 'Uigboern', 'Uilleam', 'Uinsionn', 'Ulbon', 'Ulfmaerr', 'Ulvelaik', 'Unnurr', 'Vaasa', 'Valadenya', 'Valerius', 'Varin', 'Varvia', 'Vollmr',
        'Vychan', 'Wace', 'Waenwryht', 'Waescburne', 'Waldramm', 'Walijan', 'Wallihelm', 'Wandi', 'Wann', 'Waren', 'Warto', 'Wendido', 'Wenis', 'Werro', 'Wigis', 'Willaperht', 'Willimod', 'Winiholdo', 'Wolf', 'Wudoreafa', 'Wulfgar', 'Wulfric', 'Wulfrith', 'Wyrduàn', 'Yaligan',
        'Yarrik', 'YaYarzar', 'Yedda', 'Yofenia', 'Zaasz', 'Zareius', 'Zarrag', 'Zolt', 'Namen', 'Abvia', 'Adalheit', 'Aeldra', 'Aelfdene', 'Aeltra', 'Aemete', 'Aethelmaere', 'Aidan', 'Ailin', 'Aimil', 'Aine', 'Airleas', 'Aislinn', 'Alain', 'Alaria', 'Allsun',
        'Alundra', 'Alviss', 'Amhiunn', 'Andaria', 'Aoiffe', 'Astryd', 'Athalindi', 'Attheneldre', 'Aylen', 'Baduhildi', 'Baldwine', 'Banbrigge', 'Beathag', 'Bebhinn', 'Beorhthildi', 'Berahta', 'Berangari', 'Bloddwyn', 'Brangwen', 'Brann', 'Breandan', 'Bridhid', 'Brita', 'Bronwyn',
        'Brunihildi', 'Cadhla', 'Caellach', 'Caitlin', 'Caomhiun', 'Ceara', 'Chodhildi', 'Ciarda', 'Conn', 'Creiddylad', 'Cristin', 'Cwladys', 'Dalaria', 'Damneya', 'Deardrui', 'Deorawine', 'Doire', 'Doireann', 'Domhnull', 'Duana', 'Dyddplentyn', 'Eadgyth', 'Ealasaid', 'Earwine',
        'Eibhlin', 'Eideann', 'Eilis', 'Eister', 'Elspe', 'Engelberhta', 'Enit', 'Eodoaine', 'Eorlariel', 'Erinn', 'Eysellt', 'Fionnghuala', 'Flanna', 'Freyja', 'Gala', 'Gertrut', 'Ghleanna', 'Gilsberhta', 'Giorsal', 'Gisela', 'Glynydd', 'Grisjahildi', 'Gunnhild', 'Gwendolyn',
        'Gwenhwyvar', 'Gwlsdys', 'Haduwig', 'Herthe', 'Herwig', 'Hilde', 'Hildieth', 'Hildigard', 'Hlutwig', 'Hrothwine', 'HuldraIda', 'Iduna', 'ImmaIngrida', 'Itu', 'Kelda','Duerrsturm', 'Trutzwueste', 'Koenigswueste', 'Eichenbruch', 'Baerensumpf', 'Untersteig', 'Hochfelde', 'Duerrberge', 
        'Duesterfelde', 'Sternental', 'Klingenstadt', 'Eichentann', 'Adlersbach', 'Duesterwald', 'Fuchspass', 'Sturmhain', 'Sturmwacht', 'Duerrfeld', 'Silbersee', 'Goldsturm', 'Schwalbental', 'Adlersstiege', 'Donnerwald', 'Baerensturm', 
        'Duestersumpf', 'Blitzburg', 'Mondhain', 'Wolkenwies', 'Dunkelfluss', 'Falkental', 'Klingenbach', 'Tiefsturm', 'Trutzwald', 'Feuerfeld', 'Donnerwalde', 'Donnerpass', 'Sternenbruch', 'Sturmsee', 'Adlersmeer', 'Feuerwald', 
        'Duestersee', 'Donnertann', 'Wolfswies', 'Tiefhuegel', 'Oberberge', 'Tiefstiege', 'Kaltenstiege', 'Sternennest', 'Donnerfels', 'Feuerwueste', 'Duestersee', 'Dunkelfels', 'Duerrnest', 'Brachfeld', 'Goldtal', 'Baerenstiege', 
        'Blitzbach', 'Tiefwacht', 'Kaltenhuegel', 'Mondberge', 'Dunkelwald', 'Schoenschlucht', 'Schwalbenstadt', 'Feuerhoehe', 'Goldburg', 'Kleinstrom', 'Hochhuegel', 'Tieffurt', 'Schwalbenhain', 'Drachenstein', 'Drachensee', 'Brachhuegel', 
        'Kaltenfluss', 'Hochsteig', 'Brachmeer', 'Goldwald', 'Kleinwacht', 'Silberwacht', 'Koenigsfeld', 'Baerensee', 'Adlersnest', 'Schoensteig', 'Drachensumpf', 'Tiefsteig', 'Wolkenanhoehen', 'Sonnensturm', 'Falkensee', 'Klingenbach', 
        'Klingenhuegel', 'Sonnensumpf', 'Unterburg', 'Sonnensteig', 'Tiefbach', 'Silberwacht', 'Fuchswueste', 'Drachenhoehe', 'Tiefsturm', 'Falkensteig', 'Adlersfluss', 'Schoenfels', 'Schoenhoehe', 'Eichenstrom', 'Brachstein', 'Hochwies', 
        'Dunkelmeer', 'Dunkelhuegel', 'Brachwacht', 'Trutzfels', 'Feuerhain', 'Duesterstrom', 'Hochhain', 'Koenigswies', 'Brachtal', 'Oberhoehe', 'Silbertann', 'Blitznest', 'Eichental', 'Schoenhain', 'Falkensturm', 'Fuchshoehe', 
        'Feueranhoehen', 'Obersee', 'Duerrstrom', 'Fuchshoehe', 'Klingenbruch', 'Kleinfeld', 'Blitztal', 'Dunkelbruch', 'Eichenhain', 'Mondmeer', 'Dunkelbruch', 'Feuerstrom', 'Eichenstrom', 'Brachstrom', 'Duerrhain', 'Dunkelwies', 
        'Koenigssturm', 'Drachenstrom', 'Sonnentann', 'Wolkenwald', 'Mondstiege', 'Feuerstrom', 'Blitzstein', 'Blitzwueste', 'Sternennest', 'Obertal', 'Tiefburg', 'Eichenwies', 'Klingenburg', 'Feuerwald', 'Baerenhoehe', 'Koenigswald', 
        'Fuchsfeld', 'Untertann', 'Eichenwald', 'Baerensteig', 'Sturmnest', 'Dunkeltann', 'Oberstadt', 'Koenigsfluss', 'Tieffelde', 'Feuerburg', 'Duerrfluss', 'Hochstiege', 'Eichenbach', 'Blitztann', 'Donnerschlucht', 'Klingenstadt', 
        'Sigen', 'Kenlat', 'Kenanth', 'Yalanth', 'SilithdraenLo', 'Silen', 'MiMi', 'Mianth', 'Loenlat', 'Kenlad', 'LoIsith', 'Kenen', 'Gaanth', 'Isgen', 'Loladanth', 'Gallat', 'MiMiKen', 'LoMi', 'Loanth', 'Silgenen', 'Sien', 'IsMienladSil', 'Xassil', 'IsladKen', 
        'Kenanth', 'SilMilad', 'Ishir', 'Ishirlad', 'Yalen', 'Ragol', 'Gremnak', 'Grarag', 'Ragol', 'Granakgoshnak', 'Ragall', 'Gurgall', 'Gremnaknak', 'Gremgoshlogg', 'Zunlogg', 'Gremgall', 'Granak', 'Granakgoshlogg', 'Tazragrag', 'Ragall', 'Granaknak', 'Zun', 'Tazrag', 'Grarag', 'Gremlogg', 
        'Grem', 'Ralogg', 'Zungolgoshgosh', 'Gurnakrag', 'loggrag', 'Tazrag', 'Taznak', 'Rarag', 'Gralogg', 'Dugasch', 'Thorgrim', 'Borlasch', 'Himrasch', 'EbboArom', 'Sabuk', 'Schraxbur', 'Rurasch', 'Jadin', 'Bando', 'Lidrasch', 'Odgisch', 'Duwim', 'Hamrax Polosch', 'Xaltho', 
        'Ultram', 'Geramfrim', 'Famasch', 'Iun', 'Folosch', 'Sedor', 'Nelesch', 'Thagrim', 'Hagam', 'Hornibosch', 'Muglim', 'Erasch', 'Mare', 'Marlinhanswinn', 'Peptram', 'Marwinnhintram', 'Finnhans', 'Peptramtramhin', 'Finnhin', 'Peprit', 
        'Mertramlinhans', 'Merlintramtramhans', 'Pephans', 'Berrit', 'Berrit', 'Marhans', 'Peptram', 'Samtram', 'Finnhin', 'Samhans', 'Pephans', 'Merrittramhinhin', 'Mar', 'Marlinlinwinn', 'Peplin', 'Samhinhin', 
        'Merhanstram', 'Marhintram', 'Samhanshans', 'Finnhinhin', 'Ladiana', 'Ladrahna', 'Brigisiaianatine', 'Ladianagitta', 'Sahiana', 'Brigrahnariatine', 'Ladarra', 'Brigrahnaarrarahna', 'Rosrahna', 'Samianatineriatine', 'Samiana', 'Merisia', 
        'Rosrahna', 'Sahrahnaiana', 'Rosiana', 'Rostine', 'Mergitta', 'Tiarahna', 'Ladgittaisia', 'Sahiana', 'Mera', 'Merria', 'Ladgittaarraiana', 'Rosgitta', 'Saharraria', 'Ladria', 'Brigtineisia', 'Berrit', 'Berwinn', 'Samhin', 'Pepwinn', 
        'Bertram', 'Merhanswinn', 'Peprithanshanshin', 'Marwinn', 'Samwinn', 'Pepwinnwinnhans', 'Berhin', 'Merhans', 'Bertram', 'Pephin', 'Berhans', 'Marlin', 'Marrit', 'Merlintramhans', 'Mariu', 'Samritrit', 'Berwinn', 'Marhin', 'Berhans', 'Berhans', 
        'Marwinnritlin', 'Marlin', 'Peptram', 'Pepo', 'Zorgath', 'Forarath', 'Fornoschnoschnosch', 'Ekgath', 'Zorgathgathiathsch', 'GaZor', 'Gohlarath', 'Fornuh', 'Gohlnosch', 'Gorguh', 'Gaarathgatharath', 'ZorFor', 
        'Gohloul', 'Gonosch', 'OlbiathZor', 'GorFor', 'Gogath', 'Forschnosch', 'GorZor', 'Forgath', 'Olbnuh', 'Foriath', 'Gohlsch', 'Gaarath', 'Gornosch', 'Zornoschguh', 'Goro', 'GamashFor', 'OlKei', 'Too', 'Arbahl', 'Runith', 'Klinerde', 'Toter', 'Runderde', 'Cenreth', 
        'DierIn', 'Klamling', 'Sargr', 'Dierder', 'MeKei', 'Klinderkunwurz', 'Hartol', 'Soli', 'Ganlibas', 'Dierder', 'Rundter', 'Sarter', 'Holkuneinol', 'Sowurz', 'Klinber', 'Dierst', 'WanSo', 'Klamig', 'Meamm', 'Klamdring', 'Klame', 'Sospan', 'Haldring', 'Schol', 
        'Todringdring', 'Ardring', 'Dierber', 'Klamkunrol', 'Bimdor', 'Baudring', 'Keibahl', 'IsEin', 'IsWanter', 'Soder', 'Hunamm', 'Iskeni', 'Wanatz', 'Hal', 'Klinspan', 'Sarant', 'HartKlinken', 'DierMe', 'Ganter', 'Keikar', 'RunAlEin', 'Cenatz', 'Runner', 'Glimspan', 
        'Glimner', 'Mekardor', 'AlArteretzgleif', 'Cenu', 'Cender', 'Keio', 'GandringkunWanker', 'Halrat', 'KlamIndring', 'Inter', 'Klamli', 'Borter', 'KeiBim', 'Meoma', 'Arwurz', 'Eina', 'Older', 'Glimdringerdei', 'Alst', 'Bauol', 'HalBim', 'RunIs', 'Runding', 'Sarbahl', 'Arder', 'Bimst', 'Klamweb', 'Schetz']);
    return name;

def helping():
    messagebox.showinfo(_("Help"), _("Help comes here later."))
    return;

def close_window(): 
    tkFenster.destroy()

# make a random location
def randomlocation():
    maplocation = random.randrange(1000, 8000, 4)
    localmap = str(maplocation)
    return localmap;

# see if the user has entered a value or if it is random.
def randomport():
    myport = random.randrange(9100, 9999, 4)
    return myport;

# see if the user has entered a value or if it is random.
def randomuuid():
    randomuuid = uuid.uuid4()
    return randomuuid;

# create a config file
def write_region():
    config = configparser.ConfigParser()
    
    # assemble region location
    maplocation = str(entryLocation.get()) # Holt die Daten aus der Eingabe, hier die maplocation.
    if maplocation=='' : maplocation = randomlocation() + ',' + randomlocation()

    # capitalization gross- kleinschreibung beachten
    config.optionxform = str

    # generate a uuid for all entries
    ruuid = str(entryRegionUUID.get()) # Holt die Daten aus der Eingabe, hier die maplocation.
    if ruuid=='' : ruuid = randomuuid()
    # Size
    Size_var = str(entrySize.get()) # Holt die Daten aus der Eingabe, hier die maplocation.
    if Size_var=='' : Size_var = "256"
    # InternalPort
    InternalPort = str(entryInternalPort.get()) # Holt die Daten aus der Eingabe, hier der InternalPort.
    if InternalPort=='' : InternalPort = randomport()
    # MaxPrims
    MaxPrims = str(entryMaxPrims.get()) # Holt die Daten aus der Eingabe, hier MaxPrims.
    if MaxPrims=='' : MaxPrims = '10000'
    # MaxAgents
    MaxAgents = str(entryMaxAgents.get()) # Holt die Daten aus der Eingabe, hier MaxAgents.
    if MaxAgents=='' : MaxAgents = '20'
    #entryAllowAlternatePorts
    AllowAlternatePorts = str(entryAllowAlternatePorts.get())
    if AllowAlternatePorts=='' : AllowAlternatePorts = 'False'
    #entryResolveAdress
    ResolveAdress = str(entryResolveAdress.get())
    if ResolveAdress=='' : ResolveAdress = 'False'
    #checkResolveAdress
    if checkResolveAdress.get()==0 : checkResolveAdressoff = ';'
    else: checkResolveAdressoff = ''
    #entryDefaultLanding
    DefaultLanding = str(entryDefaultLanding.get())
    if DefaultLanding=='' : DefaultLanding = '<128,128,21>'
    #checkDefaultLanding 
    if checkDefaultLanding.get()==0 : checkDefaultLandingoff = ';'
    else: checkDefaultLandingoff = ''
    #entryNonPhysicalPrimMax
    NonPhysicalPrimMax = str(entryNonPhysicalPrimMax.get())
    if NonPhysicalPrimMax=='' : NonPhysicalPrimMax = '1024'
    #checkResolveAdress = checkResolveAdress.get()
    if checkNonPhysicalPrimMax.get()==0 : checkNonPhysicalPrimMaxoff = ';'
    else: checkNonPhysicalPrimMaxoff = ''
    #entryPhysicalPrimMax
    PhysicalPrimMax = str(entryPhysicalPrimMax.get())
    if PhysicalPrimMax=='' : PhysicalPrimMax = '64'
    #checkResolveAdress = checkResolveAdress.get()
    if checkPhysicalPrimMax.get()==0 : checkPhysicalPrimMaxoff = ';'
    else: checkPhysicalPrimMaxoff = ''

    #entryClampPrimSize
    ClampPrimSize = str(entryClampPrimSize.get())
    if ClampPrimSize=='' : ClampPrimSize = 'False'
    #checkResolveAdress = checkResolveAdress.get()
    if checkClampPrimSize.get()==0 : checkClampPrimSizeoff = ';'
    else: checkClampPrimSizeoff = ''

    #entryMaxPrimsPerUser
    MaxPrimsPerUser = str(entryMaxPrimsPerUser.get())
    if MaxPrimsPerUser=='' : MaxPrimsPerUser = '-1'
    #checkResolveAdress = checkResolveAdress.get()
    if checkMaxPrimsPerUser.get()==0 : checkMaxPrimsPerUseroff = ';'
    else: checkMaxPrimsPerUseroff = ''

    #entryScopeID
    ScopeID = str(entryScopeID.get())
    if ScopeID=='' : ScopeID = ruuid
    #checkResolveAdress = checkResolveAdress.get()
    if checkScopeID.get()==0 : checkScopeIDoff = ';'
    else: checkScopeIDoff = ''

    #entryRegionType
    RegionType = str(entryRegionType.get())
    if RegionType=='' : RegionType = 'Mainland'
    #checkResolveAdress = checkResolveAdress.get()
    if checkRegionType.get()==0 : checkRegionTypeoff = ';'
    else: checkRegionTypeoff = ''

    #entryMaptileStaticUUID
    MaptileStaticUUID = str(entryMaptileStaticUUID.get())
    if MaptileStaticUUID=='' : MaptileStaticUUID = ruuid
    #checkResolveAdress = checkResolveAdress.get()
    if checkMaptileStaticUUID.get()==0 : checkMaptileStaticUUIDoff = ';'
    else: checkMaptileStaticUUIDoff = ''

    #entryMaptileStaticFile
    MaptileStaticFile = str(entryMaptileStaticFile.get())
    if MaptileStaticFile=='' : MaptileStaticFile = '"water.jpg"'
    #checkResolveAdress = checkResolveAdress.get()
    if checkMaptileStaticFile.get()==0 : checkMaptileStaticFileoff = ';'
    else: checkMaptileStaticFileoff = ''

    #entryMasterAvatarFirstName
    MasterAvatarFirstName = str(entryMasterAvatarFirstName.get())
    if MasterAvatarFirstName=='' : MasterAvatarFirstName = 'John'
    #checkResolveAdress = checkResolveAdress.get()
    if checkMasterAvatarFirstName.get()==0 : checkMasterAvatarFirstNameoff = ';'
    else: checkMasterAvatarFirstNameoff = ''

    #entryMasterAvatarLastName
    MasterAvatarLastName = str(entryMasterAvatarLastName.get())
    if MasterAvatarLastName=='' : MasterAvatarLastName = 'Doe'
    #checkResolveAdress = checkResolveAdress.get()
    if checkMasterAvatarLastName.get()==0 : checkMasterAvatarLastNameoff = ';'
    else: checkMasterAvatarLastNameoff = ''

    #entryMasterAvatarSandboxPassword
    MasterAvatarSandboxPassword = str(entryMasterAvatarSandboxPassword.get())
    if MasterAvatarSandboxPassword=='' : MasterAvatarSandboxPassword = 'passwd'
    #checkResolveAdress = checkResolveAdress.get()
    if checkMasterAvatarSandboxPassword.get()==0 : checkMasterAvatarSandboxPasswordoff = ';'
    else: checkMasterAvatarSandboxPasswordoff = ''

    #entryInternalAddress
    InternalAddress = str(entryInternalAddress.get())
    if InternalAddress=='' : InternalAddress = "0.0.0.0"
    #checkResolveAdress = checkResolveAdress.get()
    if checkResolveAdress.get()==0 : checkResolveAdressoff = ';'
    else: checkResolveAdressoff = ''

    # ExternalHostName
    ExternalHostName = str(entryExternalHostName.get()) # Holt die Daten aus der Eingabe, hier ExternalHostName.
    if ExternalHostName=='' : ExternalHostName = "SYSTEMIP"

    # region name
    regionname = str(entryRegionName.get()) # Holt die Daten aus der Eingabe, hier regionname.    
    if regionname=='' : regionname = randomname()

    # Ist der Regionsname bereits vergeben dann Zahlen an den Regionsnamen anhaengen.

    
    
    # Change space to subline for the regionname
    regionnameout = regionname 
    confdatei = regionnameout.replace(" ", "_")
       
    config[regionnameout] = {'RegionUUID': ruuid,
                          'Location': maplocation,
                          'SizeX': Size_var,
                          'SizeY': Size_var,
                          'SizeZ': Size_var,
                          'InternalAddress': InternalAddress,
                          'InternalPort': InternalPort,
                          'AllowAlternatePorts': AllowAlternatePorts,
                          checkResolveAdressoff + 'ResolveAddress': ResolveAdress,
                          'ExternalHostName': ExternalHostName,
                          'MaxPrims': MaxPrims,
                          'MaxAgents': MaxAgents,
                          checkDefaultLandingoff + 'DefaultLanding': DefaultLanding,
                          checkNonPhysicalPrimMaxoff + 'NonPhysicalPrimMax': NonPhysicalPrimMax,
                          checkPhysicalPrimMaxoff + 'PhysicalPrimMax': PhysicalPrimMax,
                          checkClampPrimSizeoff + 'ClampPrimSize': ClampPrimSize,
                          checkMaxPrimsPerUseroff + 'MaxPrimsPerUser': MaxPrimsPerUser,
                          checkScopeIDoff + 'ScopeID': ScopeID,
                          checkRegionTypeoff + 'RegionType': RegionType,
                          checkMaptileStaticUUIDoff + 'MaptileStaticUUID': MaptileStaticUUID,
                          checkMaptileStaticFileoff + 'MaptileStaticFile': MaptileStaticFile,
                          checkMasterAvatarFirstNameoff + 'MasterAvatarFirstName': MasterAvatarFirstName,
                          checkMasterAvatarLastNameoff + 'MasterAvatarLastName': MasterAvatarLastName,
                          checkMasterAvatarSandboxPasswordoff + 'MasterAvatarSandboxPassword': MasterAvatarSandboxPassword}

    ##### Dateinamen aendern falls er schon vorhanden ist #####
    #PATH = './' + confdatei + '.ini'
    #if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        # File exists
        #i=0
        #n = int(entryRegionamount.get()) # Holt die Daten aus der Eingabe, hier die Menge der Regionen.
        #for i in range(i, n):
            #with open(confdatei + str(i) + '.ini', 'w') as configfile: config.write(configfile)
    #else:
        # File not exists
        #with open(confdatei + '.ini', 'w') as configfile: config.write(configfile)

    with open(confdatei + '.ini', 'w') as configfile: config.write(configfile)

def createconfig():
    i=0
    n = int(entryRegionamount.get()) # Holt die Daten aus der Eingabe, hier die Menge der Regionen.

    for i in range(i, n):
	    write_region()
    else:
	    return n;

def createmulti():
    messagebox.showinfo(_("Create"), _("MultiRegion hat noch keine Funktion."))
    return;

def start():
    if checkMultiRegionamount.get()==0 : createconfig()
    else: createmulti()

    return;

def clear_input_field():
   entryRegionName.delete(0, END)
   entryLocation.delete(0, END)
   entryRegionUUID.delete(0, END)
   entrySize.delete(0, END)
   entryInternalPort.delete(0, END)
   entryAllowAlternatePorts.delete(0, END)
   entryResolveAdress.delete(0, END)
   entryExternalHostName.delete(0, END)
   entryMaxPrims.delete(0, END)
   entryMaxAgents.delete(0, END)
   entryDefaultLanding.delete(0, END)
   entryNonPhysicalPrimMax.delete(0, END)
   entryPhysicalPrimMax.delete(0, END)
   entryClampPrimSize.delete(0, END)
   entryMaxPrimsPerUser.delete(0, END)
   entryScopeID.delete(0, END)
   entryRegionType.delete(0, END)
   entryMaptileStaticUUID.delete(0, END)
   entryMaptileStaticFile.delete(0, END)
   entryMasterAvatarFirstName.delete(0, END)
   entryMasterAvatarLastName.delete(0, END)
   entryMasterAvatarSandboxPassword.delete(0, END)
   entryInternalAddress.delete(0, END)
   entryRegionamount.delete(0, END)
   entryRegionamount.insert(10, "1") # Mindestens eine Region erstellen.
   # Checkbox clear
   checkDefaultLanding.set(0)
   checkNonPhysicalPrimMax.set(0)
   checkPhysicalPrimMax.set(0)
   checkClampPrimSize.set(0)
   checkMaxPrimsPerUser.set(0)
   checkScopeID.set(0)
   checkRegionType.set(0)
   checkMaptileStaticUUID.set(0)
   checkMaptileStaticFile.set(0)
   checkResolveAdress.set(0)
   checkMasterAvatarFirstName.set(0)
   checkMasterAvatarLastName.set(0)
   checkMasterAvatarSandboxPassword.set(0)

    
######################################################
############ Ultra Region Generator UI ###############
######################################################
#Grid tkFenster Parameter und Bedeutung:
#row, column 	
# Zeile bzw. Spalte, in der die GUI-Komponente angeordnet wird.
#
#padx, pady 	
# Leerer Platz rechts und links bzw. ober- und unterhalb der GUI-Komponente
#
#sticky 	
# Legt fest, wie die GUI-Komponente innerhalb der Zelle platziert wird, falls die Zelle größer als die GUI-Komponente ist. 
# Die Werte 'n', 'e', 's', 'w', 'ne', 'se', 'sw', 'nw' stehen für Himmelsrichtungen, 
# die Werte 'ew', 'ns', 'nesw' entlang der codierten Himmelsrichtungen.

# Fenster
tkFenster = Tk()
tkFenster.title('RegionsGenerator') # Titel des Fensters.
tkFenster.iconbitmap('opensim.ico') # Bild des Fensters.
tkFenster.configure(bg='#E8E8E8') # Hintergrundfarbe des Fensters.
#tkFenster.geometry("800x850+937+134") # Groesse des Fensters.

# Rot #FFCFC9 Gruen #00FFBC Gelb #FFF070

# Label mit Aufschrift RegionName
labelRegionName = Label(master=tkFenster, bg='#F9CDAD', text=_('Region Name'))
labelRegionName.grid(row=0, column=0, padx='5', pady='5', sticky='ew')
# Entry für RegionName
entryRegionName = Entry(master=tkFenster, bg='white', width='32')
entryRegionName.grid(row=0, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryRegionName,balloonmsg= _("insert region name"))

# Label mit Aufschrift Location
labelLocation = Label(master=tkFenster, bg='#F9CDAD', text=_('Location'))
labelLocation.grid(row=1, column=0, padx='5', pady='5', sticky='ew')
# Entry für Location
entryLocation = Entry(master=tkFenster, bg='white', width='32')
entryLocation.grid(row=1, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryLocation,balloonmsg= _("Location x,y example 1000,1000"))

# Label mit Aufschrift RegionUUID
labelRegionUUID = Label(master=tkFenster, bg='#F9CDAD', text=_('Region UUID'))
labelRegionUUID.grid(row=2, column=0, padx='5', pady='5', sticky='ew')
# Entry für RegionUUID
entryRegionUUID = Entry(master=tkFenster, bg='white', width='32')
entryRegionUUID.grid(row=2, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryRegionUUID,balloonmsg= _("RegionUUID blank creates a random."))

# Label mit Aufschrift Size
labelSize = Label(master=tkFenster, bg='#F9CDAD', text=_('Size'))
labelSize.grid(row=3, column=0, padx='5', pady='5', sticky='ew')
# Entry für Size
entrySize = Entry(master=tkFenster, bg='white', width='32')
entrySize.grid(row=3, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entrySize,balloonmsg= _("If size is not specified it will default to the legacy size of 256."))

# Label mit Aufschrift InternalAddress
labelInternalAddress = Label(master=tkFenster, bg='#F9CDAD', text=_('Internal Address'))
labelInternalAddress.grid(row=4, column=0, padx='5', pady='5', sticky='ew')
# Entry für InternalAddress
entryInternalAddress = Entry(master=tkFenster, bg='white', width='32')
entryInternalAddress.grid(row=4, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryInternalAddress,balloonmsg= _("Internal Address"))
# Checkbutton für InternalAddress
#checkInternalAddress = IntVar()
#Checkbutton(tkFenster, text="turn on", variable=checkInternalAddress).grid(row=4, column=2, sticky=W)

# Label mit Aufschrift InternalPort
labelInternalPort = Label(master=tkFenster, bg='#F9CDAD', text=_('Internal Port'))
labelInternalPort.grid(row=5, column=0, padx='5', pady='5', sticky='ew')
# Entry für InternalPort
entryInternalPort = Entry(master=tkFenster, bg='white', width='32')
entryInternalPort.grid(row=5, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryInternalPort,balloonmsg= _("InternalPort blank creates a random."))

# Label mit Aufschrift AllowAlternatePorts
labelAllowAlternatePorts = Label(master=tkFenster, bg='#F9CDAD', text=_('Allow Alternate Ports'))
labelAllowAlternatePorts.grid(row=6, column=0, padx='5', pady='5', sticky='ew')
# Entry für AllowAlternatePorts
entryAllowAlternatePorts = Entry(master=tkFenster, bg='white', width='32')
entryAllowAlternatePorts.grid(row=6, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryAllowAlternatePorts,balloonmsg= _("AllowAlternatePorts"))

# Label mit Aufschrift ExternalHostName
labelExternalHostName = Label(master=tkFenster, bg='#F9CDAD', text=_('External Host Name'))
labelExternalHostName.grid(row=7, column=0, padx='5', pady='5', sticky='ew')
# Entry für ExternalHostName
entryExternalHostName = Entry(master=tkFenster, bg='white', width='32')
entryExternalHostName.grid(row=7, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryExternalHostName,balloonmsg= _("External Host Name"))
# Checkbutton für ExternalHostName
#checkExternalHostName = IntVar()
#Checkbutton(tkFenster, text="turn on", variable=checkExternalHostName).grid(row=7, column=2, sticky=W)

# Label mit Aufschrift MaxPrims
labelMaxPrims = Label(master=tkFenster, bg='#F9CDAD', text=_('Max Prims'))
labelMaxPrims.grid(row=8, column=0, padx='5', pady='5', sticky='ew')
# Entry für MaxPrims
entryMaxPrims = Entry(master=tkFenster, bg='white', width='32')
entryMaxPrims.grid(row=8, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryMaxPrims,balloonmsg= _("Limit prims to the regions."))
# Checkbutton für MaxPrims
#checkMaxPrims = IntVar()
#Checkbutton(tkFenster, text="turn on", variable=checkMaxPrims).grid(row=8, column=2, sticky=W)

# Label mit Aufschrift MaxAgents
labelMaxAgents = Label(master=tkFenster, bg='#F9CDAD', text=_('Max Agents'))
labelMaxAgents.grid(row=9, column=0, padx='5', pady='5', sticky='ew')
# Entry für MaxAgents
entryMaxAgents = Entry(master=tkFenster, bg='white', width='32')
entryMaxAgents.grid(row=9, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryMaxAgents,balloonmsg= _("Limit Agents to the regions."))
# Checkbutton für MaxAgents
#checkMaxAgents = IntVar()
#Checkbutton(tkFenster, text="turn on", variable=checkMaxAgents).grid(row=9, column=2, sticky=W)

# Label mit Aufschrift DefaultLanding
labelDefaultLanding = Label(master=tkFenster, bg='#F9CDAD', text=_('Default Landing'))
labelDefaultLanding.grid(row=10, column=0, padx='5', pady='5', sticky='ew')
# Entry für DefaultLanding
entryDefaultLanding = Entry(master=tkFenster, bg='white', width='32')
entryDefaultLanding.grid(row=10, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryDefaultLanding,balloonmsg= _("DefaultLanding"))
# Checkbutton für DefaultLanding
checkDefaultLanding = IntVar()
Checkbutton(tkFenster, text=_("turn on"), variable=checkDefaultLanding).grid(row=10, column=2, sticky=W)

# Label mit Aufschrift NonPhysicalPrimMax
labelNonPhysicalPrimMax = Label(master=tkFenster, bg='#F9CDAD', text=_('Non Physical Prim Max'))
labelNonPhysicalPrimMax.grid(row=11, column=0, padx='5', pady='5', sticky='ew')
# Entry für NonPhysicalPrimMax
entryNonPhysicalPrimMax = Entry(master=tkFenster, bg='white', width='32')
entryNonPhysicalPrimMax.grid(row=11, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryNonPhysicalPrimMax,balloonmsg= _("NonPhysicalPrimMax"))
# Checkbutton für NonPhysicalPrimMax
checkNonPhysicalPrimMax = IntVar()
Checkbutton(tkFenster, text=_("turn on"), variable=checkNonPhysicalPrimMax).grid(row=11, column=2, sticky=W)

# Label mit Aufschrift PhysicalPrimMax
labelPhysicalPrimMax = Label(master=tkFenster, bg='#F9CDAD', text=_('Physical Prim Max'))
labelPhysicalPrimMax.grid(row=12, column=0, padx='5', pady='5', sticky='ew')
# Entry für PhysicalPrimMax
entryPhysicalPrimMax = Entry(master=tkFenster, bg='white', width='32')
entryPhysicalPrimMax.grid(row=12, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryPhysicalPrimMax,balloonmsg= _("PhysicalPrimMax"))
# Checkbutton für PhysicalPrimMax
checkPhysicalPrimMax = IntVar()
Checkbutton(tkFenster, text=_("turn on"), variable=checkPhysicalPrimMax).grid(row=12, column=2, sticky=W)

# Label mit Aufschrift ClampPrimSize
labelClampPrimSize = Label(master=tkFenster, bg='#F9CDAD', text=_('Clamp Prim Size'))
labelClampPrimSize.grid(row=13, column=0, padx='5', pady='5', sticky='ew')
# Entry für ClampPrimSize
entryClampPrimSize = Entry(master=tkFenster, bg='white', width='32')
entryClampPrimSize.grid(row=13, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryClampPrimSize,balloonmsg= _("ClampPrimSize"))
# Checkbutton für ClampPrimSize
checkClampPrimSize = IntVar()
Checkbutton(tkFenster, text=_("turn on"), variable=checkClampPrimSize).grid(row=13, column=2, sticky=W)

# Label mit Aufschrift MaxPrimsPerUser
labelMaxPrimsPerUser = Label(master=tkFenster, bg='#F9CDAD', text=_('Max Prims Per User'))
labelMaxPrimsPerUser.grid(row=14, column=0, padx='5', pady='5', sticky='ew')
# Entry für MaxPrimsPerUser
entryMaxPrimsPerUser = Entry(master=tkFenster, bg='white', width='32')
entryMaxPrimsPerUser.grid(row=14, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryMaxPrimsPerUser,balloonmsg= _("MaxPrimsPerUser"))
# Checkbutton für MaxPrimsPerUser
checkMaxPrimsPerUser = IntVar()
Checkbutton(tkFenster, text=_("turn on"), variable=checkMaxPrimsPerUser).grid(row=14, column=2, sticky=W)

# Label mit Aufschrift ScopeID
labelScopeID = Label(master=tkFenster, bg='#F9CDAD', text=_('Scope ID'))
labelScopeID.grid(row=15, column=0, padx='5', pady='5', sticky='ew')
# Entry für ScopeID
entryScopeID = Entry(master=tkFenster, bg='white', width='32')
entryScopeID.grid(row=15, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryScopeID,balloonmsg= _("ScopeID"))
# Checkbutton für ScopeID
checkScopeID = IntVar()
Checkbutton(tkFenster, text=_("turn on"), variable=checkScopeID).grid(row=15, column=2, sticky=W)

# Label mit Aufschrift RegionType
labelRegionType = Label(master=tkFenster, bg='#F9CDAD', text=_('Region Type'))
labelRegionType.grid(row=16, column=0, padx='5', pady='5', sticky='ew')
# Entry für RegionType
entryRegionType = Entry(master=tkFenster, bg='white', width='32')
entryRegionType.grid(row=16, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryRegionType,balloonmsg= _("RegionType"))
# Checkbutton für RegionType
checkRegionType = IntVar()
Checkbutton(tkFenster, text=_("turn on"), variable=checkRegionType).grid(row=16, column=2, sticky=W)

# Label mit Aufschrift MaptileStaticUUID
labelMaptileStaticUUID = Label(master=tkFenster, bg='#F9CDAD', text=_('Maptile Static UUID'))
labelMaptileStaticUUID.grid(row=17, column=0, padx='5', pady='5', sticky='ew')
# Entry für MaptileStaticUUID
entryMaptileStaticUUID = Entry(master=tkFenster, bg='white', width='32')
entryMaptileStaticUUID.grid(row=17, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryMaptileStaticUUID,balloonmsg= _("MaptileStaticUUID"))
# Checkbutton für MaptileStaticUUID
checkMaptileStaticUUID = IntVar()
Checkbutton(tkFenster, text=_("turn on"), variable=checkMaptileStaticUUID).grid(row=17, column=2, sticky=W)

# Label mit Aufschrift MaptileStaticFile
labelMaptileStaticFile = Label(master=tkFenster, bg='#F9CDAD', text=_('Maptile Static File'))
labelMaptileStaticFile.grid(row=18, column=0, padx='5', pady='5', sticky='ew')
# Entry für MaptileStaticFile
entryMaptileStaticFile = Entry(master=tkFenster, bg='white', width='32')
entryMaptileStaticFile.grid(row=18, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryMaptileStaticFile,balloonmsg= _("MaptileStaticFile"))
# Checkbutton für MaptileStaticFile
checkMaptileStaticFile = IntVar()
Checkbutton(tkFenster, text=_("turn on"), variable=checkMaptileStaticFile).grid(row=18, column=2, sticky=W)

# Label mit Aufschrift ResolveAdress
labelResolveAdress = Label(master=tkFenster, bg='#F9CDAD', text=_('Resolve Adress'))
labelResolveAdress.grid(row=19, column=0, padx='5', pady='5', sticky='ew')
# Entry für ResolveAdress
entryResolveAdress = Entry(master=tkFenster, bg='white', width='32')
entryResolveAdress.grid(row=19, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryResolveAdress,balloonmsg= _("ResolveAdress"))
# Checkbutton für ResolveAdress
checkResolveAdress = IntVar()
Checkbutton(tkFenster, text=_("turn on"), variable=checkResolveAdress).grid(row=19, column=2, sticky=W)

# Label mit Aufschrift MasterAvatarFirstName
labelMasterAvatarFirstName = Label(master=tkFenster, bg='#F9CDAD', text=_('Master Avatar First Name'))
labelMasterAvatarFirstName.grid(row=20, column=0, padx='5', pady='5', sticky='ew')
# Entry für MasterAvatarFirstName
entryMasterAvatarFirstName = Entry(master=tkFenster, bg='white', width='32')
entryMasterAvatarFirstName.grid(row=20, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryMasterAvatarFirstName,balloonmsg= _("MasterAvatarFirstName"))
# Checkbutton für MasterAvatarFirstName
checkMasterAvatarFirstName = IntVar()
Checkbutton(tkFenster, text=_("turn on"), variable=checkMasterAvatarFirstName).grid(row=20, column=2, sticky=W)

# Label mit Aufschrift MasterAvatarLastName
labelMasterAvatarLastName = Label(master=tkFenster, bg='#F9CDAD', text=_('Master Avatar Last Name'))
labelMasterAvatarLastName.grid(row=21, column=0, padx='5', pady='5', sticky='ew')
# Entry für MasterAvatarLastName
entryMasterAvatarLastName = Entry(master=tkFenster, bg='white', width='32')
entryMasterAvatarLastName.grid(row=21, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryMasterAvatarLastName,balloonmsg= _("Master Avatar Last Name"))
# Checkbutton für MasterAvatarLastName
checkMasterAvatarLastName = IntVar()
Checkbutton(tkFenster, text=_("turn on"), variable=checkMasterAvatarLastName).grid(row=21, column=2, sticky=W)

# Label mit Aufschrift MasterAvatarSandboxPassword
labelMasterAvatarSandboxPassword = Label(master=tkFenster, bg='#F9CDAD', text=_('Master Avatar Sandbox Password'))
labelMasterAvatarSandboxPassword.grid(row=22, column=0, padx='5', pady='5', sticky='ew')
# Entry für MasterAvatarSandboxPassword
entryMasterAvatarSandboxPassword = Entry(master=tkFenster, bg='white', width='32')
entryMasterAvatarSandboxPassword.grid(row=22, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryMasterAvatarSandboxPassword,balloonmsg= _("Master Avatar Sandbox Password"))
# Checkbutton für MasterAvatarSandboxPassword
checkMasterAvatarSandboxPassword = IntVar()
Checkbutton(tkFenster, text=_("turn on"), variable=checkMasterAvatarSandboxPassword).grid(row=22, column=2, sticky=W)

# Label mit Aufschrift Regionamount
labelRegionamount = Label(master=tkFenster, bg='#00FFBC', text=_('Number of regions'))
labelRegionamount.grid(row=23, column=0, padx='5', pady='5', sticky='ew')
# Entry für Region amount
entryRegionamount = Entry(master=tkFenster, bg='white', width='32')
entryRegionamount.grid(row=23, column=1, padx='5', pady='5', sticky='ew')
entryRegionamount.insert(10, "1") # Mindestens eine Region erstellen.
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryRegionamount,balloonmsg= _("The desired number of regions."))
# Checkbutton für MultiRegionamount
checkMultiRegionamount = IntVar()
Checkbutton(tkFenster, text=_("Multiple"), variable=checkMultiRegionamount).grid(row=23, column=2, sticky=W)

################################# Buttons ##################################################

# Button zum Erstellen
#RegionCreate = Button(master=tkFenster, text=_('Create'), width='22', bg='#00FFBC', command=createconfig)
RegionCreate = Button(master=tkFenster, text=_('Create'), width='22', bg='#00FFBC', command=start)
RegionCreate.grid(row=25, column=0, padx='5', pady='5')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(RegionCreate,balloonmsg= _("Creating the region configurations."))

# Button zum Clear
buttonClear = Button(master=tkFenster, text=_('Clear'), width='10', bg='#FFCFC9', command=clear_input_field)
buttonClear.grid(row=25, column=1, padx='5', pady='5')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(buttonClear,balloonmsg= _("Delete data."))

# Button zum Help
buttonHelp = Button(master=tkFenster, text=_('Help'), width='10', bg='#FFF070', command=helping)
buttonHelp.grid(row=25, column=2, padx='5', pady='5')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(buttonHelp,balloonmsg= _("Request help."))

# Button zum Abbrechen
buttonExit = Button(master=tkFenster, text=_('Exit'), width='10', bg='#FFCFC9', command=close_window)
buttonExit.grid(row=25, column=3, padx='5', pady='5')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(buttonExit,balloonmsg= _("Exit program."))

###################### Aktivierung des Fensters #######################
tkFenster.mainloop()