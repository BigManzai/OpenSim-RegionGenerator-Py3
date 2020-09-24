#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#

# Wenn IP auf Random steht wird dann wird automatisch SYSTEMIP genutzt.
# Wenn Size auf Random steht wird dann wird automatisch 256 genutzt.
# Wenn Location auf Random steht wird dann werden automatisch Zufallswerte zwischen 1000-8000 genutzt.
# Wenn Port auf Random steht wird dann werden automatisch Zufallswerte zwischen 9100-9999 genutzt.
# Wenn UUID auf Random steht wird dann wird automatisch eine generiert.
# Wenn Region name auf Random steht wird dann wird automatisch ein Zufallsname genutzt.
# Wenn Number of regions auf Random steht wird dann wird automatisch 1 genutzt.

# funktion off, random und wert als auswahl möglich machen.

import configparser
import uuid
import random
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.tix import * #Tooltips
from tkinter import messagebox
import random
import gettext


gettext.install('RegionsGen')
#lang1 = gettext.translation('RegionsGen', 'locale', languages=['de']) # Nur eine Sprache
#_ = lang1.gettext

#langall = gettext.translation('RegionsGen', 'locale') # Automatische auswahl
#_ = langall.gettext

# Uebersetzen geht so:
# ... _( )
# also ohne uebersetzung
# print('This is a not translatable string.')
# mit uebersetzung
# print(_('This is a translatable string.'))

# Extrahieren funktioniert in der Konsole im Programmpfad des Programmes so (Pfad anpassen):
# Pfad-zu\python.exe Pfad-zu\Tools\i18n\pygettext.py -d base -o Uebersetzungsdatei.pot Programmname.py
# C:\Python38\python.exe C:\Python38\Tools\i18n\pygettext.py -d base -o RegionsGen.pot RegionsGenUIV009.py
# Diese POT Datei kann mit PoEdit dann in jede X Beliebige Sprache uebersetzt werden. Beispiel RegionsGen.po und RegionsGen.mo.
# Die Dateien kommen in das Verzeichnis Programmverzeichnis\locale\de\LC_MESSAGES Beipiel hier ist de fuer Deutsch.

# Unter Anzeigen -> Befehlspalette... -> Python: Select Interpreter kann man eine 
# der installierten Python Versionen auswählen die genutzt werden. Beispiel Python 2.7 oder 3.8.

# EXE Datei mit pyinstaller:
# pyinstaller muss mit pip installiert werden.
# pip install pyinstaller
# Alle Python Skripte hinten anhängen.
# pyinstaller --windowed --noconsole --onefile RegionsGen.py random_name_def.py


######################################################
########## Ultra Region Generator Namen      #########
######################################################

# random name
#import random

