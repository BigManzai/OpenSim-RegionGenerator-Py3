#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#####
# Python 3.8.5
# Dies ist ein Baukasten zum erstellen von OpenSimulator Region Konfigurationsdateien.
# Weitere Informationen zu Regions.ini hier: http://opensimulator.org/wiki/Configuring_Regions
# Dies erstellt auch automatisch Konfigurationsdateien indem es Zufallseintraege nutzt.
# Die Sprachen koennen einfach erweitert werden.
# Im jetzigen zustand funktioniert es noch nicht 100%, es sollte aber dennoch für viele eine grosse Hilfe sein.

import configparser
import uuid
import random
from tkinter import *
from tkinter.tix import * #tkinter Tooltips
from tkinter import messagebox
import random
import gettext

gettext.install('RegionsGen')

### Abschnitt zum testen der einzelnen Sprachen: ###
#lang1 = gettext.translation('RegionsGen', 'locale', languages=['de']) # Nur eine Sprache
#lang2 = gettext.translation('RegionsGen', 'locale', languages=['fr']) # Nur eine Sprache
#lang3 = gettext.translation('RegionsGen', 'locale', languages=['es']) # Nur eine Sprache
#lang4 = gettext.translation('RegionsGen', 'locale', languages=['en']) # Nur eine Sprache
#_ = lang1.gettext
#_ = lang2.gettext
#_ = lang3.gettext
#_ = lang4.gettext

langall = gettext.translation('RegionsGen', 'locale') # Automatische auswahl der Sprache
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
# pyinstaller --windowed --noconsole --onefile RegionGenerator.py C:\Python38\Lib\gettext.py

# TODO: Testen Python NetworkX

# Vari
maplocation = ''
counter = 0
mapsprung = 0
xcounter = 0
ycounter = 0
regionsintnr = 0
mapintcounter = 0

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
    messagebox.showinfo(_("Help"), _("The created region configuration files only need to be moved to the Regions directory.\n\nThen restart the OpenSimulator.\n\nPlease a maximum of 15 standard regions per OpenSimulator when using mySQL.\n\nIf you use mesh on your regions, please drastically reduce the number of regions per OpenSimulator.\n\nIf you use a lot of mesh and scripts, it is better to only use one region per OpenSimulator.\n\nVariable VAR regions should always run individually.\n\nWhen using sqLite you should be careful, a region with around 6000 prims is roughly the limit, after which errors can occur in the database."))
    return;

def close_window(): 
    tkFenster.destroy() # Fenster schiessen

# make a random location, wird nicht mehr aufgerufen und ist nur noch als Information hier.
def randomlocation():
    maplocation = random.randrange(1000, 8000, 4)
    localmap = str(maplocation)
    return localmap;

# Map zusammenbauen
def osmap(mapx, mapy):
    global maplocation
    mapxstr = str(mapx) # int to str
    mapystr = str(mapy) # int to str
    maplocation = mapxstr + ',' + mapystr # zusammenbauen zu Beispiel: 1000,1000
    return maplocation;

# see if the user has entered a value or if it is random.
# TODO: Doppelte vermeiden!!! durch addieren von mapintcounter geloest
def randomport():
    myport = random.randrange(9100, 9999, 4) ++ mapintcounter
    return myport;

# see if the user has entered a value or if it is random.
def randomuuid():
    randomuuid = uuid.uuid4()
    return randomuuid;

