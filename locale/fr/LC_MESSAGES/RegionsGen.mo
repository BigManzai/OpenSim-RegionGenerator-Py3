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
     �  A  �  ;  1  P   m  �   �  �   �  �   F  C   �       )  "     L  ;   l     �     �     �  (   �     �  -        <     T     \     q  �   �       O     d   b  v  �     >     N     m     z  6   �  6   �     �          #     5     S  "   p  
   �  	   �     �     �  4   �                2     F     V  '   c     �     �     �     �     �     �  �  �      �  q  �  o  a  S   �  �   %   �   #!  �   
"  U   �"     $#         7       +   8                (            
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
PO-Revision-Date: 2020-10-05 19:28+0200
Last-Translator: 
Language-Team: 
Language: fr
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Generated-By: pygettext.py 1.5
X-Generator: Poedit 2.4.1
Plural-Forms: nplurals=2; plural=(n > 1);
 Autoriser les ports alternatifs AllowAlternatePorts non utilisé.
Laissez-le toujours faux. Taille prim de pince Effacer Créer Création des configurations de région. Atterrissage par défaut Atterrissage par défaut
exemple : 128 128,21 Supprimez les données. Quitter Programme de sortie. Nom de l’hôte externe Adresse IP externe du routeur ou du nom de domaine.
(doit être le même pour toutes les régions du dossier)
Blank crée SYSTEMIP Aide Port IP pour toutes les connexions client entrantes.
Blank crée un aléatoire. Si la taille n’est pas spécifiée, il
par défaut à la taille héritée de 256.
blanc crée 256. Si c’est vrai, si un spectateur tente de créer un prim qui a une dimension plus grande que le NonphysicalPrimMax,
alors cette dimension est réduite à NonphysicalPrimMax.
La valeur par défaut est fausse ; Ce paramètre peut également être utilisé dans la section [Startup] d’OpenSim.ini.
Si le paramètre de région existe, il remplacera le paramètre OpenSim.ini. Adresse interne Adresse interne
norme: 0.0.0.0 Port interne Emplacement Emplacement x
exemple: 5000
blanc crée un aléatoire. Emplacement y
exemple: 5000
blanc crée un aléatoire. Fichier statique Maptile Maptile Statique UUID MaptileStaticFile Nom de maître Avatar Prénom Nom de famille Master Avatar Mot de passe master Avatar Sandbox Max Agents Max Prims Prims max par utilisateur Non physique Prim Max Nombre de prims disponibles pour chaque utilisateur. Nombre de régions Physique Prim Max Nom de la région
  Type de région Région UUID Région UUID
blanc crée un aléatoire. Demandez de l’aide. Résoudre l’adresse ResolveAdresse ID d’étendue ScopeID Taille Les fichiers de configuration de région créés doivent uniquement être déplacés vers le répertoire Régions.

Redémarrez ensuite le OpenSimulator.

Veuillez utiliser mySQL, un maximum de 15 régions standard par OpenSimulator.

Si vous utilisez des mailles sur vos régions, réduisez considérablement le nombre de régions par OpenSimulator.

Si vous utilisez beaucoup de mailles et de scripts, il est préférable d’utiliser seulement une région par OpenSimulator.

Les régions VAR variables doivent toujours fonctionner individuellement.

Lors de l’utilisation sqLite vous devez être prudent, une région avec environ 6000 prims est à peu près la limite, après quoi des erreurs peuvent se produire dans la base de données. Le nombre souhaité de régions. Dimensions maximales pour un prim non physique.
Il s’agit d’un numéro unique qui s’applique aux coordonnées X, Y et Z.
Cela affectera la redimensionnement des prims existants. Par défaut est 256.
Ce paramètre peut également être utilisé dans la section [Startup] d’OpenSim.ini.
Si le paramètre de région existe, il remplacera le paramètre OpenSim.ini. Les dimensions maximales d’un prim physique. Il s’agit d’un numéro unique qui s’applique aux coordonnées X, Y et Z.
Cela affectera la redimensionnement des prims existants. Par défaut est 10.
Ce paramètre peut également être utilisé dans la section [Startup] d’OpenSim.ini.
Si le paramètre de région existe, il remplacera le paramètre OpenSim.ini. Le nombre maximum d’agents qui peuvent être dans la région à un moment donné. Le nombre maximal de prims que la région sera répertorié comme support.
Toutefois, cette limite n’est pas actuellement appliquée par OpenSimulator.
En raison de contraintes de protocole LL,
la limite maximale qui peut être affichée est de 45000. Type de région comme indiqué dans l’onglet Pacte de la boîte de dialogue Région/Succession dans une visionneuse Seconde Vie standard.
Peut être utilisé pour spécifier continent, domaine, etc en fonction du type de grille. UUID de texture à utiliser comme maptile pour cette région.
Définissez uniquement si vous avez désactivé la génération dynamique de la vignette de carte à partir du contenu de la région. insérer le nom de la région
exemple : Ma terre virtuelle
blanc crée un aléatoire. s’allumer 