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
