��    9      �  O   �      �     �  4   �     4     D     J  #   Q     u  #   �     �     �     �     �  l   �     I  D   N  V   �  I  �     4  "   E     h     v  0     0   �     �     �     		     	     4	     L	  
   k	  	   v	     �	     �	  -   �	     �	     �	     �	     
     
  #   
     C
     Q
     `
     n
     w
     
  K  �
     �  A  �  ;  1  P   m  �   �  �   �  �   F  C   �       -  "     P  D   i     �     �  	   �  %   �  
   �  '   
     2  
   I     T     j  k   |     �  M   �  V   <  �  �       !   .     P     ^  @   g  <   �     �     �          &     <     S     r  	   ~     �     �  4   �     �            
   %     0  2   <     o     �     �     �     �     �  �  �  $   l  �  �  �     g   �       �   !  �   �!  \   �"     #         7       +   8                (            
       	          &                    #            -       !                 1   2       5          %      6      0   "          /                            $           ,         9              '   *   )   .       3   4                 Allow Alternate Ports AllowAlternatePorts Not Used.
Leave it always False. Clamp Prim Size Clear Create Creating the region configurations. Default Landing Default Landing
example: 128,128,21 Delete data. Exit Exit program. External Host Name External IP Address of the router or FQDN.
(must be the same for all regions on file)
Blank creates SYSTEMIP Help IP port for all incoming client connections.
Blank creates a random. If size is not specified it will
default to the legacy size of 256.
blank creates 256. If true then if a viewer attempts to create a prim which has any dimension larger than the NonphysicalPrimMax,
then that dimension is reduced to NonphysicalPrimMax.
Default is false; This setting can also be used in the [Startup] section of OpenSim.ini.
If the region setting exists then it will override the OpenSim.ini setting. Internal Address Internal Address
standard: 0.0.0.0 Internal Port Location Location x
example: 5000
blank creates a random. Location y
example: 5000
blank creates a random. Maptile Static File Maptile Static UUID MaptileStaticFile Master Avatar First Name Master Avatar Last Name Master Avatar Sandbox Password Max Agents Max Prims Max Prims Per User Non Physical Prim Max Number of prims that each user has available. Number of regions Physical Prim Max Region Name Region Type Region UUID Region UUID
blank creates a random. Request help. Resolve Adress ResolveAdress Scope ID ScopeID Size The created region configuration files only need to be moved to the Regions directory.

Then restart the OpenSimulator.

Please a maximum of 15 standard regions per OpenSimulator when using mySQL.

If you use mesh on your regions, please drastically reduce the number of regions per OpenSimulator.

If you use a lot of mesh and scripts, it is better to only use one region per OpenSimulator.

Variable VAR regions should always run individually.

When using sqLite you should be careful, a region with around 6000 prims is roughly the limit, after which errors can occur in the database. The desired number of regions. The maximum dimensions for a non-physical prim.
This is a single number which applies to X, Y and Z co-ordinates.
This will affect resizing of existing prims. Default is 256.
This setting can also be used in the [Startup] section of OpenSim.ini.
If the region setting exists then it will override the OpenSim.ini setting. The maximum dimensions of a physical prim. This is a single number which applies to X, Y and Z co-ordinates.
This will affect resizing of existing prims. Default is 10.
This setting can also be used in the [Startup] section of OpenSim.ini.
If the region setting exists then it will override the OpenSim.ini setting. The maximum number of agents that can be in the in the region at any given time. The maximum number of prims that the region will be listed as supporting.
However, this limit is not currently enforced by OpenSimulator.
Due to LL protocol constraints,
the maximum limit that can be shown is 45000. The region type as shown in the Covenant tab of the Region/Estate dialog in a standard Second Life viewer.
Can be used to specify Mainland, Estate, etc. based on type of grid. UUID of texture to use as a maptile for this region.
Only set if you have disabled dynamic generation of the map tile from the region contents. insert region name
example: My Virtual Land
blank creates a random. turn on Project-Id-Version: 
PO-Revision-Date: 2020-10-05 19:26+0200
Last-Translator: 
Language-Team: 
Language: de_DE
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Generated-By: pygettext.py 1.5
X-Generator: Poedit 2.4.1
Plural-Forms: nplurals=2; plural=(n != 1);
 Alternate Ports zulassen AllowAlternatePorts wird nicht verwendet.
Lassen Sie es immer false. Clamp Prim Größe Zurücksetzen Erstellen Erstellen der Regionskonfigurationen. Landepunkt Standardlandepunkt
Beispiel: 128,128,21 Dateneingabe löschen. Schließen Beendet das Programm. Externer Hostname Externe IP-Adresse des Routers oder FQDN.
(muss für alle Dateiregionen gleich sein)
Leer erstellt SYSTEMIP Hilfe IP-Port für alle eingehenden Clientverbindungen.
Leer erzeugt einen Zufalls. Wenn die Größe nicht angegeben ist, wird
Standardgröße von 256.
leer erstellt 256. Wenn true, dann, wenn ein Betrachter versucht, einen Prim zu erstellen, die eine Dimension größer als die nonphysicalPrimMax hat,
dann wird diese Dimension auf NonphysicalPrimMax reduziert.
Der Standardwert ist false; Diese Einstellung kann auch im Abschnitt [Startup] von OpenSim.ini verwendet werden.
Wenn die Regionseinstellung vorhanden ist, überschreibt sie die Einstellung OpenSim.ini. Interne Adresse Interne Adresse
Standard: 0.0.0.0 Interner Port Standort Standort x
Beispiel: 5000
leer wird ein Zufallsprinzip erstellt. Lage y
Beispiel: 5000
leer wird ein Zufallsprinzip erstellt. Maptile Statische Datei Maptile Statische UUID MaptileStaticFile Master Avatar Vorname Master Avatar Nachname Master Avatar Sandbox Passwort Max Agenten Max Prims Max Prims pro Benutzer Nicht physische prim Max Anzahl der prims, über die jeder Benutzer verfügt. Anzahl der Regionen Physischer Prim Max Name der Region Regionstyp Region UUID Region UUID
leer wird ein Zufallsprinzip erstellt. Bitten Sie um Hilfe. Auflösungsadresse ResolveAdress Bereichs ID Bereichs ID Größe Die erstellten Regionskonfigurationsdateien müssen nur in das Verzeichnis Regionen verschoben werden.

Starten Sie dann den OpenSimulator neu.

Bitte maximal 15 Standardregionen pro OpenSimulator, wenn Sie mySQL verwenden.

Wenn Sie Mesh in Ihren Regionen verwenden, reduzieren Sie die Anzahl der Regionen pro OpenSimulator drastisch.

Wenn Sie viele Netze und Skripts verwenden, ist es besser, nur eine Region pro OpenSimulator zu verwenden.

Variable VAR-Regionen sollten immer einzeln ausgeführt werden.

Bei der Verwendung von sqLite sollten Sie vorsichtig sein, eine Region mit rund 6000 Prims ist ungefähr die Grenze, nach der Fehler in der Datenbank auftreten können. Die gewünschte Anzahl von Regionen. Die maximalen Dimensionen für einen nicht-physischen Prim.
Dies ist eine einzelne Zahl, die für X-, Y- und Z-Koordinaten gilt.
Dies wirkt sich auf die Größenänderung der vorhandenen Prims aus. Der Standardwert ist 256.
Diese Einstellung kann auch im Abschnitt [Startup] von OpenSim.ini verwendet werden.
Wenn die Regionseinstellung vorhanden ist, überschreibt sie die Einstellung OpenSim.ini. Die maximalen Abmessungen eines physikalischen Prims. Dies ist eine einzelne Zahl, die für X-, Y- und Z-Koordinaten gilt.
Dies wirkt sich auf die Größenänderung der vorhandenen Prims aus. Der Standardwert ist 10.
Diese Einstellung kann auch im Abschnitt [Startup] von OpenSim.ini verwendet werden.
Wenn die Regionseinstellung vorhanden ist, überschreibt sie die Einstellung OpenSim.ini. Die maximale Anzahl von Agenten, die sich zu einem bestimmten Zeitpunkt in der Region befinden können. Die maximale Anzahl von Prims, die von der Region als unterstützend aufgeführt werden.
Dieses Limit wird derzeit jedoch von OpenSimulator nicht erzwungen.
Aufgrund von LL-Protokolleinschränkungen
die maximale Grenze, die angezeigt werden kann, ist 45000. Der Regionstyp, wie auf der Registerkarte "Bündnis" des Dialogfelds Region/Estate in einem standardmäßigen Second Life-Viewer angezeigt.
Kann verwendet werden, um Festland, Nachlass usw. basierend auf dem Rastertyp anzugeben. UUID der Textur, die als Maptile für diese Region verwendet werden soll.
Wird nur festgelegt, wenn Sie die dynamische Generierung der Kartenkachel aus dem Regionsinhalt deaktiviert haben. Bereichsname einfügen
Beispiel: Mein virtuelles Land
leer wird ein Zufallsprinzip erstellt. einschalten 