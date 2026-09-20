---
tipo: concepto
subtipo: metodologia
tags: [osm, datos, conservacion, metodologia]
fuentes: ["[[2026-09-20-osm-hualaihue1]]"]
actualizado: 2026-09-20
confianza: media
---

# `protect_class` en OSM

OpenStreetMap codifica el tipo de protección de un `boundary=protected_area` en la etiqueta
numérica `protect_class`. Valores observados en [[hualaihue|Hualaihué]]:

| Valor | Área | Lectura |
|---|---|---|
| 2 | [[parque-nacional-hornopiren]], [[parque-nacional-pumalin]] | parque nacional (equivalente IUCN II) |
| 5 | [[amcp-fiordo-comau]] | paisaje protegido / uso múltiple |
| 7 | [[sistema-humedales-hornopiren]] | recurso natural específico |
| 98 | [[reserva-biosfera-bosques-templados-lluviosos]] | reserva de la biósfera (fuera de la escala IUCN) |
| — | [[fundo-huinay]] | sin valor asignado |

## Cómo usarlo (y cómo no)

`protect_class` es una **etiqueta colaborativa**, no una clasificación oficial. Sirve para
agrupar y filtrar dentro de OSM; no equivale a la categoría IUCN ni a la figura legal
chilena, y su ausencia no significa "no protegido" — el caso de [[fundo-huinay]], con 31.745
ha y sin valor, lo muestra.

Para cualquier análisis del MVP: **filtrar por `boundary=protected_area`, no por
`protect_class`**, o se pierde la conservación privada.

⚠️ La correspondencia entre estos valores y las categorías IUCN es conocimiento general del
modelo y no está verificada contra la documentación de OSM ni contra fuente ingerida.

## Fuentes

- [[2026-09-20-osm-hualaihue1]]
