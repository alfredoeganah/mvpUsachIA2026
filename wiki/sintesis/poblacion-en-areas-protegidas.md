---
tipo: sintesis
subtipo: cruce-de-fuentes
tags: [hualaihue, poblacion, conservacion, sintesis, habitabilidad]
fuentes: ["[[2026-09-20-osm-hualaihue1]]", "[[2026-09-20-osm-hualaihue2]]"]
actualizado: 2026-09-20
confianza: media
---

# Población dentro de las áreas protegidas

Primer cruce entre las dos fuentes del wiki: las 65 localidades de
[[2026-09-20-osm-hualaihue2]] contra los polígonos de protección de
[[2026-09-20-osm-hualaihue1]]. **Es el hallazgo central del wiki hasta ahora.**

## Resultado

| Área protegida | Localidades dentro | Habitantes dentro |
|---|---|---|
| [[reserva-biosfera-bosques-templados-lluviosos]] | **48** de 65 | **8.524** |
| [[fundo-huinay]] | 1 | 35 |
| [[parque-nacional-hornopiren]] | 0 | 0 |
| [[parque-nacional-pumalin]] | 0 | 0 |
| [[sistema-humedales-hornopiren]] | 0 | 0 |
| [[amcp-fiordo-comau]] | 0 | 0 |

## Lectura

**El 98% de la población mapeada de Hualaihué vive dentro de un área protegida** — y es
siempre la misma: la Reserva de la Biósfera. [[hornopiren|Hornopirén]] (3.629 hab),
[[contao|Contao]] (784) y 46 localidades más caen dentro de sus 2,16 millones de ha.

Al mismo tiempo, **las cinco figuras restantes no contienen a nadie**. Ni un habitante dentro
de los dos parques nacionales, el humedal urbano o el área marina.

Las dos afirmaciones juntas dicen algo preciso sobre cómo se protege este territorio:

> Las figuras estrictas de Hualaihué se aplicaron sobre territorio deshabitado. La única
> figura que cubre gente es la más laxa y la que menos obliga.

Esto es coherente con el diseño de una reserva de la biósfera UNESCO-MAB, que **está pensada
para incluir población** en sus zonas de transición: no es una restricción de uso sino un
marco de gobernanza. ⚠️ caracterización general del modelo, sin fuente ingerida (P-003).

Pero tiene una consecuencia concreta y verificable: **decir "el 98% de los habitantes de
Hualaihué vive en un área protegida" es cierto y a la vez engañoso.** Cualquier salida del
MVP que use ese indicador debe decir de qué figura se trata. Ver
[[solapamiento-de-areas-protegidas]].

## El caso Huinay

[[huinay|Huinay]] (35 hab) es la única localidad dentro de un área de
[[conservacion-privada|conservación privada]]: vive dentro del [[fundo-huinay|Fundo Huinay]],
31.745 ha de la [[fundacion-huinay|Fundación San Ignacio de Huinay]]. Es el único punto del
territorio donde población y conservación privada se superponen — y por tanto el único lugar
donde la pregunta "¿quién decide sobre el uso del suelo donde vives?" tiene una respuesta
privada.

No hay en las fuentes nada sobre la relación entre esos 35 habitantes y la fundación. Es una
de las preguntas más interesantes que el wiki puede plantear y no responder todavía.

## Los que quedan fuera: el Hualaihué insular

17 localidades (177 hab con dato) caen **fuera** de la Reserva de la Biósfera. Son las islas
y puntas del sur y el poniente:

| Localidad | Hab | | Localidad | Hab |
|---|---|---|---|---|
| Quiaca | 60 | | Isla Pelada | (sin dato) |
| Isla Malomacún | 38 | | Chaucahue | (sin dato) |
| Costa Llanchid | 34 | | Isla Manzano | (sin dato) |
| Caleta Llancahué | 24 | | Isla Caicura | (sin dato) |
| Caleta Andrade | 21 | | Isla Aulén | (sin dato) |
| | | | Isla Linguar, Manila, Baltazar, Puerto Bonito, 3 sin nombre | (sin dato) |

La reserva de la biósfera es **andina y continental**; deja fuera el Hualaihué marítimo e
insular. Ese Hualaihué de islas, caletas y viviendas aisladas es el que no tiene ninguna
figura de protección encima ni, según [[acceso-a-servicios]], servicio alguno mapeado cerca.

Lo que sí tiene, según la tercera ingesta, es **transporte público marítimo codificado como
camino estatal**: las rutas `CAM0078` y `CAM0015` sirven a Isla Malomacún, Isla Llinguar,
Isla Llanchid, Caleta Andrade, Baltazar, Puerto Bonito y Caleta Llancahué — exactamente esta
lista. El Estado llega a ellas por mar aunque ninguna figura de conservación las cubra.
Ver [[conectividad-de-hualaihue]].

## Advertencias metodológicas

- Cada localidad es **un punto**, su centro nominal en OSM, no su superficie poblada. Una
  localidad extensa puede estar parcialmente dentro y contarse como fuera, o al revés.
- La suma **8.701 hab** es la cobertura de OSM con dato INE 2017, no la población comunal.
- Los polígonos no están recortados a la comuna: algunas de estas localidades podrían caer
  fuera de Hualaihué. Depende de P-001.
- Población 2017, geometrías 2026. Nueve años de desfase.

## Fuentes

- [[2026-09-20-osm-hualaihue1]] — polígonos de áreas protegidas
- [[2026-09-20-osm-hualaihue2]] — localidades y población