def randomname():
    name = random.choice(['Abod', 'Adalbeort', 'Adalgar', 'Adham', 'Adken', 'Adulfuns', 'Aelf', 'Aelfraid', 'Aelfric', 'Aelor',
        'Aescby', 'Aethel', 'Aethelberht', 'Aethelisdun', 'Ahanor', 'Aherne', 'Ahrin', 'Aidan', 'Aidtun', 'Aifrid',
        'Ailean', 'Aimil', 'Aineislis', 'Arileas', 'Aislinn', 'Alain', 'Albhaois', 'Albion', 'Aldus', 'Aler', 'Algonthir',
        'Alraed', 'Alhric', 'Alhwin', 'Alian', 'Allsun', 'Alviss', 'Amalasand', 'Amalien', 'Amario', 'Amber', 'Amhiunn',
        'Amhlaidh', 'Amires', 'Amlauril', 'Amon', 'Anant', 'Anaurathiel', 'Andariel', 'Andarius', 'Anfalas', 'Anhlaoigh',
        'Anntoin', 'Anwyl', 'Aodh', 'Aodha', 'Aodhagan', 'Aodhan', 'Aoidh', 'Aoiffe', 'Aonghus', 'Aralian', 'Aralt', 'Arela',
        'Arheyu', 'Arndell', 'Arnhold', 'Arni', 'Arnwald', 'Arnwulf', 'Arombolosch', 'Arregaithel', 'Artair', 'Arthwr',
        'Arthylomis', 'Artur', 'Asgault', 'Athàlùsa', 'Athdara', 'Athdara', 'Attewelle', 'Avis', 'Awurin', 'Aylen', 'Baehloew',
        'Bagon', 'Bain', 'Bairghith', 'Baldmar', 'Banain', 'Banbrigge', 'Bangan', 'Banlòr', 'Banurr', 'Bardawulf', 'Bardhardt',
        'Bargash', 'Barghan', 'Barthr', 'Beadu', 'Beagan', 'Bearach', 'Beathag', 'Bebhinn', 'Becere', 'Beledene', 'Beonetleah',
        'Beorc', 'Beordtraed', 'Beorht', 'Beorhthram', 'Beormann', 'Beornet', 'Beorttun', 'Beorwalt', 'Berchtwald', 'Bercleah',
        'Berdine', 'Berin', 'Berinhardt', 'Bhaird', 'Bhaltair', 'Bhaltair', 'Bhragas', 'Binge', 'Binok', 'Binokee', 'Blaecleah',
        'Blaed', 'Blar', 'Bliths', 'Bloddwyn', 'Blotsm', 'Bluainach', 'Boda', 'Bofind', 'Bofind', 'Bogohardt', 'Boltar', 'Born',
        'Boron', 'Bothi', 'Boyne', 'Bradach', 'Brangwen', 'Brann', 'Breandan', 'Bret', 'Brian', 'Bridhid', 'Brock', 'Bronwyn',
        'Broth', 'Bryn', 'Brys', 'Buadhach', 'Buidhe', 'Burgal', 'Burr', 'Cadawig', 'Caddrairc', 'Cadel', 'Cadhla', 'Caellach',
        'Caerau', 'Caerghallan', 'Cai', 'Cailean', 'Caileass', 'Cain', 'Caitlin', 'Calldwr', 'Cambeul', 'Cameron', 'Canshron',
        'Cant', 'Caoinleain', 'Caolabhuinn', 'Caolaidhe', 'Caomh', 'Caomhan', 'Caomhiun', 'Caradoc', 'Caramichil', 'Cariadland',
        'Carleas', 'Carriag', 'Carridin', 'Casidhe', 'Cassimir', 'Cathan', 'Cathaoirmor', 'Cathasach', 'Cathmaol', 'Ceallach',
        'Ceannfhionn', 'Ceara', 'Cearbhallain', 'Cearnach', 'Cearrbhach', 'Ceileachan', 'Cein', 'Cellanir', 'Ceneric', 'Ceran',
        'Chalice', 'Chandiris', 'Charea', 'Cianan', 'Ciarda', 'Cillcumhan', 'Cillin', 'Cinfhaolaidh', 'Cingesleah', 'Cinnard',
        'Cinneididh', 'Cinnfhail', 'Ciulthinn', 'Claefer', 'Elspe', 'Elsurion', 'Endover', 'Engelbergt', 'Engholm', 'Enit', 'Eodoaine',
        'Eoghan', 'Eoin', 'Eorforwic', 'Eorl', 'Ingmar', 'Iniadea', 'Inis', 'Iosep', 'Isan', 'Isedria', 'Isenham', 'Itu', 'Ivhar', 'Jami',
        'Jander', 'Jaral', 'Jeffries', 'Claeg', 'Cleve', 'Clif', 'Clywd', 'Coal', 'Coalan', 'Coed', 'Coilin', 'Coille', 'Coinneach',
        'Coire', 'Conaire', 'Conan', 'Conn', 'Conndchadh', 'Corbmac', 'Corcurachan', 'Corelja', 'Corondal', 'Corondhal', 'Corzar',
        'Craccas', 'Creag', 'Creaga', 'Creiddylad', 'Creya', 'Cristin', 'Cuinn', 'Curadhan', 'Cuthbeorht', 'Cwen', 'Cwladys', 'Cynbel',
        'Cyne', 'Cyneburhleah', 'Cyneric', 'Cynesige', 'Cyrius', 'Cythranil', 'Daegelbeorht', 'Daegeseage', 'Dael', 'Daeltun', 'Daeran',
        'Daghat', 'Dagian', 'Dagomar', 'Dagr', 'Daimhin', 'Dalach', 'Dalr', 'Dalyell', 'Danr', 'Daregas', 'Darhan', 'Dariel', 'Darwyn',
        'Dearan', 'Deardrui', 'Deasach', 'Deasmumhan', 'Debroun', 'Defyaio', 'Delair', 'Dellingr', 'Demandred', 'Demyavan', 'Dene', 'Denethor',
        'Denu', 'Deorward', 'Dercarat', 'Derenai', 'Derylynn', 'Dewi', 'Dewi', 'Diamar', 'Diarmaoid', 'Dikibyr', 'Diolmhain', 'Diomassach',
        'Direa', 'Diss', 'Doghailen', 'Dogrim', 'Doire', 'Doireann', 'Domhnull', 'Dorminil', 'Draca', 'Drugiself', 'Dryw', 'Dseoran', 'Duria',
        'Duana', 'Dubh', 'Dubhgan', 'Dubhghall', 'Dubhglas', 'Dubhlachan', 'Dubhloach', 'Dubhthach', 'Duddaleah', 'Dufrhealh', 'Duhlasar',
        'Dumond', 'Dunleah', 'Dunn', 'Dyddplentyn', 'Dylan', 'Dylan', 'Eachan', 'Eachthighearn', 'Eada', 'Eadbeorht', 'Eadgar', 'Eadmund',
        'Eadwulf', 'Ealadhach', 'Ealdraed', 'Ealhard', 'Ealhdun', 'Eamon', 'Eanruig', 'Earnest', 'Earric', 'Eathelin', 'Eatun', 'Eberk',
        'Eburhardt', 'Ecgbeorth', 'Eferhard', 'Efrania', 'Ehren', 'Eibhlin', 'Eideann', 'Eilis', 'Einher', 'Einion', 'Eiric', '/', 'Eirik',
        'Eister', 'Elanear', 'Eldrias', 'Elemthain', 'Ellinar', 'Elram', 'Elrias', 'Eostre', 'Erinn', 'Erminric', 'Ertha', 'Estcot', 'Esthandir',
        'Esyathol', 'Ethiyanil', 'Eyrekr', 'Eysellt', 'Faegan', 'Faeroth', 'Faerrleah', 'Faerven', 'Faerwald', 'Fairhinath', 'Famek', 'Faodhagan',
        'Fearbhirigh', 'Fearghal', 'Fearghus', 'Fearn', 'Feich', 'Felabeorht', 'Felizitas', 'Fender', 'Feoras', 'Fiamar', 'Filmaen', 'Fingolfin',
        'Fionn', 'Fionnghalac', 'Fionnghuala', 'Fips', 'Firlionel', 'Flanna', 'Fleotig', 'Floinn', 'Flynt', 'Fridu', 'Friduric', 'Frimunt',
        'Fugentun', 'Gaelan', 'Gaelbhan', 'Galchobhar', 'Gallgaidheal', 'Gandalf', 'Garisin', 'Garivou', 'Garm', 'Garthr', 'Garwig', 'Geatan',
        'Genji', 'Gerhwas', 'Gerrod', 'Gerwalt', 'Ghleanna', 'Gilolla', 'Gimli', 'Giollamhuire', 'Giollaruaidh', 'Gionnan', 'Giorsal', 'Gipcyan',
        'Gislbyr', 'Gled', 'Glenndun', 'Glynydd', 'Gnarf', 'Gnimsch', 'Gnosch', 'Goathaire', 'Goda', 'Godehard', 'Godgifu', 'Gondo', 'Goridh',
        'Goridh', 'Gorman', 'Gorman', 'Goscelin', 'Gothfraidh', 'Grada', 'Graegleah', 'Griswald', 'Gruffudd', 'Gunnhar', 'Guthr', 'Gwalchmai',
        'Gwendolyn', 'Gwenhwyvar', 'Gwlsdys', 'Gyldan', 'Gyrwode', 'Gytha', 'Gyvron', 'Hacor', 'Hadu', 'Haele', 'Haesel', 'Haestibgas',
        'Hafirinm', 'Hafleikr', 'Haga', 'Hakon', 'Halag', 'Halfdan', 'Halifrid', 'Halig', 'Haltor', 'Hammar', 'Hanraoi', 'Haorinas', 'Harad',
        'Haragraf', 'Harailt', 'Harpo', 'Harti', 'Haruald', 'Hearpere', 'Heathleah', 'Heimrik', 'Heort', 'Heriberaht', 'Herimann', 'Herwig',
        'Hidlimar', 'Hilbrand', 'Hildhard', 'Hohberht', 'Hoibeard', 'Hoireabard', 'Holda', 'Honod', 'Howel', 'Howel', 'Hugiberaht', 'Hugiet',
        'Hunfrid', 'Hunig', 'Iaian', 'Ifig', 'Iltak', 'Imrahil', 'Jezer', 'Joreg', 'Jozan', 'Kaja', 'Kandorys', 'Kerwyn', 'Kiarr', 'Kief',
        'Kiollsig', 'Kirkja', 'Kirkjabyr', 'Knut', 'Kort', 'Korulas', 'Krak', 'Krossbyr', 'Kuambyr', 'Kulbari', 'Kunagnos', 'Kuonraed', 'Kyan',
        'Kythauriel', 'Labhruinn', 'Ladhaoise', 'Laec', 'Lagan', 'Laghras', 'Laird', 'Landbercht', 'Langr', 'Laochailan', 'Laudrius', 'Leagorn',
        'Leamhnach', 'Leander', 'Leannan', 'Leathlaghra', 'Lebennin', 'Lefael', 'Leif', 'Leoma', 'Leraneal', 'Leschko', 'Leskoh', 'Lethanon',
        'Leutpald', 'Lilias', 'Lind', 'Lindael', 'Lindberg', 'Lintflas', 'Lioslaith', 'Liusadh', 'Llwyd', 'Llyn', 'Llyweilun', 'Logmann', 'Lokti',
        'Lomarin', 'Lonn', 'Lothar', 'Lotharingen', 'Lubig', 'Lughaidh', 'Lughaidh', 'Luighseacg', 'Toireasa', 'Torma', 'Torr', 'Torra', 'Truda',
        'Ula', 'Ura', 'Walda', 'Waldburga', 'Winifrid', 'Wulfila', 'Wulfrith', 'Wulfsige', 'Ladhaoise', 'Larissa', 'Lidda', 'Lilias', 'Liusadh',
        'Luighseacg', 'Luisadh', 'Mab', 'Maertisa', 'Maeva', 'Magamhildi', 'Mahthildin', 'Maible', 'Maighdlin', 'Maire', 'Mairghread', 'Mairi',
        'Marcail', 'Maredud', 'Mathildi', 'Maura', 'Maureen', 'Meadhbh', 'Mearr', 'Mercia', 'Meredydd', 'Mhari', 'Mildraed', 'Minne', 'Miureall',
        'Moibeal', 'Moire', 'Moireach', 'Monca', 'Morag', 'Morgant', 'Moya', 'Muire', 'Muirgheal', 'Muirne', 'Nadjala', 'Niall', 'Odharait',
        'Oona', 'Oonagh', 'Ordwime', 'Pianwig', 'Raginmund', 'Raoghnait', 'Rioghnach', 'Rois', 'Rozumund', 'Ruomhildr', 'Sadhbh', 'Sadhbha',
        'Saidhghin', 'Salaidh', 'Sibeal', 'Sigilwig', 'Sigimund', 'Signi', 'Sine', 'Siobhan', 'Sion', 'Siubhan', 'Siusan', 'Sorcha', 'Sosanna',
        'Swynedd', 'Taithleach', 'Tanya', 'Thoridyss', 'Toirdealbach', 'Luisadh', 'Lundr', 'Luthais', 'Lyrandis', 'Lyrsil', 'Lysil', 'Lysira',
        'Maarkan', 'Mab', 'Macothiel', 'Madelhari', 'Maegth', 'Maeva', 'Magafeld', 'Magnus', 'Maible', 'Maighdlin', 'Maire', 'Mairghread',
        'Mairi', 'Maithilis', 'Mandel', 'Mannfrith', 'Maodighomhnaigh', 'Maolmin', 'Maolmin', 'Maolmuire', 'Maoltuile', 'Marcail', 'Maredud',
        'Mari', 'Maril', 'Marla', 'Maskol', 'Maura', 'Maureen', 'Meadhbh', 'Mearr', 'Meginhardt', 'Meliondor', 'Meredydd', 'Merehloew', 'Mersc',
        'Messkir', 'Metira', 'Metrios', 'Mhari', 'Mialee', 'Micheil', 'Minarvos', 'Minata', 'Mirtek', 'Miureall', 'Modread', 'Mog-Macha',
        'Moibeal', 'Moineruadh', 'Moineruadh', 'Moire', 'Moireach', 'Moldrack', 'Monca', 'Morag', 'Morcan', 'Morfinn', 'Morgant', 'Morgen',
        'Morogh', 'Mortun', 'Moya', 'Muir', 'Muire', 'Muireadhaigh', 'Muirgheal', 'Muirne', 'Murchadh', 'Murthuile', 'Mylnburne', 'Naheniel',
        'Nathondal', 'Naul', 'Neblehle', 'Nerviar', 'Newyddllyn', 'Niaeha', 'Niall', 'Nichus', 'Niewheall', 'Norberaht', 'Nuallan', 'Odbert',
        'Odharait', 'Odhrean', 'Odimorr', 'Odwulf', 'Oleifr', 'Ollaneg', 'Olvaerr', 'Omid', 'Oona', 'Oonagh', 'Ordalf', 'Orharikr', 'Osbeorht',
        'Oskar', 'Osmaer', 'Osraed', 'Osric', 'Othomann', 'Owein', 'Owein', 'Padraig', 'Padriac', 'Paduicg', 'Parlan', 'Parlan', 'Peadair',
        'Peadar', 'Pennleah', 'Peppi', 'Perin', 'Permeyah', 'Preostleah', 'Quarz', 'Radagast', 'Rafmag', 'Allweg', 'Ragdal', 'El', 'Zoreh',
        'Raghallach', 'Raghnall', 'Raginmund', 'Rahn', 'Raiola', 'Raja', 'Ramiris', 'Randwulf', 'Raoghnait', 'Raskogr', 'Rauthuellir', 'Raymir',
        'Readwulf', 'Regaf', 'Regdar', 'Reginberaht', 'Reidhachadh', 'Rhinfflew', 'Rhuk', 'Rhydag', 'Rhys', 'Riagan', 'Rian', 'Ridere', 'Rikar',
        'Rille', 'Riocard', 'Riodhr', 'Rioghbhardan', 'Rioghnach', 'Rodhlann', 'Rognuald', 'Rois', 'Ronan', 'Rotland', 'Ruadhan', 'Ruarc',
        'Rudrik', 'Rudugeard', 'Rumenea', 'Ruodger', 'Ruodlant', 'Ruomhildr', 'Rurik', 'Sadhbh', 'Sadhbha', 'Saegar', 'Saelec', 'Saerfren',
        'Saeweard', 'Saidhghin', 'Sailbheastar', 'Saitham', 'Sala', 'Salaidh', 'Salasu', 'San', 'Rhaal', 'Saphir', 'Saretus', 'Sargas', 'Saxon',
        'Scanlan', 'Sceaphierde', 'Scelfleah', 'Schiraljie', 'Scirwode', 'Scolaighe', 'Scrileadh', 'Seadaidh', 'Seain', 'Seanachan', 'Seanan',
        'Seanlaoch', 'Seann', 'Secgleah', 'Seiradan', 'Selvagitas', 'Sentaia', 'Sgeulaiche', 'Sha', 'Rell', 'ShaRed', 'Shane', 'Shauir',
        'Sibeal', 'Siddael', 'Sigifrith', 'Sigilwig', 'Sigimund', 'Sigiwald', 'Signi', 'Sigurdhr', 'Silanay', 'Silmalinnon', 'Silmarilon',
        'Silviara', 'Sim', 'Sindira', 'Sine', 'Siobhan', 'Siodhachan', 'Siolta', 'Siomonn', 'Sion', 'Sithethak', 'Siubhan', 'Siudhne',
        'Siusan', 'Skentha', 'Skereye', 'Skorag', 'Skypr', 'Slaedr', 'Slaghan', 'Sliaghin', 'Solamh', 'Somahirle', 'Sorcha', 'Sruthair',
        'Sruthan', 'Stanach', 'Steorra', 'Stodhierde', 'Strom', 'Sucram', 'Suileabhan', 'Suthrland', 'Swynedd', 'Tabbert', 'Tad', 'Taffy',
        'Taithleach', 'Tamnais', 'Taran', 'Taurelias', 'Tearlach', 'Teimhnean', 'Temara', 'Tendrik', 'Tespius', 'Tewdwr', 'Thalion', 'Thamios',
        'Tharimis', 'Thegn', 'Theuobald', 'Theuroik', 'Thoidgeirford', 'Thoraths', 'Thorbiartr', 'Thorbiorn', 'Thorfin', 'Thorir', 'Thoud',
        'Throaldr', 'Thruhleow', 'Thrythwig', 'Tiak', 'Tighearnach', 'Tioboid', 'Tiomoid', 'Tirell', 'Togtar', 'Toirdealbach', 'Toireasa',
        'Tomas', 'Torc', 'Tordek', 'Torm', 'Tormaigh', 'Torr', 'Torra', 'Tosdramos', 'Trahayarn', 'Tramiel', 'Trea', 'Treabhar', 'Treasach',
        'Trekarraz', 'Trent', 'Trevelian', 'Trystan', 'Tsoladin', 'Tuathal', 'Turgal', 'Txorass', 'Tygr', 'Tyrion', 'Ualtar', 'Udo', 'Uigboern',
        'Uilleam', 'Uinsionn', 'Ulbon', 'Ulfmaerr', 'Ulvelaik', 'Unnurr', 'Vaasa', 'Valadenya', 'Valerius', 'Varin', 'Varvia', 'Vollmr',
        'Vychan', 'Wace', 'Waenwryht', 'Waescburne', 'Waldramm', 'Walijan', 'Wallihelm', 'Wandi', 'Wann', 'Waren', 'Warto', 'Wendido', 'Wenis',
        'Werro', 'Wigis', 'Willaperht', 'Willimod', 'Winiholdo', 'Wolf', 'Wudoreafa', 'Wulfgar', 'Wulfric', 'Wulfrith', 'Wyrduàn', 'Yaligan',
        'Yarrik', 'YaYarzar', 'Yedda', 'Yofenia', 'Zaasz', 'Zareius', 'Zarrag', 'Zolt2.)Weibliche', 'Namen', 'Abvia', 'Adalheit', 'Aeldra',
        'Aelfdene', 'Aeltra', 'Aemete', 'Aethelmaere', 'Aidan', 'Ailin', 'Aimil', 'Aine', 'Airleas', 'Aislinn', 'Alain', 'Alaria', 'Allsun',
        'Alundra', 'Alviss', 'Amhiunn', 'Andaria', 'Aoiffe', 'Astryd', 'Athalindi', 'Attheneldre', 'Aylen', 'Baduhildi', 'Baldwine', 'Banbrigge',
        'Beathag', 'Bebhinn', 'Beorhthildi', 'Berahta', 'Berangari', 'Bloddwyn', 'Brangwen', 'Brann', 'Breandan', 'Bridhid', 'Brita', 'Bronwyn',
        'Brunihildi', 'Cadhla', 'Caellach', 'Caitlin', 'Caomhiun', 'Ceara', 'Chodhildi', 'Ciarda', 'Conn', 'Creiddylad', 'Cristin', 'Cwladys',
        'Dalaria', 'Damneya', 'Deardrui', 'Deorawine', 'Doire', 'Doireann', 'Domhnull', 'Duana', 'Dyddplentyn', 'Eadgyth', 'Ealasaid', 'Earwine',
        'Eibhlin', 'Eideann', 'Eilis', 'Eister', 'Elspe', 'Engelberhta', 'Enit', 'Eodoaine', 'Eorlariel', 'Erinn', 'Eysellt', 'Fionnghuala',
        'Flanna', 'Freyja', 'Gala', 'Gertrut', 'Ghleanna', 'Gilsberhta', 'Giorsal', 'Gisela', 'Glynydd', 'Grisjahildi', 'Gunnhild', 'Gwendolyn',
        'Gwenhwyvar', 'Gwlsdys', 'Haduwig', 'Herthe', 'Herwig', 'Hilde', 'Hildieth', 'Hildigard', 'Hlutwig', 'Hrothwine', 'HuldraIda', 'Iduna',
        'ImmaIngrida', 'Itu', 'Kelda','Duerrsturm', 'Trutzwueste', 'Koenigswueste', 'Eichenbruch', 'Baerensumpf', 'Untersteig', 'Hochfelde', 'Duerrberge', 
        'Duesterfelde', 'Sternental', 'Klingenstadt', 'Eichentann', 'Adlersbach', 'Duesterwald', 'Fuchspass', 'Sturmhain', 
        'Sturmwacht', 'Duerrfeld', 'Silbersee', 'Goldsturm', 'Schwalbental', 'Adlersstiege', 'Donnerwald', 'Baerensturm', 
        'Duestersumpf', 'Blitzburg', 'Mondhain', 'Wolkenwies', 'Dunkelfluss', 'Falkental', 'Klingenbach', 'Tiefsturm', 
        'Trutzwald', 'Feuerfeld', 'Donnerwalde', 'Donnerpass', 'Sternenbruch', 'Sturmsee', 'Adlersmeer', 'Feuerwald', 
        'Duestersee', 'Donnertann', 'Wolfswies', 'Tiefhuegel', 'Oberberge', 'Tiefstiege', 'Kaltenstiege', 'Sternennest', 
        'Donnerfels', 'Feuerwueste', 'Duestersee', 'Dunkelfels', 'Duerrnest', 'Brachfeld', 'Goldtal', 'Baerenstiege', 
        'Blitzbach', 'Tiefwacht', 'Kaltenhuegel', 'Mondberge', 'Dunkelwald', 'Schoenschlucht', 'Schwalbenstadt', 'Feuerhoehe', 
        'Goldburg', 'Kleinstrom', 'Hochhuegel', 'Tieffurt', 'Schwalbenhain', 'Drachenstein', 'Drachensee', 'Brachhuegel', 
        'Kaltenfluss', 'Hochsteig', 'Brachmeer', 'Goldwald', 'Kleinwacht', 'Silberwacht', 'Koenigsfeld', 'Baerensee', 
        'Adlersnest', 'Schoensteig', 'Drachensumpf', 'Tiefsteig', 'Wolkenanhoehen', 'Sonnensturm', 'Falkensee', 'Klingenbach', 
        'Klingenhuegel', 'Sonnensumpf', 'Unterburg', 'Sonnensteig', 'Tiefbach', 'Silberwacht', 'Fuchswueste', 'Drachenhoehe', 
        'Tiefsturm', 'Falkensteig', 'Adlersfluss', 'Schoenfels', 'Schoenhoehe', 'Eichenstrom', 'Brachstein', 'Hochwies', 
        'Dunkelmeer', 'Dunkelhuegel', 'Brachwacht', 'Trutzfels', 'Feuerhain', 'Duesterstrom', 'Hochhain', 'Koenigswies', 
        'Brachtal', 'Oberhoehe', 'Silbertann', 'Blitznest', 'Eichental', 'Schoenhain', 'Falkensturm', 'Fuchshoehe', 
        'Feueranhoehen', 'Obersee', 'Duerrstrom', 'Fuchshoehe', 'Klingenbruch', 'Kleinfeld', 'Blitztal', 'Dunkelbruch', 
        'Eichenhain', 'Mondmeer', 'Dunkelbruch', 'Feuerstrom', 'Eichenstrom', 'Brachstrom', 'Duerrhain', 'Dunkelwies', 
        'Koenigssturm', 'Drachenstrom', 'Sonnentann', 'Wolkenwald', 'Mondstiege', 'Feuerstrom', 'Blitzstein', 'Blitzwueste', 
        'Sternennest', 'Obertal', 'Tiefburg', 'Eichenwies', 'Klingenburg', 'Feuerwald', 'Baerenhoehe', 'Koenigswald', 
        'Fuchsfeld', 'Untertann', 'Eichenwald', 'Baerensteig', 'Sturmnest', 'Dunkeltann', 'Oberstadt', 'Koenigsfluss', 
        'Tieffelde', 'Feuerburg', 'Duerrfluss', 'Hochstiege', 'Eichenbach', 'Blitztann', 'Donnerschlucht', 'Klingenstadt', 
        'Sigen', 'Kenlat', 'Kenanth', 'Yalanth', 'SilithdraenLo', 'Silen', 'MiMi', 'Mianth', 'Loenlat', 'Kenlad', 'LoIsith', 'Kenen', 
        'Gaanth', 'Isgen', 'Loladanth', 'Gallat', 'MiMiKen', 'LoMi', 'Loanth', 'Silgenen', 'Sien', 'IsMienladSil', 'Xassil', 'IsladKen', 
        'Kenanth', 'SilMilad', 'Ishir', 'Ishirlad', 'Yalen', 'Ragol', 'Gremnak', 'Grarag', 'Ragol', 'Granakgoshnak', 'Ragall', 'Gurgall', 'Gremnaknak', 
        'Gremgoshlogg', 'Zunlogg', 'Gremgall', 'Granak', 'Granakgoshlogg', 'Tazragrag', 'Ragall', 'Granaknak', 'Zun', 'Tazrag', 'Grarag', 'Gremlogg', 
        'Grem', 'Ralogg', 'Zungolgoshgosh', 'Gurnakrag', 'loggrag', 'Tazrag', 'Taznak', 'Rarag', 'Gralogg', 'Dugasch', 'Thorgrim', 'Borlasch', 'Himrasch', 
        'EbboArom', 'Sabuk', 'Schraxbur', 'Rurasch', 'Jadin', 'Bando', 'Lidrasch', 'Odgisch', 'Duwim', 'Hamrax Polosch', 'Xaltho', 
        'Ultram', 'Geramfrim', 'Famasch', 'Iun', 'Folosch', 'Sedor', 'Nelesch', 'Thagrim', 'Hagam', 'Hornibosch', 'Muglim', 'Erasch', 
        'Mare', 'Marlinhanswinn', 'Peptram', 'Marwinnhintram', 'Finnhans', 'Peptramtramhin', 'Finnhin', 'Peprit', 
        'Mertramlinhans', 'Merlintramtramhans', 'Pephans', 'Berrit', 'Berrit', 'Marhans', 'Peptram', 'Samtram', 
        'Finnhin', 'Samhans', 'Pephans', 'Merrittramhinhin', 'Mar', 'Marlinlinwinn', 'Peplin', 'Samhinhin', 
        'Merhanstram', 'Marhintram', 'Samhanshans', 'Finnhinhin', 'Ladiana', 'Ladrahna', 'Brigisiaianatine', 'Ladianagitta', 
        'Sahiana', 'Brigrahnariatine', 'Ladarra', 'Brigrahnaarrarahna', 'Rosrahna', 'Samianatineriatine', 'Samiana', 'Merisia', 
        'Rosrahna', 'Sahrahnaiana', 'Rosiana', 'Rostine', 'Mergitta', 'Tiarahna', 'Ladgittaisia', 'Sahiana', 
        'Mera', 'Merria', 'Ladgittaarraiana', 'Rosgitta', 'Saharraria', 'Ladria', 'Brigtineisia', 'Berrit', 'Berwinn', 'Samhin', 'Pepwinn', 
        'Bertram', 'Merhanswinn', 'Peprithanshanshin', 'Marwinn', 'Samwinn', 'Pepwinnwinnhans', 'Berhin', 'Merhans', 
        'Bertram', 'Pephin', 'Berhans', 'Marlin', 'Marrit', 'Merlintramhans', 'Mariu', 'Samritrit', 'Berwinn', 'Marhin', 'Berhans', 'Berhans', 
        'Marwinnritlin', 'Marlin', 'Peptram', 'Pepo', 'Zorgath', 'Forarath', 'Fornoschnoschnosch', 'Ekgath', 
        'Zorgathgathiathsch', 'GaZor', 'Gohlarath', 'Fornuh', 'Gohlnosch', 'Gorguh', 'Gaarathgatharath', 'ZorFor', 
        'Gohloul', 'Gonosch', 'OlbiathZor', 'GorFor', 'Gogath', 'Forschnosch', 'GorZor', 'Forgath', 'Olbnuh', 'Foriath', 'Gohlsch', 'Gaarath', 
        'Gornosch', 'Zornoschguh', 'Goro', 'GamashFor', 'OlKei', 'Too', 'Arbahl', 'Runith', 'Klinerde', 'Toter', 'Runderde', 'Cenreth', 
        'DierIn', 'Klamling', 'Sargr', 'Dierder', 'MeKei', 'Klinderkunwurz', 'Hartol', 'Soli', 'Ganlibas', 'Dierder', 'Rundter', 'Sarter', 
        'Holkuneinol', 'Sowurz', 'Klinber', 'Dierst', 'WanSo', 'Klamig', 'Meamm', 'Klamdring', 'Klame', 'Sospan', 'Haldring', 'Schol', 
        'Todringdring', 'Ardring', 'Dierber', 'Klamkunrol', 'Bimdor', 'Baudring', 'Keibahl', 'IsEin', 'IsWanter', 'Soder', 'Hunamm', 'Iskeni', 
        'Wanatz', 'Hal', 'Klinspan', 'Sarant', 'HartKlinken', 'DierMe', 'Ganter', 'Keikar', 'RunAlEin', 'Cenatz', 'Runner', 'Glimspan', 
        'Glimner', 'Mekardor', 'AlArteretzgleif', 'Cenu', 'Cender', 'Keio', 'GandringkunWanker', 'Halrat', 'KlamIndring', 'Inter', 'Klamli', 'Borter', 
        'KeiBim', 'Meoma', 'Arwurz', 'Eina', 'Older', 'Glimdringerdei', 'Alst', 'Bauol', 'HalBim', 'RunIs', 'Runding', 'Sarbahl', 'Arder', 'Bimst', 'Klamweb', 'Schetz']);
    return name;

