from django.db import models

tributarios=(
(0,'No registra'),
(1,'Simplificado'),
(2,'Común'),
)

naturalezas=(
(1,'Natural'),
(2,'Juridica'),
)

ciiu=(
(1011,	'Procesamiento y conservación de carne y productos cárnicos'),
(1012,	'Procesamiento y conservación de pescados, crustáceos y moluscos'),
(1030,	'Elaboración de aceites y grasas de origen vegetal y animal'),
(1051,	'Elaboración de productos de molinería'),
(1052,	'Elaboración de almidones y productos derivados del almidón'),
(1062,	'Descafeinado, tostión y molienda del café'),
(1063,	'Elaboración de otros derivados del café'),
(1071,	'Elaboración y refinación de azúcar'),
(1072,	'Elaboración de panela'),
(1081,	'Elaboración de productos de panadería'),
(1082,	'Elaboración de cacao, chocolate y productos de confitería'),
(1083,	'Elaboración de macarrones, fideos, alcuzcuz y productos farináceos similares'),
(1084,	'Elaboración de comidas y platos preparados'),
(1089,	'Elaboración de otros productos alimenticios n.c.p.'),
(1090,	'Elaboración de alimentos preparados para animales'),
(1410,	'Confección de prendas de vestir, excepto prendas de piel'),
(1521,	'Fabricación de calzado de cuero y piel, con cualquier tipo de suela'),
(1522,	'Fabricación de otros tipos de calzado, excepto calzado de cuero y piel'),
(10201,	'Procesamiento y conservación de frutas, legumbres, hortalizas y tubérculos (excepto elaboración de jugos de frutas)'),
(10401,	'Elaboración de productos lácteos (excepto bebidas)'),
(14201,	'Fabricación de prendas de vestir de piel'),
(14301,	'Fabricación de prendas de vestir  de punto y ganchillo'),
(58113,	'Edición y publicación de libros (Tarifa especial para los contribuyentes que cumplen condiciones del Acuerdo 98 de 2003)'),
(2410,	'Industrias básicas de hierro y de acero'),
(2431,	'Fundición de hierro y de acero'),
(2432,	'Fundición de metales no ferrosos'),
(2910,	'Fabricación de vehículos automotores y sus motores'),
(2920,	'Fabricación de carrocerías para vehículos automotores; fabricación de remolques y semirremolques'),
(2930,	'Fabricación de partes, piezas (autopartes) y accesorios (lujos) para vehículos automotores'),
(3011,	'Construcción de barcos y de estructuras flotantes'),
(3012,	'Construcción de embarcaciones de recreo y deporte'),
(3020,	'Fabricación de locomotoras y de material rodante para ferrocarriles'),
(3030,	'Fabricación de aeronaves, naves espaciales y de maquinaria conexa'),
(3040,	'Fabricación de vehículos militares de combate'),
(3091,	'Fabricación de motocicletas'),
(3092,	'Fabricación de bicicletas y de sillas de ruedas para personas con discapacidad'),
(3099,	'Fabricación de otros tipos de equipo de transporte n.c.p.'),
(510,	'Extracción de hulla (carbón de piedra)'),
(520,	'Extracción de carbón lignito'),
(610,	'Extracción de petróleo crudo'),
(620,	'Extracción de gas natural'),
(710,	'Extracción de minerales de hierro'),
(721,	'Extracción de minerales de uranio y de torio'),
(722,	'Extracción de oro y otros metales preciosos'),
(723,	'Extracción de minerales de níquel'),
(729,	'Extracción de otros minerales metalíferos no ferrosos n.c.p.'),
(811,	'Extracción de piedra, arena, arcillas comunes, yeso y anhidrita'),
(812,	'Extracción de arcillas de uso industrial, caliza, caolín y bentonitas'),
(820,	'Extracción de esmeraldas, piedras preciosas y semipreciosas'),
(891,	'Extracción de minerales para la fabricación de abonos y productos químicos'),
(892,	'Extracción de halita (sal)'),
(899,	'Extracción de otros minerales no metálicos n.c.p.'),
(1101,	'Destilación, rectificación y mezcla de bebidas alcohólicas'),
(1102,	'Elaboración de bebidas fermentadas no destiladas'),
(1103,	'Producción de malta, elaboración de cervezas y otras bebidas malteadas'),
(1104,	'Elaboración de bebidas no alcohólicas, producción de aguas minerales y de otras aguas embotelladas'),
(1200,	'Elaboración de productos de tabaco'),
(1311,	'Preparación e hilatura de fibras textiles'),
(1312,	'Tejeduría de productos textiles'),
(1313,	'Acabado de productos textiles'),
(1391,	'Fabricación de tejidos de punto y ganchillo'),
(1392,	'Confección de artículos con materiales textiles, excepto prendas de vestir'),
(1393,	'Fabricación de tapetes y alfombras para pisos'),
(1394,	'Fabricación de cuerdas, cordeles, cables, bramantes y redes'),
(1399,	'Fabricación de otros artículos textiles n.c.p.'),
(1511,	'Curtido y recurtido de cueros; recurtido y teñido de pieles.'),
(1512,	'Fabricación de artículos de viaje, bolsos de mano y artículos similares elaborados en cuero, y fabricación de artículos de talabartería y guarnicionería.'),
(1513,	'Fabricación de artículos de viaje, bolsos de mano y artículos similares; artículos de talabartería y guarnicionería elaborados en otros materiales'),
(1523,	'Fabricación de partes del calzado'),
(1610,	'Aserrado, acepillado e impregnación de la madera'),
(1620,	'Fabricación de hojas de madera para enchapado; fabricación de tableros contrachapados, tableros laminados, tableros de partículas y otros tableros y paneles'),
(1630,	'Fabricación de partes y piezas de madera, de carpintería y ebanistería para la construcción y para edificios'),
(1640,	'Fabricación de recipientes de madera'),
(1690,	'Fabricación de otros productos de madera; fabricación de artículos de corcho, cestería y espartería'),
(1701,	'Fabricación de pulpas (pastas) celulósicas; papel y cartón'),
(1702,	'Fabricación de papel y cartón ondulado (corrugado); fabricación de envases, empaques y de embalajes de papel y cartón.'),
(1709,	'Fabricación de otros artículos de papel y cartón'),
(1910,	'Fabricación de productos de hornos de coque'),
(1921,	'Fabricación de productos de la refinación del petróleo'),
(1922,	'Actividad de mezcla de combustibles'),
(2011,	'Fabricación de sustancias y productos químicos básicos'),
(2012,	'Fabricación de abonos y compuestos inorgánicos nitrogenados'),
(2013,	'Fabricación de plásticos en formas primarias'),
(2014,	'Fabricación de caucho sintético en formas primarias'),
(2021,	'Fabricación de plaguicidas y otros productos químicos de uso agropecuario'),
(2022,	'Fabricación de pinturas, barnices y revestimientos similares, tintas para impresión y masillas'),
(2023,	'Fabricación de jabones y detergentes, preparados para limpiar y pulir; perfumes y preparados de tocador'),
(2029,	'Fabricación de otros productos químicos n.c.p.'),
(2030,	'Fabricación de fibras sintéticas y artificiales'),
(2100,	'Fabricación de productos farmacéuticos, sustancias químicas medicinales y productos botánicos de uso farmacéutico'),
(2211,	'Fabricación de llantas y neumáticos de caucho'),
(2212,	'Reencauche de llantas usadas'),
(2219,	'Fabricación de formas básicas de caucho y otros productos de caucho n.c.p.'),
(2219,	'Fabricación de formas básicas de caucho y otros productos de caucho n.c.p.'),
(2221,	'Fabricación de formas básicas de plástico'),
(2229,	'Fabricación de artículos de plástico n.c.p.'),
(2310,	'Fabricación de vidrio y productos de vidrio'),
(2391,	'Fabricación de productos refractarios'),
(2392,	'Fabricación de materiales de arcilla para la construcción'),
(2393,	'Fabricación de otros productos de cerámica y porcelana'),
(2394,	'Fabricación de cemento, cal y yeso'),
(2395,	'Fabricación de artículos de hormigón, cemento y yeso'),
(2396,	'Corte, tallado y acabado de la piedra'),
(2399,	'Fabricación de otros productos minerales no metálicos n.c.p.'),
(2421,	'Industrias básicas de metales preciosos'),
(2429,	'Industrias básicas de otros metales no ferrosos'),
(2511,	'Fabricación de productos metálicos para uso estructural'),
(2512,	'Fabricación de tanques, depósitos y recipientes de metal, excepto los utilizados para el envase o transporte de mercancías'),
(2513,	'Fabricación de generadores de vapor, excepto calderas de agua caliente para calefacción central'),
(2520,	'Fabricación de armas y municiones'),
(2591,	'Forja, prensado, estampado y laminado de metal; pulvimetalurgia'),
(2593,	'Fabricación de artículos de cuchillería, herramientas de mano y artículos de ferretería'),
(2599,	'Fabricación de otros productos elaborados de metal n.c.p.'),
(2610,	'Fabricación de componentes y tableros electrónicos'),
(2620,	'Fabricación de computadoras y de equipo periférico'),
(2640,	'Fabricación de aparatos electrónicos de consumo'),
(2651,	'Fabricación de equipo de medición, prueba, navegación y control'),
(2630,	'Fabricación de equipos de comunicación'),
(2652,	'Fabricación de relojes'),
(2660,	'Fabricación de equipo de irradiación y equipo electrónico de uso médico y terapéutico'),
(2670,	'Fabricación de instrumentos ópticos y equipo fotográfico'),
(2680,	'Fabricación de soportes magnéticos y ópticos'),
(2711,	'Fabricación de motores, generadores y transformadores eléctricos.'),
(2712,	'Fabricación de aparatos de distribución y control de la energía eléctrica'),
(2720,	'Fabricación de pilas, baterías y acumuladores eléctricos'),
(2731,	'Fabricación de hilos y cables eléctricos y de fibra óptica'),
(2740,	'Fabricación de equipos eléctricos de iluminación'),
(2750,	'Fabricación de aparatos de uso domestico'),
(2732,	'Fabricación de dispositivos de (cableado'),
(2811,	'Fabricación de motores, turbinas, y partes para motores de combustión interna'),
(2812,	'Fabricación de equipos de potencia hidráulica y neumática'),
(2813,	'Fabricación de otras bombas, compresores, grifos y válvulas'),
(2814,	'Fabricación de cojinetes, engranajes, trenes de engranajes y piezas de transmisión'),
(2816,	'Fabricación de equipo de elevación y manipulación'),
(2815,	'Fabricación de hornos, hogares y quemadores industriales'),
(2817,	'Fabricación de maquinaria y equipo de oficina (excepto computadoras y equipo periférico)'),
(2790,	'Fabricación de otros tipos de equipo eléctrico n.c.p'),
(2818,	'Fabricación de herramientas manuales con motor'),
(2819,	'Fabricación de otros tipos de maquinaria y equipo de uso general n.c.p.'),
(2822,	'Fabricación de máquinas formadoras de metal y de máquinas herramienta'),
(2823,	'Fabricación de maquinaria para la metalurgia'),
(2824,	'Fabricación de maquinaria para explotación de minas y canteras y para obras de construcción'),
(2821,	'Fabricación de maquinaria agropecuaria y forestal'),
(2825,	'Fabricación de maquinaria para la elaboración de alimentos, bebidas y tabaco'),
(2826,	'Fabricación de maquinaria para la elaboración de productos textiles, prendas de vestir y cueros'),
(2829,	'Fabricación de otros tipos de maquinaria y equipo de uso especial n.c.p.'),
(3110,	'Fabricación de muebles'),
(3120,	'Fabricación de colchones y somieres'),
(3210,	'Fabricación de joyas, bisutería y artículos conexos'),
(3220,	'Fabricación de instrumentos musicales'),
(3240,	'Fabricación de juegos, juguetes y rompecabezas'),
(3250,	'Fabricación de instrumentos, aparatos y materiales médicos y odontológicos (incluido mobiliario)'),
(3290,	'Otras industrias manufactureras n.c.p.'),
(3512,	'Transmisión de energía eléctrica'),
(3821,	'Tratamiento y disposición de desechos no peligrosos'),
(3511,	'Generación de energía eléctrica'),
(3822,	'Tratamiento y disposición de desechos peligrosos'),
(3830,	'Recuperación de materiales'),
(5812,	'Edición de directorios y listas de correo'),
(5819,	'Otros trabajos de edición'),
(5820,	'Edición de programas de informática (software)'),
(5911,	'Actividades de producción de películas cinematográficas, videos, programas, anuncios y comerciales de televisión (excepto programación de televisión)'),
(5912,	'Actividades de postproducción de películas cinematográficas, videos, programas, anuncios y comerciales de televisión  (excepto programación de televisión)'),
(10202,	'Elaboración de jugos de frutas'),
(5920,	'Actividades de grabación de sonido y edición de música'),
(10402,	'Elaboración de bebidas lácteas'),
(14202,	'Fabricación de artículos de piel (excepto prendas de vestir)'),
(14302,	'Fabricación de artículos de punto y ganchillo (excepto prendas de vestir)'),
(3230,	'Fabricación de artículos y equipo para la práctica del deporte   (excepto prendas de vestir y calzado)'),
(35201,	'Producción de gas'),
(36001,	'Captación y tratamiento de agua'),
(58112,	'Edición y publicación de libros'),
(4631,	'Comercio al por mayor de productos alimenticios'),
(4721,	'Comercio al por menor de productos agrícolas para el consumo en establecimientos especializados'),
(4722,	'Comercio al por menor de leche, productos lácteos y huevos, en establecimientos especializados'),
(4723,	'Comercio al por menor de carnes (incluye aves de corral), productos cárnicos, pescados y productos de mar, en establecimientos especializados'),
(4729,	'Comercio al por menor de otros productos alimenticios n.c.p., en establecimientos especializados'),
(46451,	'Comercio al por mayor de productos farmacéuticos y medicinales'),
(46201,	'Comercio al por mayor de materias primas agrícolas en bruto (alimentos)'),
(47111,	'Comercio al por menor en establecimientos no especializados con surtido compuesto principalmente por alimentos, bebidas o tabaco (excepto licores y cigarrillos)'),
(47192,	'Comercio al por menor en establecimientos no especializados, con surtido compuesto principalmente por drogas, medicamentos, textos escolares, libros y cuadernos.'),
(47611,	'Comercio al por menor y al por mayor  de libros, textos escolares y cuadernos'),
(47731,	'Comercio al por menor de productos farmacéuticos y medicinales en establecimientos especializados'),
(47811,	'Comercio al por menor de alimentos en puestos de venta móviles'),
(47911,	'Comercio al por menor de alimentos y productos agrícolas en bruto; venta de textos escolares y libros (incluye cuadernos escolares); venta de drogas y medicamentos realizado a través de internet'),
(47921,	'Comercio al por menor de alimentos y productos agrícolas en bruto; venta de textos escolares y libros (incluye cuadernos escolares); venta de drogas y medicamentos realizado a través de casas de venta o por correo'),
(47991,	'Otros tipos de comercio al por menor no realizado en establecimientos, puestos de venta o mercados de textos escolares y libros (incluye cuadernos escolares); venta de drogas y medicamentos'),
(4511,	'Comercio de vehículos automotores nuevos'),
(4512,	'Comercio de vehículos automotores usados'),
(45411,	'Comercio de motocicletas'),
(46631,	'Comercio al por mayor de materiales de construcción'),
(47521,	'Comercio al por menor de materiales de construcción'),
(47912,	'Comercio al por menor y al por mayor de madera y materiales para construcción; venta de automotores (incluidas motocicletas)  realizado a través de internet'),
(47922,	'Comercio al por menor y al por mayor de madera y materiales para construcción; venta de automotores (incluidas motocicletas)  realizado a través de casas de venta o por correo'),
(47992,	'Otros tipos de comercio al por menor no realizado en establecimientos, puestos de venta o mercados de  materiales para construcción; venta de automotores (incluidas motocicletas)'),
(4731,	'Comercio al por menor de combustible para automotores'),
(46322,	'Comercio al por mayor de licores y cigarrillos'),
(46492,	'Venta de joyas'),
(46612,	'Comercio al por mayor de combustibles  derivados del petróleo'),
(47112,	'Comercio al por menor en establecimientos no especializados con surtido compuesto principalmente  por licores y cigarrillos'),
(47242,	'Comercio al por menor de licores y cigarrillos'),
(47813,	'Comercio al por menor de cigarrillos y licores en puestos de venta móviles'),
(47913,	'Comercio al por menor de cigarrillos y licores; venta de combustibles derivados del petróleo y venta de joyas  realizado a través de internet'),
(47923,	'Comercio al por menor de cigarrillos y licores; venta de combustibles derivados del petróleo y venta de joyas  realizado a través de casas de venta o por correo'),
(47993,	'Otros tipos de comercio al por menor no realizado en establecimientos, puestos de venta o mercados de cigarrillos y licores; venta de combustibles derivados del petróleo y venta de joyas'),
(3514,	'Comercialización de energía eléctrica'),
(4530,	'Comercio de partes, piezas (autopartes) y accesorios (lujos) para vehículos automotores'),
(4641,	'Comercio al por mayor de productos textiles y productos confeccionados para uso doméstico'),
(4642,	'Comercio al por mayor de prendas de vestir'),
(4643,	'Comercio al por mayor de calzado'),
(4644,	'Comercio al por mayor de aparatos y equipo de uso doméstico'),
(4651,	'Comercio al por mayor de computadores, equipo periférico y programas de informática'),
(4652,	'Comercio al por mayor de equipo, partes y piezas electrónicos y de telecomunicaciones'),
(4653,	'Comercio al por mayor de maquinaria y equipo agropecuarios'),
(4659,	'Comercio al por mayor de otros tipos de maquinaria y equipo n.c.p.'),
(4662,	'Comercio al por mayor de metales y productos metalíferos'),
(4664,	'Comercio al por mayor de productos químicos básicos, cauchos y plásticos en formas primarias y productos químicos de uso agropecuario'),
(4665,	'Comercio al por mayor de desperdicios, desechos y chatarra'),
(4665,	'Comercio al por mayor de desperdicios, desechos y chatarra'),
(4669,	'Comercio al por mayor de otros productos n.c.p.'),
(4690,	'Comercio al por mayor no especializado'),
(4732,	'Comercio al por menor de lubricantes (aceites, grasas), aditivos y productos de limpieza para vehículos automotores'),
(4741,	'Comercio al por menor de computadores, equipos periféricos, programas de informática y equipos de telecomunicaciones en establecimientos especializados'),
(4742,	'Comercio al por menor de equipos y aparatos de sonido y de video, en establecimientos especializados'),
(4751,	'Comercio al por menor de productos textiles en establecimientos especializados'),
(4753,	'Comercio al por menor de tapices, alfombras y cubrimientos para paredes y pisos en establecimientos especializados.'),
(4754,	'Comercio al por menor de electrodomésticos y gasodomesticos de uso doméstico, muebles y equipos de iluminación'),
(4755,	'Comercio al por menor de artículos y utensilios de uso domestico'),
(4759,	'Comercio al por menor de otros artículos domésticos en establecimientos especializados'),
(4762,	'Comercio al por menor de artículos deportivos, en establecimientos especializados'),
(4769,	'Comercio al por menor de otros artículos culturales y de entretenimiento n.c.p. en establecimientos especializados'),
(4771,	'Comercio al por menor de prendas de vestir y sus accesorios (incluye artículos de piel) en establecimientos especializados'),
(4772,	'Comercio al por menor de todo tipo de calzado y artículos de cuero y sucedáneos del cuero en establecimientos especializados.'),
(4774,	'Comercio al por menor de otros productos nuevos en establecimientos especializados'),
(4775,	'Comercio al por menor de artículos de segunda mano'),
(4782,	'Comercio al por menor de productos textiles, prendas de vestir y calzado, en puestos de venta móviles'),
(4789,	'Comercio al por menor de otros productos en puestos de venta móviles'),
(45412,	'Comercio de partes, piezas y accesorios de motocicletas'),
(46202,	'Comercio al por mayor de materias primas pecuarias y animales vivos'),
(46321,	'Comercio al por mayor de bebidas y tabaco (diferentes a licores y cigarrillos)'),
(46452,	'Comercio al por mayor de productos cosméticos y de tocador (excepto productos farmacéuticos y medicinales)'),
(46491,	'Comercio al por mayor de otros utensilios domésticos n.c.p. (excepto joyas)'),
(46611,	'Comercio al por mayor de combustibles sólidos, líquidos, gaseosos y productos conexos (excepto combustibles derivados del petróleo)'),
(46632,	'Comercio al por mayor de  artículos de ferretería, pinturas, productos de vidrio, equipo y materiales de fontanería y calefacción'),
(47241,	'Comercio al por menor de bebidas y productos del tabaco, en establecimientos especializados  (excepto licores y cigarrillos)'),
(47191,	'Comercio al por menor en establecimientos no especializados con surtido compuesto principalmente por productos diferentes de alimentos (víveres en general) y bebidas y tabaco (excepto drogas, medicamentos, textos escolares, libros y cuadernos.)'),
(47522,	'Comercio al por menor de artículos de ferretería, pinturas y productos de vidrio en establecimientos especializados (excepto materiales de construcción)'),
(47612,	'Comercio al por menor de periódicos, materiales y artículos de papelería y escritorio, en establecimientos especializados (excepto libros, textos escolares y cuadernos)'),
(47732,	'Comercio al por menor de productos cosméticos y artículos de tocador en establecimientos especializados (excepto productos  farmacéuticos y medicinales)'),
(47812,	'Comercio al por menor de  bebidas y tabaco en puestos de venta móviles (excepto licores y cigarrillos)'),
(47914,	'Comercio al por menor de demás productos n.c.p.  realizado a través de internet'),
(47924,	'Comercio al por menor de demás productos n.c.p.  realizado a través de casas de venta o por correo'),
(47994,	'Otros tipos de comercio al por menor no realizado en establecimientos, puestos de venta o mercados de demás productos n.c.p.'),
(64992,	'Actividades comerciales de las casas de empeño o compraventa'),
(4911,	'Transporte férreo de pasajeros'),
(4912,	'Transporte férreo de carga'),
(4921,	'Transporte de pasajeros'),
(4922,	'Transporte mixto'),
(4923,	'Transporte de carga por carretera'),
(4930,	'Transporte por tuberías'),
(5011,	'Transporte de pasajeros marítimo y de cabotaje'),
(5012,	'Transporte de carga marítimo y de cabotaje'),
(5021,	'Transporte fluvial de pasajeros'),
(5022,	'Transporte fluvial de carga'),
(5111,	'Transporte aéreo nacional de pasajeros'),
(5112,	'Transporte aéreo internacional de pasajeros'),
(5121,	'Transporte aéreo nacional de carga'),
(5122,	'Transporte aéreo internacional de carga'),
(5222,	'Actividades de puertos y servicios complementarios para el transporte acuático'),
(5813,	'Edición de periódicos, revistas y otras publicaciones periódicas'),
(6010,	'Actividades de programación y transmisión en el servicio de radiodifusión sonora'),
(58111,	'Servicio de edición de libros'),
(60201,	'Actividades de programación de televisión'),
(4111,	'Construcción de edificios residenciales'),
(4112,	'Construcción de edificios no residenciales'),
(4210,	'Construcción de carreteras y vías de ferrocarril'),
(4220,	'Construcción de proyectos de servicio público'),
(4290,	'Construcción de otras obras de ingeniería civil'),
(4311,	'Demolición'),
(4312,	'Preparación del terreno'),
(4321,	'Instalaciones eléctricas de la construcción'),
(4322,	'Instalaciones de fontanería, calefacción y aire acondicionado de la construcción'),
(4329,	'Otras instalaciones especializadas de la construcción'),
(4330,	'Terminación y acabado de edificios y obras de ingeniería civil'),
(4390,	'Otras actividades especializadas para la construcción de edificios y obras de ingeniería civil'),
(5914,	'Actividades de exhibición de películas cinematográficas y videos'),
(6202,	'Actividades de consultoría informática y actividades de administración de instalaciones informáticas'),
(39002,	'Actividades de saneamiento ambiental y otros servicios de gestión de desechos prestados por contratistas de construcción, constructores y urbanizadores'),
(69101,	'Actividades jurídicas como consultoría profesional'),
(69201,	'Actividades de contabilidad, teneduría de libros, auditoría financiera y asesoría tributaria como consultoría profesional'),
(70101,	'Actividades de administración empresarial como consultoría profesional'),
(70201,	'Actividades de consultoría de gestión'),
(71101,	'Actividades de arquitectura e ingeniería y otras actividades conexas de consultoría técnica'),
(71201,	'Ensayos y análisis técnicos como consultoría profesional'),
(72101,	'Investigaciones y desarrollo experimental en el campo de las ciencias naturales y la ingeniería  como consultoría profesional'),
(72201,	'Investigaciones y desarrollo experimental en el campo de las ciencias sociales y las humanidades  como consultoría profesional'),
(73201,	'Estudios de mercado y realización de encuestas de opinión pública como consultoría profesional'),
(74101,	'Actividades especializadas de diseño como consultoría profesional'),
(74901,	'Otras actividades profesionales, científicas y técnicas n.c.p. como consultoría profesional (incluye actividades de periodistas)'),
(5511,	'Alojamiento en hoteles'),
(5512,	'Alojamiento en aparta-hoteles'),
(5513,	'Alojamiento en centros vacacionales'),
(5514,	'Alojamiento rural'),
(5519,	'Otros tipos de alojamientos para visitantes'),
(5520,	'Actividades de zonas de camping y parques para vehículos recreacionales'),
(5530,	'Servicio por horas  de alojamiento'),
(5590,	'Otros tipos de alojamiento n.c.p.'),
(5611,	'Expendio a la mesa de comidas preparadas'),
(5612,	'Expendio por autoservicio de comidas preparadas'),
(5613,	'Expendio de comidas preparadas en cafeterías'),
(5619,	'Otros tipos de expendio de comidas preparadas n.c.p.'),
(5621,	'Catering para eventos'),
(5629,	'Actividades de otros servicios de comidas'),
(5630,	'Expendio de bebidas alcohólicas para el consumo dentro del establecimiento'),
(8010,	'Actividades de seguridad privada'),
(8020,	'Actividades de servicios de sistemas de seguridad'),
(8030,	'Actividades de detectives e investigadores privados'),
(64993,	'Servicios de las casas de empeño o compraventas'),
(161,	'Actividades de apoyo a la agricultura'),
(162,	'Actividades de apoyo a la ganadería'),
(164,	'Tratamiento de semillas para propagación'),
(240,	'Servicios de apoyo a la silvicultura'),
(910,	'Actividades de apoyo para la extracción de petróleo y de gas natural'),
(990,	'Actividades de apoyo para otras actividades de explotación de minas y canteras'),
(1061,	'Trilla de café'),
(1811,	'Actividades de impresión'),
(1812,	'Actividades de servicios relacionados con la impresión'),
(1820,	'Producción de copias a partir de grabaciones originales'),
(2592,	'Tratamiento y revestimiento de metales; mecanizado'),
(3311,	'Mantenimiento y reparación especializado de productos elaborados en metal'),
(3312,	'Mantenimiento y reparación especializado de maquinaria y equipo'),
(3313,	'Mantenimiento y reparación especializado de equipo electrónico y óptico'),
(3314,	'Mantenimiento y reparación especializado de equipo eléctrico'),
(3315,	'Mantenimiento y reparación especializado de equipo de transporte, excepto los vehículos automotores, motocicletas y bicicletas'),
(3319,	'Mantenimiento y reparación de otros tipos de equipos y sus componentes n.c.p.'),
(3320,	'Instalación especializada de maquinaria y equipo industrial'),
(3513,	'Distribución de energía eléctrica'),
(3530,	'Suministro de vapor y aire acondicionado'),
(3700,	'Evacuación y tratamiento de aguas residuales'),
(3811,	'Recolección de desechos no peligrosos'),
(3812,	'Recolección de desechos peligrosos'),
(4520,	'Mantenimiento y reparación de vehículos automotores.'),
(4542,	'Mantenimiento y reparación de motocicletas y de sus partes y piezas'),
(4610,	'Comercio al por mayor a cambio de una retribución o por contrata'),
(5221,	'Actividades de estaciones, vías y servicios complementarios para el transporte terrestre'),
(5210,	'Almacenamiento y depósito'),
(5223,	'Actividades de aeropuertos, servicios de navegación aérea y demás actividades conexas al transporte aéreo'),
(5224,	'Manipulación de carga'),
(5229,	'Otras actividades complementarias al transporte'),
(5310,	'Actividades postales nacionales'),
(5320,	'Actividades de mensajería'),
(5913,	'Actividades de distribución de películas cinematográficas, videos, programas, anuncios y comerciales de televisión'),
(6110,	'Actividades de telecomunicaciones alámbricas'),
(6120,	'Actividades de telecomunicaciones inalámbricas'),
(6130,	'Actividades de telecomunicación satelital'),
(6190,	'Otras actividades de telecomunicaciones'),
(6201,	'Actividades de desarrollo de sistemas informáticos (planificación, análisis, diseño, programación, pruebas)'),
(6209,	'Otras actividades de tecnologías de información y actividades de servicios informáticos'),
(6311,	'Procesamiento de datos, alojamiento (hosting) y actividades relacionadas'),
(6312,	'Portales Web'),
(6391,	'Actividades de agencias de noticias'),
(6399,	'Otras actividades de servicio de información n.c.p.'),
(6612,	'Corretaje de valores y de contratos de productos básicos'),
(6613,	'Otras actividades relacionadas con el mercado de valores'),
(6629,	'Evaluación de riesgos y daños, y otras actividades de servicios auxiliares'),
(66112,	'Actividades de las bolsas de valores'),
(6810,	'Actividades inmobiliarias realizadas con bienes propios o arrendados'),
(6820,	'Actividades inmobiliarias realizadas a cambio de una retribución o por contrata'),
(7310,	'Publicidad'),
(7420,	'Actividades de fotografía'),
(7500,	'Actividades veterinarias'),
(7710,	'Alquiler y arrendamiento de vehículos automotores'),
(7721,	'Alquiler y arrendamiento de equipo recreativo y deportivo'),
(7722,	'Alquiler de videos y discos'),
(7729,	'Alquiler y arrendamiento de otros efectos personales y enseres domésticos n.c.p.'),
(7730,	'Alquiler y arrendamiento de otros tipos de maquinaria, equipo y bienes tangibles n.c.p.'),
(7740,	'Arrendamiento de propiedad intelectual y productos similares, excepto obras protegidas por derechos de autor'),
(7810,	'Actividades de agencias de empleo'),
(7820,	'Actividades de agencias de empleo temporal'),
(7830,	'Otras actividades de suministro de recurso humano'),
(7911,	'Actividades de las agencias de viaje'),
(7912,	'Actividades de operadores turísticos'),
(7990,	'Otros servicios de reserva y actividades relacionadas'),
(8110,	'Actividades combinadas de apoyo a instalaciones'),
(8121,	'Limpieza general interior de edificios'),
(8129,	'Otras actividades de limpieza de edificios e instalaciones industriales'),
(8130,	'Actividades de paisajismo y servicios de mantenimiento conexos'),
(8211,	'Actividades combinadas de servicios administrativos de oficina'),
(8219,	'Fotocopiado, preparación de documentos y otras actividades especializadas de apoyo a oficina'),
(8220,	'Actividades de centros de llamadas (Call center)'),
(8230,	'Organización de convenciones y eventos comerciales'),
(8291,	'Actividades de agencias de cobranza y oficinas de calificación crediticia'),
(8292,	'Actividades de envase y empaque'),
(8299,	'Otras actividades de servicio de apoyo a las empresas n.c.p.'),
(8541,	'Educación técnica profesional'),
(8542,	'Educación tecnológica'),
(8543,	'Educación de instituciones universitarias o de escuelas tecnológicas'),
(8552,	'Enseñanza deportiva y recreativa'),
(8544,	'Educación de universidades'),
(8553,	'Enseñanza cultural'),
(8559,	'Otros tipos de educación n.c.p.'),
(8560,	'Actividades de apoyo a la educación'),
(8610,	'Actividades de hospitales y clínicas, con internación'),
(8720,	'Actividades de atención residencial, para el cuidado de pacientes con retardo mental, enfermedad mental y consumo de sustancias psicoactivas'),
(8730,	'Actividades de atención en instituciones para el cuidado de personas mayores y/o discapacitadas'),
(8790,	'Otras actividades de atención en instituciones con alojamiento'),
(8810,	'Actividades de asistencia social sin alojamiento para personas mayores y discapacitadas'),
(8890,	'Otras actividades de asistencia social sin alojamiento'),
(9321,	'Actividades de parques de atracciones y parques temáticos'),
(9511,	'Mantenimiento y reparación de computadores y de equipo periférico'),
(9512,	'Mantenimiento y reparación de equipos de comunicación'),
(9521,	'Mantenimiento y reparación de aparatos electrónicos de consumo'),
(9522,	'Mantenimiento y reparación de aparatos domésticos y equipos domésticos y de jardinería'),
(9523,	'Reparación de calzado y artículos de cuero'),
(9524,	'Reparación de muebles y accesorios para el hogar'),
(9529,	'Mantenimiento y reparación de otros efectos personales y enseres domésticos'),
(9601,	'Lavado y limpieza, incluso la limpieza en seco, de productos textiles y de piel'),
(9602,	'Peluquería y otros tratamientos de belleza'),
(9603,	'Pompas fúnebres y actividades relacionadas'),
(35202,	'Distribución de combustibles gaseosos por tuberías'),
(36002,	'Distribución de agua'),
(39001,	'Actividades de saneamiento ambiental y otros servicios de gestión de desechos (excepto los servicios prestados por contratistas de construcción, constructores y urbanizadores)'),
(60202,	'Actividades de transmisión de televisión'),
(69102,	'Actividades jurídicas en el ejercicio de una profesión liberal'),
(69202,	'Actividades de contabilidad, teneduría de libros, auditoría financiera y asesoría tributaria en el ejercicio de una profesión liberal'),
(70102,	'Actividades de administración empresarial en el ejercicio de una profesión liberal'),
(70202,	'Actividades de  gestión en el ejercicio de una profesión liberal'),
(71102,	'Actividades de arquitectura e ingeniería y otras actividades conexas en el ejercicio de una profesión liberal'),
(71202,	'Ensayos y análisis técnicos como consultoría profesional en el ejercicio de una profesión liberal'),
(72102,	'Investigaciones y desarrollo experimental en el campo de las ciencias naturales y la ingeniería  en el ejercicio de una profesión liberal'),
(72202,	'Investigaciones y desarrollo experimental en el campo de las ciencias sociales y las humanidades  en el ejercicio de una profesión liberal'),
(73202,	'Estudios de mercado y realización de encuestas de opinión pública en el ejercicio de una profesión liberal'),
(74102,	'Actividades especializadas de diseño en el ejercicio de una profesión liberal'),
(74902,	'Otras actividades profesionales, científicas y técnicas n.c.p. en el ejercicio de una profesión liberal'),
(85232,	'Educación de formación laboral'),
(85511,	'Educación académica no formal (excepto programas de educación básica primaria, básica secundaria y media no gradual con fines de validación)'),
(85512,	'Educación académica no formal impartida mediante programas de educación básica primaria, básica secundaria y media no gradual con fines de validación'),
(86211,	'Actividades de la práctica médica, sin internación (excepto actividades de promoción y prevención que realicen las entidades e instituciones promotoras y prestadoras de servicios de salud de naturaleza pública o privada, con recursos que provengan  del Sistema General  de Seguridad Social en  Salud.)'),
(86221,	'Actividades de la práctica odontológica, sin internación (excepto actividades de promoción y prevención que realicen las entidades e instituciones promotoras y prestadoras de servicios de salud de naturaleza pública o privada, con recursos que provengan  del Sistema General  de Seguridad Social en  Salud.)'),
(86911,	'Actividades de apoyo diagnóstico (excepto actividades de promoción y prevención que realicen las entidades e instituciones promotoras y prestadoras de servicios de salud de naturaleza pública o privada, con recursos que provengan  del Sistema General  de Seguridad Social en  Salud.)'),
(86921,	'Actividades de apoyo terapéutico (excepto actividades de promoción y prevención que realicen las entidades e instituciones promotoras y prestadoras de servicios de salud de naturaleza pública o privada, con recursos que provengan  del Sistema General  de Seguridad Social en  Salud.)'),
(86991,	'Otras actividades de atención de la salud humana (excepto actividades de promoción y prevención que realicen las entidades e instituciones promotoras y prestadoras de servicios de salud de naturaleza pública o privada, con recursos que provengan  del Sistema General  de Seguridad Social en  Salud.)'),
(87101,	'Actividades de atención residencial medicalizada de tipo general (excepto actividades de promoción y prevención que realicen las entidades e instituciones promotoras y prestadoras de servicios de salud de naturaleza pública o privada, con recursos que provengan  del Sistema General  de Seguridad Social en  Salud.)'),
(92001,	'Actividades de juegos de destreza, habilidad, conocimiento y fuerza'),
(93291,	'Otras actividades recreativas y de esparcimiento n.c.p. (excepto juegos de suerte y azar, discotecas y similares )'),
(9411,	'Actividades de asociaciones empresariales y de empleadores'),
(9499,	'Actividades de otras asociaciones n.c.p.'),
(8511,	'Educación de la primera infancia'),
(8512,	'Educación preescolar'),
(8513,	'Educación básica primaria'),
(8521,	'Educación básica secundaria'),
(8522,	'Educación media académica'),
(85231,	'Educación media técnica'),
(8530,	'Establecimientos que combinan diferentes niveles de educación inicial, preescolar, básica primaria, básica secundaria y media'),
(6411,	'Banca Central'),
(6412,	'Bancos comerciales'),
(6421,	'Actividades de las corporaciones financieras'),
(6422,	'Actividades de las compañías de financiamiento'),
(6423,	'Banca de segundo piso'),
(6424,	'Actividades de las cooperativas financieras'),
(6431,	'Fideicomisos, fondos y entidades financieras similares'),
(6491,	'Leasing financiero (arrendamiento financiero)'),
(6492,	'Actividades financieras de fondos de empleados y otras formas asociativas del sector solidario'),
(6493,	'Actividades de compra de cartera o factoring'),
(6494,	'Otras actividades de distribución de fondos'),
(6495,	'Instituciones especiales oficiales'),
(6511,	'Seguros generales'),
(6512,	'Seguros de vida'),
(6513,	'Reaseguros'),
(6521,	'Servicios de seguros sociales de salud'),
(6514,	'Capitalización'),
(6522,	'Servicios de seguros sociales de riesgos profesionales'),
(6532,	'Régimen de ahorro individual (RAI)'),
(6619,	'Otras actividades auxiliares de las actividades de servicios financieros n.c.p.'),
(6621,	'Actividades de agentes y corredores de seguros'),
(6630,	'Actividades de administración de fondos'),
(6614,	'Actividades de las casas de cambio'),
(6615,	'Actividades de los profesionales de compra y venta de divisas'),
(64991,	'Otras actividades de servicio financiero, excepto las de seguros y pensiones n.c.p.'),
(66111,	'Administración de mercados financieros (excepto actividades de las bolsas de valores)'),
)


class barrios(models.Model):
    id= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45,blank=False)

class empresas(models.Model):
    id = models.AutoField(primary_key=True)
    fechacenso = models.DateField(blank=False)
    nombre = models.TextField(blank=False)
    identificacion = models.TextField(blank=False)
    direccion = models.TextField(blank=False)
    propietario = models.TextField(blank=False)
    email = models.TextField(blank=False)
    telefono = models.BigIntegerField(blank=False)
    fecharegistro = models.DateField(blank=False)
    actividad = models.IntegerField(choices=ciiu)
    regimen = models.IntegerField(choices=tributarios)
    naturaleza = models.IntegerField(choices=naturalezas)
    stiker = models.IntegerField(blank=False)
    ica = models.BooleanField(blank=False)
    observaciones = models.TextField(blank=False)
    fotos = models.ImageField(blank=True)
    barrio = models.ForeignKey(barrios)

class administradores(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(blank=False, max_length=12, unique=True)
    clave = models.CharField(blank=False, max_length=10)
