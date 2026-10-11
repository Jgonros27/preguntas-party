"""Nombres conocidos para representar, dibujar o describir sin palabras clave."""
PEOPLE = '''
Harry Potter|Hogwarts,Varita,Cicatriz,Mago
Hermione Granger|Hogwarts,Varita,Harry,Ron
Ron Weasley|Hogwarts,Harry,Hermione,Pelirrojo
Voldemort|Harry,Mago,Oscuro,Nariz
Dumbledore|Hogwarts,Director,Barba,Mago
Hagrid|Hogwarts,Gigante,Barba,Harry
Dobby|Elfo,Calcetín,Harry,Libre
Spider-Man|Telaraña,Araña,Peter,Parker
Batman|Murciélago,Gotham,Robin,Bruce
Superman|Krypton,Capa,Clark,Vuelo
Wonder Woman|Lazo,Amazona,Diana,Heroína
Iron Man|Armadura,Tony,Stark,Vengadores
Hulk|Verde,Fuerza,Bruce,Banner
Thor|Martillo,Trueno,Asgard,Dios
Capitán América|Escudo,Steve,Rogers,Vengadores
Lobezno|Garras,Mutante,Logan,Metal
Deadpool|Máscara,Rojo,Mercenario,Marvel
Black Panther|Wakanda,Rey,Marvel,Traje
Thanos|Guante,Piedras,Vengadores,Chasquido
Doctor Strange|Mago,Marvel,Portal,Capa
Joker|Payaso,Batman,Gotham,Sonrisa
Harley Quinn|Joker,Bate,Payasa,Gotham
Darth Vader|Casco,Negro,Fuerza,Star Wars
Luke Skywalker|Jedi,Espada,Fuerza,Star Wars
Princesa Leia|Star Wars,Moños,Rebelión,Luke
Yoda|Verde,Pequeño,Jedi,Fuerza
Chewbacca|Peludo,Wookiee,Han,Star Wars
R2-D2|Robot,Azul,Blanco,Star Wars
C-3PO|Robot,Dorado,Idioma,Star Wars
Han Solo|Star Wars,Piloto,Falcón,Chewbacca
Obi-Wan Kenobi|Jedi,Fuerza,Star Wars,Maestro
Mandaloriano|Casco,Star Wars,Grogu,Cazarrecompensas
Frodo|Anillo,Hobbit,Mordor,Bolsón
Gandalf|Mago,Barba,Bastón,Anillo
Gollum|Anillo,Tesoro,Hobbit,Mordor
Legolas|Elfo,Arco,Flecha,Anillo
Aragorn|Rey,Espada,Anillo,Gondor
Bilbo Bolsón|Hobbit,Anillo,Dragón,Aventura
Sherlock Holmes|Detective,Watson,Lupa,Londres
Indiana Jones|Sombrero,Látigo,Arqueólogo,Aventura
James Bond|Espía,Agente,007,Licencia
Jack Sparrow|Pirata,Barco,Caribe,Brújula
Forrest Gump|Correr,Chocolate,Banco,Tom Hanks
Rocky Balboa|Boxeo,Guantes,Stallone,Filadelfia
Terminator|Robot,Futuro,Schwarzenegger,Máquina
Mary Poppins|Paraguas,Niñera,Magia,Bolso
Miércoles Addams|Trenzas,Negro,Familia,Mano
Morticia Addams|Negro,Familia,Melena,Gómez
Gómez Addams|Familia,Bigote,Morticia,Traje
Mano de los Addams|Dedos,Familia,Miércoles,Andar
Drácula|Vampiro,Sangre,Colmillos,Transilvania
Frankenstein|Monstruo,Tornillos,Electricidad,Criatura
King Kong|Gorila,Gigante,Rascacielos,Isla
Godzilla|Monstruo,Japón,Gigante,Reptil
E.T.|Extraterrestre,Bicicleta,Dedo,Casa
Pennywise|Payaso,Globo,Terror,Alcantarilla
Freddy Krueger|Pesadilla,Garras,Sombrero,Terror
Jason Voorhees|Máscara,Hockey,Terror,Viernes
Hannibal Lecter|Silencio,Corderos,Máscara,Caníbal
Zorro|Espada,Antifaz,Capa,Letra
Robinson Crusoe|Isla,Náufrago,Viernes,Supervivencia
Don Quijote|Molino,Sancho,Caballero,Cervantes
Sancho Panza|Quijote,Escudero,Burro,Cervantes
Robin Hood|Arco,Bosque,Robar,Pobres
Peter Pan|Volar,Nunca Jamás,Campanilla,Niño
Campanilla|Hada,Polvo,Peter Pan,Alas
Capitán Garfio|Pirata,Cocodrilo,Gancho,Peter Pan
Alicia|Maravillas,Conejo,Sombrero,País
Caperucita Roja|Lobo,Abuela,Bosque,Cesta
Cenicienta|Zapato,Calabaza,Medianoche,Príncipe
Blancanieves|Manzana,Enanos,Espejo,Princesa
Bella|Bestia,Libro,Castillo,Rosa
Bestia|Bella,Rosa,Castillo,Monstruo
Ariel|Sirena,Mar,Cola,Úrsula
Úrsula|Tentáculos,Sirena,Voz,Mar
Aladdín|Lámpara,Genio,Alfombra,Yasmín
Genio de Aladdín|Lámpara,Deseos,Azul,Magia
Yasmín|Aladdín,Princesa,Tigre,Alfombra
Jafar|Aladdín,Serpiente,Villano,Lámpara
Elsa|Hielo,Frozen,Reina,Anna
Anna de Frozen|Elsa,Nieve,Hermana,Olaf
Olaf|Nieve,Zanahoria,Frozen,Muñeco
Mulan|China,Guerrera,Dragón,Ejército
Pocahontas|Río,Mapache,Disney,Colonos
Vaiana|Océano,Maui,Barco,Isla
Maui|Vaiana,Anzuelo,Semidiós,Océano
Rapunzel|Pelo,Torre,Largo,Princesa
Maléfica|Cuernos,Dragón,Villana,Hechizo
Cruella de Vil|Dálmatas,Abrigo,Pelo,Villana
Simba|León,Rey,Mufasa,Nala
Mufasa|León,Rey,Simba,Padre
Scar|León,Cicatriz,Villano,Mufasa
Timón|Suricata,Pumba,Simba,Hakuna Matata
Pumba|Jabalí,Timón,Simba,Hakuna Matata
Rafiki|Mandril,Bastón,Simba,Rey León
Baloo|Oso,Selva,Mowgli,Libro
Mowgli|Niño,Selva,Baloo,Lobo
Bagheera|Pantera,Selva,Mowgli,Negra
Shere Khan|Tigre,Selva,Mowgli,Villano
Tarzán|Selva,Liana,Gorila,Jane
Jane de Tarzán|Selva,Gorila,Inglaterra,Exploración
Dumbo|Elefante,Orejas,Volar,Circo
Bambi|Ciervo,Bosque,Disney,Tambor
Pinocho|Nariz,Madera,Mentira,Grillo
Pepito Grillo|Pinocho,Conciencia,Insecto,Sombrero
Mickey Mouse|Ratón,Disney,Orejas,Minnie
Minnie Mouse|Ratón,Lazo,Disney,Mickey
Donald|Pato,Marinero,Disney,Daisy
Goofy|Disney,Alto,Amigo,Torpe
Pluto|Perro,Mickey,Disney,Collar
Winnie the Pooh|Oso,Miel,Disney,Amigos
Tigger|Tigre,Saltar,Pooh,Rayas
Woody|Vaquero,Toy Story,Sombrero,Juguete
Buzz Lightyear|Espacio,Toy Story,Infinito,Juguete
Jessie de Toy Story|Vaquera,Trenzas,Juguete,Woody
Rex de Toy Story|Dinosaurio,Verde,Juguete,Tímido
Nemo|Pez,Payaso,Mar,Buscar
Dory|Pez,Azul,Memoria,Nemo
Rayo McQueen|Coche,Carrera,Cars,Rojo
Mate de Cars|Grúa,Óxido,Coche,Rayo
Remy|Rata,Ratatouille,Cocinar,París
Wall-E|Robot,Basura,Espacio,Eva
Sulley|Monstruo,Azul,Pelo,Mike
Mike Wazowski|Monstruo,Verde,Ojo,Sulley
Alegría de Inside Out|Emoción,Amarillo,Riley,Sonrisa
Tristeza de Inside Out|Emoción,Azul,Riley,Llorar
Shrek|Ogro,Verde,Fiona,Pantano
Fiona|Shrek,Princesa,Ogro,Verde
Asno de Shrek|Burro,Ogro,Dragona,Hablar
Gato con Botas|Espada,Sombrero,Shrek,Ojos
Po de Kung Fu Panda|Panda,Kung Fu,Guerrero,Fideos
Gru|Minions,Villano,Luna,Despicable Me
Minion|Amarillo,Gafas,Gru,Plátano
Bob Esponja|Piña,Mar,Amarillo,Patricio
Patricio|Estrella,Rosa,Bob Esponja,Mar
Calamardo|Tentáculos,Bob Esponja,Clarinete,Mar
Don Cangrejo|Dinero,Bob Esponja,Restaurante,Pinzas
Pikachu|Pokémon,Amarillo,Rayo,Cola
Charmander|Pokémon,Fuego,Cola,Rojo
Squirtle|Pokémon,Tortuga,Agua,Azul
Bulbasaur|Pokémon,Planta,Verde,Semilla
Ash Ketchum|Pokémon,Pikachu,Gorra,Entrenador
Goku|Dragon Ball,Guerrero,Bolas,Kamehameha
Vegeta|Dragon Ball,Príncipe,Guerrero,Goku
Naruto|Ninja,Anime,Chakra,Naranja
Doraemon|Gato,Robot,Bolsillo,Nobita
Nobita|Doraemon,Gafas,Colegio,Torpe
Shin Chan|Niño,Anime,Travieso,Culo
Heidi|Montaña,Abuelo,Pedro,Cabra
Marco|Madre,Viaje,Mono,Italia
Inspector Gadget|Robot,Detective,Aparato,Sobrina
Scooby-Doo|Perro,Misterio,Shaggy,Furgoneta
Shaggy|Scooby,Comida,Miedo,Misterio
Snoopy|Perro,Charlie Brown,Caseta,Cómic
Garfield|Gato,Lasaña,Naranja,Perezoso
Tom|Gato,Jerry,Ratón,Perseguir
Jerry|Ratón,Tom,Queso,Perseguir
Bugs Bunny|Conejo,Zanahoria,Looney Tunes,Orejas
Pato Lucas|Pato,Negro,Looney Tunes,Bugs Bunny
Piolín|Canario,Silvestre,Amarillo,Jaula
Silvestre|Gato,Piolín,Looney Tunes,Negro
Correcaminos|Coyote,Rápido,Desierto,Carretera
Coyote|Correcaminos,Trampa,Desierto,Acme
Popeye|Espinacas,Marinero,Olivia,Músculo
Tintín|Reportero,Milú,Mechón,Aventura
Astérix|Galo,Poción,Obélix,Romano
Obélix|Menhir,Astérix,Galo,Jabalí
Lucky Luke|Vaquero,Revólver,Sombrero,Dalton
Mortadelo|Disfraz,Cómic,Filemón,Calvo
Filemón|Mortadelo,TIA,Cómic,Jefe
Superlópez|Capa,Cómic,Bigote,Superhéroe
Mafalda|Cómic,Sopa,Quino,Niña
Homer Simpson|Rosquilla,Springfield,Calvo,Cerveza
Marge Simpson|Azul,Pelo,Springfield,Homer
Bart Simpson|Monopatín,Springfield,Travieso,Homer
Lisa Simpson|Saxofón,Springfield,Lista,Bart
Maggie Simpson|Chupete,Springfield,Bebé,Amarillo
Bob el Constructor|Obra,Herramienta,Casco,Construir
Peppa Pig|Cerdita,Barro,Rosa,George
George Pig|Peppa,Dinosaurio,Hermano,Cerdito
Bluey|Perrita,Azul,Familia,Bingo
Bingo de Bluey|Perrita,Naranja,Hermana,Familia
Dora la Exploradora|Mochila,Mapa,Botas,Aventura
Mario|Nintendo,Bigote,Fontanero,Luigi
Luigi|Verde,Mario,Bigote,Nintendo
Princesa Peach|Mario,Rosa,Corona,Nintendo
Bowser|Mario,Tortuga,Caparazón,Villano
Sonic|Erizo,Azul,Rápido,Sega
Pac-Man|Amarillo,Fantasma,Laberinto,Comer
Link|Zelda,Espada,Verde,Héroe
Lara Croft|Tomb Raider,Arqueóloga,Aventura,Tumba
Donkey Kong|Gorila,Barril,Nintendo,Plátano
Kratos|God of War,Barba,Hacha,Guerrero
Steve de Minecraft|Bloque,Pico,Construir,Videojuego
Ralph|Romper,Videojuego,Disney,Grande
Vanel lope|Ralph,Carreras,Dulces,Videojuego
'''.replace('Vanel lope','Vanellope')