######################################################
########## Ultra Region Generator Funktionen #########
######################################################

def helping():
    messagebox.showinfo("Helping", "Alles was in Rot zu sehen ist funktioniert nur automatisch. \nAlles was Grün ist kann wahlweise auch ausgefüllt werden, funktioniert aber auch automatisch. \nIn Gelb dargestellte Funktionen befinden sich im Test.")
    return;

def clearing():
    messagebox.showinfo("Clearing", "Ohne Funktion")
    return;

def close_window(): 
    tkFenster.destroy()

# make a random location
def randomlocation():
    maplocation = random.randrange(1000, 8000, 4)
    localmap = str(maplocation)
    return localmap;

# assemble region location
# maplocation = randomlocation() + ',' + randomlocation()

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
    global ExternalHostName_var, InternalPort_var, RegionUUID_var, RegionName_var, RegionAmount_var, LocationX_var, LocationY_var

    config = configparser.ConfigParser()
    
    # assemble region location
    maplocation = str(entryLocation.get()) # Holt die Daten aus der Eingabe, hier die maplocation.
    if maplocation=='' : maplocation = randomlocation() + ',' + randomlocation()

    # capitalization gross- kleinschreibung beachten
    config.optionxform = str

    # any name
    #regionname = randomname();
    #regionnameout = randomname();
    regionname = str(entryRegionName.get()) # Holt die Daten aus der Eingabe, hier die regionname.
    regionnameout = str(entryRegionName.get()) # Holt die Daten aus der Eingabe, hier die regionname.
    if regionname=='' : regionname = randomname()
    if regionnameout=='' : regionnameout = randomname()

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
    if MaxAgents=='' : MaxAgents = '50'

    ##### Nachfolgendes fehlt noch

    #entryAllowAlternatePorts
    AllowAlternatePorts = str(entryAllowAlternatePorts.get())
    if AllowAlternatePorts=='' : AllowAlternatePorts = 'False'
    #entryResolveAdress
    ResolveAdress = str(entryResolveAdress.get())
    if ResolveAdress=='' : ResolveAdress = 'False'
    #entryDefaultLanding
    DefaultLanding = str(entryDefaultLanding.get())
    if DefaultLanding=='' : DefaultLanding = '<128,128,21>'
    #entryNonPhysicalPrimMax
    NonPhysicalPrimMax = str(entryNonPhysicalPrimMax.get())
    if NonPhysicalPrimMax=='' : NonPhysicalPrimMax = '1024'
    #entryPhysicalPrimMax
    PhysicalPrimMax = str(entryPhysicalPrimMax.get())
    if PhysicalPrimMax=='' : PhysicalPrimMax = '64'
    #entryClampPrimSize
    ClampPrimSize = str(entryClampPrimSize.get())
    if ClampPrimSize=='' : ClampPrimSize = 'False'
    #entryMaxPrimsPerUser
    MaxPrimsPerUser = str(entryMaxPrimsPerUser.get())
    if MaxPrimsPerUser=='' : MaxPrimsPerUser = '-1'
    #entryScopeID
    ScopeID = str(entryScopeID.get())
    if ScopeID=='' : ScopeID = ruuid   
    #entryRegionType
    RegionType = str(entryRegionType.get())
    if RegionType=='' : RegionType = 'Mainland'
    #entryMaptileStaticUUID
    MaptileStaticUUID = str(entryMaptileStaticUUID.get())
    if MaptileStaticUUID=='' : MaptileStaticUUID = ruuid
    #entryMaptileStaticFile
    MaptileStaticFile = str(entryMaptileStaticFile.get())
    if MaptileStaticFile=='' : MaptileStaticFile = '"water.jpg"'
    #entryMasterAvatarFirstName
    MasterAvatarFirstName = str(entryMasterAvatarFirstName.get())
    if MasterAvatarFirstName=='' : MasterAvatarFirstName = 'John'
    #entryMasterAvatarLastName
    MasterAvatarLastName = str(entryMasterAvatarLastName.get())
    if MasterAvatarLastName=='' : MasterAvatarLastName = 'Doe'
    #entryMasterAvatarSandboxPassword
    MasterAvatarSandboxPassword = str(entryMasterAvatarSandboxPassword.get())
    if MasterAvatarSandboxPassword=='' : MasterAvatarSandboxPassword = 'passwd'
    #entryInternalAddress
    InternalAddress = str(entryInternalAddress.get())
    if InternalAddress=='' : InternalAddress = "0.0.0.0"
    #entryResolveAdress
    ResolveAdress = str(entryResolveAdress.get())
    if ResolveAdress=='' : ResolveAdress = "False"
    #ResolveAddress = "False"

    
    # ExternalHostName
    ExternalHostName = str(entryExternalHostName.get()) # Holt die Daten aus der Eingabe, hier ExternalHostName.
    if ExternalHostName=='' : ExternalHostName = "SYSTEMIP"
    
    # Change space to subline for the filename
    confdatei = regionnameout.replace(" ", "_")
    
   
    config[regionnameout] = {'RegionUUID': ruuid,
                          'Location': maplocation,
                          'SizeX': Size_var,
                          'SizeY': Size_var,
                          'SizeZ': Size_var,
                          'InternalAddress': InternalAddress,
                          'InternalPort': InternalPort,
                          'AllowAlternatePorts': AllowAlternatePorts,
                          'ResolveAddress': ResolveAdress,
                          'ExternalHostName': ExternalHostName,
                          'MaxPrims': MaxPrims,
                          'MaxAgents': MaxAgents,
                          ';DefaultLanding': DefaultLanding,
                          ';NonPhysicalPrimMax': NonPhysicalPrimMax,
                          ';PhysicalPrimMax': PhysicalPrimMax,
                          ';ClampPrimSize': ClampPrimSize,
                          ';MaxPrimsPerUser': MaxPrimsPerUser,
                          ';ScopeID': ScopeID,
                          ';RegionType': RegionType,
                          'MaptileStaticUUID': MaptileStaticUUID,
                          ';MaptileStaticFile': MaptileStaticFile,
                          ';MasterAvatarFirstName': MasterAvatarFirstName,
                          ';MasterAvatarLastName': MasterAvatarLastName,
                          ';MasterAvatarSandboxPassword': MasterAvatarSandboxPassword}

    with open(confdatei + '.ini', 'w') as configfile: config.write(configfile)

