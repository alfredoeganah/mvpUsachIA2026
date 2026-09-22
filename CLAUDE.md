# Esquema del wiki — mvpUsachIA2026

Este repositorio es un **wiki mantenido por LLM** sobre el territorio de la comuna de
Hualaihué (Región de Los Lagos, Chile) y sobre el proyecto MVP USACH IA 2026 que lo usa
como caso de estudio. Sigue el patrón descrito en [[Prompts]].


Todo el wiki se escribe en **español**. Los nombres de archivo van en kebab-case sin tildes
(`parque-nacional-hornopiren.md`), pero el título H1 y los enlaces `[[...]]` usan el nombre
real con tildes mediante alias: `[[parque-nacional-hornopiren|Parque Nacional Hornopirén]]`.
Dentro de tablas el pipe debe escaparse (`[[pagina\|Alias]]`), como exige Obsidian.

## Las tres capas

1. **`raw/`** — fuentes inmutables. Nunca se modifican ni se borran. Solo se leen.
2. **`wiki/`** — todo lo generado por el LLM. El LLM es dueño exclusivo de esta capa.
3. **`CLAUDE.md`** (este archivo) — el esquema. Se co-evoluciona con el usuario.

## Estructura de `wiki/`

```
wiki/
  index.md                  catálogo de todas las páginas, por categoría
  log.md                    bitácora cronológica append-only
  overview.md               síntesis viva: qué sabemos hoy y qué está en disputa
  fuentes/                  una página por fuente ingerida desde raw/
  dominio/
    entidades/              cosas reales: áreas protegidas, localidades, instituciones
    conceptos/              figuras legales, categorías, ecosistemas, metodologías
  sintesis/                 análisis que cruzan dos o más fuentes
  proyecto/                 capa de proyecto: charter, decisiones, datos, preguntas
```

Las dos capas se cruzan: las páginas de `proyecto/` enlazan a `dominio/`, nunca al revés
salvo en la sección "Uso en el proyecto" de una entidad. Así el wiki de dominio sigue
siendo reutilizable si el proyecto cambia de rumbo.

## Frontmatter obligatorio

Toda página de `wiki/` (excepto `index.md` y `log.md`) lleva:

```yaml
---
tipo: entidad | concepto | fuente | proyecto | sintesis
subtipo: area-protegida | localidad | institucion | figura-legal | ...
tags: [hualaihue, conservacion, ...]
fuentes: ["[[nombre-de-la-pagina-de-fuente]]"]
actualizado: AAAA-MM-DD
confianza: alta | media | baja
---
```

`confianza` es explícita y honesta:
- **alta** — afirmado directamente por una fuente en `raw/`.
- **media** — derivado o calculado por el LLM a partir de una fuente (ej. superficie
  calculada desde geometría), o conocimiento general bien establecido.
- **baja** — conocimiento general del modelo sin fuente ingerida. Requiere verificación.

## Reglas de veracidad

Son la parte más importante de este esquema.

1. **Cita o marca.** Cada afirmación no trivial lleva su origen. Si viene de `raw/`, se cita
   la página de fuente. Si viene del conocimiento general del modelo, se marca en línea con
   `⚠️ sin fuente ingerida` y la página baja a `confianza: baja`.
2. **Nunca inventar cifras.** Superficies, fechas, códigos legales y nombres propios solo se
   escriben si están en una fuente o si el LLM los calculó — y si los calculó, se dice cómo.
3. **Las contradicciones se registran, no se resuelven en silencio.** Cuando una fuente nueva
   choca con una página existente, se añade una sección `## Contradicciones` en la página y
   una entrada en [[overview]]. No se borra el dato viejo.
4. **Distinguir dato oficial de dato derivado.** Ej.: la superficie que declara el MMA vs. la
   calculada desde el polígono OSM son dos números distintos y ambos se reportan.

## Operaciones

### Ingerir (`ingesta`)

Cuando el usuario deja una fuente en `raw/` y pide procesarla:

1. Leer la fuente completa. Para datos tabulares o geoespaciales, escribir un script corto
   de extracción antes de redactar nada.
2. Conversar los hallazgos clave con el usuario **antes** de escribir el wiki.
3. Crear `wiki/fuentes/AAAA-MM-DD-slug.md` con: procedencia, licencia, alcance, método de
   extracción, inventario de lo que contiene y limitaciones conocidas.
4. Crear o actualizar las páginas de entidad y concepto que toque la fuente.
5. Actualizar `index.md` y `overview.md`.
6. Añadir la entrada al `log.md`.

### Consultar (`consulta`)

1. Leer `index.md` primero, luego las páginas relevantes; solo bajar a `raw/` si el wiki no
   alcanza.
2. Responder con citas a páginas del wiki (`[[pagina]]`) y, cuando corresponda, a la fuente.
3. **Si la respuesta tiene valor duradero, ofrecer archivarla como página nueva.** Las
   comparaciones, análisis y conexiones no deben quedar solo en el chat.

### Lintear (`lint`)

