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
import random_name_def
import tkinter as tk
import tkinter.ttk as ttk
import gettext

gettext.install('RegionsGen')
lang1 = gettext.translation('RegionsGen', 'locale', languages=['de']) # Nur eine Sprache
_ = lang1.gettext

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

### Variable ###
top_level = ""
root = ""
val = ""
w_win = ""

### Variable Voreinstellung ###
Size_var = "256"
InternalAddress_var = "0.0.0.0"
InternalPort_var = "Random"
AllowAlternatePorts_var = "False"
ResolveAddress_var = "off"
ExternalHostName_var = "SYSTEMIP"
MaxPrims_var = "off"
MaxAgents_var = "40"
DefaultLanding_var = "off"
NonPhysicalPrimMax_var = "off"
PhysicalPrimMax_var = "off"
ClampPrimSize_var = "off"
MaxPrimsPerUser_var = "off"
ScopeID_var = "off"
RegionType_var = "off"
MaptileStaticUUID_var = "Random"
MaptileStaticFile_var = "off"
MasterAvatarFirstName_var = "off"
MasterAvatarLastName_var = "off"
MasterAvatarSandboxPassword_var = "off"
Create_var = ""
Quit_var = ""
RegionAmount_var = ""
RegionName_var = "Random"
LocationX_var = "Random"
LocationY_var = "Random"
RegionUUID_var = "Random"

# Hmm
regionnameout = ""
off = ";"

######################################################
########## Ultra Region Generator Funktionen #########
######################################################

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
    maplocation = randomlocation() + ',' + randomlocation()

    # capitalization gross- kleinschreibung beachten
    config.optionxform = str

    # any name
    regionname = random_name_def.randomname();
    regionnameout = random_name_def.randomname();

    # generate a uuid for all entries
    ruuid = randomuuid()

    # Change space to subline for the filename
    confdatei = regionnameout.replace(" ", "_")
    
    #'RegionUUID': ruuid
    #RegionUUID_var2 = "'RegionUUID'" + ":" + ruuid
    #InternalPort_var = randomport()
    
    config[regionnameout] = {'RegionUUID': ruuid,
                          'Location': maplocation,
                          'SizeX': Size_var,
                          'SizeY': Size_var,
                          'SizeZ': Size_var,
                          'InternalAddress': InternalAddress_var,
                          'InternalPort': randomport(),
                          'AllowAlternatePorts': 'False',
                          'ResolveAddress': 'False',
                          'ExternalHostName': ExternalHostName_var,
                          'MaxPrims': '100000',
                          'MaxAgents': '50',
                          ';DefaultLanding': '<128,128,21>',
                          ';NonPhysicalPrimMax': '1024',
                          ';PhysicalPrimMax': '64',
                          ';ClampPrimSize': 'False',
                          ';MaxPrimsPerUser': '-1',
                          ';ScopeID': ruuid,
                          ';RegionType': 'Mainland',
                          'MaptileStaticUUID': ruuid,
                          ';MaptileStaticFile': '"water.jpg"',
                          ';MasterAvatarFirstName': 'John',
                          ';MasterAvatarLastName': 'Doe',
                          ';MasterAvatarSandboxPassword': 'passwd'}

    with open(confdatei + '.ini', 'w') as configfile: config.write(configfile)


######################################################
############ Ultra Region Generator UI ###############
######################################################

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    root.iconbitmap('opensim.ico')
    top = Toplevel1 (root)
    init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    #set_Tk_var()
    top = Toplevel1 (w)
    init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("800x850+937+134")
        top.minsize(176, 1)
        top.maxsize(6724, 1590)
        top.resizable(1, 1)
        top.title("Ultimate Region Generator")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

