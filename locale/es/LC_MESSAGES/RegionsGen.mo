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
     �  A  �  ;  1  P   m  �   �  �   �  �   F  C   �       *  "     M  9   k     �     �     �  ,   �     �  *        @     P     V     j  t   �     �  \   �  L   Y  ~  �     %  %   8     ^  
   m  2   x  2   �     �     �               8  %   R     x  	   �     �     �  3   �     �               +     ;  *   N     y     �     �     �     �     �  �  �     z  s  �  s    P   �  �   �  �   �   �   �!  S   P"     �"         7       +   8                (            
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
Language: es
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Generated-By: pygettext.py 1.5
X-Generator: Poedit 2.4.1
Plural-Forms: nplurals=2; plural=(n != 1);
 Permitir puertos alternativos AllowAlternatePorts no utilizados.
Déjalo siempre Falso. Tamaño de la abrazadera Prim Limpiar Crear Creación de las configuraciones de región. Aterrizaje por defecto Aterrizaje por defecto
ejemplo: 128.128,21 Eliminar datos. Salir Salir del programa. Nombre de host externo Dirección IP externa del router o FQDN.
(debe ser el mismo para todas las regiones registradas)
Blank crea SYSTEMIP Ayuda Puerto IP para todas las conexiones de cliente entrantes.
El espacio en blanco crea un azar. Si no se especifica el tamaño,
tamaño heredado de 256.
en blanco crea 256. Si es true, entonces si un espectador intenta crear un prim que tiene cualquier dimensión mayor que el NonphysicalPrimMax,
entonces esa dimensión se reduce a NonphysicalPrimMax.
El valor predeterminado es false; Este ajuste también se puede utilizar en la sección [Startup] de OpenSim.ini.
Si existe la configuración de la región, invalidará la configuración de OpenSim.ini. Dirección interna Dirección interna
estándar: 0.0.0.0 Puerto interno Ubicación Ubicación x
ejemplo: 5000
en blanco crea un azar. Ubicación y
ejemplo: 5000
en blanco crea un azar. Archivo estático Maptile Maptile Static UUID MaptileStaticFile Nombre del avatar maestro Nombre del avatar maestro Contraseña de Maestro Avatar Sandbox Max Agentes Max Prims Máximo prims por usuario No Físico Prim Max Número de prims que cada usuario tiene disponible. Número de regiones Physical Prim Max Nombre de la Región Tipo de región UUID de la región UUID de la región
en blanco crea un azar. Solicite ayuda. Resolver la dirección ResolveAdress Identificador de ámbito ScopeID Tamaño Los archivos de configuración de región creados solo deben moverse al directorio Regiones.

A continuación, reinicie OpenSimulator.

Por favor, un máximo de 15 regiones estándar por OpenSimulator cuando utilice mySQL.

Si utiliza malla en sus regiones, reduzca drásticamente el número de regiones por OpenSimulator.

Si utiliza una gran cantidad de malla y scripts, es mejor utilizar solo una región por OpenSimulator.

Las regiones VAR variables siempre deben ejecutarse individualmente.

Al utilizar sqLite debe tener cuidado, una región con alrededor de 6000 prims es aproximadamente el límite, después de lo cual pueden producirse errores en la base de datos. El número deseado de regiones. Las cotas máximas para un prim no físico.
Este es un solo número que se aplica a las coordenadas X, Y y Z.
Esto afectará al cambio de tamaño de las cebas existentes. El valor predeterminado es 256.
Este ajuste también se puede utilizar en la sección [Startup] de OpenSim.ini.
Si existe la configuración de la región, invalidará la configuración de OpenSim.ini. Las dimensiones máximas de un prim físico. Este es un solo número que se aplica a las coordenadas X, Y y Z.
Esto afectará al cambio de tamaño de las cebas existentes. El valor predeterminado es 10.
Este ajuste también se puede utilizar en la sección [Startup] de OpenSim.ini.
Si existe la configuración de la región, invalidará la configuración de OpenSim.ini. El número máximo de agentes que pueden estar en la región en un momento dado. El número máximo de prims que la región aparecerá como soporte.
Sin embargo, OpenSimulator no aplica actualmente este límite.
Debido a las restricciones del protocolo LL,
el límite máximo que se puede mostrar es 45000. Escriba el tipo de región como se muestra en la pestaña Pacto del cuadro de diálogo Región/Estate en un visor de Second Life estándar.
Se puede utilizar para especificar mainland, Estate, etc. en función del tipo de cuadrícula. UUID de textura para usar como maptil para esta región.
Solo se establece si ha deshabilitado la generación dinámica del icono de mapa a partir del contenido de la región. insertar el nombre de la región
ejemplo: Mi Tierra Virtual
en blanco crea un azar. prender 