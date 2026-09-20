# Bitácora

Registro cronológico append-only. Últimas entradas: `grep "^## \[" wiki/log.md | tail -5`

## [2026-09-20] setup | Instanciación del wiki

Se instancia el patrón LLM Wiki sobre el vault `mvpUsachIA2026`, a partir de [[Prompt 1]].

- Esquema escrito en `CLAUDE.md`: tres capas, frontmatter obligatorio, reglas de veracidad,
  operaciones (ingesta / consulta / lint), convenciones geoespaciales.
- Estructura creada: `wiki/{fuentes,dominio/entidades,dominio/conceptos,proyecto}`.
- Decisiones D-001 (dos capas), D-002 (español), D-003 (confianza explícita),
  D-004 (superficie oficial y calculada por separado). Ver [[decisiones]].

## [2026-09-20] ingesta | OSM Hualaihué — export Overpass (hualaihue1.geojson)

Primera fuente. 10 features (8 Polygon, 2 MultiPolygon), 10,1 MB, licencia ODbL,
timestamp 2026-09-20T18:47:21Z.

**Páginas creadas (30):** 1 de fuente, 9 de áreas protegidas y espacios públicos, 4 de
lugares, 3 de instituciones/eventos, 8 de conceptos, 4 de proyecto y la síntesis
[[overview]] — más `index.md` y `log.md`.

**Hallazgos:**
- Cinco figuras de protección distintas conviven en la comuna; cronología 1988→2024 que va
  de la cordillera al borde urbano. Ver [[overview]].
- 2018 como año bisagra: [[donacion-tompkins-2018]] mueve ~420.000 ha al Estado.
- Contradicción sin resolver: [[amcp-fiordo-comau]] declara 414,55 ha, su polígono mide
  144,1 ha (−65%).
- Los polígonos no están recortados a la comuna y se solapan →
  [[solapamiento-de-areas-protegidas]]. Bloquea cualquier indicador comunal.
- Áreas verdes urbanas mapeadas en toda la comuna: 1,6 ha.

**Método:** superficies por excedente esférico (Chamberlain & Duquette, R = 6.371.008,8 m).
Contrastado contra cifras oficiales: diferencias de 0,1–1,1%, salvo Fiordo Comau.

**Abierto:** P-001 a P-008 en [[preguntas-abiertas]]. La de mayor retorno es P-001, el
polígono del límite comunal.

## [2026-09-20] lint | Primera pasada, wiki completo

Se escribe `lint.py` y se ejecuta sobre las 32 páginas.

- Enlaces rotos: **0**
- Páginas huérfanas: **0**
- Sin frontmatter: **0**
- `confianza: baja`: **7** — las cuatro figuras legales ([[parque-nacional]], [[amcp-mu]],
  [[conservacion-privada]], [[humedal-urbano]]), [[contao]], [[huinay]] y el charter
  [[proyecto-mvp-usach-ia-2026]].

Las cuatro figuras legales se resuelven con una sola ingesta (los textos de la BCN ya
enlazados en el dato OSM, P-003). El charter se resuelve conversando, no con fuentes (P-007).