### label ###
        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.013, rely=0.010, height=38, width=252)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='nw')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(justify='left')
        self.Label1.configure(text='''Region Name''')
        self.tooltip_font = "TkDefaultFont"
        self.Label1_tooltip = \
        ToolTip(self.Label1, self.tooltip_font, _('''Region Name'''))

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.013, rely=0.040, height=38, width=252)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='nw')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(justify='left')
        self.Label2.configure(text='''Location''')
        self.tooltip_font = "TkDefaultFont"
        self.Label2_tooltip = \
        ToolTip(self.Label2, self.tooltip_font, _('''Location'''))

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.013, rely=0.070, height=38, width=104)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(anchor='nw')
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(justify='left')
        self.Label4.configure(text='''RegionUUID''')
        self.tooltip_font = "TkDefaultFont"
        self.Label4_tooltip = \
        ToolTip(self.Label4, self.tooltip_font, _('''RegionUUID'''))

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.013, rely=0.100, height=38, width=252)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(anchor='nw')
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(justify='left')
        self.Label3.configure(text='''Size''')
        self.tooltip_font = "TkDefaultFont"
        self.Label3_tooltip = \
        ToolTip(self.Label3, self.tooltip_font, _('''Size'''))

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.013, rely=0.137, height=38, width=152)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(anchor='nw')
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(justify='left')
        self.Label6.configure(text='''InternalPort''')
        self.tooltip_font = "TkDefaultFont"
        self.Label6_tooltip = \
        ToolTip(self.Label6, self.tooltip_font, _('''InternalPort'''))

        self.Label7 = tk.Label(top)
        self.Label7.place(relx=0.013, rely=0.211, height=38, width=252)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(anchor='nw')
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(justify='left')
        self.Label7.configure(text='''AllowAlternatePorts''')
        self.tooltip_font = "TkDefaultFont"
        self.Label7_tooltip = \
        ToolTip(self.Label7, self.tooltip_font, _('''AllowAlternatePorts'''))

        self.Label8 = tk.Label(top)
        self.Label8.place(relx=0.013, rely=0.242, height=37, width=152)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(anchor='nw')
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(justify='left')
        self.Label8.configure(text='''ResolveAddress''')
        self.tooltip_font = "TkDefaultFont"
        self.Label8_tooltip = \
        ToolTip(self.Label8, self.tooltip_font, _('''ResolveAddress'''))

        self.Label10 = tk.Label(top)
        self.Label10.place(relx=0.013, rely=0.168, height=38, width=152)
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(activeforeground="black")
        self.Label10.configure(anchor='nw')
        self.Label10.configure(background="#d9d9d9")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(highlightbackground="#d9d9d9")
        self.Label10.configure(highlightcolor="black")
        self.Label10.configure(justify='left')
        self.Label10.configure(text='''ExternalHostName''')
        self.tooltip_font = "TkDefaultFont"
        self.Label10_tooltip = \
        ToolTip(self.Label10, self.tooltip_font, _('''ExternalHostName'''))

        self.Label11 = tk.Label(top)
        self.Label11.place(relx=0.013, rely=0.284, height=38, width=152)
        self.Label11.configure(activebackground="#f9f9f9")
        self.Label11.configure(activeforeground="black")
        self.Label11.configure(anchor='nw')
        self.Label11.configure(background="#d9d9d9")
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(highlightbackground="#d9d9d9")
        self.Label11.configure(highlightcolor="black")
        self.Label11.configure(justify='left')
        self.Label11.configure(text='''MaxPrims''')
        self.tooltip_font = "TkDefaultFont"
        self.Label11_tooltip = \
        ToolTip(self.Label11, self.tooltip_font, _('''MaxPrims'''))

        self.Label12 = tk.Label(top)
        self.Label12.place(relx=0.013, rely=0.316, height=37, width=152)
        self.Label12.configure(activebackground="#f9f9f9")
        self.Label12.configure(activeforeground="black")
        self.Label12.configure(anchor='nw')
        self.Label12.configure(background="#d9d9d9")
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(highlightbackground="#d9d9d9")
        self.Label12.configure(highlightcolor="black")
        self.Label12.configure(justify='left')
        self.Label12.configure(text='''MaxAgents''')
        self.tooltip_font = "TkDefaultFont"
        self.Label12_tooltip = \
        ToolTip(self.Label12, self.tooltip_font, _('''MaxAgents'''))

        self.Label13 = tk.Label(top)
        self.Label13.place(relx=0.013, rely=0.347, height=38, width=152)
        self.Label13.configure(activebackground="#f9f9f9")
        self.Label13.configure(activeforeground="black")
        self.Label13.configure(anchor='nw')
        self.Label13.configure(background="#d9d9d9")
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(foreground="#000000")
        self.Label13.configure(highlightbackground="#d9d9d9")
        self.Label13.configure(highlightcolor="black")
        self.Label13.configure(text='''DefaultLanding''')
        self.tooltip_font = "TkDefaultFont"
        self.Label13_tooltip = \
        ToolTip(self.Label13, self.tooltip_font, _('''DefaultLanding'''))

        self.Label14 = tk.Label(top)
        self.Label14.place(relx=0.013, rely=0.4, height=37, width=200)
        self.Label14.configure(activebackground="#f9f9f9")
        self.Label14.configure(activeforeground="black")
        self.Label14.configure(anchor='nw')
        self.Label14.configure(background="#d9d9d9")
        self.Label14.configure(disabledforeground="#a3a3a3")
        self.Label14.configure(foreground="#000000")
        self.Label14.configure(highlightbackground="#d9d9d9")
        self.Label14.configure(highlightcolor="black")
        self.Label14.configure(justify='left')
        self.Label14.configure(text='''NonPhysicalPrimMax''')
        self.tooltip_font = "TkDefaultFont"
        self.Label14_tooltip = \
        ToolTip(self.Label14, self.tooltip_font, _('''NonPhysicalPrimMax'''))

        self.Label15 = tk.Label(top)
        self.Label15.place(relx=0.013, rely=0.432, height=38, width=200)
        self.Label15.configure(activebackground="#f9f9f9")
        self.Label15.configure(activeforeground="black")
        self.Label15.configure(anchor='nw')
        self.Label15.configure(background="#d9d9d9")
        self.Label15.configure(disabledforeground="#a3a3a3")
        self.Label15.configure(foreground="#000000")
        self.Label15.configure(highlightbackground="#d9d9d9")
        self.Label15.configure(highlightcolor="black")
        self.Label15.configure(justify='left')
        self.Label15.configure(text='''PhysicalPrimMax''')
        self.tooltip_font = "TkDefaultFont"
        self.Label15_tooltip = \
        ToolTip(self.Label15, self.tooltip_font, _('''PhysicalPrimMax'''))

        self.Label16 = tk.Label(top)
        self.Label16.place(relx=0.013, rely=0.463, height=38, width=200)
        self.Label16.configure(activebackground="#f9f9f9")
        self.Label16.configure(activeforeground="black")
        self.Label16.configure(anchor='nw')
        self.Label16.configure(background="#d9d9d9")
        self.Label16.configure(disabledforeground="#a3a3a3")
        self.Label16.configure(foreground="#000000")
        self.Label16.configure(highlightbackground="#d9d9d9")
        self.Label16.configure(highlightcolor="black")
        self.Label16.configure(justify='left')
        self.Label16.configure(text='''ClampPrimSize''')
        self.tooltip_font = "TkDefaultFont"
        self.Label16_tooltip = \
        ToolTip(self.Label16, self.tooltip_font, _('''ClampPrimSize'''))

        self.Label17 = tk.Label(top)
        self.Label17.place(relx=0.013, rely=0.495, height=38, width=200)
        self.Label17.configure(activebackground="#f9f9f9")
        self.Label17.configure(activeforeground="black")
        self.Label17.configure(anchor='nw')
        self.Label17.configure(background="#d9d9d9")
        self.Label17.configure(disabledforeground="#a3a3a3")
        self.Label17.configure(foreground="#000000")
        self.Label17.configure(highlightbackground="#d9d9d9")
        self.Label17.configure(highlightcolor="black")
        self.Label17.configure(justify='left')
        self.Label17.configure(text='''MaxPrimsPerUser''')
        self.tooltip_font = "TkDefaultFont"
        self.Label17_tooltip = \
        ToolTip(self.Label17, self.tooltip_font, _('''MaxPrimsPerUser'''))

        self.Label18 = tk.Label(top)
        self.Label18.place(relx=0.013, rely=0.526, height=37, width=200)
        self.Label18.configure(activebackground="#f9f9f9")
        self.Label18.configure(activeforeground="black")
        self.Label18.configure(anchor='nw')
        self.Label18.configure(background="#d9d9d9")
        self.Label18.configure(disabledforeground="#a3a3a3")
        self.Label18.configure(foreground="#000000")
        self.Label18.configure(highlightbackground="#d9d9d9")
        self.Label18.configure(highlightcolor="black")
        self.Label18.configure(justify='left')
        self.Label18.configure(text='''ScopeID''')
        self.tooltip_font = "TkDefaultFont"
        self.Label18_tooltip = \
        ToolTip(self.Label18, self.tooltip_font, _('''ScopeID'''))

        self.Label19 = tk.Label(top)
        self.Label19.place(relx=0.013, rely=0.558, height=38, width=200)
        self.Label19.configure(activebackground="#f9f9f9")
        self.Label19.configure(activeforeground="black")
        self.Label19.configure(anchor='nw')
        self.Label19.configure(background="#d9d9d9")
        self.Label19.configure(disabledforeground="#a3a3a3")
        self.Label19.configure(foreground="#000000")
        self.Label19.configure(highlightbackground="#d9d9d9")
        self.Label19.configure(highlightcolor="black")
        self.Label19.configure(justify='left')
        self.Label19.configure(text='''RegionType''')
        self.tooltip_font = "TkDefaultFont"
        self.Label19_tooltip = \
        ToolTip(self.Label19, self.tooltip_font, _('''RegionType'''))

        self.Label20 = tk.Label(top)
        self.Label20.place(relx=0.013, rely=0.589, height=37, width=200)
        self.Label20.configure(activebackground="#f9f9f9")
        self.Label20.configure(activeforeground="black")
        self.Label20.configure(anchor='nw')
        self.Label20.configure(background="#d9d9d9")
        self.Label20.configure(disabledforeground="#a3a3a3")
        self.Label20.configure(foreground="#000000")
        self.Label20.configure(highlightbackground="#d9d9d9")
        self.Label20.configure(highlightcolor="black")
        self.Label20.configure(justify='left')
        self.Label20.configure(text='''MaptileStaticUUID''')
        self.tooltip_font = "TkDefaultFont"
        self.Label20_tooltip = \
        ToolTip(self.Label20, self.tooltip_font, _('''MaptileStaticUUID'''))

        self.Label21 = tk.Label(top)
        self.Label21.place(relx=0.013, rely=0.621, height=38, width=200)
        self.Label21.configure(activebackground="#f9f9f9")
        self.Label21.configure(activeforeground="black")
        self.Label21.configure(anchor='nw')
        self.Label21.configure(background="#d9d9d9")
        self.Label21.configure(disabledforeground="#a3a3a3")
        self.Label21.configure(foreground="#000000")
        self.Label21.configure(highlightbackground="#d9d9d9")
        self.Label21.configure(highlightcolor="black")
        self.Label21.configure(justify='left')
        self.Label21.configure(text='''MaptileStaticFile''')
        self.tooltip_font = "TkDefaultFont"
        self.Label21_tooltip = \
        ToolTip(self.Label21, self.tooltip_font, _('''MaptileStaticFile'''))

        self.Label22 = tk.Label(top)
        self.Label22.place(relx=0.013, rely=0.674, height=37, width=200)
        self.Label22.configure(activebackground="#f9f9f9")
        self.Label22.configure(activeforeground="black")
        self.Label22.configure(anchor='nw')
        self.Label22.configure(background="#d9d9d9")
        self.Label22.configure(disabledforeground="#a3a3a3")
        self.Label22.configure(foreground="#000000")
        self.Label22.configure(highlightbackground="#d9d9d9")
        self.Label22.configure(highlightcolor="black")
        self.Label22.configure(justify='left')
        self.Label22.configure(text='''MasterAvatarFirstName''')
        self.tooltip_font = "TkDefaultFont"
        self.Label22_tooltip = \
        ToolTip(self.Label22, self.tooltip_font, _('''MasterAvatarFirstName'''))

        self.Label23 = tk.Label(top)
        self.Label23.place(relx=0.013, rely=0.705, height=38, width=200)
        self.Label23.configure(activebackground="#f9f9f9")
        self.Label23.configure(activeforeground="black")
        self.Label23.configure(anchor='nw')
        self.Label23.configure(background="#d9d9d9")
        self.Label23.configure(disabledforeground="#a3a3a3")
        self.Label23.configure(foreground="#000000")
        self.Label23.configure(highlightbackground="#d9d9d9")
        self.Label23.configure(highlightcolor="black")
        self.Label23.configure(justify='left')
        self.Label23.configure(text='''MasterAvatarLastName''')
        self.tooltip_font = "TkDefaultFont"
        self.Label23_tooltip = \
        ToolTip(self.Label23, self.tooltip_font, _('''MasterAvatarLastName'''))

        self.Label24 = tk.Label(top)
        self.Label24.place(relx=0.013, rely=0.737, height=40, width=252)
        self.Label24.configure(activebackground="#f9f9f9")
        self.Label24.configure(activeforeground="black")
        self.Label24.configure(anchor='nw')
        self.Label24.configure(background="#d9d9d9")
        self.Label24.configure(disabledforeground="#a3a3a3")
        self.Label24.configure(foreground="#000000")
        self.Label24.configure(highlightbackground="#d9d9d9")
        self.Label24.configure(highlightcolor="black")
        self.Label24.configure(justify='left')
        self.Label24.configure(text='''MasterAvatarSandboxPassword''')
        self.tooltip_font = "TkDefaultFont"
        self.Label24_tooltip = \
        ToolTip(self.Label24, self.tooltip_font, _('''MasterAvatarSandboxPassword'''))

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.013, rely=0.770, height=38, width=252)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(anchor='nw')
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(justify='left')
        self.Label5.configure(text='''InternalAddress''')
        self.tooltip_font = "TkDefaultFont"
        self.Label5_tooltip = \
        ToolTip(self.Label5, self.tooltip_font, _('''InternalAddress'''))

        self.Label25 = tk.Label(top)
        self.Label25.place(relx=0.013, rely=0.8, height=37, width=252)
        self.Label25.configure(activebackground="#f9f9f9")
        self.Label25.configure(activeforeground="black")
        self.Label25.configure(anchor='nw')
        self.Label25.configure(background="#d9d9d9")
        self.Label25.configure(disabledforeground="#a3a3a3")
        self.Label25.configure(foreground="#000000")
        self.Label25.configure(highlightbackground="#d9d9d9")
        self.Label25.configure(highlightcolor="black")
        self.Label25.configure(justify='left')
        self.Label25.configure(text='''Region amount''')
        self.tooltip_font = "TkDefaultFont"
        self.Label25_tooltip = \
        ToolTip(self.Label25, self.tooltip_font, _('''Region amount'''))