def createconfig():
    
    i=0
    
    n = int(entryRegionamount.get()) # Holt die Daten aus der Eingabe, hier die Menge der Regionen.
    #if n=='' : n=1 #Wenn nichts angegeben wird dann eine Region erstellen.

    for i in range(i, n):
	    write_region()
    else:
	    return;

def clear_input_field():
   #Entry.delete(0, END)
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
tkFenster.title('RegionsGenerator')
tkFenster.iconbitmap('opensim.ico')
#tkFenster.geometry("800x850+937+134") #Groesse des Fensters vorgeben.

# Rot #FFCFC9 Gruen #00FFBC Gelb #FFF070

# Label mit Aufschrift RegionName
labelRegionName = Label(master=tkFenster, bg='#00FFBC', text='Region Name')
labelRegionName.grid(row=0, column=0, padx='5', pady='5', sticky='ew')
# Entry für RegionName
entryRegionName = Entry(master=tkFenster, bg='white', width='32')
entryRegionName.grid(row=0, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryRegionName,balloonmsg= "insert region name")

# Label mit Aufschrift Location
labelLocation = Label(master=tkFenster, bg='#00FFBC', text='Location')
labelLocation.grid(row=1, column=0, padx='5', pady='5', sticky='ew')
# Entry für Location
entryLocation = Entry(master=tkFenster, bg='white', width='32')
entryLocation.grid(row=1, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryLocation,balloonmsg= "Location x,y example 1000,1000")

