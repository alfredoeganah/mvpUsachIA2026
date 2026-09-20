---
tipo: proyecto
subtipo: bitacora-decisiones
tags: [proyecto, decisiones]
actualizado: 2026-09-20
confianza: alta
---

# Decisiones

Registro de decisiones de diseño del wiki y del proyecto. Append-only: una decisión revocada
se marca como superada, no se borra.

## [2026-09-20] D-001 — Wiki en dos capas: dominio y proyecto

**Decisión.** Separar `wiki/dominio/` (territorio de Hualaihué) de `wiki/proyecto/` (el MVP).
El proyecto enlaza al dominio; el dominio no depende del proyecto.

**Por qué.** El conocimiento territorial sobrevive a cualquier cambio de rumbo del MVP. Si el
proyecto pivota, el wiki de dominio sigue sirviendo.

**Costo.** Más estructura que mantener y la tentación permanente de mezclar capas.

## [2026-09-20] D-002 — Wiki en español

**Decisión.** Todas las páginas en español. Nombres de archivo en kebab-case sin tildes,
títulos y alias con tildes.

**Por qué.** Las fuentes son chilenas (OSM en español, normativa, bases del MMA). Traducir
introduce errores en nombres propios y figuras legales que no tienen equivalente en inglés.

## [2026-09-20] D-003 — Confianza explícita en cada página

**Decisión.** Campo `confianza: alta|media|baja` en el frontmatter, y marca en línea
`⚠️ sin fuente ingerida` en cada afirmación que venga del conocimiento general del modelo.

**Por qué.** Un wiki escrito por un LLM sobre pocas fuentes acumula afirmaciones plausibles
pero no verificadas. Sin marcarlas, a los tres meses son indistinguibles de las fundadas.
Hace el lint posible: `grep -l "confianza: baja" -r wiki/`.

## [2026-09-20] D-004 — Reportar superficie oficial y calculada por separado

**Decisión.** Nunca reemplazar una cifra oficial por una calculada ni promediarlas. Las dos
se muestran, con el método del cálculo declarado.

**Por qué.** El caso [[amcp-fiordo-comau]] (414,55 ha declaradas vs. 144,1 ha de polígono)
habría desaparecido bajo cualquier criterio de "elegir un número". La discrepancia **es** el
hallazgo.

## [2026-09-20] D-005 — Umbral de página propia y páginas catálogo

**Decisión.** No toda entidad de una fuente tiene página. Localidades con ≥ 200 hab, la
capital comunal, o relevancia estructural (ej. estar dentro de un área protegida) sí; el
resto va como fila en una página catálogo — [[localidades-de-hualaihue]]. Los servicios
(campings, hospedajes, miradores, capillas) casi nunca tienen página. Regla completa en
`CLAUDE.md`.

**Por qué.** La segunda fuente trajo 124 elementos. Una página por elemento daría un grafo de
cientos de nodos hoja sin enlaces entrantes, ilegible en Obsidian y sin valor analítico. El
catálogo conserva el 100% del dato sin saturar el grafo.

**Costo.** Cuando una fuente nueva hace cruzar el umbral a una localidad, hay que crearle
página y reemplazar su fila por un enlace. Trabajo manual recurrente.

## [2026-09-20] D-006 — Carpeta `wiki/sintesis/` para cruces entre fuentes

**Decisión.** Los análisis que combinan dos o más fuentes viven en `wiki/sintesis/`, no
dentro de la página de una fuente ni de una entidad.

**Por qué.** [[poblacion-en-areas-protegidas]] es el hallazgo más valioso del wiki y no
pertenece a ninguna de las dos fuentes que lo producen. Enterrado en una página de fuente,
nadie lo encuentra. Además obliga a preguntarse en cada ingesta *qué se puede calcular ahora
que antes no*, que es donde está el valor de acumular.

## [2026-09-20] D-007 — Longitudes solo sobre ways, nunca sobre relaciones

**Decisión.** Toda cifra de longitud del wiki se calcula sumando **ways**. Las relaciones de
ruta (`type=route`) se usan para leer metadatos —operador, duración, nombre oficial— pero
nunca para medir.

**Por qué.** Una relación de ruta agrega las geometrías de sus ways: contar ambos duplica.
La [[carretera-austral|Ruta 7]] da 406,3 km sumando relación y ways, y 89,0 km contando solo
ways. La diferencia no es un matiz, es un factor de 4,5.

**Cómo verificarlo.** Si una longitud parece desproporcionada frente a la escala del
territorio, sospechar doble conteo antes que error de proyección.
