---
tipo: fuente
subtipo: geoespacial
tags: [osm, overpass, geojson, hualaihue, poblacion, turismo, servicios]
archivo: raw/hualaihue2.geojson
actualizado: 2026-09-20
confianza: alta
---

# OSM Hualaihué — poblados y servicios (hualaihue2.geojson)

Segundo export de OpenStreetMap vía overpass-turbo, del **2026-09-20T19:09:51Z**, con 124
features de **localidades, turismo y equipamiento** de [[hualaihue|Hualaihué]]. Es la capa
humana que faltaba: responde la pregunta P-004 de [[preguntas-abiertas]].

## Procedencia

| | |
|---|---|
| Archivo | `raw/hualaihue2.geojson` (57.525 bytes) |
| Generador | overpass-turbo |
| Timestamp | 2026-09-20T19:09:51Z |
| Origen | www.openstreetmap.org |
| Licencia | ODbL |

## Contenido

124 features: **111 puntos y 13 polígonos**. Sin solapamiento entre categorías.

| Categoría | N.º | Detalle |
|---|---|---|
| `place` | 65 | 1 `town` ([[hornopiren\|Hornopirén]]), 1 `village` ([[contao\|Contao]]), 52 `hamlet`, 11 `isolated_dwelling` |
| `tourism` | 47 | 21 campings, 8 miradores, 7 hospedajes, 6 atracciones, 3 hoteles, 1 oficina de información, 1 museo |
| `amenity` | 12 | 8 lugares de culto, 2 CESFAM, 1 municipalidad, 1 mercado |

**45 de las 65 localidades traen población**, todas con `population:date=2017` y
`source:population=INE`. Suma: **8.701 habitantes** — cobertura de la fuente, no población
comunal (ver abajo).

Los 13 polígonos son edificios: iglesias y capillas (6), CESFAM (2), municipalidad, hotel,
y tres sin nombre.

## Método de extracción

Poblaciones leídas directamente de la etiqueta `population`. Cruces geoespaciales contra
[[2026-09-20-osm-hualaihue1]] por ray casting punto-en-polígono sobre el anillo exterior,
descontando anillos interiores. Distancias por proyección plana local. Resultados en
[[poblacion-en-areas-protegidas]] y [[acceso-a-servicios]].

## Lo que esta fuente desbloquea

Por primera vez se pueden cruzar las dos capas del wiki: **quién vive dónde respecto de las
áreas protegidas**. El resultado está en [[poblacion-en-areas-protegidas]] y es el hallazgo
central de esta ingesta.

También permite [[poblacion-de-hualaihue]], [[turismo-en-hualaihue]] y
[[acceso-a-servicios]].

## Limitaciones

1. **8.701 hab no es la población de Hualaihué.** Es la suma de las 45 localidades que OSM
   mapea *con* dato. Faltan 20 localidades sin cifra y se desconoce cuántas localidades no
   están mapeadas. El censo comunal sigue sin estar en `raw/`.
2. **Los datos de población son de 2017.** Tienen nueve años al momento de esta ingesta.
3. **Un `place` es un punto, no un área.** Decir "la localidad está dentro del área
   protegida" significa que su punto nominal cae dentro del polígono. Para localidades
   extensas es una aproximación.
4. **La ausencia de servicio no es ausencia real.** El déficit que muestra
   [[acceso-a-servicios]] es déficit *de mapeo*, y el sesgo de mapeo favorece a
   [[hornopiren|Hornopirén]] ([[calidad-de-datos-osm]]).
5. **Turismo sobrerrepresentado frente a servicios básicos.** 47 features de turismo contra
   12 de equipamiento. No hay escuelas, ni comercio, ni transporte, ni bomberos, ni
   carabineros en el export. Eso es un sesgo de la consulta o de OSM, no del territorio.
6. **Sin límite comunal**, igual que la primera fuente: P-001 sigue abierta.

## Notas de etiquetado

- `Quildaco Bajo`, `Quildaco Muy` y `Quidaco Alto` conviven con grafías distintas de lo que
  parece la misma raíz toponímica. Probable error de tipeo en OSM (`Muy` por `Medio`).
  ⚠️ inferencia, no verificada.
- Tres localidades y tres features de turismo vienen **sin `name`**.
- `is_in=Chile, Latin America` en 5 localidades: etiqueta obsoleta de OSM, sin valor
  analítico.
- `Cabañas Lehuan` / `name:es=Cabañas Lahuan`: el nombre principal y el localizado difieren.

## Fuentes

Página de fuente primaria. Archivo: `raw/hualaihue2.geojson`.