# Label mit Aufschrift RegionUUID
labelRegionUUID = Label(master=tkFenster, bg='#00FFBC', text='RegionUUID')
labelRegionUUID.grid(row=2, column=0, padx='5', pady='5', sticky='ew')
# Entry für RegionUUID
entryRegionUUID = Entry(master=tkFenster, bg='white', width='32')
entryRegionUUID.grid(row=2, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryRegionUUID,balloonmsg= "RegionUUID blank creates a random.")

# Label mit Aufschrift Size
labelSize = Label(master=tkFenster, bg='#00FFBC', text='Size')
labelSize.grid(row=3, column=0, padx='5', pady='5', sticky='ew')
# Entry für Size
entrySize = Entry(master=tkFenster, bg='white', width='32')
entrySize.grid(row=3, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entrySize,balloonmsg= "If size is not specified it will default to the legacy size of 256.")

# Label mit Aufschrift InternalPort
labelInternalPort = Label(master=tkFenster, bg='#00FFBC', text='InternalPort')
labelInternalPort.grid(row=4, column=0, padx='5', pady='5', sticky='ew')
# Entry für InternalPort
entryInternalPort = Entry(master=tkFenster, bg='white', width='32')
entryInternalPort.grid(row=4, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryInternalPort,balloonmsg= "InternalPort blank creates a random.")