# create a config file
def write_region(mapintcounter, regionsintnr):
    config = configparser.ConfigParser()
    global counter, xcounter, ycounter, maplocation

    # capitalization gross- kleinschreibung beachten
    config.optionxform = str

    # generate a uuid for all entries
    ruuid = str(entryRegionUUID.get()) # Holt die Daten aus der Eingabe, hier die RegionUUID.
    if ruuid=='' : ruuid = randomuuid() # Wenn leer dann eine Zufallszahl generieren.

    # InternalPort
    InternalPort = str(entryInternalPort.get()) # Holt die Daten aus der Eingabe, hier der InternalPort.
    if InternalPort=='' : InternalPort = random.randrange(9100, 9999, 4) ++ mapintcounter # Wenn leer dann eine Zufallszahl generieren.

    # MaxPrims
    MaxPrims = str(entryMaxPrims.get()) # Holt die Daten aus der Eingabe, hier MaxPrims.
    if MaxPrims=='' : MaxPrims = '10000' # Wenn leer dann vorgabe verwenden.

    # MaxAgents
    MaxAgents = str(entryMaxAgents.get()) # Holt die Daten aus der Eingabe, hier MaxAgents.
    if MaxAgents=='' : MaxAgents = '20' # Wenn leer dann vorgabe verwenden.

    # AllowAlternatePorts
    AllowAlternatePorts = str(entryAllowAlternatePorts.get()) # Holt die Daten aus der Eingabe
    if AllowAlternatePorts=='' : AllowAlternatePorts = 'False' # Wenn leer dann vorgabe verwenden.

    # ResolveAdress
    ResolveAdress = str(entryResolveAdress.get()) # Holt die Daten aus der Eingabe
    if ResolveAdress=='' : ResolveAdress = 'False' # Wen leer dann vorgabe verwenden.
    # Einstellung ein- ausschalten.
    if checkResolveAdress.get()==0 : checkResolveAdressoff = ';' # Einstellung ein- ausschalten.
    else: checkResolveAdressoff = ''

    # DefaultLanding
    DefaultLanding = str(entryDefaultLanding.get()) # Holt die Daten aus der Eingabe
    if DefaultLanding=='' : DefaultLanding = '128,128,21' # Wenn leer dann vorgabe verwenden.
    # Einstellung ein- ausschalten.
    if checkDefaultLanding.get()==0 : checkDefaultLandingoff = ';' # Einstellung ein- ausschalten.
    else: checkDefaultLandingoff = ''

    # NonPhysicalPrimMax
    NonPhysicalPrimMax = str(entryNonPhysicalPrimMax.get()) # Holt die Daten aus der Eingabe
    if NonPhysicalPrimMax=='' : NonPhysicalPrimMax = '1024' # Wenn leer dann vorgabe verwenden.
    # Einstellung ein- ausschalten.
    if checkNonPhysicalPrimMax.get()==0 : checkNonPhysicalPrimMaxoff = ';' # Einstellung ein- ausschalten.
    else: checkNonPhysicalPrimMaxoff = ''

    # PhysicalPrimMax
    PhysicalPrimMax = str(entryPhysicalPrimMax.get()) # Holt die Daten aus der Eingabe
    if PhysicalPrimMax=='' : PhysicalPrimMax = '64' # Wen leer dann vorgabe verwenden.
    # Einstellung ein- ausschalten.
    if checkPhysicalPrimMax.get()==0 : checkPhysicalPrimMaxoff = ';' # Einstellung ein- ausschalten.
    else: checkPhysicalPrimMaxoff = ''
    
    # ClampPrimSize
    ClampPrimSize = str(entryClampPrimSize.get()) # Holt die Daten aus der Eingabe
    if ClampPrimSize=='' : ClampPrimSize = 'False' # Wenn leer dann vorgabe verwenden.
    # Einstellung ein- ausschalten.
    if checkClampPrimSize.get()==0 : checkClampPrimSizeoff = ';' # Einstellung ein- ausschalten.
    else: checkClampPrimSizeoff = ''

    # MaxPrimsPerUser
    MaxPrimsPerUser = str(entryMaxPrimsPerUser.get()) # Holt die Daten aus der Eingabe
    if MaxPrimsPerUser=='' : MaxPrimsPerUser = '-1' # Wenn leer dann vorgabe verwenden.
    # Einstellung ein- ausschalten.
    if checkMaxPrimsPerUser.get()==0 : checkMaxPrimsPerUseroff = ';' # Einstellung ein- ausschalten.
    else: checkMaxPrimsPerUseroff = ''

    # ScopeID
    ScopeID = str(entryScopeID.get()) # Holt die Daten aus der Eingabe
    if ScopeID=='' : ScopeID = ruuid # Wen leer dann vorgabe verwenden.
    # Einstellung ein- ausschalten.
    if checkScopeID.get()==0 : checkScopeIDoff = ';' # Einstellung ein- ausschalten.
    else: checkScopeIDoff = ''

    # RegionType
    RegionType = str(entryRegionType.get()) # Holt die Daten aus der Eingabe
    if RegionType=='' : RegionType = 'Mainland' # Wenn leer dann vorgabe verwenden.
    # Einstellung ein- ausschalten.
    if checkRegionType.get()==0 : checkRegionTypeoff = ';' # Einstellung ein- ausschalten.
    else: checkRegionTypeoff = ''

    #entryMaptileStaticUUID
    MaptileStaticUUID = str(entryMaptileStaticUUID.get()) # Holt die Daten aus der Eingabe
    if MaptileStaticUUID=='' : MaptileStaticUUID = ruuid # Wenn leer dann vorgabe verwenden.
    # Einstellung ein- ausschalten.
    if checkMaptileStaticUUID.get()==0 : checkMaptileStaticUUIDoff = ';' # Einstellung ein- ausschalten.
    else: checkMaptileStaticUUIDoff = ''

    # MaptileStaticFile
    MaptileStaticFile = str(entryMaptileStaticFile.get()) # Holt die Daten aus der Eingabe
    if MaptileStaticFile=='' : MaptileStaticFile = '"water.jpg"' # Wenn leer dann vorgabe verwenden.
    # Einstellung ein- ausschalten.
    if checkMaptileStaticFile.get()==0 : checkMaptileStaticFileoff = ';' # Einstellung ein- ausschalten.
    else: checkMaptileStaticFileoff = ''

    # MasterAvatarFirstName
    MasterAvatarFirstName = str(entryMasterAvatarFirstName.get()) # Holt die Daten aus der Eingabe
    if MasterAvatarFirstName=='' : MasterAvatarFirstName = 'John' # Wenn leer dann vorgabe verwenden.
    # Einstellung ein- ausschalten.
    if checkMasterAvatarFirstName.get()==0 : checkMasterAvatarFirstNameoff = ';' # Einstellung ein- ausschalten.
    else: checkMasterAvatarFirstNameoff = ''

    # MasterAvatarLastName
    MasterAvatarLastName = str(entryMasterAvatarLastName.get()) # Holt die Daten aus der Eingabe
    if MasterAvatarLastName=='' : MasterAvatarLastName = 'Doe' # Wenn leer dann vorgabe verwenden.
    # Einstellung ein- ausschalten.
    if checkMasterAvatarLastName.get()==0 : checkMasterAvatarLastNameoff = ';' # Einstellung ein- ausschalten.
    else: checkMasterAvatarLastNameoff = ''

    # MasterAvatarSandboxPassword
    MasterAvatarSandboxPassword = str(entryMasterAvatarSandboxPassword.get()) # Holt die Daten aus der Eingabe
    if MasterAvatarSandboxPassword=='' : MasterAvatarSandboxPassword = 'passwd' # Wenn leer dann vorgabe verwenden.
    # Einstellung ein- ausschalten.
    if checkMasterAvatarSandboxPassword.get()==0 : checkMasterAvatarSandboxPasswordoff = ';' # Einstellung ein- ausschalten.
    else: checkMasterAvatarSandboxPasswordoff = ''

    # InternalAddress
    InternalAddress = str(entryInternalAddress.get()) # Holt die Daten aus der Eingabe
    if InternalAddress =='' : InternalAddress = "0.0.0.0" # Wenn leer dann vorgabe verwenden.
    # Einstellung ein- ausschalten.
    if checkResolveAdress.get()==0 : checkResolveAdressoff = ';' # Einstellung ein- ausschalten.
    else: checkResolveAdressoff = ''

    # ExternalHostName
    ExternalHostName = str(entryExternalHostName.get()) # Holt die Daten aus der Eingabe, hier ExternalHostName.
    if ExternalHostName =='' : ExternalHostName = "SYSTEMIP" # Wenn leer dann vorgabe verwenden.

    # mapliste: 0 = mapx, 1 = mapy, 2 = mapsprung var
    mapliste = ["0", "1", "2"] # ich benutze hier eine liste zum konvertieren von string und integer weil ich sonst probleme von str nach int habe

    # Size
    Size_var = entrySize.get() # Holt die Daten aus der Eingabe, hier Size.
    if Size_var=='' : Size_var = "256"
    mapliste[2] = Size_var # listeneintrag 2 ueberschreiben zum konvertieren von str to int
    mapsprung = int(mapliste[2])//256 # beruecksichtigung von var regionen / = teilen mit komma // = teilen ohne komma - Beispiele: 1 = 256 single region ... 4 = var region 1024

    # assemble region location
    maplocationx = entryLocationx.get() # Holt den string aus der Eingabe, hier die maplocation.
    maplocationy = entryLocationy.get() # Holt den string aus der Eingabe, hier die maplocation.

    if maplocationx =='' : maplocationx = random.randrange(1000, 8000, 4) # Zufallszahl generieren
    if maplocationy =='' : maplocationy = random.randrange(1000, 8000, 4) # Zufallszahl generieren

    mapliste[0] = maplocationx # listeneintrag 0 ueberschreiben
    mapliste[1] = maplocationy # listeneintrag 1 ueberschreiben

    maplocationxinteger = int(mapliste[0]) # listeneintrag 0 als integer speichern
    maplocationyinteger = int(mapliste[1]) # listeneintrag 1 als integer speichern

    ### Aneinanderreien von Regionen als Block ohne random.
    if mapintcounter == 0: osmap(maplocationxinteger + 0,maplocationyinteger + 0)
    if mapintcounter == 1: osmap(maplocationxinteger + 1,maplocationyinteger + 0)
    if mapintcounter == 6: osmap(maplocationxinteger + 2,maplocationyinteger + 0)
    if mapintcounter == 12: osmap(maplocationxinteger + 3,maplocationyinteger + 0)
    if mapintcounter == 20: osmap(maplocationxinteger + 4,maplocationyinteger + 0)
    if mapintcounter == 30: osmap(maplocationxinteger + 5,maplocationyinteger + 0)
    if mapintcounter == 42: osmap(maplocationxinteger + 6,maplocationyinteger + 0)

    if mapintcounter == 2: osmap(maplocationxinteger + 0,maplocationyinteger + 1)
    if mapintcounter == 3: osmap(maplocationxinteger + 1,maplocationyinteger + 1)
    if mapintcounter == 7: osmap(maplocationxinteger + 2,maplocationyinteger + 1)
    if mapintcounter == 13: osmap(maplocationxinteger + 3,maplocationyinteger + 1)
    if mapintcounter == 21: osmap(maplocationxinteger + 4,maplocationyinteger + 1)
    if mapintcounter == 31: osmap(maplocationxinteger + 5,maplocationyinteger + 1)
    if mapintcounter == 43: osmap(maplocationxinteger + 6,maplocationyinteger + 1)

    if mapintcounter == 4: osmap(maplocationxinteger + 0,maplocationyinteger + 2)
    if mapintcounter == 5: osmap(maplocationxinteger + 1,maplocationyinteger + 2)
    if mapintcounter == 8: osmap(maplocationxinteger + 2,maplocationyinteger + 2)
    if mapintcounter == 14: osmap(maplocationxinteger + 3,maplocationyinteger + 2)
    if mapintcounter == 22: osmap(maplocationxinteger + 4,maplocationyinteger + 2)
    if mapintcounter == 32: osmap(maplocationxinteger + 5,maplocationyinteger + 2)
    if mapintcounter == 44: osmap(maplocationxinteger + 6,maplocationyinteger + 2)

    if mapintcounter == 9: osmap(maplocationxinteger + 0,maplocationyinteger + 3)
    if mapintcounter == 10: osmap(maplocationxinteger + 1,maplocationyinteger + 3)
    if mapintcounter == 11: osmap(maplocationxinteger + 2,maplocationyinteger + 3)
    if mapintcounter == 15: osmap(maplocationxinteger + 3,maplocationyinteger + 3)
    if mapintcounter == 23: osmap(maplocationxinteger + 4,maplocationyinteger + 3)
    if mapintcounter == 33: osmap(maplocationxinteger + 5,maplocationyinteger + 3)
    if mapintcounter == 45: osmap(maplocationxinteger + 6,maplocationyinteger + 3)

    if mapintcounter == 16: osmap(maplocationxinteger + 0,maplocationyinteger + 4)
    if mapintcounter == 17: osmap(maplocationxinteger + 1,maplocationyinteger + 4)
    if mapintcounter == 18: osmap(maplocationxinteger + 2,maplocationyinteger + 4)
    if mapintcounter == 19: osmap(maplocationxinteger + 3,maplocationyinteger + 4)
    if mapintcounter == 24: osmap(maplocationxinteger + 4,maplocationyinteger + 4)
    if mapintcounter == 34: osmap(maplocationxinteger + 5,maplocationyinteger + 4)
    if mapintcounter == 46: osmap(maplocationxinteger + 6,maplocationyinteger + 4)

    if mapintcounter == 25: osmap(maplocationxinteger + 0,maplocationyinteger + 5)
    if mapintcounter == 26: osmap(maplocationxinteger + 1,maplocationyinteger + 5)
    if mapintcounter == 27: osmap(maplocationxinteger + 2,maplocationyinteger + 5)
    if mapintcounter == 28: osmap(maplocationxinteger + 3,maplocationyinteger + 5)
    if mapintcounter == 29: osmap(maplocationxinteger + 4,maplocationyinteger + 5)
    if mapintcounter == 35: osmap(maplocationxinteger + 5,maplocationyinteger + 5)
    if mapintcounter == 47: osmap(maplocationxinteger + 6,maplocationyinteger + 5)

    if mapintcounter == 36: osmap(maplocationxinteger + 0,maplocationyinteger + 6)
    if mapintcounter == 37: osmap(maplocationxinteger + 1,maplocationyinteger + 6)
    if mapintcounter == 38: osmap(maplocationxinteger + 2,maplocationyinteger + 6)
    if mapintcounter == 39: osmap(maplocationxinteger + 3,maplocationyinteger + 6)
    if mapintcounter == 40: osmap(maplocationxinteger + 4,maplocationyinteger + 6)
    if mapintcounter == 41: osmap(maplocationxinteger + 5,maplocationyinteger + 6)
    if mapintcounter == 48: osmap(maplocationxinteger + 6,maplocationyinteger + 6)

    if mapintcounter == 49: osmap(maplocationxinteger + 0,maplocationyinteger + 7)
    if mapintcounter == 50: osmap(maplocationxinteger + 1,maplocationyinteger + 7)
    if mapintcounter == 51: osmap(maplocationxinteger + 2,maplocationyinteger + 7)
    if mapintcounter == 52: osmap(maplocationxinteger + 3,maplocationyinteger + 7)
    if mapintcounter == 53: osmap(maplocationxinteger + 4,maplocationyinteger + 7)
    if mapintcounter == 54: osmap(maplocationxinteger + 5,maplocationyinteger + 7)
    if mapintcounter == 55: osmap(maplocationxinteger + 6,maplocationyinteger + 7)

    # 55 Reihen als Block sind fertig. LibreOffice Calc hat das so sortiert.


    # Ab 56 einfach den counter erhoehen.
    if mapintcounter >= 56: # Ist der counter = 0 die angegebene Position nutzen, ansonsten zaehler unter beruecksichtigung der Regionsgroesse hochsetzen.
        if mapintcounter % 2:
            # ist der counter ungrade, localisation x zaehler hoch setzen

            #maplocationxinteger += counter # vor der beruecksichtigung der var groesse
            maplocationxinteger += mapintcounter # vor der beruecksichtigung der var groesse    

            if mapsprung > 1: maplocationxinteger += mapsprung # nach der beruecksichtigung der var groesse
            osmap(maplocationxinteger, maplocationyinteger) # Neu map Beispiel: map(1000, 1000) ergibt eine variable string mit dem inhalt 1000,1000 die direkt in die config geschrieben werden kann.
            #print(mapintcounter, regionsintnr)
        else: 
            # oder ist der counter grade, localisation y zaehler hoch setzen
            #maplocationyinteger += counter # vor der beruecksichtigung der var groesse
            maplocationyinteger += mapintcounter # vor der beruecksichtigung der var groesse
            if mapsprung > 1: maplocationyinteger += mapsprung # nach der beruecksichtigung der var groesse
            osmap(maplocationxinteger, maplocationyinteger) # Neu map Beispiel: map(1000, 1000) ergibt eine variable string mit dem inhalt 1000,1000 die direkt in die config geschrieben werden kann.
            #print(mapintcounter, regionsintnr)

    # region name
    regionname = entryRegionName.get() # Holt die Daten aus der Eingabe, hier regionname.
    # Ist der Regionsname bereits vergeben dann Zahlen an den Regionsnamen anhaengen.
    if regionname =='' : 
        regionname = randomname()
        regionnameout = regionname
    else:
        regionnameout = regionname + ' ' + str(mapintcounter)
        #counter += 1

    # Leerzeichen durch unterstriche austauschen denn leerzeichen sind im Dateinamen nicht erlaubt.
    confdatei = regionnameout.replace(" ", "_")

    # Konfiguration erstellen.
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
                          checkDefaultLandingoff + 'DefaultLanding': '<' + DefaultLanding + '>',
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

    with open(confdatei + '.ini', 'w') as configfile: config.write(configfile)

