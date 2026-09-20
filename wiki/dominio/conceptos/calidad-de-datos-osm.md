---
tipo: concepto
subtipo: metodologia
tags: [osm, datos, calidad, metodologia]
fuentes: ["[[2026-09-20-osm-hualaihue1]]", "[[2026-09-20-osm-hualaihue2]]", "[[2026-09-20-osm-hualaihue3]]"]
actualizado: 2026-09-20
confianza: alta
---

# Calidad de los datos OSM en Hualaihué

Qué tan confiables son las tres fuentes OSM ingeridas y qué sesgos hereda cualquier análisis
que se construya sobre ellas.

## Lo que está bien

- **Trazabilidad alta**: 5 de 10 features traen `wikidata` y `wikipedia`; 4 apuntan a bases
  oficiales del MMA (`areasprotegidas.mma.gob.cl`, `simbio.mma.gob.cl`,
  `humedaleschile.mma.gob.cl`); 3 traen `related_law` con URL de la BCN.
- **Detalle geométrico razonable** en las áreas grandes: 89.932 vértices la reserva de la
  biósfera, 19.274 Pumalín, 3.871 el humedal.
- **Actualizada**: incluye el humedal urbano declarado en febrero de 2024.

## Los sesgos

**1. Sesgo urbano.** Los tres espacios públicos mapeados suman 2,1 ha y **dos de los tres
están en [[hornopiren|Hornopirén]]**. [[contao|Contao]] tiene una sola plaza, dibujada con 5
vértices (un rectángulo). Ausencia de dato ≠ ausencia de plaza.

**2. Etiquetado heterogéneo.** `CONAF` vs `Conaf` en features distintas. Solo 6 de 10
features traen `boundary`; solo 3 traen `addr:city`. No se puede filtrar por comuna usando
las etiquetas.

**3. Geometría vs. acto administrativo.** El caso [[amcp-fiordo-comau]]: 414,55 ha declaradas
contra 144,1 ha de polígono. OSM puede ir por detrás del decreto.

**4. Recorte inexistente.** Ver [[solapamiento-de-areas-protegidas]].

## Lo que agrega la segunda fuente

**A favor.** Las 45 poblaciones vienen con `population:date=2017` y `source:population=INE`:
procedencia explícita, algo poco común en OSM. Dos campings traen `check_date=2026-01-09`,
verificación en terreno de hace ocho meses.

**En contra, y es grave:** la fuente mapea **47 features de turismo contra 12 de
equipamiento básico**. No hay escuelas, comercio, transporte, bomberos ni carabineros. Un
análisis ingenuo concluiría que Hualaihué es una comuna turística sin servicios públicos.
Lo que en realidad muestra es **qué mapea la gente que mapea OSM**: lo que un visitante
busca, no lo que un habitante usa.

**El sesgo urbano se confirma y se agrava.** El 42% de las features de turismo y
equipamiento está a menos de 3 km de [[hornopiren|Hornopirén]]. 18 localidades con población
—1.588 hab— no tienen nada mapeado a 2 km ([[acceso-a-servicios]]). Parte de ese vacío es
real y parte es que nadie las ha mapeado; **las fuentes actuales no permiten separarlos**.

**Toponimia inconsistente.** `Quildaco Bajo` / `Quildaco Muy` / `Quidaco Alto`; `Cabañas
Lehuan` con `name:es=Cabañas Lahuan`; tres localidades y tres servicios sin `name`. Cinco
localidades arrastran el tag obsoleto `is_in=Chile, Latin America`.

**Fragmentación de topónimos.** Cinco registros "Pichicolo" y tres "Quildaco/Quidaco" que
probablemente son conglomerados únicos. Cualquier ranking por localidad los subestima
([[poblacion-de-hualaihue]]).

## Lo que agrega la tercera fuente

**A favor.** Es la fuente mejor referenciada del wiki: la relación de la
[[carretera-austral|Ruta 7]] declara `source=Vialidad`, 213 tramos traen `source:ref` y 212
un `official_name` de la vialidad chilena. Los nombres oficiales de ruta
(*"Contao - La Poza - Rolecha - El Varal"*) son en sí mismos un dato sobre qué localidades el
Estado considera conectadas.

**Riesgo nuevo: doble conteo.** Las relaciones de ruta agregan las mismas geometrías que sus
ways. `ref=7` da 406,3 km sumando ambos y 89,0 km contando solo ways. Toda longitud del wiki
se calcula sobre ways (D-007).

**Riesgo nuevo: proximidad ≠ conectividad.** La distancia de una localidad al camino más
cercano es fácil de calcular y fácil de malinterpretar: el 30% de la red son huellas y 113,6
km (22%) tienen acceso privado o solo tolerado. Ver [[red-vial-de-hualaihue]] y P-013.

**Cobertura desigual dentro de la propia fuente.** Solo 27 de 916 tramos declaran
`smoothness`, 23 `maxspeed`. Solo un transbordador de once declara frecuencia. Se conoce la
topología de la red, no su nivel de servicio.

**Cuarta grafía de Quildaco.** La ruta W-749 se llama oficialmente *"Quidalco Bajo - La Poza
II"*, sumando `Quidalco` a las tres grafías ya conocidas. El problema toponímico no es solo
de OSM: viene también de los nombres oficiales.

## Implicancia para el MVP

Cualquier indicador que el MVP calcule sobre esta base debe declarar que mide **cobertura
OSM**, no realidad territorial. Si el producto va a afirmar cosas sobre el territorio, hace
falta al menos una fuente oficial de contraste. Ver [[preguntas-abiertas]].

## Fuentes

- [[2026-09-20-osm-hualaihue1]] · [[2026-09-20-osm-hualaihue2]] · [[2026-09-20-osm-hualaihue3]]
