Þ    9      ä  O   ¬      è     é  4   ÿ     4     D     J  #   Q     u  #        ©     ¶     »     É  l   Ü     I  D   N  V     I  ê     4  "   E     h     v  0     0   °     á     õ     		     	     4	     L	  
   k	  	   v	     	     	  -   ©	     ×	     é	     û	     
     
  #   
     C
     Q
     `
     n
     w
     
  K  
     Ð  A  ï  ;  1  P   m  ×   ¾  ¯        F  C   Ö       #  "     F  V   e     ¼  	   Û     å  *   ì       (   0     Y     x  $        ¤  ¯   ·  	   g  h   q      Ú  º  {     6  "   I     l     |  =     =   Á  $   ÿ  (   $  0   M     ~       <   ¹     ö       *   %     P  3   o     £     ¹     Õ     è       6     '   D     l               ®  	   ¾  N  È         6    Õ   N   o"  ö   ¾"    µ#  Ñ   ¸$  a   %  	   ì%         7       +   8                (            
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
PO-Revision-Date: 2020-10-08 14:21+0200
Language-Team: 
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Generated-By: pygettext.py 1.5
X-Generator: Poedit 2.4.1
Last-Translator: 
Plural-Forms: nplurals=1; plural=0;
Language: ja
 ä»£æ¿ãã¼ããè¨±å¯ãã ä»£æ¿ãã¼ããä½¿ç¨ãã¾ããã
å¸¸ã« False ã®ã¾ã¾ã«ãã¦ããã¾ãã ã¯ã©ã³ãããªã ãµã¤ãº ã¯ãªã¢ ä½æ ãªã¼ã¸ã§ã³æ§æãä½æãã¾ãã ããã©ã«ãã®çé¸ ããã©ã«ãã®çé¸
ä¾: 128,128,21 ãã¼ã¿ãåé¤ãã¾ãã çµäº ãã­ã°ã©ã ãçµäºãã¾ãã å¤é¨ãã¹ãå ã«ã¼ã¿ã¼ã¾ãã¯ FQDN ã®å¤é¨ IP ã¢ãã¬ã¹ã
(ãã¡ã¤ã«ä¸ã®ãã¹ã¦ã®é åã§åãã§ãªããã°ãªãã¾ãã)
ç©ºç½ã¯ã·ã¹ãã IPãä½æãã¾ã ãã«ã ãã¹ã¦ã®çä¿¡ã¯ã©ã¤ã¢ã³ãæ¥ç¶ã® IP ãã¼ãã
ç©ºç½ã¯ã©ã³ãã ãä½æãã¾ãã size ãæå®ããã¦ããªãå ´åã¯ããµã¤ãº
ããã©ã«ãã¯ã256 ã®å¾æ¥ã®ãµã¤ãºã«è¨­å®ããã¾ãã
ç©ºç½ã¯ 256 ãä½æãã¾ãã ãã true ãªããè¦è´èãéç©çPrimMaxããå¤§ããªæ¬¡åãæã¤ããªã ãä½æãããã¨ããå ´åã
ãã®å¾ããã®æ¬¡åã¯éç©çããªã ããã¯ã¹ã«æ¸å°ãã¾ãã
ããã©ã«ãã¯ false ã§ãããã®è¨­å®ã¯ OpenSim.ini ã® [ã¹ã¿ã¼ãã¢ãã] ã»ã¯ã·ã§ã³ã§ãä½¿ç¨ã§ãã¾ãã
ãªã¼ã¸ã§ã³è¨­å®ãå­å¨ããå ´åã¯ãOpenSim.ini è¨­å®ããªã¼ãã¼ã©ã¤ãããã¾ãã åé¨ã¢ãã¬ã¹ åé¨ã¢ãã¬ã¹
æ¨æº: 0.0.0.0 åé¨ãã¼ã å ´æ ä½ç½® x
ä¾: 5000
ç©ºç½ã¯ã©ã³ãã ãä½æãã¾ãã ä½ç½® y
ä¾: 5000
ç©ºç½ã¯ã©ã³ãã ãä½æãã¾ãã ãããã¿ã¤ã«éçãã¡ã¤ã« ãããã¿ã¤ã«ã¹ã¿ãã£ãã¯UUID ãã¡ã¤ã«ããããã¿ã¤ã«ã§è¡¨ç¤ºãã ãã¹ã¿ã¼ã¢ãã¿ã¼å ãã¹ã¿ã¼ã¢ãã¿ã¼ã®å§ ãã¹ã¿ã¼ã¢ãã¿ã¼ãµã³ãããã¯ã¹ãã¹ã¯ã¼ã æå¤§ã¨ã¼ã¸ã§ã³ã ããã¯ã¹ããªã  ã¦ã¼ã¶ã¼ãããã®æå¤§ããªã æ° éç©çããªã ããã¯ã¹ åã¦ã¼ã¶ã¼ãä½¿ç¨ã§ããããªã ã®æ°ã ãªã¼ã¸ã§ã³ã®æ° ç©çããªã ããã¯ã¹ ãªã¼ã¸ã§ã³å ãªã¼ã¸ã§ã³ã®ç¨®é¡ å°å UUID å°å UUID
ç©ºç½ã¯ã©ã³ãã ãä½æãã¾ãã ãã«ãããªã¯ã¨ã¹ããã¾ãã ãã¬ã¹ãè§£æ±ºãã ãªã¾ã«ãã¢ãã¬ã¹ ã¹ã³ã¼ã ID ã¹ã³ã¼ã ID ãµã¤ãº ä½æãããé åæ§æãã¡ã¤ã«ã¯ãRegions ãã£ã¬ã¯ããªã«ç§»åããã ãã§æ¸ã¿ã¾ãã

ãã®å¾ããªã¼ãã³ã·ãã¥ã¬ã¼ã¿ãåèµ·åãã¾ãã

mySQL ãä½¿ç¨ããå ´åã¯ãOpenSimulator ãã¨ã«æå¤§ 15 ã®æ¨æºãªã¼ã¸ã§ã³ãä½¿ç¨ãã¦ãã ããã

ãä½¿ãã®å°åã§ã¡ãã·ã¥ãä½¿ç¨ããå ´åã¯ãOpenSimulator ãããã®é åæ°ãå¤§å¹ã«æ¸ããã¦ãã ããã

ã¡ãã·ã¥ã¨ã¹ã¯ãªãããå¤ãä½¿ç¨ããå ´åã¯ãOpenSimulator ãã¨ã« 1 ã¤ã®é åã®ã¿ãä½¿ç¨ãããã¨ããããã¾ãã

å¯å¤ã® VAR é åã¯ãå¸¸ã«åå¥ã«å®è¡ããå¿è¦ãããã¾ãã

sqLite ãä½¿ç¨ããå ´åã¯ãç´ 6000 ããªã ãæã¤é åãã»ã¼éçã§ããããã®å¾ã«ãã¼ã¿ãã¼ã¹ã§ã¨ã©ã¼ãçºçããå¯è½æ§ãããã¾ãã å¿è¦ãªãªã¼ã¸ã§ã³æ°ã éç©çããªã ã®æå¤§ãµã¤ãºã
ããã¯ãXãYãZ åº§æ¨ã«é©ç¨ãããåä¸ã®æ°å¤ã§ãã
ããã¯æ¢å­ã®ããªã ã®ãµã¤ãºå¤æ´ã«å½±é¿ãã¾ããããã©ã«ãã¯ 256 ã§ãã
ãã®è¨­å®ã¯ OpenSim.ini ã® [ã¹ã¿ã¼ãã¢ãã] ã»ã¯ã·ã§ã³ã§ãä½¿ç¨ã§ãã¾ãã
ãªã¼ã¸ã§ã³è¨­å®ãå­å¨ããå ´åã¯ãOpenSim.ini è¨­å®ããªã¼ãã¼ã©ã¤ãããã¾ãã ç©çããªã ã®æå¤§ãµã¤ãºãããã¯ãXãYãZ åº§æ¨ã«é©ç¨ãããåä¸ã®æ°å¤ã§ãã
ããã¯æ¢å­ã®ããªã ã®ãµã¤ãºå¤æ´ã«å½±é¿ãã¾ããããã©ã«ãã¯ 10 ã§ãã
ãã®è¨­å®ã¯ OpenSim.ini ã® [ã¹ã¿ã¼ãã¢ãã] ã»ã¯ã·ã§ã³ã§ãä½¿ç¨ã§ãã¾ãã
ãªã¼ã¸ã§ã³è¨­å®ãå­å¨ããå ´åã¯ãOpenSim.ini è¨­å®ããªã¼ãã¼ã©ã¤ãããã¾ãã ç¹å®ã®æç¹ã§é ååã«å­å¨ã§ããã¨ã¼ã¸ã§ã³ãã®æå¤§æ°ã å°åããµãã¼ãã¨ãã¦ãªã¹ããããããªã ã®æå¤§æ°ã
ãã ãããã®å¶éã¯ç¾å¨ãOpenSimulator ã«ãã£ã¦å¼·å¶ããã¦ãã¾ããã
LL ãã­ãã³ã«ã®å¶ç´ã«ããã
è¡¨ç¤ºã§ããä¸éã¯ 45000 ã§ãã æ¨æºã®ã»ã«ã³ãã©ã¤ããã¥ã¼ã¢ã®[ãªã¼ã¸ã§ã³/ä¸åç£]ãã¤ã¢ã­ã°ã®[ã³ã´ãã³ã]ã¿ãã«è¡¨ç¤ºãããé åã¿ã¤ãã
ã°ãªããã®ç¨®é¡ã«åºã¥ãã¦ãæ¬åãä¸åç£ãªã©ãæå®ããããã«ä½¿ç¨ã§ãã¾ãã ãã®é åã®ãããã¿ã¤ã«ã¨ãã¦ä½¿ç¨ãããã¯ã¹ãã£ã® UUIDã
ãªã¼ã¸ã§ã³ ã³ã³ãã³ãããããã ã¿ã¤ã«ã®åççæãç¡å¹ã«ãã¦ããå ´åã«ã®ã¿è¨­å®ãã¾ãã é ååã®æ¿å¥
ä¾: ãã¤ãã¼ãã£ã«ã©ã³ã
ç©ºç½ã¯ã©ã³ãã ãä½æãã¾ãã ç¹ãã 