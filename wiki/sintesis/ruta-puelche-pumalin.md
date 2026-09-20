---
tipo: sintesis
subtipo: consulta-archivada
tags: [hualaihue, conectividad, ruteo, pumalin, carretera-austral, transbordadores]
fuentes: ["[[2026-09-20-osm-hualaihue1]]", "[[2026-09-20-osm-hualaihue2]]", "[[2026-09-20-osm-hualaihue3]]"]
actualizado: 2026-09-20
confianza: media
---

# Ruta Caleta Puelche → Parque Nacional Pumalín

Consulta del 2026-09-20: *¿cuál es el camino más corto desde Puelche al Parque Pumalín?*
Resuelta con análisis de grafo sobre las geometrías de `raw/` — primera aplicación del
método que pedía P-013.

**La respuesta depende de en qué te muevas, y la diferencia es de 22 km.**

|                       | Distancia    | Carretera | Transbordador | Desembarco                                                |
| --------------------- | ------------ | --------- | ------------- | --------------------------------------------------------- |
| **En vehículo**       | **112,9 km** | 55,3 km   | 57,6 km       | Leptepú (−42,4885 / −72,4365), **en el borde** del parque |
| A pie / solo pasajero | 91,2 km      | 55,3 km   | 35,9 km       | fiordo Comau (−42,2570 / −72,3933), dentro del parque     |

## La ruta en vehículo (112,9 km)

Es la única que sirve si llevas auto.

```
Caleta Puelche ──[Carretera Austral, 54,3 km]──> Hornopirén
     │
     └─ terminal de transbordadores de Hornopirén
            │
            └──[Somarco, 57,6 km de navegación, 3 h 30]──> Leptepú ✦ borde de Pumalín
```