### buttons ###

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.35, rely=0.863, height=42, width=100)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Create''')
        self.Button1.configure(command=write_region)
        self.tooltip_font = "TkDefaultFont"
        self.Button1_tooltip = \
        ToolTip(self.Button1, self.tooltip_font, _('''Create'''))

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.525, rely=0.863, height=42, width=100)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Quit''')
        self.Button2.configure(command=destroy_window)
        self.tooltip_font = "TkDefaultFont"
        self.Button2_tooltip = \
        ToolTip(self.Button2, self.tooltip_font, _('''Quit'''))

### entry ###

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.35, rely=0.011,height=26, relwidth=0.338)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")
        self.Entry1.configure(textvariable=RegionName_var)
        self.Entry1.insert(0, "Random")
        self.tooltip_font = "TkDefaultFont"
        self.Entry1_tooltip = \
        ToolTip(self.Entry1, self.tooltip_font, _('''Region Name'''))

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.35, rely=0.042,height=26, relwidth=0.155)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="blue")
        self.Entry2.configure(selectforeground="white")
        self.Entry2.configure(textvariable=LocationX_var)
        #self.Entry2.insert(0, "Random")
        self.tooltip_font = "TkDefaultFont"
        self.Entry2_tooltip = \
        ToolTip(self.Entry2, self.tooltip_font, _('''LocationX'''))

        self.Entry3 = tk.Entry(top)
        self.Entry3.place(relx=0.531, rely=0.042,height=26, relwidth=0.155)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="blue")
        self.Entry3.configure(selectforeground="white")
        self.Entry3.configure(textvariable=LocationY_var)
        #self.Entry3.insert(0, "Random")
        self.tooltip_font = "TkDefaultFont"
        self.Entry3_tooltip = \
        ToolTip(self.Entry3, self.tooltip_font, _('''LocationY'''))

        self.Entry4 = tk.Entry(top)
        self.Entry4.place(relx=0.35, rely=0.105,height=26, relwidth=0.094)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#d9d9d9")
        self.Entry4.configure(highlightcolor="black")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(selectbackground="blue")
        self.Entry4.configure(selectforeground="white")
        self.Entry4.configure(textvariable=Size_var)
        self.Entry4.insert(0, "256")
        self.tooltip_font = "TkDefaultFont"
        self.Entry4_tooltip = \
        ToolTip(self.Entry4, self.tooltip_font, _('''Size'''))

        self.Entry5 = tk.Entry(top)
        self.Entry5.place(relx=0.35, rely=0.768,height=26, relwidth=0.155)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(highlightbackground="#d9d9d9")
        self.Entry5.configure(highlightcolor="black")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(selectbackground="blue")
        self.Entry5.configure(selectforeground="white")
        self.Entry5.configure(textvariable=InternalAddress_var)
        self.Entry5.insert(0, "0.0.0.0")
        self.tooltip_font = "TkDefaultFont"
        self.Entry5_tooltip = \
        ToolTip(self.Entry5, self.tooltip_font, _('''InternalAddress'''))

        self.Entry6 = tk.Entry(top)
        self.Entry6.place(relx=0.35, rely=0.074,height=26, relwidth=0.338)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(highlightbackground="#d9d9d9")
        self.Entry6.configure(highlightcolor="black")
        self.Entry6.configure(insertbackground="black")
        self.Entry6.configure(selectbackground="blue")
        self.Entry6.configure(selectforeground="white")
        self.Entry6.configure(textvariable=RegionUUID_var)
        #self.Entry6.insert(0, "Random")
        self.tooltip_font = "TkDefaultFont"
        self.Entry6_tooltip = \
        ToolTip(self.Entry6, self.tooltip_font, _('''RegionUUID'''))

        self.Entry7 = tk.Entry(top)
        self.Entry7.place(relx=0.35, rely=0.137,height=26, relwidth=0.155)
        self.Entry7.configure(background="white")
        self.Entry7.configure(disabledforeground="#a3a3a3")
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.configure(foreground="#000000")
        self.Entry7.configure(highlightbackground="#d9d9d9")
        self.Entry7.configure(highlightcolor="black")
        self.Entry7.configure(insertbackground="black")
        self.Entry7.configure(selectbackground="blue")
        self.Entry7.configure(selectforeground="white")
        self.Entry7.configure(textvariable=InternalPort_var)
        #self.Entry7.insert(0, "Random")
        self.tooltip_font = "TkDefaultFont"
        self.Entry7_tooltip = \
        ToolTip(self.Entry7, self.tooltip_font, _('''InternalPort'''))

        self.Entry8 = tk.Entry(top)
        self.Entry8.place(relx=0.35, rely=0.211,height=26, relwidth=0.155)
        self.Entry8.configure(background="white")
        self.Entry8.configure(disabledforeground="#a3a3a3")
        self.Entry8.configure(font="TkFixedFont")
        self.Entry8.configure(foreground="#000000")
        self.Entry8.configure(highlightbackground="#d9d9d9")
        self.Entry8.configure(highlightcolor="black")
        self.Entry8.configure(insertbackground="black")
        self.Entry8.configure(selectbackground="blue")
        self.Entry8.configure(selectforeground="white")
        self.Entry8.configure(textvariable=AllowAlternatePorts_var)
        self.Entry8.insert(0, "False")
        self.tooltip_font = "TkDefaultFont"
        self.Entry8_tooltip = \
        ToolTip(self.Entry8, self.tooltip_font, _('''AllowAlternatePorts'''))

        self.Entry9 = tk.Entry(top)
        self.Entry9.place(relx=0.35, rely=0.242,height=26, relwidth=0.155)
        self.Entry9.configure(background="white")
        self.Entry9.configure(disabledforeground="#a3a3a3")
        self.Entry9.configure(font="TkFixedFont")
        self.Entry9.configure(foreground="#000000")
        self.Entry9.configure(highlightbackground="#d9d9d9")
        self.Entry9.configure(highlightcolor="black")
        self.Entry9.configure(insertbackground="black")
        self.Entry9.configure(selectbackground="blue")
        self.Entry9.configure(selectforeground="white")
        self.Entry9.configure(textvariable=ResolveAddress_var)
        self.Entry9.insert(0, "off")
        self.tooltip_font = "TkDefaultFont"
        self.Entry9_tooltip = \
        ToolTip(self.Entry9, self.tooltip_font, _('''ResolveAddress'''))

        self.Entry10 = tk.Entry(top)
        self.Entry10.place(relx=0.35, rely=0.168,height=26, relwidth=0.155)
        self.Entry10.configure(background="white")
        self.Entry10.configure(disabledforeground="#a3a3a3")
        self.Entry10.configure(font="TkFixedFont")
        self.Entry10.configure(foreground="#000000")
        self.Entry10.configure(highlightbackground="#d9d9d9")
        self.Entry10.configure(highlightcolor="black")
        self.Entry10.configure(insertbackground="black")
        self.Entry10.configure(selectbackground="blue")
        self.Entry10.configure(selectforeground="white")
        self.Entry10.configure(textvariable=ExternalHostName_var)
        self.Entry10.insert(0, "SYSTEMIP")
        self.tooltip_font = "TkDefaultFont"
        self.Entry10_tooltip = \
        ToolTip(self.Entry10, self.tooltip_font, _('''ExternalHostName'''))

        self.Entry11 = tk.Entry(top)
        self.Entry11.place(relx=0.35, rely=0.284,height=26, relwidth=0.155)
        self.Entry11.configure(background="white")
        self.Entry11.configure(disabledforeground="#a3a3a3")
        self.Entry11.configure(font="TkFixedFont")
        self.Entry11.configure(foreground="#000000")
        self.Entry11.configure(highlightbackground="#d9d9d9")
        self.Entry11.configure(highlightcolor="black")
        self.Entry11.configure(insertbackground="black")
        self.Entry11.configure(selectbackground="blue")
        self.Entry11.configure(selectforeground="white")
        self.Entry11.configure(textvariable=MaxPrims_var)
        #self.Entry11.insert(0, "-1")
        self.tooltip_font = "TkDefaultFont"
        self.Entry11_tooltip = \
        ToolTip(self.Entry11, self.tooltip_font, _('''MaxPrims'''))

        self.Entry12 = tk.Entry(top)
        self.Entry12.place(relx=0.35, rely=0.316,height=26, relwidth=0.155)
        self.Entry12.configure(background="white")
        self.Entry12.configure(disabledforeground="#a3a3a3")
        self.Entry12.configure(font="TkFixedFont")
        self.Entry12.configure(foreground="#000000")
        self.Entry12.configure(highlightbackground="#d9d9d9")
        self.Entry12.configure(highlightcolor="black")
        self.Entry12.configure(insertbackground="black")
        self.Entry12.configure(selectbackground="blue")
        self.Entry12.configure(selectforeground="white")
        self.Entry12.configure(textvariable=MaxAgents_var)
        self.Entry12.insert(0, "40")
        self.tooltip_font = "TkDefaultFont"
        self.Entry12_tooltip = \
        ToolTip(self.Entry12, self.tooltip_font, _('''MaxAgents'''))

        self.Entry13 = tk.Entry(top)
        self.Entry13.place(relx=0.35, rely=0.347,height=26, relwidth=0.155)
        self.Entry13.configure(background="white")
        self.Entry13.configure(disabledforeground="#a3a3a3")
        self.Entry13.configure(font="TkFixedFont")
        self.Entry13.configure(foreground="#000000")
        self.Entry13.configure(highlightbackground="#d9d9d9")
        self.Entry13.configure(highlightcolor="black")
        self.Entry13.configure(insertbackground="black")
        self.Entry13.configure(selectbackground="blue")
        self.Entry13.configure(selectforeground="white")
        self.Entry13.configure(textvariable=DefaultLanding_var)
        #self.Entry13.insert(0, "off")
        self.tooltip_font = "TkDefaultFont"
        self.Entry13_tooltip = \
        ToolTip(self.Entry13, self.tooltip_font, _('''DefaultLanding'''))

        self.Entry14 = tk.Entry(top)
        self.Entry14.place(relx=0.35, rely=0.4,height=26, relwidth=0.155)
        self.Entry14.configure(background="white")
        self.Entry14.configure(disabledforeground="#a3a3a3")
        self.Entry14.configure(font="TkFixedFont")
        self.Entry14.configure(foreground="#000000")
        self.Entry14.configure(highlightbackground="#d9d9d9")
        self.Entry14.configure(highlightcolor="black")
        self.Entry14.configure(insertbackground="black")
        self.Entry14.configure(selectbackground="blue")
        self.Entry14.configure(selectforeground="white")
        self.Entry14.configure(textvariable=NonPhysicalPrimMax_var)
        #self.Entry14.insert(0, "off")
        self.tooltip_font = "TkDefaultFont"
        self.Entry14_tooltip = \
        ToolTip(self.Entry14, self.tooltip_font, _('''NonPhysicalPrimMax'''))

        self.Entry15 = tk.Entry(top)
        self.Entry15.place(relx=0.35, rely=0.432,height=26, relwidth=0.155)
        self.Entry15.configure(background="white")
        self.Entry15.configure(disabledforeground="#a3a3a3")
        self.Entry15.configure(font="TkFixedFont")
        self.Entry15.configure(foreground="#000000")
        self.Entry15.configure(highlightbackground="#d9d9d9")
        self.Entry15.configure(highlightcolor="black")
        self.Entry15.configure(insertbackground="black")
        self.Entry15.configure(selectbackground="blue")
        self.Entry15.configure(selectforeground="white")
        self.Entry15.configure(textvariable=PhysicalPrimMax_var)
        #self.Entry15.insert(0, "off")
        self.tooltip_font = "TkDefaultFont"
        self.Entry15_tooltip = \
        ToolTip(self.Entry15, self.tooltip_font, _('''PhysicalPrimMax'''))

        self.Entry16 = tk.Entry(top)
        self.Entry16.place(relx=0.35, rely=0.463,height=26, relwidth=0.155)
        self.Entry16.configure(background="white")
        self.Entry16.configure(disabledforeground="#a3a3a3")
        self.Entry16.configure(font="TkFixedFont")
        self.Entry16.configure(foreground="#000000")
        self.Entry16.configure(highlightbackground="#d9d9d9")
        self.Entry16.configure(highlightcolor="black")
        self.Entry16.configure(insertbackground="black")
        self.Entry16.configure(selectbackground="blue")
        self.Entry16.configure(selectforeground="white")
        self.Entry16.configure(textvariable=ClampPrimSize_var)
        #self.Entry16.insert(0, "off")
        self.tooltip_font = "TkDefaultFont"
        self.Entry16_tooltip = \
        ToolTip(self.Entry16, self.tooltip_font, _('''ClampPrimSize'''))

        self.Entry17 = tk.Entry(top)
        self.Entry17.place(relx=0.35, rely=0.495,height=26, relwidth=0.155)
        self.Entry17.configure(background="white")
        self.Entry17.configure(disabledforeground="#a3a3a3")
        self.Entry17.configure(font="TkFixedFont")
        self.Entry17.configure(foreground="#000000")
        self.Entry17.configure(highlightbackground="#d9d9d9")
        self.Entry17.configure(highlightcolor="black")
        self.Entry17.configure(insertbackground="black")
        self.Entry17.configure(selectbackground="blue")
        self.Entry17.configure(selectforeground="white")
        self.Entry17.configure(textvariable=MaxPrimsPerUser_var)
        #self.Entry17.insert(0, "off")
        self.tooltip_font = "TkDefaultFont"
        self.Entry17_tooltip = \
        ToolTip(self.Entry17, self.tooltip_font, _('''MaxPrimsPerUser'''))

        self.Entry18 = tk.Entry(top)
        self.Entry18.place(relx=0.35, rely=0.526,height=26, relwidth=0.155)
        self.Entry18.configure(background="white")
        self.Entry18.configure(disabledforeground="#a3a3a3")
        self.Entry18.configure(font="TkFixedFont")
        self.Entry18.configure(foreground="#000000")
        self.Entry18.configure(highlightbackground="#d9d9d9")
        self.Entry18.configure(highlightcolor="black")
        self.Entry18.configure(insertbackground="black")
        self.Entry18.configure(selectbackground="blue")
        self.Entry18.configure(selectforeground="white")
        self.Entry18.configure(textvariable=ScopeID_var)
        #self.Entry18.insert(0, "off")
        self.tooltip_font = "TkDefaultFont"
        self.Entry18_tooltip = \
        ToolTip(self.Entry18, self.tooltip_font, _('''ScopeID'''))

        self.Entry19 = tk.Entry(top)
        self.Entry19.place(relx=0.35, rely=0.558,height=26, relwidth=0.155)
        self.Entry19.configure(background="white")
        self.Entry19.configure(disabledforeground="#a3a3a3")
        self.Entry19.configure(font="TkFixedFont")
        self.Entry19.configure(foreground="#000000")
        self.Entry19.configure(highlightbackground="#d9d9d9")
        self.Entry19.configure(highlightcolor="black")
        self.Entry19.configure(insertbackground="black")
        self.Entry19.configure(selectbackground="blue")
        self.Entry19.configure(selectforeground="white")
        self.Entry19.configure(textvariable=RegionType_var)
        #self.Entry19.insert(0, "off")
        self.tooltip_font = "TkDefaultFont"
        self.Entry19_tooltip = \
        ToolTip(self.Entry19, self.tooltip_font, _('''RegionType'''))

        self.Entry20 = tk.Entry(top)
        self.Entry20.place(relx=0.35, rely=0.589,height=26, relwidth=0.338)
        self.Entry20.configure(background="white")
        self.Entry20.configure(disabledforeground="#a3a3a3")
        self.Entry20.configure(font="TkFixedFont")
        self.Entry20.configure(foreground="#000000")
        self.Entry20.configure(highlightbackground="#d9d9d9")
        self.Entry20.configure(highlightcolor="black")
        self.Entry20.configure(insertbackground="black")
        self.Entry20.configure(selectbackground="blue")
        self.Entry20.configure(selectforeground="white")
        self.Entry20.configure(textvariable=MaptileStaticUUID_var)
        #self.Entry20.insert(0, "Random")
        self.tooltip_font = "TkDefaultFont"
        self.Entry20_tooltip = \
        ToolTip(self.Entry20, self.tooltip_font, _('''MaptileStaticUUID'''))

        self.Entry21 = tk.Entry(top)
        self.Entry21.place(relx=0.35, rely=0.621,height=26, relwidth=0.155)
        self.Entry21.configure(background="white")
        self.Entry21.configure(disabledforeground="#a3a3a3")
        self.Entry21.configure(font="TkFixedFont")
        self.Entry21.configure(foreground="#000000")
        self.Entry21.configure(highlightbackground="#d9d9d9")
        self.Entry21.configure(highlightcolor="black")
        self.Entry21.configure(insertbackground="black")
        self.Entry21.configure(selectbackground="blue")
        self.Entry21.configure(selectforeground="white")
        self.Entry21.configure(textvariable=MaptileStaticFile_var)
        #self.Entry21.insert(0, "off")
        self.tooltip_font = "TkDefaultFont"
        self.Entry21_tooltip = \
        ToolTip(self.Entry21, self.tooltip_font, _('''MaptileStaticFile'''))

        self.Entry22 = tk.Entry(top)
        self.Entry22.place(relx=0.35, rely=0.674,height=26, relwidth=0.155)
        self.Entry22.configure(background="white")
        self.Entry22.configure(disabledforeground="#a3a3a3")
        self.Entry22.configure(font="TkFixedFont")
        self.Entry22.configure(foreground="#000000")
        self.Entry22.configure(highlightbackground="#d9d9d9")
        self.Entry22.configure(highlightcolor="black")
        self.Entry22.configure(insertbackground="black")
        self.Entry22.configure(selectbackground="blue")
        self.Entry22.configure(selectforeground="white")
        self.Entry22.configure(textvariable=MasterAvatarFirstName_var)
        #self.Entry22.insert(0, "off")
        self.tooltip_font = "TkDefaultFont"
        self.Entry22_tooltip = \
        ToolTip(self.Entry22, self.tooltip_font, _('''MasterAvatarFirstName'''))

        self.Entry23 = tk.Entry(top)
        self.Entry23.place(relx=0.35, rely=0.705,height=26, relwidth=0.155)
        self.Entry23.configure(background="white")
        self.Entry23.configure(disabledforeground="#a3a3a3")
        self.Entry23.configure(font="TkFixedFont")
        self.Entry23.configure(foreground="#000000")
        self.Entry23.configure(highlightbackground="#d9d9d9")
        self.Entry23.configure(highlightcolor="black")
        self.Entry23.configure(insertbackground="black")
        self.Entry23.configure(selectbackground="blue")
        self.Entry23.configure(selectforeground="white")
        self.Entry23.configure(textvariable=MasterAvatarLastName_var)
        #self.Entry23.insert(0, "off")
        self.tooltip_font = "TkDefaultFont"
        self.Entry23_tooltip = \
        ToolTip(self.Entry23, self.tooltip_font, _('''MasterAvatarLastName'''))

        self.Entry24 = tk.Entry(top)
        self.Entry24.place(relx=0.35, rely=0.737,height=26, relwidth=0.155)
        self.Entry24.configure(background="white")
        self.Entry24.configure(disabledforeground="#a3a3a3")
        self.Entry24.configure(font="TkFixedFont")
        self.Entry24.configure(foreground="#000000")
        self.Entry24.configure(highlightbackground="#d9d9d9")
        self.Entry24.configure(highlightcolor="black")
        self.Entry24.configure(insertbackground="black")
        self.Entry24.configure(selectbackground="blue")
        self.Entry24.configure(selectforeground="white")
        self.Entry24.configure(textvariable=MasterAvatarSandboxPassword_var)
        #self.Entry24.insert(0, "off")
        self.tooltip_font = "TkDefaultFont"
        self.Entry24_tooltip = \
        ToolTip(self.Entry24, self.tooltip_font, _('''MasterAvatarSandboxPassword'''))

        self.Entry25 = tk.Entry(top)
        self.Entry25.place(relx=0.35, rely=0.8,height=26, relwidth=0.063)
        self.Entry25.configure(background="white")
        self.Entry25.configure(disabledforeground="#a3a3a3")
        self.Entry25.configure(font="TkFixedFont")
        self.Entry25.configure(foreground="#000000")
        self.Entry25.configure(highlightbackground="#d9d9d9")
        self.Entry25.configure(highlightcolor="black")
        self.Entry25.configure(insertbackground="black")
        self.Entry25.configure(selectbackground="blue")
        self.Entry25.configure(selectforeground="white")
        self.Entry25.configure(textvariable=RegionAmount_var)
        self.Entry25.insert(0, "1")
        self.tooltip_font = "TkDefaultFont"
        self.Entry25_tooltip = \
        ToolTip(self.Entry25, self.tooltip_font, _('''Region amount'''))