def createconfig():
    i=0
    n = int(entryRegionamount.get()) # Holt die Daten aus der Eingabe, hier die Menge der Regionen.

    for i in range(i, n):
	    write_region(mapintcounter = i, regionsintnr = n)
    else:
	    return mapintcounter, regionsintnr;

def clear_input_field():
   global counter, mapsprung, xcounter, ycounter
   counter = 0
   xcounter = 0
   ycounter = 0
   mapsprung = 0
   # Entry clear
   entryRegionName.delete(0, END)
   entryLocationx.delete(0, END)
   entryLocationy.delete(0, END)
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
#tkFenster.geometry("800x850+937+134") # Groesse des Fensters vorgeben.

# Rot #FFCFC9 - Gruen #00FFBC - Gelb #FFF070

# Label mit Aufschrift RegionName
labelRegionName = Label(master=tkFenster, bg='#F9CDAD', text=_('Region Name'))
labelRegionName.grid(row=0, column=0, padx='5', pady='5', sticky='ew')
# Entry für RegionName
entryRegionName = Entry(master=tkFenster, bg='white', width='32')
entryRegionName.grid(row=0, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryRegionName,balloonmsg= _("insert region name\nexample: My Virtual Land\nblank creates a random."))

# Label mit Aufschrift Location
labelLocation = Label(master=tkFenster, bg='#F9CDAD', text=_('Location'))
labelLocation.grid(row=1, column=0, padx='5', pady='5', sticky='ew')
# Entry für Location
entryLocationx = Entry(master=tkFenster, bg='white', width='32')
entryLocationx.grid(row=1, column=1, padx='5', pady='5', sticky='w')
entryLocationy = Entry(master=tkFenster, bg='white', width='32')
entryLocationy.grid(row=1, column=2, padx='5', pady='5', sticky='w')

balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryLocationx,balloonmsg= _("Location x\nexample: 5000\nblank creates a random."))
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryLocationy,balloonmsg= _("Location y\nexample: 5000\nblank creates a random."))

# Label mit Aufschrift RegionUUID
labelRegionUUID = Label(master=tkFenster, bg='#F9CDAD', text=_('Region UUID'))
labelRegionUUID.grid(row=2, column=0, padx='5', pady='5', sticky='ew')
# Entry für RegionUUID
entryRegionUUID = Entry(master=tkFenster, bg='white', width='32')
entryRegionUUID.grid(row=2, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryRegionUUID,balloonmsg= _("Region UUID\nblank creates a random."))

# Label mit Aufschrift Size
labelSize = Label(master=tkFenster, bg='#F9CDAD', text=_('Size'))
labelSize.grid(row=3, column=0, padx='5', pady='5', sticky='ew')
# Entry für Size
entrySize = Entry(master=tkFenster, bg='white', width='32')
entrySize.grid(row=3, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entrySize,balloonmsg= _("If size is not specified it will\ndefault to the legacy size of 256.\nblank creates 256."))

# Label mit Aufschrift InternalAddress
labelInternalAddress = Label(master=tkFenster, bg='#F9CDAD', text=_('Internal Address'))
labelInternalAddress.grid(row=4, column=0, padx='5', pady='5', sticky='ew')
# Entry für InternalAddress
entryInternalAddress = Entry(master=tkFenster, bg='white', width='32')
entryInternalAddress.grid(row=4, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryInternalAddress,balloonmsg= _("Internal Address\nstandard: 0.0.0.0"))

