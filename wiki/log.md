# Bitácora

Registro cronológico append-only. Últimas entradas: `grep "^## \[" wiki/log.md | tail -5`

## [2026-09-20] setup | Instanciación del wiki

Se instancia el patrón LLM Wiki sobre el vault `mvpUsachIA2026`, a partir de [[Prompts]].

- Esquema escrito en `CLAUDE.md`: tres capas, frontmatter obligatorio, reglas de veracidad,
  operaciones (ingesta / consulta / lint), convenciones geoespaciales.
- Estructura creada: `wiki/{fuentes,dominio/entidades,dominio/conceptos,proyecto}`.
- Decisiones D-001 (dos capas), D-002 (español), D-003 (confianza explícita),
  D-004 (superficie oficial y calculada por separado). Ver [[decisiones]].

## [2026-09-20] ingesta | OSM Hualaihué — export Overpass (hualaihue1.geojson)

Primera fuente. 10 features (8 Polygon, 2 MultiPolygon), 10,1 MB, licencia ODbL,
timestamp 2026-09-20T18:47:21Z.

**Páginas creadas (30):** 1 de fuente, 9 de áreas protegidas y espacios públicos, 4 de
lugares, 3 de instituciones/eventos, 8 de conceptos, 4 de proyecto y la síntesis
[[overview]] — más `index.md` y `log.md`.

**Hallazgos:**
- Cinco figuras de protección distintas conviven en la comuna; cronología 1988→2024 que va
  de la cordillera al borde urbano. Ver [[overview]].
- 2018 como año bisagra: [[donacion-tompkins-2018]] mueve ~420.000 ha al Estado.
- Contradicción sin resolver: [[amcp-fiordo-comau]] declara 414,55 ha, su polígono mide
  144,1 ha (−65%).
- Los polígonos no están recortados a la comuna y se solapan →
  [[solapamiento-de-areas-protegidas]]. Bloquea cualquier indicador comunal.
- Áreas verdes urbanas mapeadas en toda la comuna: 1,6 ha.

**Método:** superficies por excedente esférico (Chamberlain & Duquette, R = 6.371.008,8 m).
Contrastado contra cifras oficiales: diferencias de 0,1–1,1%, salvo Fiordo Comau.

**Abierto:** P-001 a P-008 en [[preguntas-abiertas]]. La de mayor retorno es P-001, el
polígono del límite comunal.

## [2026-09-20] lint | Primera pasada, wiki completo

Se escribe `lint.py` y se ejecuta sobre las 32 páginas.

- Enlaces rotos: **0**
- Páginas huérfanas: **0**
- Sin frontmatter: **0**
- `confianza: baja`: **7** — las cuatro figuras legales ([[parque-nacional]], [[amcp-mu]],
  [[conservacion-privada]], [[humedal-urbano]]), [[contao]], [[huinay]] y el charter
  [[proyecto-mvp-usach-ia-2026]].

Las cuatro figuras legales se resuelven con una sola ingesta (los textos de la BCN ya
enlazados en el dato OSM, P-003). El charter se resuelve conversando, no con fuentes (P-007).

## [2026-09-20] ingesta | OSM Hualaihué — poblados y servicios (hualaihue2.geojson)

Segunda fuente. 124 features (111 puntos, 13 polígonos), 57,5 KB, ODbL,
timestamp 2026-09-20T19:09:51Z. Es la **capa humana** que faltaba: resuelve parcialmente
P-004.

**Contenido:** 65 localidades (1 `town`, 1 `village`, 52 caseríos, 11 viviendas aisladas),
47 features de turismo, 12 de equipamiento. 45 localidades con población INE 2017, suma
8.701 hab.

**Hallazgo central — [[poblacion-en-areas-protegidas]]:** cruce punto-en-polígono con la
primera fuente. **48 de 65 localidades y el 98% de la población mapeada (8.524 hab) caen
dentro de la [[reserva-biosfera-bosques-templados-lluviosos|Reserva de la Biósfera]]. Las
otras cuatro figuras estrictas no contienen a nadie**; [[huinay|Huinay]] (35 hab) es el único
caso de población dentro de [[conservacion-privada|conservación privada]]. La tesis del wiki
se reescribió en torno a esto ([[overview]]).

**Otros hallazgos:**
- 18 localidades con 1.588 hab sin ningún servicio mapeado a 2 km; 17 localidades insulares
  fuera de toda protección → [[acceso-a-servicios]].
- Equipamiento total de la comuna en OSM: 2 CESFAM, 1 municipio, 1 mercado, 8 lugares de
  culto. **Cero escuelas** contra 47 features de turismo → sesgo grave, ver
  [[calidad-de-datos-osm]] y P-010.
