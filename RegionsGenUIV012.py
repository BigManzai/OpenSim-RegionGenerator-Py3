#!/usr/bin/python

# Ein minimalistisches Beispiel eine Regions.ini mit Python 3.8.5 zu erstellen.
# Dies soll zum verständniss und als Grundlage für eigene Programme dienen.
#
# A minimalistic example of creating a Regions.ini with Python 3.8.5.
# This should serve as a basis for understanding and for your own programs.

# Wenn IP freigelassen wird dann wird automatisch SYSTEMIP genutzt.
# Wenn Size freigelassen wird dann wird automatisch 256 genutzt.
# Wenn Location freigelassen wird dann werden automatisch Zufallswerte zwischen 1000-8000 genutzt.
# Wenn Port freigelassen wird dann werden automatisch Zufallswerte zwischen 9100-9999 genutzt.
# Wenn UUID freigelassen wird dann wird automatisch eine generiert.
# Wenn Region name freigelassen wird dann wird automatisch ein Zufallsname genutzt.
# Wenn Number of regions freigelassen wird dann wird automatisch 1 genutzt.

import configparser
import uuid
import random
import sys
import random_name_def
import tkinter as tk
import tkinter.ttk as ttk
from time import time, localtime, strftime
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

# Global
val = None
top_level = None
root = None
serverip = None
automaticregion = None
automaticuuid = None
w_win = None
myip = 'SYSTEMIP'
regionsize = '256'

# make a random location
def randomlocation():
    maplocation = random.randrange(1000, 8000, 4)
    localmap = str(maplocation)
    return localmap;

# assemble region location
maplocation = randomlocation() + ',' + randomlocation()

# make a random port
def randomport():
    myport = random.randrange(9100, 9999, 4)
    return myport;

# make a random UUID
def randomuuid():
    randomuuid = uuid.uuid4()
    return randomuuid;

# set a ip
def set_ip():
    print(_('no function!'))
    return myip;

# set size
def set_size():
    print(_('no function!'))
    regionsize = '256'
    return regionsize;

# set location
def set_location():
    print(_('no function!'))
    return;

# set uuid
def set_uuid():
    print(_('no function!'))
    return;

# set location
def set_region_name():
    print(_('no function!'))

# set Number of regions
def set_number_regions():
    print(_('no function!'))
    return;