# Label mit Aufschrift AllowAlternatePorts
labelAllowAlternatePorts = Label(master=tkFenster, bg='#FFF070', text='AllowAlternatePorts')
labelAllowAlternatePorts.grid(row=5, column=0, padx='5', pady='5', sticky='ew')
# Entry für AllowAlternatePorts
entryAllowAlternatePorts = Entry(master=tkFenster, bg='white', width='32')
entryAllowAlternatePorts.grid(row=5, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryAllowAlternatePorts,balloonmsg= "AllowAlternatePorts")

# Label mit Aufschrift ResolveAdress
labelResolveAdress = Label(master=tkFenster, bg='#FFF070', text='ResolveAdress')
labelResolveAdress.grid(row=6, column=0, padx='5', pady='5', sticky='ew')
# Entry für ResolveAdress
entryResolveAdress = Entry(master=tkFenster, bg='white', width='32')
entryResolveAdress.grid(row=6, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryResolveAdress,balloonmsg= "ResolveAdress")

# Label mit Aufschrift ExternalHostName
labelExternalHostName = Label(master=tkFenster, bg='#00FFBC', text='ExternalHostName')
labelExternalHostName.grid(row=7, column=0, padx='5', pady='5', sticky='ew')
# Entry für ExternalHostName
entryExternalHostName = Entry(master=tkFenster, bg='white', width='32')
entryExternalHostName.grid(row=7, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryExternalHostName,balloonmsg= "ExternalHostName")

