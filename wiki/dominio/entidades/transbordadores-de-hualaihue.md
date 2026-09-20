---
tipo: entidad
subtipo: catalogo
tags: [hualaihue, transbordadores, ferry, transporte, catalogo]
fuentes: ["[[2026-09-20-osm-hualaihue3]]"]
actualizado: 2026-09-20
confianza: alta
---

# Transbordadores de Hualaihué

Catálogo de las rutas marítimas de [[2026-09-20-osm-hualaihue3]]: 34 ways y 20 relaciones
con `route=ferry`. Cada ruta aparece **dos veces, una por sentido**; aquí se lista una sola
vez. Análisis en [[conectividad-de-hualaihue]].

## Rutas de vehículos (`ferry=trunk`)

Las que cargan autos. Son las que mantienen viva la [[carretera-austral|Carretera Austral]].

| Ruta | km | Duración | Operador | Reserva | Peaje |
|---|---|---|---|---|---|
| Caleta La Arena – Caleta Puelche | 6,0 | 0:45 | Transportes del Estuario | no | tarifa |
| [[hornopiren\|Hornopirén]] – Leptepú | 58,7 | 3:30 | Somarco | sí | sí |
| [[pichicolo\|Pichicolo]] – Caleta Gonzalo | 77,8 | 5:00 | Naviera Puelche | sí | sí |
| Chumeldén – Pichicolo | 65,6 | — | Naviera Puelche | sí | sí |
| Ayacara – Pichicolo | 49,8 | — | Naviera Puelche | sí | sí |
| Puerto Montt – Chaitén | 170,4 | 8:30 | Naviera Austral | sí | sí |
| Puerto Montt – Ayacara | 105,0 | 5:30 | Naviera Austral | sí | sí |

El de Caleta La Arena es **el único con frecuencia declarada**: `interval=00:30`, con
intervalos condicionales de hasta 2 h entre medianoche y las 6 de la mañana. Horarios:
https://testuario.cl/rutas-y-horarios/ · El de Hornopirén: https://www.barcazas.cl/barcazas/hornopiren-caleta-gonzalo

## Rutas de pasajeros (`ferry=footway`)

`motor_vehicle=no`, `bicycle=no`, `horse=no`. Varias con `reservation=required`. Son la red
que sirve al Hualaihué insular — y vienen con **código de camino del Estado**.

### `CAM0015` — 96,2 km en 11 tramos

La red marítima principal del Estado en la comuna. Encadena las caletas del fiordo Comau
saltando de una a otra, y de ahí se ramifica:

```
Hornopirén → Manila → Quiaca → Telele → Huinay → Porcelana Chica
     15,6 km    8,4     12,3     15,5        4,7        = 56,5 km
```

| Tramo | km | Tarifa |
|---|---|---|
| [[hornopiren\|Hornopirén]] – Manila | 15,6 | sí |
| Telele – [[huinay\|Huinay]] | 15,5 | sí |
| Quiaca – Telele | 12,3 | sí |
| [[hornopiren\|Hornopirén]] – Caleta Llancahué | 11,9 | sin dato |
| Manila – Quiaca | 8,4 | sí |
| Baltazar – Puerto Bonito | 7,5 | sin dato |
| Caleta Andrade – Baltazar | 6,9 | sin dato |
| Leptepú – Vodudahue | 5,0 | sí |
| [[huinay\|Huinay]] – Porcelana Chica | 4,7 | sí |
| Dos tramos sin nombre | 5,7 y 2,7 | sin dato |

Manila, Quiaca, Caleta Andrade, Baltazar y Puerto Bonito son localidades del catálogo
([[localidades-de-hualaihue]]), varias sin dato de población y sin ningún servicio mapeado.
La ruta las conecta igual.

### `CAM0078` — 14,0 km en 8 tramos

El circuito insular frente a [[pichicolo|Pichicolo]]: Isla Malomacún – Isla Llinguar – Isla
Llanchid – Costa Pichicolo Sur – Pichicolo. Todos con tarifa, ninguno con nombre propio, de
1,0 a 4,0 km cada uno.

### `CAM0005` — 25,3 km

Un solo tramo: **Poyo – [[pichicolo|Pichicolo]]**.

### Tramos sin código

Cuatro tramos de 12,3 a 55,3 km sin `ref`, dos de ellos con `source` en el documento
**"Cómo llegar a Huinay"** de la [[fundacion-huinay|Fundación Huinay]]. El acceso a
[[huinay|Huinay]] está documentado, además de por el Estado vía `CAM0015`, por la fundación
dueña del suelo. Relevante para P-009.

## Rutas de largo alcance que solo pasan

No sirven a Hualaihué, pero atraviesan el área del export y por eso aparecen:
**Puerto Montt – Puerto Edén – Puerto Natales** (Navimag, 1.488 km, 74 h) y **Ruta Chaitén**
vía Ayacara (Naviera Austral, 178,5 km, 9 h). Excluirlas de cualquier cálculo comunal.

## Operadores

| Operador | Rutas |
|---|---|
| Naviera Puelche | Pichicolo ↔ Ayacara, Chumeldén, Caleta Gonzalo |
| Somarco | Hornopirén – Leptepú |
| Transportes del Estuario | Caleta La Arena – Caleta Puelche |
| Naviera Austral | Puerto Montt – Chaitén / Ayacara |
| Navimag | Puerto Montt – Puerto Natales (solo pasa) |
| *(sin operador en el dato)* | todas las rutas `CAM…` de pasajeros |

Que las rutas con código estatal no declaren operador es un vacío del dato, no
necesariamente del servicio. ⚠️

## Fuentes

- [[2026-09-20-osm-hualaihue3]]
