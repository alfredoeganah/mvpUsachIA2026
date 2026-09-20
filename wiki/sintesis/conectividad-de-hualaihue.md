---
tipo: sintesis
subtipo: cruce-de-fuentes
tags: [hualaihue, conectividad, transporte, carretera-austral, transbordadores]
fuentes: ["[[2026-09-20-osm-hualaihue2]]", "[[2026-09-20-osm-hualaihue3]]"]
actualizado: 2026-09-20
confianza: media
---

# Conectividad de Hualaihué

Cruce de la red de transporte de [[2026-09-20-osm-hualaihue3]] con las 65 localidades de
[[2026-09-20-osm-hualaihue2]]. **Reencuadra el retrato del territorio que traía el wiki.**

## El hecho estructural: una comuna entre dos cortes

La [[carretera-austral|Carretera Austral]] atraviesa Hualaihué, pero **no es continua**. En
los dos extremos de la comuna el camino se acaba y hay que embarcarse:

| Corte | Ruta | Distancia | Duración | Reserva | Frecuencia |
|---|---|---|---|---|---|
| **Norte** (entrada) | Caleta La Arena – Caleta Puelche | 6,0 km | 0:45 | no | cada 30 min |
| **Sur** (salida) | Hornopirén – Leptepú | 58,7 km | 3:30 | **sí** | sin dato |

Es decir: **no se puede entrar ni salir de Hualaihué por tierra.** Quien recorre la Carretera
Austral de norte a sur cruza la comuna entre dos embarques, y el del sur dura tres horas y
media y exige reserva previa.

Esto cambia la lectura de todo lo anterior. [[hornopiren|Hornopirén]] no es solo la capital
comunal con el 42% de la población: es **el final del camino continuo** y el puerto desde el
que se retoma la Carretera Austral. Su concentración de servicios, campings y hospedajes
([[acceso-a-servicios]], [[turismo-en-hualaihue]]) es en buena medida la de un punto de
espera obligado.

## Corrección a una afirmación previa del wiki

Después de la segunda ingesta, este wiki describía un "Hualaihué insular sin nada". El dato
de transporte lo matiza:

**58 de las 65 localidades tienen un camino mapeado a menos de 1 km** — 8.680 de los 8.701
habitantes mapeados (99,8%). Incluido [[huinay|Huinay]], a 30 m de una huella.

Solo 7 localidades quedan a más de 1 km de cualquier camino, y **4 de ellas están a menos de
150 m de una ruta de transbordador**: Puerto Bonito, Baltazar, Chaucahue y Caleta Andrade
(21 hab con dato). Las tres restantes — Llanchid, Isla Pelada y una sin nombre — no tienen
dato de población.

⚠️ **Con una advertencia que no hay que soltar:** proximidad a un camino mapeado **no es
conectividad**. Una huella (`highway=track`) de 200 m junto a una caleta no conecta con nada.
El 30% de la red son tracks y hay 41 km de vía con `access=private`. Verificar conectividad
real exige análisis de grafo sobre la red, que estas fuentes permiten y que todavía no se ha
hecho (P-013).

## El Estado clasifica el mar como camino

Las rutas marítimas que sirven al Hualaihué insular vienen etiquetadas con **códigos de
camino**: `CAM0015`, `CAM0078`, `CAM0005`. No son servicios turísticos: son la red vial del
Estado continuada sobre el agua.

| Código | km | Sirve a |
|---|---|---|
| `CAM0015` | 96,2 | la cadena del fiordo Comau — Hornopirén → Manila → Quiaca → Telele → [[huinay\|Huinay]] → Porcelana Chica (56,5 km) — más los ramales a Caleta Llancahué, Vodudahue, Caleta Andrade, Baltazar y Puerto Bonito |
| `CAM0078` | 14,0 | el circuito insular de [[pichicolo\|Pichicolo]]: Isla Malomacún, Isla Llinguar, Isla Llanchid, Costa Pichicolo Sur |
| `CAM0005` | 25,3 | Poyo – [[pichicolo\|Pichicolo]] |