# Label mit Aufschrift MaxPrims
labelMaxPrims = Label(master=tkFenster, bg='#00FFBC', text='MaxPrims')
labelMaxPrims.grid(row=8, column=0, padx='5', pady='5', sticky='ew')
# Entry für MaxPrims
entryMaxPrims = Entry(master=tkFenster, bg='white', width='32')
entryMaxPrims.grid(row=8, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryMaxPrims,balloonmsg= "Limit prims to the regions.")

# Label mit Aufschrift MaxAgents
labelMaxAgents = Label(master=tkFenster, bg='#00FFBC', text='MaxAgents')
labelMaxAgents.grid(row=9, column=0, padx='5', pady='5', sticky='ew')
# Entry für MaxAgents
entryMaxAgents = Entry(master=tkFenster, bg='white', width='32')
entryMaxAgents.grid(row=9, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryMaxAgents,balloonmsg= "Limit Agents to the regions.")

# Label mit Aufschrift DefaultLanding
labelDefaultLanding = Label(master=tkFenster, bg='#FFF070', text='DefaultLanding')
labelDefaultLanding.grid(row=10, column=0, padx='5', pady='5', sticky='ew')
# Entry für DefaultLanding
entryDefaultLanding = Entry(master=tkFenster, bg='white', width='32')
entryDefaultLanding.grid(row=10, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryDefaultLanding,balloonmsg= "DefaultLanding")

# Label mit Aufschrift NonPhysicalPrimMax
labelNonPhysicalPrimMax = Label(master=tkFenster, bg='#FFF070', text='NonPhysicalPrimMax')
labelNonPhysicalPrimMax.grid(row=11, column=0, padx='5', pady='5', sticky='ew')
# Entry für NonPhysicalPrimMax
entryNonPhysicalPrimMax = Entry(master=tkFenster, bg='white', width='32')
entryNonPhysicalPrimMax.grid(row=11, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryNonPhysicalPrimMax,balloonmsg= "NonPhysicalPrimMax")

# Label mit Aufschrift PhysicalPrimMax
labelPhysicalPrimMax = Label(master=tkFenster, bg='#FFF070', text='PhysicalPrimMax')
labelPhysicalPrimMax.grid(row=12, column=0, padx='5', pady='5', sticky='ew')
# Entry für PhysicalPrimMax
entryPhysicalPrimMax = Entry(master=tkFenster, bg='white', width='32')
entryPhysicalPrimMax.grid(row=12, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryPhysicalPrimMax,balloonmsg= "PhysicalPrimMax")

