---
tipo: proyecto
subtipo: backlog
tags: [proyecto, lint, fuentes, backlog]
actualizado: 2026-09-20
confianza: alta
---

# Preguntas abiertas

Lo que el wiki no puede responder hoy, y qué fuente lo resolvería. Ordenado por cuánto
desbloquea.

## Bloqueantes

**P-001 · ¿Qué porcentaje de Hualaihué está protegido?**
No calculable: los polígonos no están recortados a la comuna y se solapan entre sí
([[solapamiento-de-areas-protegidas]]).
→ *Fuente necesaria:* polígono oficial del límite comunal (división político-administrativa,
INE o BCN). **Es la fuente de mayor retorno por costo del backlog.**

**P-002 · ¿Cuál es la superficie real de la AMCP Fiordo Comau?**
414,55 ha declaradas contra 144,1 ha de polígono OSM — 65% de diferencia sin explicar
([[amcp-fiordo-comau]]).
→ *Fuente necesaria:* polígono oficial del MMA (`simbio.mma.gob.cl`, ficha 1711) o el decreto
(http://bcn.cl/31cp9).

**P-003 · ¿Qué obliga realmente cada figura de protección?**
Cinco figuras en el wiki y ninguna con su régimen jurídico respaldado por fuente. Las cuatro
páginas de figura legal están en `confianza: baja`: [[parque-nacional]], [[amcp-mu]],
[[conservacion-privada]], [[humedal-urbano]].
→ *Fuente necesaria:* los tres textos de la BCN ya enlazados en el dato OSM
(http://bcn.cl/31csf, http://bcn.cl/2qz6g, http://bcn.cl/31cp9) y la Ley 21.202.

## Vacíos de datos

**P-004 · ~~No hay ninguna capa humana.~~ Parcialmente resuelta el 2026-09-20** con
[[2026-09-20-osm-hualaihue2]]: 65 localidades, 8.701 hab (INE 2017), turismo y equipamiento.
**Caminos y conectividad resueltos el 2026-09-20** con [[2026-09-20-osm-hualaihue3]].
**Sigue faltando:** economía (pesca, salmonicultura, empleo), escuelas, y un censo más
reciente que 2017.
→ *Fuente necesaria:* Censo 2024 a nivel de entidad poblada.

**P-005 · ¿Faltan áreas protegidas vecinas?** El export no incluye el Parque Nacional Alerce
Andino ni la Reserva Nacional Llanquihue, colindantes por el norte. Puede que simplemente no
intersecten la comuna.
→ *Verificación:* nueva consulta Overpass con bbox ampliado.

**P-006 · ¿Cuánto de Pumalín cae en Hualaihué?** Depende de P-001.

## Nuevas, abiertas por la segunda ingesta

**P-009 · ¿Cuál es la relación entre los 35 habitantes de [[huinay|Huinay]] y la fundación
propietaria del suelo donde viven?** Único caso del territorio de población dentro de
[[conservacion-privada|conservación privada]] ([[poblacion-en-areas-protegidas]]). Quién
decide el uso del suelo, qué acceso tienen, si hay vínculo laboral. **Es la pregunta más
interesante que el wiki puede plantear hoy y no responder.**
→ *Fuente necesaria:* documentación de la [[fundacion-huinay|Fundación Huinay]], prensa
local, o trabajo de campo.

**P-010 · ¿El déficit de servicios es real o es falta de mapeo?** 18 localidades con 1.588
hab sin nada mapeado a 2 km ([[acceso-a-servicios]]), y cero escuelas en toda la comuna según
OSM. Las fuentes actuales **no permiten separar vacío real de vacío de mapeo**.
→ *Fuente necesaria:* directorio oficial de establecimientos educacionales (MINEDUC) y de
salud (MINSAL/DEIS) por comuna. **Segunda prioridad después de P-001.**

**P-011 · ¿Los conglomerados fragmentados son localidades distintas?** Cinco registros
"Pichicolo" (418 hab sumados), tres "Quildaco/Quidaco" (215 hab). Si son una sola entidad
poblada, el ranking de localidades del wiki está mal ordenado ([[poblacion-de-hualaihue]]).
→ *Fuente necesaria:* listado INE de entidades pobladas de la comuna.

**P-012 · ¿Qué relación hay entre turismo y áreas protegidas?** En los datos son dos capas
que casi no se tocan: un solo camping declara operador de parque nacional, y las Termas de
Cahuelmó están dentro de [[parque-nacional-pumalin|Pumalín]] sin que ninguna etiqueta lo
diga ([[turismo-en-hualaihue]]). Presumiblemente son la misma economía.
→ *Fuente necesaria:* estadísticas de visitación de CONAF; SERNATUR.

## Nuevas, abiertas por la tercera ingesta

**P-013 · ~~¿Qué localidades están realmente conectadas a la red vial?~~ Método implementado
el 2026-09-20**, aplicado por ahora a un solo par origen-destino en
[[ruta-puelche-pumalin]]. Falta correrlo sobre las 65 localidades para reemplazar la columna
"Acceso" de [[localidades-de-hualaihue]] por conectividad real. Aprendizaje del primer uso:
las ways de OSM no siempre comparten nodo en los empalmes, hay que añadir **conectores de
tolerancia de 60 m**, y esos conectores son la principal fuente de error.

*Enunciado original:* ¿Qué localidades están realmente conectadas a la red vial? El wiki hoy mide
*proximidad* al camino más cercano (58 de 65 localidades a menos de 1 km), no conectividad.
Con el 30% de la red en huellas y 113,6 km de acceso privado o tolerado, la cifra puede estar
sobrevalorando el acceso real ([[conectividad-de-hualaihue]], [[red-vial-de-hualaihue]]).
→ *Cómo se resuelve:* análisis de grafo sobre las geometrías que **ya están en `raw/`** —
construir la red, encontrar componentes conexas, medir distancia real por la red hasta
Hornopirén. **No requiere fuente nueva. Es la tarea de mayor retorno que se puede hacer hoy
sin salir a buscar datos.**

**P-014 · ¿Cuál es el nivel de servicio de los transbordadores?** Se conoce la topología y la
duración, pero solo una de once rutas declara frecuencia. Sin horarios no se puede estimar
tiempo de viaje real a Hornopirén ni el costo del aislamiento.
→ *Fuente necesaria:* horarios de barcazas.cl, testuario.cl y Naviera Puelche; itinerarios de
las rutas `CAM…` del MOP.

**P-015 · ¿Cuánto cuesta y cuánto demora llegar a Huinay?** Está a **56,5 km de navegación**
de [[hornopiren|Hornopirén]], encadenando cinco tramos de la ruta estatal `CAM0015`
(Manila, Quiaca, Telele, Huinay, Porcelana Chica) — todos de solo pasajeros y con tarifa.
Sin horarios ni tarifas no se puede estimar el costo real del aislamiento de sus 35
habitantes. Refuerza P-009.
→ *Fuente necesaria:* itinerarios y tarifas de las rutas `CAM…` del MOP, y el PDF
*"Cómo llegar a Huinay"* de la [[fundacion-huinay|Fundación Huinay]] referenciado en OSM.

**P-016 · ¿Por qué Caleta Gonzalo queda fuera del polígono de Pumalín?** Es la puerta
clásica del parque y el destino del transbordador [[pichicolo|Pichicolo]] – Caleta Gonzalo
(77,8 km, 5 h), pero su punto de desembarco **no cae dentro del polígono OSM** y está a 18 km
del camino mapeado más cercano ([[ruta-puelche-pumalin]]). Huele a límite del dato más que a
realidad del territorio.
→ *Fuente necesaria:* polígono oficial del MMA para Pumalín — la misma que resolvería P-002.

## Sobre el proyecto

**P-007 · ¿Cuál es el objetivo del MVP?** El charter
([[proyecto-mvp-usach-ia-2026]]) está casi vacío: entregable, usuario, rol de la IA y pregunta
de investigación siguen sin definir. **Esto se resuelve conversando, no buscando fuentes.**

**P-008 · ¿Qué hace la "IA" del MVP?** ¿El wiki mismo es el producto, o el wiki alimenta otra
cosa? La respuesta cambia qué páginas vale la pena construir.