# Label mit Aufschrift InternalPort
labelInternalPort = Label(master=tkFenster, bg='#F9CDAD', text=_('Internal Port'))
labelInternalPort.grid(row=5, column=0, padx='5', pady='5', sticky='ew')
# Entry für InternalPort
entryInternalPort = Entry(master=tkFenster, bg='white', width='32')
entryInternalPort.grid(row=5, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryInternalPort,balloonmsg= _("IP port for all incoming client connections.\nBlank creates a random."))

# Label mit Aufschrift AllowAlternatePorts
labelAllowAlternatePorts = Label(master=tkFenster, bg='#F9CDAD', text=_('Allow Alternate Ports'))
labelAllowAlternatePorts.grid(row=6, column=0, padx='5', pady='5', sticky='ew')
# Entry für AllowAlternatePorts
entryAllowAlternatePorts = Entry(master=tkFenster, bg='white', width='32')
entryAllowAlternatePorts.grid(row=6, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryAllowAlternatePorts,balloonmsg= _("AllowAlternatePorts Not Used.\nLeave it always False."))

# Label mit Aufschrift ExternalHostName
labelExternalHostName = Label(master=tkFenster, bg='#F9CDAD', text=_('External Host Name'))
labelExternalHostName.grid(row=7, column=0, padx='5', pady='5', sticky='ew')
# Entry für ExternalHostName
entryExternalHostName = Entry(master=tkFenster, bg='white', width='32')
entryExternalHostName.grid(row=7, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryExternalHostName,balloonmsg= _("External IP Address of the router or FQDN.\n(must be the same for all regions on file)\nBlank creates SYSTEMIP"))