# Label mit Aufschrift ClampPrimSize
labelClampPrimSize = Label(master=tkFenster, bg='#FFF070', text='ClampPrimSize')
labelClampPrimSize.grid(row=13, column=0, padx='5', pady='5', sticky='ew')
# Entry für ClampPrimSize
entryClampPrimSize = Entry(master=tkFenster, bg='white', width='32')
entryClampPrimSize.grid(row=13, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryClampPrimSize,balloonmsg= "ClampPrimSize")

# Label mit Aufschrift MaxPrimsPerUser
labelMaxPrimsPerUser = Label(master=tkFenster, bg='#FFF070', text='MaxPrimsPerUser')
labelMaxPrimsPerUser.grid(row=14, column=0, padx='5', pady='5', sticky='ew')
# Entry für MaxPrimsPerUser
entryMaxPrimsPerUser = Entry(master=tkFenster, bg='white', width='32')
entryMaxPrimsPerUser.grid(row=14, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryMaxPrimsPerUser,balloonmsg= "MaxPrimsPerUser")

# Label mit Aufschrift ScopeID
labelScopeID = Label(master=tkFenster, bg='#FFF070', text='ScopeID')
labelScopeID.grid(row=15, column=0, padx='5', pady='5', sticky='ew')
# Entry für ScopeID
entryScopeID = Entry(master=tkFenster, bg='white', width='32')
entryScopeID.grid(row=15, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryScopeID,balloonmsg= "ScopeID")

# Label mit Aufschrift RegionType
labelRegionType = Label(master=tkFenster, bg='#FFF070', text='RegionType')
labelRegionType.grid(row=16, column=0, padx='5', pady='5', sticky='ew')
# Entry für RegionType
entryRegionType = Entry(master=tkFenster, bg='white', width='32')
entryRegionType.grid(row=16, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryRegionType,balloonmsg= "RegionType")

# Label mit Aufschrift MaptileStaticUUID
labelMaptileStaticUUID = Label(master=tkFenster, bg='#FFF070', text='MaptileStaticUUID')
labelMaptileStaticUUID.grid(row=17, column=0, padx='5', pady='5', sticky='ew')
# Entry für MaptileStaticUUID
entryMaptileStaticUUID = Entry(master=tkFenster, bg='white', width='32')
entryMaptileStaticUUID.grid(row=17, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryMaptileStaticUUID,balloonmsg= "MaptileStaticUUID")

# Label mit Aufschrift MaptileStaticFile
labelMaptileStaticFile = Label(master=tkFenster, bg='#FFF070', text='MaptileStaticFile')
labelMaptileStaticFile.grid(row=18, column=0, padx='5', pady='5', sticky='ew')
# Entry für MaptileStaticFile
entryMaptileStaticFile = Entry(master=tkFenster, bg='white', width='32')
entryMaptileStaticFile.grid(row=18, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryMaptileStaticFile,balloonmsg= "MaptileStaticFile")

# Label mit Aufschrift MasterAvatarFirstName
labelMasterAvatarFirstName = Label(master=tkFenster, bg='#FFF070', text='MasterAvatarFirstName')
labelMasterAvatarFirstName.grid(row=19, column=0, padx='5', pady='5', sticky='ew')
# Entry für MasterAvatarFirstName
entryMasterAvatarFirstName = Entry(master=tkFenster, bg='white', width='32')
entryMasterAvatarFirstName.grid(row=19, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryMasterAvatarFirstName,balloonmsg= "MasterAvatarFirstName")

# Label mit Aufschrift MasterAvatarLastName
labelMasterAvatarLastName = Label(master=tkFenster, bg='#FFF070', text='MasterAvatarLastName')
labelMasterAvatarLastName.grid(row=20, column=0, padx='5', pady='5', sticky='ew')
# Entry für MasterAvatarLastName
entryMasterAvatarLastName = Entry(master=tkFenster, bg='white', width='32')
entryMasterAvatarLastName.grid(row=20, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryMasterAvatarLastName,balloonmsg= "MasterAvatarLastName")

# Label mit Aufschrift MasterAvatarSandboxPassword
labelMasterAvatarSandboxPassword = Label(master=tkFenster, bg='#FFF070', text='MasterAvatarSandboxPassword')
labelMasterAvatarSandboxPassword.grid(row=21, column=0, padx='5', pady='5', sticky='ew')
# Entry für MasterAvatarSandboxPassword
entryMasterAvatarSandboxPassword = Entry(master=tkFenster, bg='white', width='32')
entryMasterAvatarSandboxPassword.grid(row=21, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryMasterAvatarSandboxPassword,balloonmsg= "MasterAvatarSandboxPassword")

# Label mit Aufschrift InternalAddress
labelInternalAddress = Label(master=tkFenster, bg='#FFF070', text='InternalAddress')
labelInternalAddress.grid(row=22, column=0, padx='5', pady='5', sticky='ew')
# Entry für InternalAddress
entryInternalAddress = Entry(master=tkFenster, bg='white', width='32')
entryInternalAddress.grid(row=22, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryInternalAddress,balloonmsg= "InternalAddress")

# Label mit Aufschrift Region amount
labelRegionamount = Label(master=tkFenster, bg='#00FFBC', text='Number of regions')
labelRegionamount.grid(row=23, column=0, padx='5', pady='5', sticky='ew')
# Entry für Region amount
entryRegionamount = Entry(master=tkFenster, bg='white', width='32')
entryRegionamount.grid(row=23, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryRegionamount,balloonmsg= "The desired number of regions.")

###################################################################################

# Button zum Erstellen
RegionCreate = Button(master=tkFenster, text='Create', width='22', bg='#FBD975', command=createconfig)
RegionCreate.grid(row=25, column=0, padx='5', pady='5')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(RegionCreate,balloonmsg= "Erstellen der Regionskonfigurationen.")

# Button zum Clear
buttonClear = Button(master=tkFenster, text='Clear', width='10', bg='#FBD975', command=clear_input_field)
buttonClear.grid(row=25, column=1, padx='5', pady='5')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(buttonClear,balloonmsg= "Daten löschen.")

# Button zum Help
buttonHelp = Button(master=tkFenster, text='Help', width='10', bg='#FBD975', command=helping)
buttonHelp.grid(row=25, column=2, padx='5', pady='5')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(buttonHelp,balloonmsg= "Hilfe anfordern.")

# Button zum Abbrechen
buttonExit = Button(master=tkFenster, text='Exit', width='10', bg='#FBD975', command=close_window)
buttonExit.grid(row=25, column=3, padx='5', pady='5')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(buttonExit,balloonmsg= "Programm beenden.")




# Aktivierung des Fensters
tkFenster.mainloop()
