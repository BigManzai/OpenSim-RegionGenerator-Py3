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
     �  A  �  ;  1  P   m  �   �  �   �  �   F  C   �       -  "     P  4   f     �     �     �  #   �     �  #   �               "     0  l   C     �  D   �  V   �  I  Q     �  "   �     �     �  0   �  0        H     \     p     �     �     �  
   �  	   �     �     �  -        >     P     b     n     z  #   �     �     �     �     �     �     �  K  �     7  A  V  ;  �  P   �  �   %  �   �  �   �  C   =      �          7       +   8                (            
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
PO-Revision-Date: 2020-10-05 19:27+0200
Last-Translator: 
Language-Team: 
Language: en_US
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Generated-By: pygettext.py 1.5
X-Generator: Poedit 2.4.1
Plural-Forms: nplurals=2; plural=(n != 1);
 Allow Alternate Ports AllowAlternatePorts Not Used.
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
blank creates a random. turn on 