# create a config file
def write_region():
    config = configparser.ConfigParser()
    # capitalization gross- kleinschreibung beachten
    config.optionxform = str

    # any name
    regionname = random_name_def.randomname();

    # generate a uuid for all entries
    ruuid = randomuuid()

    # Change space to subline for the filename
    confdatei = regionname.replace(" ", "_")

    config[regionname] = {'RegionUUID': ruuid,
                          'Location': maplocation,
                          'SizeX': regionsize,
                          'SizeY': regionsize,
                          'SizeZ': regionsize,
                          'InternalAddress': '0.0.0.0',
                          'InternalPort': randomport(),
                          'AllowAlternatePorts': 'False',
                          'ResolveAddress': 'False',
                          'ExternalHostName': myip,
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

### User Interface ####

w = None

def set_Tk_var():
    global serverip
    serverip = tk.StringVar()
    global automaticregion
    automaticregion = tk.IntVar()
    global automaticuuid
    automaticuuid = tk.IntVar()

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
    set_Tk_var()
    top = HaupFenster (root)
    init(root, top)
    root.mainloop()

def create_HaupFenster(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_HaupFenster(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    set_Tk_var()
    top = HaupFenster (w)
    init(w, top, *args, **kwargs)
    return (w, top)

def destroy_HaupFenster():
    global w
    w.destroy()
    w = None

##### Master Window #####
class HaupFenster:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("800x450+650+150")
        top.minsize(176, 1)
        top.maxsize(6724, 1590)
        top.resizable(1, 1)
        top.title("RegionGenerator")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

##### Frame Hauptrahmen #####

        self.rData = tk.LabelFrame(top)
        self.rData.place(relx=0.038, rely=0.022, relheight=0.931, relwidth=0.925)
        self.rData.place(anchor=w, justify=w)

        self.rData.configure(relief='groove')
        self.rData.configure(foreground="black")
        self.rData.configure(text=_('''Data Input'''))
        self.rData.configure(background="#d9d9d9")
        self.rData.configure(highlightbackground="#d9d9d9")
        self.rData.configure(highlightcolor="black")

##### Label Beschriftung #####

        self.Label_Server_IP = tk.Label(self.rData)
        self.Label_Server_IP.place(relx=0.005, rely=0.079, height=26, width=128, bordermode='ignore')
        self.Label_Server_IP.configure(activebackground="#f9f9f9")
        self.Label_Server_IP.configure(activeforeground="black")
        self.Label_Server_IP.configure(background="#d9d9d9")
        self.Label_Server_IP.configure(disabledforeground="#a3a3a3")
        self.Label_Server_IP.configure(foreground="#000000")
        self.Label_Server_IP.configure(highlightbackground="#d9d9d9")
        self.Label_Server_IP.configure(highlightcolor="black")
        self.Label_Server_IP.configure(justify='left')
        self.Label_Server_IP.configure(text=_('''IP'''))

        self.Label_Size = tk.Label(self.rData)
        self.Label_Size.place(relx=0.005, rely=0.155, height=18, width=128, bordermode='ignore')
        self.Label_Size.configure(activebackground="#f9f9f9")
        self.Label_Size.configure(activeforeground="black")
        self.Label_Size.configure(background="#d9d9d9")
        self.Label_Size.configure(disabledforeground="#a3a3a3")
        self.Label_Size.configure(foreground="#000000")
        self.Label_Size.configure(highlightbackground="#d9d9d9")
        self.Label_Size.configure(highlightcolor="black")
        self.Label_Size.configure(justify='left')
        self.Label_Size.configure(text=_('''Size'''))

        self.Label_Localisation = tk.Label(self.rData)
        self.Label_Localisation.place(relx=0.005, rely=0.234, height=26, width=128, bordermode='ignore')
        self.Label_Localisation.configure(activebackground="#f9f9f9")
        self.Label_Localisation.configure(activeforeground="black")
        self.Label_Localisation.configure(background="#d9d9d9")
        self.Label_Localisation.configure(disabledforeground="#a3a3a3")
        self.Label_Localisation.configure(foreground="#000000")
        self.Label_Localisation.configure(highlightbackground="#d9d9d9")
        self.Label_Localisation.configure(highlightcolor="black")
        self.Label_Localisation.configure(justify='left')
        self.Label_Localisation.configure(text=_('''Location'''))

        self.Label_Port = tk.Label(self.rData)
        self.Label_Port.place(relx=0.005, rely=0.313, height=26, width=128, bordermode='ignore')
        self.Label_Port.configure(activebackground="#f9f9f9")
        self.Label_Port.configure(activeforeground="black")
        self.Label_Port.configure(background="#d9d9d9")
        self.Label_Port.configure(disabledforeground="#a3a3a3")
        self.Label_Port.configure(foreground="#000000")
        self.Label_Port.configure(highlightbackground="#d9d9d9")
        self.Label_Port.configure(highlightcolor="black")
        self.Label_Port.configure(justify='left')
        self.Label_Port.configure(text=_('''Port'''))

        self.Label_UUID = tk.Label(self.rData)
        self.Label_UUID.place(relx=0.005, rely=0.389, height=26, width=128, bordermode='ignore')
        self.Label_UUID.configure(activebackground="#f9f9f9")
        self.Label_UUID.configure(activeforeground="black")
        self.Label_UUID.configure(background="#d9d9d9")
        self.Label_UUID.configure(disabledforeground="#a3a3a3")
        self.Label_UUID.configure(foreground="#000000")
        self.Label_UUID.configure(highlightbackground="#d9d9d9")
        self.Label_UUID.configure(highlightcolor="black")
        self.Label_UUID.configure(justify='left')
        self.Label_UUID.configure(text=_('''UUID'''))

        self.Label_Regionname = tk.Label(self.rData)
        self.Label_Regionname.place(relx=0.005, rely=0.453, height=26, width=128, bordermode='ignore')
        self.Label_Regionname.configure(activebackground="#f9f9f9")
        self.Label_Regionname.configure(activeforeground="black")
        self.Label_Regionname.configure(background="#d9d9d9")
        self.Label_Regionname.configure(disabledforeground="#a3a3a3")
        self.Label_Regionname.configure(foreground="#000000")
        self.Label_Regionname.configure(highlightbackground="#d9d9d9")
        self.Label_Regionname.configure(highlightcolor="black")
        self.Label_Regionname.configure(justify='left')
        self.Label_Regionname.configure(text=_('''Region name'''))

        self.Label_number_regions = tk.Label(self.rData)
        self.Label_number_regions.place(relx=0.005, rely=0.549, height=26, width=128, bordermode='ignore')
        self.Label_number_regions.configure(activebackground="#f9f9f9")
        self.Label_number_regions.configure(activeforeground="black")
        self.Label_number_regions.configure(background="#d9d9d9")
        self.Label_number_regions.configure(disabledforeground="#a3a3a3")
        self.Label_number_regions.configure(foreground="#000000")
        self.Label_number_regions.configure(highlightbackground="#d9d9d9")
        self.Label_number_regions.configure(highlightcolor="black")
        self.Label_number_regions.configure(justify='left')
        self.Label_number_regions.configure(text=_('''Number of regions'''))


##### Entry Eingaben #####

        self.Entry_Server_IP = tk.Entry(self.rData)
        self.Entry_Server_IP.place(relx=0.300, rely=0.079, height=26, relwidth=0.519, bordermode='ignore')
        self.Entry_Server_IP.configure(background="white")
        self.Entry_Server_IP.configure(disabledforeground="#a3a3a3")
        self.Entry_Server_IP.configure(font="TkFixedFont")
        self.Entry_Server_IP.configure(foreground="#000000")
        self.Entry_Server_IP.configure(highlightbackground="#d9d9d9")
        self.Entry_Server_IP.configure(highlightcolor="black")
        self.Entry_Server_IP.configure(insertbackground="black")
        self.Entry_Server_IP.configure(selectbackground="blue")
        self.Entry_Server_IP.configure(selectforeground="white")
        self.Entry_Server_IP.configure(textvariable=serverip)
        self.tooltip_font = "TkDefaultFont"
        self.Entry_Server_IP_tooltip = \
        ToolTip(self.Entry_Server_IP, self.tooltip_font, _('''Youre Server IP'''))

        self.Entry_Size = tk.Entry(self.rData)
        self.Entry_Size.place(relx=0.300, rely=0.155, height=26, relwidth=0.086, bordermode='ignore')
        self.Entry_Size.configure(background="white")
        self.Entry_Size.configure(disabledforeground="#a3a3a3")
        self.Entry_Size.configure(font="TkFixedFont")
        self.Entry_Size.configure(foreground="#000000")
        self.Entry_Size.configure(highlightbackground="#d9d9d9")
        self.Entry_Size.configure(highlightcolor="black")
        self.Entry_Size.configure(insertbackground="black")
        self.Entry_Size.configure(selectbackground="blue")
        self.Entry_Size.configure(selectforeground="white")
        self.tooltip_font = "TkDefaultFont"
        self.Entry_Size_tooltip = \
        ToolTip(self.Entry_Size, self.tooltip_font, _('''Region size'''))

        self.Entry_Localisation_X = tk.Entry(self.rData)
        self.Entry_Localisation_X.place(relx=0.300, rely=0.235, height=26, relwidth=0.1, bordermode='ignore')
        self.Entry_Localisation_X.configure(background="white")
        self.Entry_Localisation_X.configure(disabledforeground="#a3a3a3")
        self.Entry_Localisation_X.configure(font="TkFixedFont")
        self.Entry_Localisation_X.configure(foreground="#000000")
        self.Entry_Localisation_X.configure(highlightbackground="#d9d9d9")
        self.Entry_Localisation_X.configure(highlightcolor="black")
        self.Entry_Localisation_X.configure(insertbackground="black")
        self.Entry_Localisation_X.configure(selectbackground="blue")
        self.Entry_Localisation_X.configure(selectforeground="white")
        self.tooltip_font = "TkDefaultFont"
        self.Entry_Localisation_X_tooltip = \
        ToolTip(self.Entry_Localisation_X, self.tooltip_font, _('''X position'''))

        self.Entry_Localisation_Y = tk.Entry(self.rData)
        self.Entry_Localisation_Y.place(relx=0.400, rely=0.235, height=26, relwidth=0.1, bordermode='ignore')
        self.Entry_Localisation_Y.configure(background="white")
        self.Entry_Localisation_Y.configure(disabledforeground="#a3a3a3")
        self.Entry_Localisation_Y.configure(font="TkFixedFont")
        self.Entry_Localisation_Y.configure(foreground="#000000")
        self.Entry_Localisation_Y.configure(highlightbackground="#d9d9d9")
        self.Entry_Localisation_Y.configure(highlightcolor="black")
        self.Entry_Localisation_Y.configure(insertbackground="black")
        self.Entry_Localisation_Y.configure(selectbackground="blue")
        self.Entry_Localisation_Y.configure(selectforeground="white")
        self.tooltip_font = "TkDefaultFont"
        self.Entry_Localisation_Y_tooltip = \
        ToolTip(self.Entry_Localisation_Y, self.tooltip_font, _('''y position'''))

        self.Entry_Port = tk.Entry(self.rData)
        self.Entry_Port.place(relx=0.300, rely=0.313, height=26, relwidth=0.1, bordermode='ignore')
        self.Entry_Port.configure(background="white")
        self.Entry_Port.configure(disabledforeground="#a3a3a3")
        self.Entry_Port.configure(font="TkFixedFont")
        self.Entry_Port.configure(foreground="#000000")
        self.Entry_Port.configure(highlightbackground="#d9d9d9")
        self.Entry_Port.configure(highlightcolor="black")
        self.Entry_Port.configure(insertbackground="black")
        self.Entry_Port.configure(selectbackground="blue")
        self.Entry_Port.configure(selectforeground="white")
        self.tooltip_font = "TkDefaultFont"
        self.Entry_Port_tooltip = \
        ToolTip(self.Entry_Port, self.tooltip_font, _('''Port'''))

        self.Entry_UUID = tk.Entry(self.rData)
        self.Entry_UUID.place(relx=0.300, rely=0.389, height=26, relwidth=0.505, bordermode='ignore')
        self.Entry_UUID.configure(background="white")
        self.Entry_UUID.configure(disabledforeground="#a3a3a3")
        self.Entry_UUID.configure(font="TkFixedFont")
        self.Entry_UUID.configure(foreground="#000000")
        self.Entry_UUID.configure(highlightbackground="#d9d9d9")
        self.Entry_UUID.configure(highlightcolor="black")
        self.Entry_UUID.configure(insertbackground="black")
        self.Entry_UUID.configure(selectbackground="blue")
        self.Entry_UUID.configure(selectforeground="white")
        self.tooltip_font = "TkDefaultFont"
        self.Entry_UUID_tooltip = \
        ToolTip(self.Entry_UUID, self.tooltip_font, _('''uuid or random'''))

        self.Entry_Regionname = tk.Entry(self.rData)
        self.Entry_Regionname.place(relx=0.300, rely=0.465, height=26, relwidth=0.424, bordermode='ignore')
        self.Entry_Regionname.configure(background="white")
        self.Entry_Regionname.configure(disabledforeground="#a3a3a3")
        self.Entry_Regionname.configure(font="TkFixedFont")
        self.Entry_Regionname.configure(foreground="#000000")
        self.Entry_Regionname.configure(highlightbackground="#d9d9d9")
        self.Entry_Regionname.configure(highlightcolor="black")
        self.Entry_Regionname.configure(insertbackground="black")
        self.Entry_Regionname.configure(selectbackground="blue")
        self.Entry_Regionname.configure(selectforeground="white")
        self.tooltip_font = "TkDefaultFont"
        self.Entry_Regionname_tooltip = \
        ToolTip(self.Entry_Regionname, self.tooltip_font, _('''Region Name'''))

        self.Entry_number_regions = tk.Entry(self.rData)
        self.Entry_number_regions.place(relx=0.300, rely=0.561, height=26, relwidth=0.073, bordermode='ignore')
        self.Entry_number_regions.configure(background="white")
        self.Entry_number_regions.configure(disabledforeground="#a3a3a3")
        self.Entry_number_regions.configure(font="TkFixedFont")
        self.Entry_number_regions.configure(foreground="#000000")
        self.Entry_number_regions.configure(highlightbackground="#d9d9d9")
        self.Entry_number_regions.configure(highlightcolor="black")
        self.Entry_number_regions.configure(insertbackground="black")
        self.Entry_number_regions.configure(selectbackground="blue")
        self.Entry_number_regions.configure(selectforeground="white")
        self.tooltip_font = "TkDefaultFont"
        self.Entry_number_regions_tooltip = \
        ToolTip(self.Entry_number_regions, self.tooltip_font, _('''how many regions'''))

###### Checkbutton #####

#Check Automatic region name.
        # self.Checkbutton_Regionname = tk.Checkbutton(self.rData)
        # self.Checkbutton_Regionname.place(relx=0.649, rely=0.453, relheight=0.122, relwidth=0.2, bordermode='ignore')
        # self.Checkbutton_Regionname.configure(activebackground="#ececec")
        # self.Checkbutton_Regionname.configure(activeforeground="#000000")
        # self.Checkbutton_Regionname.configure(background="#d9d9d9")
        # self.Checkbutton_Regionname.configure(disabledforeground="#a3a3a3")
        # self.Checkbutton_Regionname.configure(foreground="#000000")
        # self.Checkbutton_Regionname.configure(highlightbackground="#d9d9d9")
        # self.Checkbutton_Regionname.configure(highlightcolor="black")
        # self.Checkbutton_Regionname.configure(justify='left')
        # self.Checkbutton_Regionname.configure(text=_('''Automatic name'''))
        # self.Checkbutton_Regionname.configure(variable=automaticregion)
        # self.tooltip_font = "TkDefaultFont"
        # self.Checkbutton_Regionname_tooltip = \
        # ToolTip(self.Checkbutton_Regionname, self.tooltip_font, _('''Random Name'''))

#Check Automatic uuid.
        # self.Checkbutton_Automatic_uuid = tk.Checkbutton(self.rData)
        # self.Checkbutton_Automatic_uuid.place(relx=0.635, rely=0.382, relheight=0.112, relwidth=0.227, bordermode='ignore')
        # self.Checkbutton_Automatic_uuid.configure(activebackground="#ececec")
        # self.Checkbutton_Automatic_uuid.configure(activeforeground="#000000")
        # self.Checkbutton_Automatic_uuid.configure(background="#d9d9d9")
        # self.Checkbutton_Automatic_uuid.configure(disabledforeground="#a3a3a3")
        # self.Checkbutton_Automatic_uuid.configure(foreground="#000000")
        # self.Checkbutton_Automatic_uuid.configure(highlightbackground="#d9d9d9")
        # self.Checkbutton_Automatic_uuid.configure(highlightcolor="black")
        # self.Checkbutton_Automatic_uuid.configure(justify='left')
        # self.Checkbutton_Automatic_uuid.configure(text=_('''Automatic UUID'''))
        # self.Checkbutton_Automatic_uuid.configure(variable=automaticuuid)
        # self.tooltip_font = "TkDefaultFont"
        # self.Checkbutton_Automatic_uuid_tooltip = \
        # ToolTip(self.Checkbutton_Automatic_uuid, self.tooltip_font, _('''Random UUID'''))

##### Buttons #####

# Create Region Button
        self.Button_Create = tk.Button(self.rData)
        self.Button_Create.place(relx=0.041, rely=0.788, height=42, width=100, bordermode='ignore')
        self.Button_Create.configure(activebackground="#ececec")
        self.Button_Create.configure(activeforeground="#000000")
        self.Button_Create.configure(background="#d9d9d9")
        self.Button_Create.configure(disabledforeground="#a3a3a3")
        self.Button_Create.configure(foreground="#000000")
        self.Button_Create.configure(highlightbackground="#d9d9d9")
        self.Button_Create.configure(highlightcolor="black")
        self.Button_Create.configure(pady="0")
        self.Button_Create.configure(text=_('''Create'''))
        self.Button_Create.configure(command=write_region)
        self.tooltip_font = "TkDefaultFont"
        self.Button_Create_tooltip = \
        ToolTip(self.Button_Create, self.tooltip_font, _('''Creates one or more regions depending on the setting.'''))

# Exit Button
        self.Button_Exit = tk.Button(self.rData)
        self.Button_Exit.place(relx=0.200, rely=0.788, height=42, width=100, bordermode='ignore')
        self.Button_Exit.configure(activebackground="#ececec")
        self.Button_Exit.configure(activeforeground="#000000")
        self.Button_Exit.configure(background="#d9d9d9")
        self.Button_Exit.configure(disabledforeground="#a3a3a3")
        self.Button_Exit.configure(foreground="#000000")
        self.Button_Exit.configure(highlightbackground="#d9d9d9")
        self.Button_Exit.configure(highlightcolor="black")
        self.Button_Exit.configure(pady="0")
        self.Button_Exit.configure(text=_('''Exit'''))
        self.Button_Exit.configure(command=destroy_window)
        self.tooltip_font = "TkDefaultFont"
        self.Button_Exit_tooltip = \
        ToolTip(self.Button_Exit, self.tooltip_font, _('''Exit program.'''))






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


if __name__ == '__main__':
    vp_start_gui()
