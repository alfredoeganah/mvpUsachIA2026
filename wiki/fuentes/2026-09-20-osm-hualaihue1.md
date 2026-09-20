---
tipo: fuente
subtipo: geoespacial
tags: [osm, overpass, geojson, hualaihue, areas-protegidas]
archivo: raw/hualaihue1.geojson
actualizado: 2026-09-20
confianza: alta
---

# OSM Hualaihué — export Overpass (hualaihue1.geojson)

Export de OpenStreetMap generado con overpass-turbo el **2026-09-20T18:47:21Z**, con 10
polígonos de áreas protegidas y espacios públicos que intersectan la comuna de
[[hualaihue|Hualaihué]]. Es la primera fuente ingerida del wiki.

## Procedencia

| | |
|---|---|
| Archivo | `raw/hualaihue1.geojson` (10.076.078 bytes) |
| Generador | overpass-turbo |
| Timestamp | 2026-09-20T18:47:21Z |
| Origen | www.openstreetmap.org |
| Licencia | ODbL |

## Contenido

10 features: 8 `Polygon` y 2 `MultiPolygon`. Seis son áreas protegidas con
`boundary=protected_area`, tres son parques urbanos (`leisure=park`) y una es una mancha de
bosque sin nombre (`landuse=forest`, `leaf_type=needleleaved`, way/963216899, ~1,0 ha, junto
a Contao) que no justifica página propia.

| Feature | OSM id | Figura | Superficie calculada | Página |
|---|---|---|---|---|
| Reserva de la Biósfera Bosques Templados Lluviosos de los Andes Australes | relation/10731913 | Reserva de la Biósfera | 2.162.900 ha | [[reserva-biosfera-bosques-templados-lluviosos]] |
| Parque Nacional Pumalín Douglas Tompkins | relation/14151682 | Parque Nacional | 402.183 ha | [[parque-nacional-pumalin]] |
| Parque Nacional Hornopirén | relation/14152413 | Parque Nacional | 65.851 ha | [[parque-nacional-hornopiren]] |
| Fundo Huinay | relation/7782997 | Conservación privada | 31.745 ha | [[fundo-huinay]] |
| Sistema de Humedales Hornopirén | relation/17143122 | Humedal Urbano | 545 ha | [[sistema-humedales-hornopiren]] |
| Área Marina y Costera Protegida Fiordo Comau | relation/7735285 | AMCP-MU | 144 ha | [[amcp-fiordo-comau]] |
| Parque Costanera Hornopirén | way/275971531 | parque urbano | 1,1 ha | [[parque-costanera-hornopiren]] |
| Plaza de Armas (Hornopirén) | way/105827044 | plaza | 0,5 ha | [[plaza-de-armas-hornopiren]] |
| Plaza Contao | way/201214931 | plaza | 0,5 ha | [[plaza-contao]] |
| bosque sin nombre | way/963216899 | `landuse=forest` | 1,0 ha | — |

Las etiquetas OSM presentes en al menos una feature: `@id`, `name`, `leisure`, `boundary`,
`protection_title`, `start_date`, `type`, `operator`, `protect_class`, `website`, `wikidata`,
`wikipedia`, `source`, `addr:city`, `related_law`, `dog`, `chile:region`, `description`,
`note`, `alt_name`, `name:en`, `name:es`, `protected_area`, `addr:country`, `image`,
`official_name`, `official_name:en`, `ref`, `old_name`, `wikimedia_commons`, `opening_hours`,
`landuse`, `leaf_type`.

Cinco features traen `wikidata` y `wikipedia`, y cuatro apuntan a bases oficiales del MMA
(`areasprotegidas.mma.gob.cl`, `simbio.mma.gob.cl`, `humedaleschile.mma.gob.cl`). Ver
[[calidad-de-datos-osm]].

## Método de extracción

Superficies calculadas por excedente esférico (Chamberlain & Duquette, R = 6.371.008,8 m),
restando anillos interiores. Contrastadas contra las cifras oficiales que trae el propio
archivo, la diferencia es de 0,1–1,1% salvo en Fiordo Comau (ver abajo). Los centroides son
la media aritmética de los vértices, no el centroide del polígono: sirven para ubicar, no
para medir.

## Limitaciones

1. **Las geometrías no están recortadas a la comuna.** La consulta selecciona relaciones que
   intersectan Hualaihué, pero cada una viene completa. La Reserva de la Biósfera se extiende
   desde −43,34° hasta −39,42° de latitud (llega a la Región de La Araucanía) y Pumalín baja
   hasta −43,44° (Región de Aysén). **Sus superficies no son superficie protegida dentro de
   Hualaihué.** Calcular la fracción comunal requiere el polígono de la comuna, que aún no
   está en `raw/`. Ver [[preguntas-abiertas]].
2. **Los polígonos se solapan.** Fundo Huinay y la AMCP Fiordo Comau caen dentro del ámbito
   de la Reserva de la Biósfera. Sumar superficies sobrecontaría.
3. **Sin capa de población, caminos, ni límites administrativos.** El export es monotemático.
4. **Cobertura OSM parcial.** Falta al menos el Parque Nacional Alerce Andino y la Reserva
   Nacional Llanquihue, colindantes por el norte. ⚠️ observación del modelo, no verificada
   contra el archivo (que efectivamente no los contiene, pero eso no prueba que intersecten
   la comuna).

## Contradicciones detectadas

- **AMCP Fiordo Comau**: la etiqueta `description` declara **414,55 ha** protegidas, pero el
  polígono OSM mide **144,1 ha** — un 65% menos. La geometría en OSM parece incompleta
  respecto del acto que crea el área. Detalle en [[amcp-fiordo-comau]].
- **Sistema de Humedales Hornopirén**: `description` declara 551,51 ha, el polígono da
  545,2 ha (−1,1%). Diferencia compatible con el método de cálculo.
- **Parque Nacional Hornopirén**: la etiqueta `note` menciona 66.195,78 ha tras la ampliación
  de 2018, el polígono da 65.850,8 ha (−0,5%). Compatible.

## Fuentes

Esta es una página de fuente primaria. Archivo: `raw/hualaihue1.geojson`.
