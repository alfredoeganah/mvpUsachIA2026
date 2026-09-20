---
tipo: concepto
subtipo: analisis
tags: [hualaihue, poblacion, ine, demografia]
fuentes: ["[[2026-09-20-osm-hualaihue2]]"]
actualizado: 2026-09-20
confianza: media
---

# Población de Hualaihué

Cómo se distribuye la población mapeada de [[hualaihue|Hualaihué]], según los datos INE 2017
que trae [[2026-09-20-osm-hualaihue2]]. Catálogo completo en [[localidades-de-hualaihue]].

## La cifra y su letra chica

**8.701 habitantes** en 45 localidades con dato. Pero:

- 20 de las 65 localidades mapeadas **no traen población**.
- No se sabe cuántas localidades existen sin estar mapeadas.
- El dato es de **2017**: nueve años de antigüedad.

Por lo tanto **8.701 hab es un piso de cobertura OSM, no la población comunal.** Escribirlo
como "población de Hualaihué" sería un error. El censo comunal sigue fuera de `raw/`.

## Una capital y una cola muy larga

| Categoría | Localidades | Hab | % del total mapeado |
|---|---|---|---|
| `town` — [[hornopiren\|Hornopirén]] | 1 | 3.629 | 42% |
| `village` — [[contao\|Contao]] | 1 | 784 | 9% |
| `hamlet` — caseríos | 52 (43 con dato) | 4.288 | 49% |
| `isolated_dwelling` | 11 | (sin dato) | — |

La mitad de la población vive repartida en **43 caseríos con dato**, de mediana ~84
habitantes. La mayor concentración fuera de la capital no es un pueblo sino un racimo: el
grupo de [[aulen|Aulén]] (Aulén 396 + Estero Soto 113 + Quildaco Muy 84 + Quildaco Bajo 84 +
[[la-poza|La Poza]] 213) alcanza los 890 hab en pocos kilómetros, más que Contao, y sin
ningún equipamiento mapeado.

Las cinco localidades sobre 200 hab: [[aulen|Aulén]] (396),
[[caleta-manzano|Caleta Manzano]] (329), [[pichicolo|Pichicolo]] (228),
[[rolecha|Rolecha]] (227), [[la-poza|La Poza]] (213).

## El efecto de fragmentación

Cinco registros distintos comparten el topónimo *Pichicolo* y suman 418 hab; tres comparten
*Quildaco/Quidaco* y suman 215. Ordenar localidades por población **subestima sistemáticamente
a los conglomerados dispersos** frente a un pueblo compacto como Contao. Cualquier ranking
que produzca el MVP debe advertirlo. Ver [[pichicolo]].

## Geografía de la población

- El 98% vive dentro de la Reserva de la Biósfera → [[poblacion-en-areas-protegidas]].
- 1.588 hab en 18 localidades sin servicio mapeado a menos de 2 km →
  [[acceso-a-servicios]].
- 177 hab con dato viven en el Hualaihué insular, fuera de toda figura de protección.

## Fuentes

- [[2026-09-20-osm-hualaihue2]]