- Fragmentación de topónimos: 5 registros "Pichicolo" (418 hab), 3 "Quildaco" (215 hab) →
  P-011.
- Turismo de camping y microempresa familiar, desconectado de las áreas protegidas en los
  datos → [[turismo-en-hualaihue]], P-012.

**Páginas creadas (13):** 1 de fuente, 2 de síntesis ([[poblacion-en-areas-protegidas]],
[[acceso-a-servicios]]), 1 catálogo ([[localidades-de-hualaihue]]), 5 localidades
([[aulen]], [[caleta-manzano]], [[pichicolo]], [[rolecha]], [[la-poza]]), 1 institución
([[municipalidad-de-hualaihue]]), 2 de análisis ([[poblacion-de-hualaihue]],
[[turismo-en-hualaihue]]), más la reescritura de [[overview]].

**Páginas actualizadas (13):** [[hualaihue]], [[hornopiren]], [[contao]], [[huinay]],
[[fundo-huinay]], [[reserva-biosfera-bosques-templados-lluviosos]],
[[parque-nacional-hornopiren]], [[sistema-humedales-hornopiren]], [[amcp-fiordo-comau]],
[[calidad-de-datos-osm]], [[caso-de-estudio]], [[preguntas-abiertas]], [[index]].

**Esquema:** se añaden a `CLAUDE.md` las reglas de umbral de página propia, análisis entre
fuentes y datos de población; se crea `wiki/sintesis/`. Decisiones D-005 y D-006.

**Abierto:** P-009 a P-012 nuevas. P-001 (límite comunal) sigue siendo la de mayor retorno;
P-010 (escuelas y salud oficiales) pasa a segunda prioridad.

## [2026-09-20] ingesta | OSM Hualaihué — red de transporte (hualaihue3.geojson)

Tercera fuente. 1.004 features (970 LineString, 33 Point, 1 MultiLineString), 3,9 MB, ODbL,
timestamp 2026-09-20T19:16:51Z. Cierra la parte de **conectividad** de P-004.

**Contenido:** 916 vías (514,5 km), 54 features de transbordador (34 ways + 20 relaciones),
33 nodos de parada sin etiquetas propias, y la relación de la [[carretera-austral|Ruta 7]].

**Hallazgo central — [[conectividad-de-hualaihue]]:** la **Carretera Austral se interrumpe en
los dos extremos de la comuna**. Se entra por el transbordador Caleta La Arena – Caleta
Puelche (6 km, 45 min, cada 30 min) y se sale por Hornopirén – Leptepú (58,7 km, 3 h 30, con
reserva y peaje). **No se entra ni se sale de Hualaihué por tierra.**
[[hornopiren|Hornopirén]] es el final del camino, lo que reencuadra su concentración de
servicios como la de un punto de espera obligado. Tesis de [[overview]] reescrita.

**Corrección a lo afirmado tras la segunda ingesta:** el "Hualaihué insular sin nada" está
mejor conectado de lo que sugería el wiki. 58 de 65 localidades tienen camino mapeado a
menos de 1 km (8.680 hab, 99,8%); las caletas insulares están servidas por transbordadores
con **código de camino del Estado** (`CAM0015`, `CAM0078`, `CAM0005`). Lo que falta allí es
equipamiento, no vía de acceso. Registrado en [[acceso-a-servicios]] y
[[poblacion-en-areas-protegidas]].

**Otros hallazgos:**
- Red vial: 514,5 km, **20% de asfalto**, 43% huellas y senderos, 22% con acceso privado o
  tolerado; los 27 tramos que declaran `smoothness` son todos `horrible` o peor →
  [[red-vial-de-hualaihue]].
- [[pichicolo|Pichicolo]] (228 hab) es cabecera de seis rutas marítimas: el segundo puerto de
  la comuna.
- El acceso a [[huinay|Huinay]] está documentado por la propia
  [[fundacion-huinay|Fundación Huinay]] (`source` = su PDF *"Cómo llegar a Huinay"*), y sus
  rutas no llevan código estatal → refuerza P-009, abre P-015.
- La **V-707** es la única vía del territorio que existe para acceder a un área protegida.
- El corredor **W-609** (53,5 km, *"Contao - La Poza - Rolecha - El Varal"*) tiene nombre
  oficial y cero servicios mapeados a lo largo.

**Riesgo metodológico nuevo:** doble conteo relación/way. `ref=7` da 406,3 km sumando ambos
y 89,0 km contando solo ways. Fijado en D-007.

**Páginas creadas (5):** [[2026-09-20-osm-hualaihue3]], [[conectividad-de-hualaihue]],
[[carretera-austral]], [[transbordadores-de-hualaihue]], [[red-vial-de-hualaihue]].