TITLES = '''
El rey león|Simba,Mufasa,Sabana,Disney
Tiburón|Mar,Aleta,Spielberg,Playa
Harry Potter y la piedra filosofal|Hogwarts,Mago,Varita,Escuela
Spider-Man|Araña,Telaraña,Peter,Superhéroe
Jurassic Park|Dinosaurio,Isla,Spielberg,Parque
Titanic|Barco,Iceberg,Jack,Rose
Avatar|Azul,Pandora,Na'vi,Cameron
Star Wars|Jedi,Espacio,Fuerza,Vader
El señor de los anillos|Frodo,Hobbit,Mordor,Gandalf
El Hobbit|Bilbo,Dragón,Enano,Tolkien
Frozen|Elsa,Anna,Hielo,Olaf
Toy Story|Juguete,Woody,Buzz,Pixar
Buscando a Nemo|Pez,Océano,Payaso,Dory
Shrek|Ogro,Verde,Fiona,Asno
Aladdín|Genio,Lámpara,Alfombra,Yasmín
La sirenita|Ariel,Cola,Mar,Úrsula
La bella y la bestia|Rosa,Castillo,Princesa,Hechizo
Blancanieves y los siete enanitos|Manzana,Princesa,Espejo,Mina
Cenicienta|Zapato,Calabaza,Medianoche,Hada
Pinocho|Madera,Mentira,Nariz,Grillo
Dumbo|Elefante,Orejas,Circo,Volar
Bambi|Ciervo,Bosque,Tambor,Disney
Peter Pan|Volar,Garfio,Campanilla,Nunca Jamás
El libro de la selva|Mowgli,Baloo,Pantera,Disney
Mulan|China,Guerrera,Dragón,Ejército
Pocahontas|Río,Mapache,Disney,John Smith
Vaiana|Maui,Océano,Barco,Isla
Enredados|Rapunzel,Torre,Pelo,Pascal
Encanto|Colombia,Familia,Mirabel,Bruno
Coco|México,Música,Muertos,Miguel
Ratatouille|Rata,París,Cocina,Remy
Cars|Coche,Carrera,Rayo,Mate
Wall-E|Robot,Basura,Espacio,Eva
Up|Globo,Casa,Abuelo,Russell
Del revés|Emoción,Riley,Alegría,Tristeza
Monstruos S.A.|Sulley,Mike,Puerta,Susto
Los increíbles|Superhéroe,Familia,Traje,Pixar
Kung Fu Panda|Po,Artes marciales,Fideos,Guerrero
Madagascar|Zoológico,León,Pingüino,Isla
Ice Age|Mamut,Perezoso,Hielo,Ardilla
Gru: mi villano favorito|Minions,Luna,Amarillo,Niñas
Lilo y Stitch|Hawái,Extraterrestre,Azul,Familia
Cómo entrenar a tu dragón|Vikingo,Desdentao,Hipo,Volar
Zootrópolis|Coneja,Zorro,Policía,Ciudad
El gigante de hierro|Robot,Niño,Metal,Animación
El viaje de Chihiro|Japón,Baños,Espíritu,Ghibli
Mi vecino Totoro|Bosque,Japón,Paraguas,Ghibli
La princesa Mononoke|Bosque,Lobo,Japón,Ghibli
Regreso al futuro|DeLorean,Doc,Marty,Tiempo
E.T.|Extraterrestre,Bicicleta,Elliott,Spielberg
Indiana Jones|Látigo,Sombrero,Arqueólogo,Aventura
Rocky|Boxeo,Stallone,Filadelfia,Guantes
Terminator|Robot,Schwarzenegger,Futuro,Máquina
Matrix|Neo,Pastilla,Simulación,Máquina
Misión imposible|Espía,Tom Cruise,Agente,Acción
James Bond|Espía,007,Agente,Licencia
Piratas del Caribe|Jack Sparrow,Barco,Tesoro,Mar
Forrest Gump|Correr,Chocolate,Tom Hanks,Banco
Náufrago|Isla,Wilson,Tom Hanks,Supervivencia
Solo en casa|Kevin,Ladrones,Navidad,Trampas
Los Goonies|Tesoro,Pirata,Niños,Aventura
Los cazafantasmas|Fantasma,Mochila,Nueva York,Trampa
Gremlins|Gizmo,Agua,Medianoche,Criatura
Jumanji|Juego,Selva,Tablero,Aventura
King Kong|Gorila,Isla,Rascacielos,Gigante
Godzilla|Japón,Monstruo,Gigante,Reptil
Superman|Capa,Krypton,Clark,Vuelo
Batman|Gotham,Murciélago,Joker,Bruce
Wonder Woman|Lazo,Amazona,Diana,Heroína
Iron Man|Armadura,Tony,Stark,Marvel
Los Vengadores|Marvel,Equipo,Superhéroe,Thanos
Guardianes de la galaxia|Groot,Mapache,Espacio,Marvel
Deadpool|Rojo,Máscara,Mercenario,Marvel
Black Panther|Wakanda,Rey,Traje,Marvel
Doctor Strange|Magia,Portal,Marvel,Capa
Los cuatro fantásticos|Equipo,Marvel,Poder,Antorcha
Mary Poppins|Paraguas,Niñera,Magia,Musical
El mago de Oz|Dorothy,Camino,Espantapájaros,Esmeralda
Charlie y la fábrica de chocolate|Wonka,Dulce,Billete,Oompa Loompa
Matilda|Niña,Telequinesis,Escuela,Trunchbull
La historia interminable|Fújur,Atreyu,Libro,Fantasía
La familia Addams|Miércoles,Mano,Morticia,Gómez
Beetlejuice|Fantasma,Rayas,Tim Burton,Nombre
Eduardo Manostijeras|Tim Burton,Cortar,Jardín,Johnny Depp
Pesadilla antes de Navidad|Jack,Calabaza,Halloween,Musical
It|Payaso,Globo,Pennywise,Terror
Drácula|Vampiro,Sangre,Transilvania,Colmillos
Frankenstein|Monstruo,Tornillos,Electricidad,Mary Shelley
Psicosis|Ducha,Motel,Hitchcock,Terror
El resplandor|Hotel,Terror,Hacha,Jack Nicholson
El exorcista|Niña,Posesión,Cura,Terror
Alien|Espacio,Monstruo,Ripley,Nave
Depredador|Selva,Extraterrestre,Camuflaje,Cazar
Scream|Máscara,Teléfono,Terror,Asesino
El sexto sentido|Fantasma,Niño,Bruce Willis,Muertos
El silencio de los corderos|Hannibal,FBI,Caníbal,Máscara
Gladiator|Roma,Arena,Russell Crowe,Espada
300|Esparta,Leónidas,Persia,Batalla
Braveheart|Escocia,William Wallace,Libertad,Mel Gibson
El padrino|Mafia,Corleone,Coppola,Familia
Pulp Fiction|Tarantino,Maletín,Baile,Travolta
Amélie|París,Camarera,Audrey Tautou,Francia
La La Land|Musical,Los Ángeles,Piano,Baile
Mamma Mia!|ABBA,Musical,Grecia,Boda
Grease|Musical,Instituto,Travolta,Sandy
Dirty Dancing|Baile,Vacaciones,Baby,Swayze
Fiebre del sábado noche|Disco,Baile,Travolta,Bee Gees
El gran showman|Circo,Musical,Hugh Jackman,Escenario
La vida es bella|Italia,Padre,Hijo,Benigni
Cinema Paradiso|Italia,Cine,Proyeccionista,Recuerdo
Ocho apellidos vascos|España,Comedia,Sevilla,Euskadi
Campeones|Baloncesto,España,Equipo,Entrenador
Mortadelo y Filemón|Disfraz,TIA,Agente,Ibáñez
Los Simpson|Springfield,Homer,Amarillo,Rosquilla
Friends|Central Perk,Sofá,Ross,Rachel
Juego de tronos|Dragón,Trono,Stark,Poniente
La casa de papel|Atraco,Profesor,Máscara,Mono rojo
Stranger Things|Hawkins,Once,Demogorgon,Ochenta
The Big Bang Theory|Sheldon,Leonard,Ciencia,Sofá
Breaking Bad|Walter White,Química,Heisenberg,Desierto
Better Call Saul|Abogado,Jimmy,Albuquerque,Breaking Bad
The Walking Dead|Zombi,Rick,Supervivencia,Apocalipsis
Miércoles|Addams,Trenzas,Mano,Academia
Sherlock|Detective,Watson,Londres,BBC
Doctor Who|TARDIS,Tiempo,Doctor,Cabina
Lost|Isla,Avión,Superviviente,Misterio
Prison Break|Cárcel,Tatuaje,Hermanos,Escape
The Mandalorian|Grogu,Casco,Star Wars,Cazarrecompensas
Vikingos|Ragnar,Barco,Nórdico,Guerrero
The Crown|Reina,Británico,Palacio,Monarquía
Downton Abbey|Inglaterra,Aristocracia,Criados,Mansión
Peaky Blinders|Gorra,Birmingham,Tommy Shelby,Gánster
House|Médico,Bastón,Diagnóstico,Hospital
Anatomía de Grey|Hospital,Cirujano,Meredith,Seattle
CSI|Crimen,Forense,Investigar,Policía
El mentalista|Patrick Jane,Crimen,Observación,Policía
Modern Family|Familia,Comedia,Phil,Gloria
Cómo conocí a vuestra madre|Ted,Barney,Robin,Nueva York
Brooklyn Nine-Nine|Policía,Comedia,Jake,Comisaría
Malcolm|Familia,Hermanos,Comedia,Hal
El príncipe de Bel-Air|Will Smith,California,Comedia,Carlton
Aquí no hay quien viva|Vecinos,Comunidad,España,Comedia
La que se avecina|Vecinos,Comunidad,España,Monte pinar
Los Serrano|Familia,España,Taberna,Diego
Cuéntame cómo pasó|Alcántara,España,Historia,Familia
El ministerio del tiempo|Viaje,Historia,España,Puerta
Águila Roja|España,Héroe,Antifaz,Siglo de Oro
Física o química|Instituto,España,Estudiante,Profesor
Merlí|Filosofía,Profesor,Instituto,Cataluña
Élite|Instituto,España,Crimen,Las Encinas
Los hombres de Paco|Policía,España,Comedia,Comisaría
Verano azul|Chanquete,Vacaciones,Nerja,Bicicleta
Heidi|Abuelo,Alpes,Pedro,Cabra
Marco|Madre,Italia,Viaje,Mono
Dragon Ball|Goku,Bolas,Guerrero,Anime
Naruto|Ninja,Chakra,Konoha,Anime
One Piece|Pirata,Luffy,Sombrero,Anime
Pokémon|Pikachu,Ash,Capturar,Monstruo
Doraemon|Robot,Gato,Nobita,Bolsillo
Shin Chan|Niño,Travieso,Anime,Familia
Bob Esponja|Piña,Patricio,Mar,Amarillo
Hora de aventuras|Finn,Jake,Espada,Animación
Gravity Falls|Dipper,Mabel,Misterio,Verano
Phineas y Ferb|Invento,Verano,Perry,Hermanos
Inspector Gadget|Detective,Aparato,Sobrina,Robot
Scooby-Doo|Perro,Misterio,Furgoneta,Shaggy
Looney Tunes|Bugs Bunny,Pato Lucas,Coyote,Animación
Tom y Jerry|Gato,Ratón,Perseguir,Animación
Los Picapiedra|Prehistoria,Pedro,Piedra,Dinosaurio
Los Supersónicos|Futuro,Robot,Espacio,Familia
Futurama|Fry,Bender,Robot,Futuro
Rick y Morty|Portal,Ciencia,Abuelo,Nieto
South Park|Colorado,Cartman,Stan,Animación
Padre de familia|Peter,Griffin,Stewie,Brian
Peppa Pig|Cerdita,Barro,George,Rosa
Bluey|Perrita,Australia,Bingo,Familia
Patrulla Canina|Perro,Rescate,Ryder,Cachorro
Dora la Exploradora|Mochila,Mapa,Botas,Aventura
Pocoyó|Azul,Pato,Elly,Niño
Teletubbies|Antena,Colina,Sol,Colores
Barrio Sésamo|Marioneta,Monstruo,Niño,Espinete
Los Lunnis|Muñeco,Televisión,Luna,Niños
Pingu|Pingüino,Nieve,Plastilina,Animación
Shaun el cordero|Oveja,Granja,Plastilina,Animación
La abeja Maya|Insecto,Willy,Colmena,Animación
La vuelta al mundo de Willy Fog|Viaje,Ochenta días,León,Verne
Los pitufos|Azul,Gargamel,Bosque,Pequeño
David el Gnomo|Bosque,Lisa,Zorro,Gorro
'''.replace('Monte pinar','Montepinar')

