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
     �  A  �  ;  1  P   m  �   �  �   �  �   F  C   �       s  "  :   �  ~   �     P     m     ~  9   �  &   �  ?   �     .  
   K  $   V  $   {  �   �     h  �   u  �   �  P  �     �  9        A     _  ]   |  ]   �  *   8  &   c     �      �  (   �  9   �     -     C  1   W  +   �  b   �  %     &   >     e     �     �  A   �      �          *  6   G     ~     �  0  �  3   �"  <  #  -  I%  �   w'  �  (  R  �)  C  +  �   \,     �,         7       +   8                (            
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
PO-Revision-Date: 2020-10-08 14:22+0200
Language-Team: 
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Generated-By: pygettext.py 1.5
X-Generator: Poedit 2.4.1
Last-Translator: 
Plural-Forms: nplurals=3; plural=(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<12 || n%100>14) ? 1 : 2);
Language: ru
 Разрешить альтернативные порты РазрешитьАлтернатПорты не используются.
Оставьте его всегда ложным. Зажим Prim размер Очистить Создать Создание конфигураций региона. Посадка по умолчанию Посадка по умолчанию
пример: 128 128,21 Удалить данные. Выход Выходная программа. Внешнее имя хозяина Внешний IP-адрес маршрутизатора или F-DN.
(должен быть одинаковым для всех регионов в файле)
Пустой создает SYSTEMIP Помощь IP-порт для всех входящих клиентских подключений.
Пустой создает случайный. Если размер не указан, он
по умолчанию до устаревшего размера 256.
пустой создает 256. Если это правда, то если зритель пытается создать чопопор, который имеет любое измерение больше, чем NonphysicalPrimMax,
то, что измерение сводится к nonphysicalPrimMax.
По умолчанию является ложным; Эта настройка также может быть использована в разделе «Стартап» OpenSim.ini.
Если параметр региона существует, то он переопределит параметр OpenSim.ini. Внутренний адрес Внутренний адрес
стандарт: 0.0.0.0 Внутренний порт Местоположение Расположение x
пример: 5000
пустой создает случайные. Расположение y
пример: 5000
пустой создает случайные. Карта Статический файл Карта Статический UUID КартаСтатикФиле Мастер Аватар Имя Мастер Аватар Фамилия Мастер Аватар Песочница Пароль Макс Агенты Макс Примс Макс Примс на пользователя Не физический Прим Макс Количество чопорных, доступных каждому пользователю. Количество регионов Физический Прим Макс Название региона Тип региона Регион UUID Регион UUID
пустой создает случайные. Запросите помощь. Разрешить Adress РешимостьАдрес Идентификатор сферы действия Сфера действия Размер Созданные файлы конфигурации регионов только должны быть перемещены в каталог регионов.

Затем перезапустим OpenSimulator.

Пожалуйста, максимум 15 стандартных регионов на OpenSimulator при использовании myS'L.

Если вы используете сетку в регионах, пожалуйста, резко сократите количество регионов на OpenSimulator.

Если вы используете много сетки и скриптов, лучше использовать только один регион на OpenSimulator.

Переменные регионы VAR должны всегда работать индивидуально.

При использовании sqLite следует быть осторожным, область с около 6000 prims примерно предел, после чего ошибки могут возникнуть в базе данных. Нужное количество регионов. Максимальные размеры для не-физической чопорной.
Это единое число, которое относится к X, Y и й координирует.
Это повлияет на размер существующих чопорных. По умолчанию 256.
Эта настройка также может быть использована в разделе «Стартап» OpenSim.ini.
Если параметр региона существует, то он переопределит параметр OpenSim.ini. Максимальные размеры физического чопора. Это единое число, которое относится к X, Y и й координирует.
Это повлияет на размер существующих чопорных. По умолчанию 10.
Эта настройка также может быть использована в разделе «Стартап» OpenSim.ini.
Если параметр региона существует, то он переопределит параметр OpenSim.ini. Максимальное количество агентов, которые могут быть в регионе в любой момент времени. Максимальное количество чопорных, что регион будет указан в качестве поддержки.
Однако в настоящее время этот предел не соблюдается OpenSimulator.
Из-за ограничений протокола LL
максимальный предел, который может быть показан, составляет 45000. Тип региона, как показано на вкладке Пакта Диалога Региона/Эстейт в стандартном просмотре Second Life.
Может быть использован для казать материк, имущество и т.д. в зависимости от типа сетки. UUID текстуры для использования в качестве картографа для этого региона.
Набор только в том случае, если вы отключили динамическое поколение плитки карты из содержимого региона. вставить имя региона
пример: Моя виртуальная земля
пустой создает случайные. нажать вкл 