Revisión de salud del wiki. Buscar y reportar:
- contradicciones entre páginas y afirmaciones obsoletas,
- páginas huérfanas (sin enlaces entrantes) y enlaces rotos,
- conceptos mencionados repetidamente que aún no tienen página,
- páginas con `confianza: baja` que podrían resolverse con una fuente concreta,
- vacíos de datos, con sugerencia de qué fuente buscar.

El lint **propone**, no ejecuta cambios grandes sin confirmación.

## Convenciones de página

- H1 = nombre real de la entidad, con tildes.
- Primer párrafo: definición de una o dos frases, autocontenida.
- Enlazar generosamente. Un enlace a una página que todavía no existe es válido: marca
  algo que vale la pena escribir después. El lint los recoge.
- Sección final `## Fuentes` con los enlaces a las páginas de fuente.
- Las páginas de área protegida usan además una tabla `## Ficha` con: figura de protección,
  categoría IUCN/`protect_class`, administrador, creación, superficie oficial, superficie
  calculada, y referencia legal.

## Umbral de página propia

Una fuente puede traer cientos de elementos. No todos merecen página. Criterio:

| Elemento | Página propia si… | Si no |
|---|---|---|
| Localidad | población ≥ 200 hab, **o** es capital comunal, **o** tiene relevancia estructural (ej. estar dentro de un área protegida) | fila en una **página catálogo** |
| Área protegida | siempre | — |
| Institución / operador | administra o gestiona algo que sí tiene página | mención en la página que gestiona |
| Servicio (camping, hospedaje, mirador, capilla) | casi nunca | fila en la página catálogo o en la página de análisis del sector |

**Página catálogo**: una sola página con la tabla completa de un conjunto homogéneo (ej.
[[localidades-de-hualaihue]]). Así ningún dato se pierde, pero el grafo no se satura con
cientos de nodos hoja. La página catálogo enlaza a las que sí tienen página propia.

Cuando una fuente nueva hace que un elemento cruce el umbral, se le crea la página y se
reemplaza su fila del catálogo por un enlace.

## Análisis entre fuentes

El valor del wiki está en cruzar fuentes, no en resumirlas por separado. Cada ingesta debe
preguntarse explícitamente **qué permite calcular ahora que antes no se podía**, y el
resultado va a `wiki/sintesis/`, no escondido en la página de fuente.

Convenciones para los cruces geoespaciales:

- **Punto en polígono**: algoritmo ray casting sobre el anillo exterior, descontando los
  anillos interiores. Un punto que representa una localidad es su centro nominal en OSM, no
  su área poblada: decir "la localidad está dentro del área" es una aproximación y debe
  declararse como tal.
- **Distancias**: proyección plana local sobre la latitud media. Válidas hasta unas decenas
  de km a esta latitud.
- **Nunca inferir ausencia desde la ausencia de dato.** Que OSM no registre un servicio en
  una localidad no significa que no exista. Se reporta como *no mapeado*, jamás como
  *inexistente*. Ver [[calidad-de-datos-osm]].

## Datos de población

- Registrar siempre el **año y la fuente** del dato (`population:date`, `source:population`),
  nunca la cifra sola.
- Las sumas de población de localidades mapeadas **no son población comunal**: son la suma de
  lo que la fuente cubre. Se etiquetan como tal en todas partes.
- Si una localidad no trae población, se escribe *(sin dato)*, no cero.

## Convenciones del log

Formato de encabezado fijo, para que sea parseable:

```
## [AAAA-MM-DD] ingesta | Título de la fuente
## [AAAA-MM-DD] consulta | Pregunta resumida
## [AAAA-MM-DD] lint | Alcance
```

Verificar lo último hecho: `grep "^## \[" wiki/log.md | tail -5`

## Notas sobre datos geoespaciales

`raw/` contiene exports de OpenStreetMap vía Overpass (GeoJSON). Al trabajarlos:

- Las geometrías **no están recortadas** a la comuna: una relación que intersecta Hualaihué
  viene completa (la Reserva de la Biósfera llega hasta la Región de La Araucanía).
- Las superficies se calculan con **excedente esférico** (fórmula de Chamberlain & Duquette,
  R = 6.371.008,8 m), restando los anillos interiores. Contrastada contra cifras oficiales da
  diferencias del orden del 0,1–1%. Es una cifra derivada: siempre reportarla como calculada
  y junto a la oficial, nunca en su reemplazo.
- OSM es colaborativo: la geometría puede estar incompleta respecto del acto administrativo
  que crea el área. Discrepancias grandes contra la superficie oficial se anotan como
  contradicción, no se promedian.

## Herramientas

`lint.py` — chequeo de salud del wiki. Ejecutar antes de cerrar una sesión de ingesta:

```
python3 lint.py
```

Reporta enlaces rotos, páginas huérfanas, páginas en `confianza: baja` y páginas sin
frontmatter. Sale con código 1 si hay enlaces rotos o frontmatter faltante. Ignora `raw/`,
los bloques de código y el código en línea, y tolera el escape `\|` de los enlaces dentro de
tablas.
