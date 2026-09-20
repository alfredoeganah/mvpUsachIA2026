---
tipo: fuente
subtipo: geoespacial
tags: [osm, overpass, geojson, hualaihue, transporte, caminos, transbordadores]
archivo: raw/hualaihue3.geojson
actualizado: 2026-09-20
confianza: alta
---

# OSM Hualaihué — red de transporte (hualaihue3.geojson)

Tercer export de OpenStreetMap vía overpass-turbo, del **2026-09-20T19:16:51Z**, con 1.004
features de **caminos, rutas y transbordadores**. Completa la parte de conectividad que
quedaba pendiente en P-004 y trae el dato estructural más importante del wiki hasta ahora:
[[hualaihue|Hualaihué]] está **cortada en ambos extremos** de la Carretera Austral.

## Procedencia

| | |
|---|---|
| Archivo | `raw/hualaihue3.geojson` (3.935.716 bytes) |
| Generador | overpass-turbo |
| Timestamp | 2026-09-20T19:16:51Z |
| Origen | www.openstreetmap.org |
| Licencia | ODbL |

## Contenido

1.004 features: **970 `LineString`, 33 `Point`, 1 `MultiLineString`**, con 64 etiquetas
distintas.

| Grupo | N.º | Detalle |
|---|---|---|
| `highway` | 916 | **514,5 km** de vía mapeada → [[red-vial-de-hualaihue]] |
| `route=ferry` | 54 | 34 ways + 20 relaciones → [[transbordadores-de-hualaihue]] |
| Nodos | 33 | paradas (`role=stop`) de las relaciones de transbordador; sin etiquetas propias |
| `route=road` | 1 | la relación de la [[carretera-austral\|Ruta 7]] |

## Método de extracción

Longitudes por proyección plana local sobre la latitud media de cada segmento, sumadas
segmento a segmento. Distancias localidad↔vía por proyección punto-segmento sobre el mismo
plano local. Cruces contra las localidades de [[2026-09-20-osm-hualaihue2]]; resultados en
[[conectividad-de-hualaihue]].

**Cuidado con el doble conteo:** las relaciones de ruta agregan las mismas geometrías que sus
ways. `ref=7` suma 406,3 km si se cuentan relación y ways juntos, pero la Ruta 7 como vía son
**89,0 km** en este export. Todas las cifras de longitud de este wiki están calculadas **solo
sobre ways**, nunca sobre relaciones. Ver D-007 en [[decisiones]].

## Lo que esta fuente desbloquea

**La Carretera Austral no es continua en Hualaihué.** Se entra a la comuna por el
transbordador Caleta La Arena – Caleta Puelche (6 km, 45 min) y se sale por Hornopirén –
Leptepú (58,7 km, 3 h 30, con reserva). No hay forma de cruzar la comuna en auto sin dos
embarques. Detalle en [[conectividad-de-hualaihue]].

Además: [[red-vial-de-hualaihue]] (514,5 km, 20% asfalto),
[[transbordadores-de-hualaihue]] (el catálogo de rutas y operadores), y el acceso a
[[huinay|Huinay]] documentado por la propia [[fundacion-huinay|Fundación Huinay]] (P-009).

## Limitaciones

1. **No está recortado a la comuna**, como las dos fuentes anteriores. La relación de la
   Ruta 7 cubre Puerto Montt – Chaitén – límite de Aysén; las rutas de Navimag
   (Puerto Montt – Puerto Natales, 74 h) y de Naviera Austral solo pasan por la zona. Los
   514,5 km de vía incluyen tramos fuera de Hualaihué.
2. **Proximidad no es conectividad.** Que una localidad tenga un camino mapeado a 30 m no
   significa que ese camino llegue a alguna parte: puede ser una huella local sin conexión a
   la red. Separar ambas cosas exige un análisis de grafo que estas fuentes permiten pero que
   aún no se ha hecho ([[preguntas-abiertas]], P-013).
3. **Sin horarios ni frecuencias, salvo una excepción.** Solo el transbordador de Caleta La
   Arena trae `interval`. Del resto se conoce la duración, no cuántas veces al día opera.
4. **Sin datos de flujo**: ni tránsito, ni pasajeros, ni carga.
5. **Calidad de vía casi sin etiquetar:** solo 27 de 916 tramos declaran `smoothness` y 23
   declaran `maxspeed`.

## Notas de etiquetado

- Los 33 nodos **no tienen etiquetas propias**: solo `@id` y `@relations`. Son puntos de
  parada referenciados desde las relaciones de transbordador. Su nombre hay que leerlo de
  `reltags`.
- Las rutas marítimas del Estado vienen con códigos `ref` de camino — **`CAM0015`,
  `CAM0078`, `CAM0005`** — es decir, el Estado las clasifica como caminos, no como servicios
  marítimos. Hallazgo relevante para [[conectividad-de-hualaihue]].
- Cada ruta de transbordador aparece **dos veces**, una por sentido (ida y vuelta como
  relaciones separadas). Contarlas como rutas distintas duplicaría.
- `Quidalco Bajo - La Poza II` (ruta W-749) usa una cuarta grafía del topónimo
  Quildaco/Quidaco/Quidalco. Ver [[calidad-de-datos-osm]].

## Fuentes

Página de fuente primaria. Archivo: `raw/hualaihue3.geojson`.