# ======================================================
# Support code for Balloon Help (also called tooltips).
# Found the original code at:
# http://code.activestate.com/recipes/576688-tooltip-for-tkinter/
# Modified by Rozen to remove Tkinter import statements and to receive
# the font as an argument.
# ======================================================

from time import time, localtime, strftime

class ToolTip(tk.Toplevel):
    """
    Provides a ToolTip widget for Tkinter.
    To apply a ToolTip to any Tkinter widget, simply pass the widget to the
    ToolTip constructor
    """
    def __init__(self, wdgt, tooltip_font, msg=None, msgFunc=None,
                 delay=0.5, follow=True):
        """
        Initialize the ToolTip

        Arguments:
          wdgt: The widget this ToolTip is assigned to
          tooltip_font: Font to be used
          msg:  A static string message assigned to the ToolTip
          msgFunc: A function that retrieves a string to use as the ToolTip text
          delay:   The delay in seconds before the ToolTip appears(may be float)
          follow:  If True, the ToolTip follows motion, otherwise hides
        """
        self.wdgt = wdgt
        # The parent of the ToolTip is the parent of the ToolTips widget
        self.parent = self.wdgt.master
        # Initalise the Toplevel
        tk.Toplevel.__init__(self, self.parent, bg='black', padx=1, pady=1)
        # Hide initially
        self.withdraw()
        # The ToolTip Toplevel should have no frame or title bar
        self.overrideredirect(True)

        # The msgVar will contain the text displayed by the ToolTip
        self.msgVar = tk.StringVar()
        if msg is None:
            self.msgVar.set('No message provided')
        else:
            self.msgVar.set(msg)
        self.msgFunc = msgFunc
        self.delay = delay
        self.follow = follow
        self.visible = 0
        self.lastMotion = 0
        # The text of the ToolTip is displayed in a Message widget
        tk.Message(self, textvariable=self.msgVar, bg='#FFFFDD',
                font=tooltip_font,
                aspect=1000).grid()

        # Add bindings to the widget.  This will NOT override
        # bindings that the widget already has
        self.wdgt.bind('<Enter>', self.spawn, '+')
        self.wdgt.bind('<Leave>', self.hide, '+')
        self.wdgt.bind('<Motion>', self.move, '+')

    def spawn(self, event=None):
        """
        Spawn the ToolTip.  This simply makes the ToolTip eligible for display.
        Usually this is caused by entering the widget

        Arguments:
          event: The event that called this funciton
        """
        self.visible = 1
        # The after function takes a time argument in milliseconds
        self.after(int(self.delay * 1000), self.show)

    def show(self):
        """
        Displays the ToolTip if the time delay has been long enough
        """
        if self.visible == 1 and time() - self.lastMotion > self.delay:
            self.visible = 2
        if self.visible == 2:
            self.deiconify()

    def move(self, event):
        """
        Processes motion within the widget.
        Arguments:
          event: The event that called this function
        """
        self.lastMotion = time()
        # If the follow flag is not set, motion within the
        # widget will make the ToolTip disappear
        #
        if self.follow is False:
            self.withdraw()
            self.visible = 1

        # Offset the ToolTip 10x10 pixes southwest of the pointer
        self.geometry('+%i+%i' % (event.x_root+20, event.y_root-10))
        try:
            # Try to call the message function.  Will not change
            # the message if the message function is None or
            # the message function fails
            self.msgVar.set(self.msgFunc())
        except:
            pass
        self.after(int(self.delay * 1000), self.show)

    def hide(self, event=None):
        """
        Hides the ToolTip.  Usually this is caused by leaving the widget
        Arguments:
          event: The event that called this function
        """
        self.visible = 0
        self.withdraw()

    def update(self, msg):
        """
        Updates the Tooltip with a new message. Added by Rozen
        """
        self.msgVar.set(msg)

# ===========================================================
#                   End of Class ToolTip
# ===========================================================

if __name__ == '__main__':
    vp_start_gui()