**Páginas actualizadas (17):** [[overview]], [[index]], [[localidades-de-hualaihue]]
(regenerada con columna de acceso), [[hualaihue]], [[hornopiren]], [[contao]],
[[pichicolo]], [[huinay]], [[rolecha]], [[la-poza]], [[caleta-manzano]],
[[parque-nacional-hornopiren]], [[parque-nacional-pumalin]], [[acceso-a-servicios]],
[[poblacion-en-areas-protegidas]], [[calidad-de-datos-osm]], [[caso-de-estudio]],
[[preguntas-abiertas]].

**Abierto:** P-013 a P-015 nuevas. **P-013 (conectividad real por análisis de grafo) no
requiere fuente nueva**: se puede resolver hoy con lo que ya está en `raw/`. P-001 (límite
comunal) sigue siendo la fuente externa de mayor retorno.

### Corrección dentro de la misma ingesta

Al detallar las rutas `CAM…` se detectó un error en la primera redacción de [[huinay]]: se
había afirmado que **ninguna** ruta hacia Huinay llevaba código estatal. Es falso — Huinay
es parada de la cadena `CAM0015`, a 56,5 km de navegación de [[hornopiren|Hornopirén]] vía
Manila, Quiaca, Telele y Porcelana Chica. Corregido en [[huinay]],
[[transbordadores-de-hualaihue]], [[conectividad-de-hualaihue]] y P-015.

El `CAM0015` completo son **96,2 km en 11 tramos**; sumado a `CAM0078` (14,0 km) y `CAM0005`
(25,3 km), el Estado mantiene **135,5 km de "camino" que es mar** en la comuna.

## [2026-09-20] consulta | Camino más corto de Caleta Puelche al Parque Pumalín

Respuesta archivada en [[ruta-puelche-pumalin]].

**Resultado:** 112,9 km en vehículo (55,3 carretera + 57,6 de transbordador, desembarcando en
Leptepú, **sobre el borde** del parque) frente a **91,2 km a pie** por los botes de pasajeros del
`CAM0015`. **La ruta más corta es 21,7 km más corta y no admite autos.**

**Método:** primera aplicación del análisis de grafo que pedía P-013 — Dijkstra sobre las
ways de [[2026-09-20-osm-hualaihue3]], con conectores de tolerancia de 60 m, filtro de modo,
y destino por punto-en-polígono contra Pumalín. Detalle y advertencias en la página.

**Hallazgos laterales:**
- Las ways de OSM no siempre comparten nodo en los empalmes: sin conectores de tolerancia el
  grafo queda fragmentado. Es la principal fuente de error del método y quedó documentado en
  P-013.
- El desembarco de **Caleta Gonzalo no cae dentro del polígono OSM de Pumalín**, pese a ser
  la puerta clásica del parque → nueva P-016.
- **Corrección dentro de la consulta:** se había escrito que Leptepú queda dentro del parque.
  No: su último vértice **coincide con un vértice del polígono** (0 m), y el punto-en-polígono
  se da vuelta según el redondeo. Además, los 9 nodos viales motorizados que sí caen dentro
  de Pumalín están desconectados de la red. Corregido en [[ruta-puelche-pumalin]] y
  [[conectividad-de-hualaihue]].
- Las dos puertas del parque (Leptepú y Caleta Gonzalo) quedan en el límite de su propia
  geometría: el polígono necesita contraste oficial, igual que [[amcp-fiordo-comau]].

**Actualizadas:** [[index]], [[conectividad-de-hualaihue]], [[preguntas-abiertas]].

## [2026-09-20] consulta | Rutas para llegar a Río Blanco

Archivada como página de entidad [[rio-blanco]] en vez de consulta suelta: el caserío no
tenía página y la ruta rinde más dentro de ella.

**Rutas:** [[hornopiren|Hornopirén]] → Río Blanco **6,6 km** por la Ruta 7 (tramo `tertiary`
pero asfaltado); Caleta Puelche → Río Blanco **61,0 km**. Ambas enteramente terrestres — sin
transbordador, a diferencia de [[ruta-puelche-pumalin]].

**Desambiguación necesaria:** hay tres "Río Blanco" en las fuentes (el caserío, un mirador a
2,0 km y una calle de ripio dentro de Hornopirén), más el río que da nombre a uno de los tres
cursos del [[sistema-humedales-hornopiren|humedal urbano]]. Quedó documentada en la página.

**Excepción a D-005:** el caserío no tiene dato de población y aun así recibe página, por
relevancia estructural — 400 m del humedal, en el corredor Hornopirén–humedal–parque
nacional, y tres de los ocho miradores de la comuna a menos de 3 km.

**Actualizadas:** [[index]], [[localidades-de-hualaihue]], [[sistema-humedales-hornopiren]].
