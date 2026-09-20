---
tipo: concepto
subtipo: metodologia
tags: [osm, datos, calidad, metodologia]
fuentes: ["[[2026-09-20-osm-hualaihue1]]"]
actualizado: 2026-09-20
confianza: alta
---

# Calidad de los datos OSM en Hualaihué

Qué tan confiable es la única fuente ingerida hasta ahora
([[2026-09-20-osm-hualaihue1]]), y qué sesgos hereda cualquier análisis que se construya
sobre ella.

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

## Implicancia para el MVP

Cualquier indicador que el MVP calcule sobre esta base debe declarar que mide **cobertura
OSM**, no realidad territorial. Si el producto va a afirmar cosas sobre el territorio, hace
falta al menos una fuente oficial de contraste. Ver [[preguntas-abiertas]].

## Fuentes

- [[2026-09-20-osm-hualaihue1]]