**135,5 km de "camino" que en realidad es mar.**

Son los nombres de las localidades que la segunda ingesta había marcado como *el Hualaihué
sin servicios y sin protección* ([[poblacion-en-areas-protegidas]],
[[acceso-a-servicios]]). **No están desconectadas: están conectadas por mar, con rutas
codificadas como caminos públicos.** Todas son `ferry=footway`: `motor_vehicle=no`, solo
pasajeros, casi todas con tarifa. Incluye a [[huinay|Huinay]], a 56,5 km de navegación de
[[hornopiren|Hornopirén]] por cinco tramos encadenados.

Catálogo completo en [[transbordadores-de-hualaihue]].

## Pichicolo, el otro puerto

[[pichicolo|Pichicolo]] (228 hab) aparece como cabecera de **seis rutas de transbordador** —
hacia Ayacara, Chumeldén, Caleta Gonzalo, Poyo y las islas del `CAM0078`. Es el segundo nodo
marítimo de la comuna después de Hornopirén, y explica por qué un caserío de 228 habitantes
tiene el peso que tiene.

## El corredor W-609

Los nombres oficiales de las rutas secundarias describen la cadena de poblados mejor que
cualquier análisis:

| Ruta | Nombre oficial | km |
|---|---|---|
| W-609 | Contao - La Poza - Rolecha - El Varal | 53,5 |
| W-739 | Caleta El Manzano - Puntilla Quillón | 7,6 |
| W-751 | Tentelhue - Nao - Rolecha | 6,5 |
| W-765 | Quildaco Bajo - La Poza | 6,4 |
| W-611 | Pichicolo - Puntilla Pichicolo | 5,7 |
| V-707 | Cruce Ruta 7 - Acceso a Parque Hornopirén | 4,9 |

La **W-609** enhebra en 53,5 km el eje poniente de la comuna: [[contao|Contao]] (784 hab),
[[la-poza|La Poza]] (213), [[rolecha|Rolecha]] (227) y El Varal (112). Ese corredor es
precisamente donde [[acceso-a-servicios]] no encontraba equipamiento: hay camino, y camino
con nombre oficial, pero no hay servicios mapeados a lo largo de él.

La **V-707** es la única vía del export que existe para acceder a un área protegida: el
[[parque-nacional-hornopiren|Parque Nacional Hornopirén]].

## Verificado por ruteo

La consulta [[ruta-puelche-pumalin]] aplicó análisis de grafo sobre esta misma red y
confirma la estructura descrita: desde Caleta Puelche la carretera llega hasta Hornopirén
(54,3 km) y ahí se acaba; seguir al sur cuesta 3 h 30 de navegación con reserva. También
mostró que **la ruta más corta en distancia no admite vehículos**: 91,2 km por los botes de
pasajeros del `CAM0015` contra 112,9 km en auto.

Y un límite duro de la red mapeada: **ningún nodo vial motorizado dentro de Pumalín es
alcanzable** desde la comuna. El transbordador deja el auto en el borde del parque y ahí
termina el camino conocido.

## Advertencias metodológicas

- Las longitudes se calculan **solo sobre ways**, nunca sobre relaciones, para no duplicar
  (ver D-007 en [[decisiones]]).
- El export no está recortado a la comuna: parte de los 514,5 km está fuera.
- Cada ruta de transbordador aparece dos veces, una por sentido.
- Localidad = un punto; la distancia a un camino se mide desde su centro nominal.
- Sin horarios (salvo Caleta La Arena) y sin datos de flujo: se conoce la topología de la
  red, no su servicio.

## Fuentes

- [[2026-09-20-osm-hualaihue2]] — localidades y población
- [[2026-09-20-osm-hualaihue3]] — caminos y transbordadores
