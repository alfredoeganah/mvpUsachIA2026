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

**P-004 · No hay ninguna capa humana.** Población, localidades, comunidades, caminos,
economía (pesca, salmonicultura, turismo), conectividad. El wiki describe un territorio sin
gente.
→ *Fuente necesaria:* Censo/INE a nivel comunal; capa de localidades pobladas.

**P-005 · ¿Faltan áreas protegidas vecinas?** El export no incluye el Parque Nacional Alerce
Andino ni la Reserva Nacional Llanquihue, colindantes por el norte. Puede que simplemente no
intersecten la comuna.
→ *Verificación:* nueva consulta Overpass con bbox ampliado.

**P-006 · ¿Cuánto de Pumalín cae en Hualaihué?** Depende de P-001.

## Sobre el proyecto

**P-007 · ¿Cuál es el objetivo del MVP?** El charter
([[proyecto-mvp-usach-ia-2026]]) está casi vacío: entregable, usuario, rol de la IA y pregunta
de investigación siguen sin definir. **Esto se resuelve conversando, no buscando fuentes.**

**P-008 · ¿Qué hace la "IA" del MVP?** ¿El wiki mismo es el producto, o el wiki alimenta otra
cosa? La respuesta cambia qué páginas vale la pena construir.
