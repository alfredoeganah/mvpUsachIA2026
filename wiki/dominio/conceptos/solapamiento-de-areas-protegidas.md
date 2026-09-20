---
tipo: concepto
subtipo: metodologia
tags: [metodologia, conservacion, gis, hualaihue]
fuentes: ["[[2026-09-20-osm-hualaihue1]]"]
actualizado: 2026-09-20
confianza: alta
---

# Solapamiento de áreas protegidas

**Las superficies de este wiki no son sumables.** Es la advertencia metodológica más
importante del proyecto y hay que repetirla en cualquier salida del MVP.

## El problema

La suma aritmética de las seis áreas protegidas del export da ~2,66 millones de ha. Esa cifra
no significa nada, por dos razones independientes:

**1. Anidamiento.** La [[reserva-biosfera-bosques-templados-lluviosos|Reserva de la Biósfera]]
(2.162.900 ha) es un marco superpuesto que contiene en su ámbito a las otras cinco. Contarla
junto a ellas duplica casi todo.

**2. Desborde comunal.** Los polígonos **no están recortados** a [[hualaihue|Hualaihué]]:

| Área | Superficie calculada | Rango latitudinal | ¿Contenida en la comuna? |
|---|---|---|---|
| [[reserva-biosfera-bosques-templados-lluviosos]] | 2.162.900 ha | −39,42 a −43,34 | no, muy por fuera |
| [[parque-nacional-pumalin]] | 402.183 ha | −42,02 a −43,44 | no, se extiende al sur |
| [[parque-nacional-hornopiren]] | 65.851 ha | −41,74 a −42,04 | plausible |
| [[fundo-huinay]] | 31.745 ha | −42,28 a −42,42 | plausible |
| [[sistema-humedales-hornopiren]] | 545 ha | −41,89 a −41,98 | sí |
| [[amcp-fiordo-comau]] | 144 ha | −42,29 a −42,42 | sí |

## Qué se necesita para resolverlo

El polígono oficial del límite comunal (fuente candidata: división político-administrativa
del INE o de la BCN). Con él, la operación correcta es: recortar cada polígono a la comuna,
**unir** las geometrías recortadas (no sumarlas) y recién ahí calcular superficie protegida y
porcentaje comunal. Anotado en [[preguntas-abiertas]].

## Fuentes

- [[2026-09-20-osm-hualaihue1]]