# Label mit Aufschrift MaxPrims
labelMaxPrims = Label(master=tkFenster, bg='#F9CDAD', text=_('Max Prims'))
labelMaxPrims.grid(row=8, column=0, padx='5', pady='5', sticky='ew')
# Entry für MaxPrims
entryMaxPrims = Entry(master=tkFenster, bg='white', width='32')
entryMaxPrims.grid(row=8, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryMaxPrims,balloonmsg= _("The maximum number of prims that the region will be listed as supporting.\nHowever, this limit is not currently enforced by OpenSimulator.\nDue to LL protocol constraints,\nthe maximum limit that can be shown is 45000."))

# Label mit Aufschrift MaxAgents
labelMaxAgents = Label(master=tkFenster, bg='#F9CDAD', text=_('Max Agents'))
labelMaxAgents.grid(row=9, column=0, padx='5', pady='5', sticky='ew')
# Entry für MaxAgents
entryMaxAgents = Entry(master=tkFenster, bg='white', width='32')
entryMaxAgents.grid(row=9, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryMaxAgents,balloonmsg= _("The maximum number of agents that can be in the in the region at any given time."))

# Label mit Aufschrift DefaultLanding
labelDefaultLanding = Label(master=tkFenster, bg='#F9CDAD', text=_('Default Landing'))
labelDefaultLanding.grid(row=10, column=0, padx='5', pady='5', sticky='ew')
# Entry für DefaultLanding
entryDefaultLanding = Entry(master=tkFenster, bg='white', width='32')
entryDefaultLanding.grid(row=10, column=1, padx='5', pady='5', sticky='ew')
balloon = Balloon(tkFenster,bg="white", title="Help")
balloon.bind_widget(entryDefaultLanding,balloonmsg= _("Default Landing\nexample: 128,128,21"))
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
balloon.bind_widget(entryNonPhysicalPrimMax,balloonmsg= _("The maximum dimensions for a non-physical prim.\nThis is a single number which applies to X, Y and Z co-ordinates.\nThis will affect resizing of existing prims. Default is 256.\nThis setting can also be used in the [Startup] section of OpenSim.ini.\nIf the region setting exists then it will override the OpenSim.ini setting."))
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
balloon.bind_widget(entryPhysicalPrimMax,balloonmsg= _("The maximum dimensions of a physical prim. This is a single number which applies to X, Y and Z co-ordinates.\nThis will affect resizing of existing prims. Default is 10.\nThis setting can also be used in the [Startup] section of OpenSim.ini.\nIf the region setting exists then it will override the OpenSim.ini setting."))
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
balloon.bind_widget(entryClampPrimSize,balloonmsg= _("If true then if a viewer attempts to create a prim which has any dimension larger than the NonphysicalPrimMax,\nthen that dimension is reduced to NonphysicalPrimMax.\nDefault is false; This setting can also be used in the [Startup] section of OpenSim.ini.\nIf the region setting exists then it will override the OpenSim.ini setting."))
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
balloon.bind_widget(entryMaxPrimsPerUser,balloonmsg= _("Number of prims that each user has available."))
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
balloon.bind_widget(entryRegionType,balloonmsg= _("The region type as shown in the Covenant tab of the Region/Estate dialog in a standard Second Life viewer.\nCan be used to specify Mainland, Estate, etc. based on type of grid."))
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
balloon.bind_widget(entryMaptileStaticUUID,balloonmsg= _("UUID of texture to use as a maptile for this region.\nOnly set if you have disabled dynamic generation of the map tile from the region contents."))
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
balloon.bind_widget(entryMasterAvatarFirstName,balloonmsg= _("Master Avatar First Name"))
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

# Label als Platzhalter zu den Buttons
labelRegionamount = Label(master=tkFenster, text=' ')
labelRegionamount.grid(row=24, column=0, padx='5', pady='5', sticky='ew')

################################# Buttons ##################################################

# Button zum Erstellen
RegionCreate = Button(master=tkFenster, text=_('Create'), width='22', bg='#00FFBC', command=createconfig)
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