FAMOUS = '''
Michael Jackson|Música,Pop,Guante,Moonwalk
Freddie Mercury|Queen,Cantante,Bigote,Bohemian Rhapsody
Elvis Presley|Rock,Cantante, tupé,Graceland
Madonna|Pop,Cantante,Like a Virgin,Música
Shakira|Colombia,Cantante,Caderas,Waka Waka
Rosalía|Motomami,Cantante,Flamenco,España
Lady Gaga|Pop,Cantante,Poker Face,Vestido
Beyoncé|Cantante,Pop,Destiny's Child,Single Ladies
Taylor Swift|Cantante,Pop,Country,Álbum
Adele|Cantante,Hello,Reino Unido,Voz
Rihanna|Cantante,Barbados,Umbrella,Fenty
David Bowie|Cantante,Ziggy Stardust,Rock,Reino Unido
Bob Marley|Reggae,Jamaica,Música,Rastas
John Lennon|Beatles,Cantante,Imagine,Liverpool
Paul McCartney|Beatles,Bajo,Liverpool,Música
Ringo Starr|Beatles,Batería,Liverpool,Música
George Harrison|Beatles,Guitarra,Liverpool,Música
Mick Jagger|Rolling Stones,Cantante,Rock,Boca
Bruce Springsteen|Boss,Rock,Cantante,Estados Unidos
Prince|Púrpura,Cantante,Guitarra,Música
Tina Turner|Cantante,Rock,Voz,Escenario
Whitney Houston|Cantante,Guardaespaldas,Voz,Pop
Céline Dion|Titanic,Cantante,Canadá,Voz
Jennifer Lopez|Cantante,Actriz,Baile,Bronx
Enrique Iglesias|Cantante,España,Bailando,Julio
Julio Iglesias|Cantante,España,Balada,Voz
Raphael|Cantante,España,Escenario,Yo soy aquel
Nino Bravo|Cantante,Libre,Valencia,Voz
Lola Flores|Faraona,Flamenco,Jerez,Cantante
Rocío Jurado|Chipiona,Cantante,La más grande,Voz
Paco de Lucía|Guitarra,Flamenco,Algeciras,Música
Camarón de la Isla|Flamenco,Cante,San Fernando,Música
Joaquín Sabina|Cantante,Úbeda,Bombín,Música
Joan Manuel Serrat|Cantante,Mediterráneo,Barcelona,Música
Alejandro Sanz|Cantante,Corazón partío,España,Guitarra
David Bisbal|Cantante,Almería,Rizos,Bulería
David Bustamante|Cantante,Cantabria,Operación Triunfo,Voz
Aitana|Cantante,Pop,Operación Triunfo,España
Ed Sheeran|Guitarra,Cantante,Pelirrojo,Reino Unido
Bruno Mars|Cantante,Pop,Hawái,Baile
Bad Bunny|Puerto Rico,Cantante,Reguetón,Música
Daddy Yankee|Puerto Rico,Gasolina,Reguetón,Cantante
Luis Fonsi|Despacito,Puerto Rico,Cantante,Música
Maluma|Colombia,Cantante,Reguetón,Música
Karol G|Colombia,Cantante,Reguetón,Música
Antonio Banderas|Actor,Málaga,Zorro,Cine
Penélope Cruz|Actriz,España,Óscar,Almodóvar
Javier Bardem|Actor,España,Óscar,Cine
Pedro Almodóvar|Director,Mancha,Cine,Volver
Tom Hanks|Actor,Forrest Gump,Náufrago,Cine
Leonardo DiCaprio|Actor,Titanic,Origen,Cine
Brad Pitt|Actor,Hollywood,Club de la lucha,Cine
Angelina Jolie|Actriz,Lara Croft,Maléfica,Cine
Johnny Depp|Actor,Jack Sparrow,Sombrero,Cine
Will Smith|Actor,Bel-Air,Hombres de negro,Cine
Jim Carrey|Actor,Comedia,Máscara,Ace Ventura
Charlie Chaplin|Bastón,Bombín,Cine mudo,Bigote
Marilyn Monroe|Actriz,Rubia,Hollywood,Vestido
Audrey Hepburn|Actriz,Tiffany,Hollywood,Elegancia
Bruce Lee|Kung Fu,Actor,Patada,Artes marciales
Jackie Chan|Actor,Kung Fu,Acrobacia,Hong Kong
Arnold Schwarzenegger|Actor,Terminator,Músculo,Austria
Sylvester Stallone|Actor,Rocky,Rambo,Boxeo
Harrison Ford|Actor,Indiana Jones,Han Solo,Cine
Tom Cruise|Actor,Misión imposible,Top Gun,Cine
Dwayne Johnson|Actor,The Rock,Músculo,Lucha
Emma Watson|Actriz,Hermione,Harry Potter,Cine
Daniel Radcliffe|Actor,Harry Potter,Gafas,Cine
Jennifer Aniston|Actriz,Friends,Rachel,Cine
Rowan Atkinson|Actor,Mr Bean,Comedia,Reino Unido
Jack Nicholson|Actor,Resplandor,Óscar,Cine
Morgan Freeman|Actor,Voz,Hollywood,Cine
Samuel L. Jackson|Actor,Marvel,Pulp Fiction,Cine
Clint Eastwood|Actor,Director,Western,Cine
Steven Spielberg|Director,Tiburón,E.T.,Cine
Quentin Tarantino|Director,Pulp Fiction,Kill Bill,Cine
Tim Burton|Director,Gótico,Manostijeras,Cine
Christopher Nolan|Director,Origen,Batman,Cine
Alfred Hitchcock|Director,Psicosis,Suspense,Cine
Walt Disney|Animación,Mickey,Estudio,Cine
Rafael Nadal|Tenis,Mallorca,Raqueta,Roland Garros
Roger Federer|Tenis,Suiza,Raqueta,Wimbledon
Novak Djokovic|Tenis,Serbia,Raqueta,Deporte
Serena Williams|Tenis,Raqueta,Estados Unidos,Deporte
Pau Gasol|Baloncesto,NBA,España,Canasta
Michael Jordan|Baloncesto,Chicago,Bulls,NBA
LeBron James|Baloncesto,NBA,Canasta,Estados Unidos
Kobe Bryant|Baloncesto,Lakers,NBA,Canasta
Shaquille O'Neal|Baloncesto,NBA,Grande,Canasta
Lionel Messi|Fútbol,Argentina,Balón,Barcelona
Cristiano Ronaldo|Fútbol,Portugal,Balón,Real Madrid
Diego Maradona|Fútbol,Argentina,Mano,Nápoles
Pelé|Fútbol,Brasil,Balón,Santos
Ronaldinho|Fútbol,Brasil,Sonrisa,Barcelona
Zinedine Zidane|Fútbol,Francia,Real Madrid,Balón
Andrés Iniesta|Fútbol,España,Mundial,Fuentealbilla
Iker Casillas|Portero,Fútbol,España,Guantes
Sergio Ramos|Fútbol,Defensa,España,Real Madrid
David Beckham|Fútbol,Inglaterra,Manchester,Real Madrid
Fernando Alonso|Fórmula 1,Asturias,Piloto,Coche
Lewis Hamilton|Fórmula 1,Reino Unido,Piloto,Coche
Michael Schumacher|Fórmula 1,Alemania,Ferrari,Piloto
Ayrton Senna|Fórmula 1,Brasil,Piloto,Coche
Marc Márquez|Moto,Cervera,Piloto,Deporte
Valentino Rossi|Moto,Italia,Piloto,Deporte
Usain Bolt|Atletismo,Jamaica,Velocidad,Correr
Michael Phelps|Natación,Piscina,Medalla,Estados Unidos
Simone Biles|Gimnasia,Salto,Medalla,Estados Unidos
Nadia Comăneci|Gimnasia,Rumanía,Diez,Medalla
Muhammad Ali|Boxeo,Guantes,Combate,Ring
Mike Tyson|Boxeo,Guantes,Ring,Combate
Miguel Induráin|Ciclismo,Navarra,Tour,Bicicleta
Alberto Contador|Ciclismo,Tour,Bicicleta,España
Carolina Marín|Bádminton,Huelva,Raqueta,Deporte
Edurne Pasaban|Montaña,Alpinismo,Cumbre,España
Jesús Calleja|Aventura,Montaña,Televisión,León
Albert Einstein|Física,Relatividad,Pelo,Ciencia
Isaac Newton|Gravedad,Manzana,Física,Ciencia
Marie Curie|Radioactividad,Nobel,Ciencia,Laboratorio
Charles Darwin|Evolución,Especies,Naturalista,Beagle
Nikola Tesla|Electricidad,Inventor,Corriente,Ciencia
Thomas Edison|Inventor,Fonógrafo,Bombilla,Electricidad
Galileo Galilei|Telescopio,Astronomía,Italia,Ciencia
Stephen Hawking|Física,Silla,Espacio,Ciencia
Leonardo da Vinci|Mona Lisa,Inventor,Renacimiento,Pintor
Pablo Picasso|Guernica,Pintor,Málaga,Cubismo
Salvador Dalí|Bigote,Pintor,Surrealismo,Relojes
Vincent van Gogh|Pintor,Girasoles,Oreja,Holanda
Frida Kahlo|Pintora,México,Cejas,Autorretrato
Diego Velázquez|Meninas,Pintor,España,Corte
Francisco de Goya|Pintor,España,Majas,Fusilamientos
Miguel Ángel|Escultor,David,Sixtina,Renacimiento
Claude Monet|Pintor,Nenúfares,Impresionismo,Francia
Antoni Gaudí|Arquitecto,Barcelona,Sagrada Familia,Modernismo
Miguel de Cervantes|Quijote,Escritor,Sancho,España
William Shakespeare|Teatro,Hamlet,Romeo,Inglaterra
Federico García Lorca|Poeta,Granada,Teatro,Bodas de sangre
Gabriel García Márquez|Escritor,Colombia,Macondo,Nobel
J. K. Rowling|Harry Potter,Escritora,Hogwarts,Reino Unido
Agatha Christie|Misterio,Escritora,Poirot,Asesinato
Julio Verne|Escritor,Viaje,Submarino,Aventura
J. R. R. Tolkien|Hobbit,Anillo,Escritor,Fant asía
Cleopatra|Egipto,Reina,Nilo,Faraón
Julio César|Roma,Emperador,Senado,Bruto
Napoleón|Francia,Emperador,Waterloo,Sombrero
Cristóbal Colón|América,Carabela,1492,Viaje
Marco Polo|Viaje,Venecia,China,Explorador
Mahatma Gandhi|India,Paz,No violencia,Gafas
Nelson Mandela|Sudáfrica,Apartheid,Prisión,Paz
Martin Luther King|Derechos,Sueño,Estados Unidos,Paz
Rosa Parks|Autobús,Derechos,Estados Unidos,Segregación
Amelia Earhart|Piloto,Avión,Vuelo,Desaparición
Neil Armstrong|Luna,Astronauta,Apolo,Espacio
Yuri Gagarin|Espacio,Cosmonauta,Vostok,URSS
Valentina Tereshkova|Espacio,Cosmonauta,Mujer,Vostok
Jane Goodall|Chimpancé,Primates,Naturaleza,Ciencia
Jacques Cousteau|Mar,Explorador,Buceo,Calypso
Félix Rodríguez de la Fuente|Lobo,Naturaleza,Televisión,Animal
David Attenborough|Naturaleza,Documental,Animal,BBC
'''.replace('Fant asía','Fantasía')

def culture():
    result=[]
    for topic,text in [('personajes',PEOPLE),('cine y series',TITLES),('famosos',FAMOUS)]:
        for line in text.strip().splitlines():
            name,words=line.strip().split('|')
            result.append({'prompt':name,'forbidden':[w.strip() for w in words.split(',')],'topic':topic,'difficulty':'easy' if topic=='personajes' else 'medium'})
    return result
