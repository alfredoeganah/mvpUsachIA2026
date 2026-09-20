---
tipo: concepto
subtipo: analisis
tags: [hualaihue, caminos, vialidad, infraestructura]
fuentes: ["[[2026-09-20-osm-hualaihue3]]"]
actualizado: 2026-09-20
confianza: media
---

# Red vial de Hualaihué

916 vías, **514,5 km** mapeados en [[2026-09-20-osm-hualaihue3]]. Qué tipo de red es.

## Composición

| Tipo | N.º | km | |
|---|---|---|---|
| `track` (huella) | 309 | 152,8 | 30% |
| `tertiary` | 102 | 88,9 | 17% |
| `residential` | 224 | 75,4 | 15% |
| `path` (sendero) | 75 | 68,0 | 13% |
| `unclassified` | 85 | 67,1 | 13% |
| `trunk` | 67 | 54,9 | 11% |
| `footway`, `primary`, otros | 54 | 7,5 | 1% |

**La categoría más extensa de la red es la huella.** Sumando `track` y `path`, **43% de los
kilómetros mapeados no son camino vehicular propiamente tal**.

## Superficie: 20% de asfalto

| Superficie | km |
|---|---|
| Tierra (`ground`, `dirt`, `earth`) | 186,7 |
| **Asfalto** | **105,4** |
| Ripio (`gravel`, `fine_gravel`, `compacted`, `pebblestone`) | 100,9 |
| `unpaved` genérico | 56,6 |
| Sin dato | 53,2 |
| Otros (adoquín, hormigón, madera, metal…) | 11,7 |

El asfalto es el **20,5%** de la red y se concentra en la
[[carretera-austral|Carretera Austral]], que sola aporta 66,8 de esos 105,4 km. Fuera de la
Ruta 7 y del casco de [[hornopiren|Hornopirén]], la comuna es de tierra y ripio.

## Señales de dificultad

- **27 tramos declaran `smoothness`, y los 27 son `horrible` (14) o `very_horrible` (13).**
  Nadie etiqueta esto salvo cuando es notable, así que no es una muestra representativa —
  pero no hay un solo tramo etiquetado como transitable sin problema. ⚠️
- De los 309 tracks, 105,8 km son `grade2` y 13,2 km `grade3`–`grade5`.
- **83 puentes** (2,4 km en total) y **4 vados** (`ford`).
- **Dos huellas son `tidal`**: transitables solo con marea baja. Una es `flood_prone`.
- Solo 23 tramos declaran `maxspeed`, el más alto 70 km/h.

## Acceso restringido

- **41,1 km con `access=private`** — 8% de la red mapeada.
- 72,5 km con `access=permissive`: paso tolerado por el dueño, revocable.

Juntos, **113,6 km (22% de la red) no son vía pública garantizada.** Es un dato a tener
presente antes de afirmar que una localidad "tiene camino"
([[conectividad-de-hualaihue]]).

## Advertencia

El export no está recortado a la comuna: parte de estos 514,5 km cae fuera de Hualaihué.
Las longitudes se calculan solo sobre ways, nunca sobre relaciones, para no duplicar
([[2026-09-20-osm-hualaihue3]]).

## Fuentes

- [[2026-09-20-osm-hualaihue3]]