**Tramo 1 — carretera, 54,3 km.** [[carretera-austral|Carretera Austral]] (Ruta 7) desde
[[hornopiren|Caleta Puelche]] hasta el terminal de [[hornopiren|Hornopirén]], con un desvío
por calles urbanas al final (Bernardo O'Higgins, Ingenieros Militares). Es el tramo asfaltado
de la comuna: la Ruta 7 es 75% asfalto ([[red-vial-de-hualaihue]]).

**Tramo 2 — transbordador, 57,6 km.** **Hornopirén – Leptepú**, operado por Somarco,
`duration=03:30`, con **reserva obligatoria y peaje**. Horarios:
https://www.barcazas.cl/barcazas/hornopiren-caleta-gonzalo

**Dónde te deja exactamente.** El último vértice de la ruta del transbordador coincide
**con un vértice del polígono** del [[parque-nacional-pumalin|Parque Nacional Pumalín]] — a
0 m. Está sobre el borde, no dentro: el punto-en-polígono da "dentro" con la coordenada
exacta y "fuera" al redondearla a 6 decimales. Es una degeneración de frontera, no un
resultado.

Consecuencia verificada: **en la red motorizada mapeada no hay ningún nodo estrictamente
dentro de Pumalín que sea alcanzable desde Caleta Puelche.** Solo 9 nodos viales
motorizados caen dentro del polígono y los 9 están desconectados de la red. En auto se llega
al borde del parque; seguir hacia adentro no está mapeado como camino vehicular. A pie sí:
la ruta de 91,2 km termina 25 km más al norte, en un punto inequívocamente interior.

⏱️ **Tiempo estimado: unas 4 h 30**, asumiendo 60 km/h promedio en la Ruta 7 (≈55 min) más
las 3 h 30 declaradas de navegación. **La velocidad es un supuesto del modelo**, no un dato:
solo 23 de 916 tramos del export declaran `maxspeed`. No incluye espera de embarque, que
sin horarios no se puede estimar (P-014).

## La ruta a pie (91,2 km)

21,7 km más corta, pero `motor_vehicle=no`: usa los botes de pasajeros de la red
**`CAM0015`** que bajan por el fiordo Comau desde Hornopirén
([[transbordadores-de-hualaihue]]). Mismos 55,3 km de carretera hasta Hornopirén, luego
35,9 km de navegación en tramos encadenados, desembarcando en el borde norte de Pumalín
frente al fiordo.

Que la ruta más corta sea la que no admite vehículos es el resultado más interesante de la
consulta: **en Hualaihué el mar es más recto que la tierra**, y la red estatal `CAM…` lo
aprovecha para los que viajan sin auto.

## Alternativa no evaluada: Caleta Gonzalo

Existe un segundo cruce vehicular hacia el sur, **[[pichicolo|Pichicolo]] – Caleta Gonzalo**
(Naviera Puelche, 77,8 km, `duration=05:00`, con reserva y peaje), y el tramo de carretera
hasta Pichicolo es más corto que hasta Hornopirén. No se calculó como ruta completa porque
**el punto de desembarco de Caleta Gonzalo no cae dentro del polígono OSM de Pumalín** — está
a 18 km del camino mapeado más cercano y fuera del área. Caleta Gonzalo es la puerta clásica
del parque, así que esto huele a límite del dato más que a realidad. Anotado como P-016.

## Método

Grafo no dirigido construido con las geometrías de [[2026-09-20-osm-hualaihue3]]:

- **Nodos**: vértices de `way`, redondeados a 6 decimales. **Solo ways, nunca relaciones**
  (D-007), para no duplicar aristas.
- **Aristas**: pares de vértices consecutivos, ponderadas por distancia con proyección plana
  local.
- **Conectores de tolerancia**: aristas artificiales entre nodos a menos de **60 m** entre
  sí. Fueron necesarias — las ways de OSM no siempre comparten el nodo exacto en los empalmes
  — y son la principal fuente de error del cálculo: un conector puede unir dos vías que en
  terreno no se tocan.
- **Filtro de modo (vehículo)**: se excluyen `ferry=footway`, `motor_vehicle=no`, y
  `highway` en `path`/`footway`/`steps`/`cycleway`.
- **Origen**: punto de la localidad Caleta Puelche de [[2026-09-20-osm-hualaihue2]]
  (−41,7422 / −72,6499); el nodo de red más cercano está a 9 m.
- **Destino**: cualquier nodo dentro del polígono de Pumalín de
  [[2026-09-20-osm-hualaihue1]] (458 nodos), por ray casting.
- **Algoritmo**: Dijkstra con corte al primer nodo destino alcanzado.
- Se excluyen las rutas de largo alcance que solo pasan por la zona (Navimag,
  Puerto Montt – Chaitén).

## Advertencias

- **Es distancia sobre la red mapeada, no tiempo de viaje real.** Sin horarios de
  transbordador no hay tiempo puerta a puerta (P-014).
- **Los conectores de 60 m pueden crear conexiones que no existen.** El resultado es
  plausible y coherente con la estructura conocida del territorio
  ([[conectividad-de-hualaihue]]), pero no está validado contra terreno.
- El export no está recortado a la comuna; parte de la red usada cae fuera de Hualaihué.
- "Llegar a Pumalín" se define aquí como **alcanzar el polígono**, no un acceso habilitado
  del parque. No hay en `raw/` ninguna capa de porterías, senderos ni guardaparques.
- **El desembarco de Leptepú cae sobre el borde del polígono**, lo que hace que el resultado
  dependa del redondeo. Los 112,9 km son la distancia hasta ese punto; tratarlos como
  "distancia hasta el interior del parque" sería forzar el dato.

## Un tercer borde del dato

Entre esta consulta y P-016 aparecen dos puntos donde el polígono OSM de Pumalín se comporta
raro justo en los accesos: **Caleta Gonzalo queda fuera** y **Leptepú cae exactamente encima
del borde**. Las dos puertas del parque están en el límite de su propia geometría. Refuerza
la sospecha de que el polígono necesita contraste con la fuente oficial del MMA — la misma
carencia que arrastra [[amcp-fiordo-comau]] desde la primera ingesta.

## Qué confirma esta consulta

Es la demostración numérica de la tesis de [[overview]]: **para ir de un punto de Hualaihué
a otro hay que embarcarse.** Los 54,3 km de carretera desde Puelche terminan en Hornopirén, y
de ahí en adelante el único camino es el agua — 3 h 30 con reserva previa. La comuna no es
un tramo de la Carretera Austral: es el intervalo entre dos de sus cortes
([[carretera-austral]]).

## Fuentes

- [[2026-09-20-osm-hualaihue1]] — polígono de Pumalín
- [[2026-09-20-osm-hualaihue2]] — punto de origen (Caleta Puelche)
- [[2026-09-20-osm-hualaihue3]] — red vial y transbordadores
