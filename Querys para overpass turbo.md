https://overpass-turbo.eu/

Usa el código con precaución.

## Query 1: Áreas Naturales, Bosques y Parques (Polígonos Grandes)

Hualaihué destaca por su geografía indómita (parques nacionales, fiordos y reservas). Esta consulta extrae exclusivamente **polígonos** de áreas protegidas, bosques y zonas naturales, esenciales para cartografía base.

`[out:json][timeout:900][maxsize:2000000000];`

`// 1. Definir el área de búsqueda (Reemplaza por tu región si no usas el mapa visual)`
`// area["ISO3166-1"="CL"]->.searchArea; // Ejemplo para Chile entero`

`(`
  `// Ciudades, pueblos y subdivisiones (Polígonos si existen, o nodos)`
  `node["place"~"city|town|village|suburb"]({{bbox}});`
  `way["place"~"city|town|village|suburb"]({{bbox}});`
  `rel["place"~"city|town|village|suburb"]({{bbox}});`
  
  `// Límites administrativos (Provincias, comunas, regiones)`
  `boundary["administrative"]({{bbox}});`

  `// Rutas de transporte y turismo (Líneas y Relaciones)`
  `way["highway"~"motorway|trunk|primary|secondary|tertiary"]({{bbox}});`
  `relation["route"~"road|hiking|bicycle|tourism|bus"]({{bbox}});`
`);`

`// Salida optimizada con geometría incluida`
`out geom;`


## Query 2: Ciudades, Pueblos, Turismo y Puntos de Interés (POIs)

Esta consulta descarga Hornopirén, Contao, Rolecha y demás localidades [1]. Está optimizada para **traer polígonos cuando existen** (como el perímetro de un museo o plaza) [1], pero incluye nodos (puntos) porque elementos como miradores o letreros de información turística casi siempre se mapean como un único punto en zonas rurales [1].

overpass

```
[out:json][timeout:900];

area["admin_level"="8"]["name"="Hualaihué"]->.comuna;

(
  // Localidades urbanas y rurales (Límites de pueblos o sus centros)
  node(area.comuna)["place"~"town|village|hamlet|isolated_dwelling"];
  way(area.comuna)["place"~"town|village|hamlet|isolated_dwelling"];

  // Turismo: Miradores, Museos, Camping, Atractivos, Termas
  node(area.comuna)["tourism"~"viewpoint|museum|attraction|camp_site|picnic_site|information|hotel|guest_house"];
  way(area.comuna)["tourism"~"viewpoint|museum|attraction|camp_site|picnic_site|information|hotel|guest_house"];
  relation(area.comuna)["tourism"~"viewpoint|museum|attraction|camp_site|picnic_site|information|hotel|guest_house"];

  // Servicios, Cultura y Edificios Públicos (Municipios, Iglesias, Mercados)
  node(area.comuna)["amenity"~"townhall|place_of_worship|marketplace|arts_centre|hospital|clinic"];
  way(area.comuna)["amenity"~"townhall|place_of_worship|marketplace|arts_centre|hospital|clinic"];
);

out geom;
```

Usa el código con precaución.

---

## Query 3: Conectividad (Carretera Austral, Rutas Marítimas y Senderos)

Para complementar los polígonos y POIs, necesitas las redes que los conectan (esencial en la Provincia de Palena). Este query extrae las vías vehiculares (como la **Ruta 7**), senderos de trekking y rutas de transbordadores/ferries.

overpass

```
[out:json][timeout:900];

area["admin_level"="8"]["name"="Hualaihué"]->.comuna;

(
  // Carreteras principales, secundarias y caminos rurales
  way(area.comuna)["highway"~"trunk|primary|secondary|tertiary|residential|unclassified|track"];
  
  // Senderos de excursión y caminata (muy comunes en la zona)
  way(area.comuna)["highway"~"path|footway|hiking"];

  // Rutas marítimas y de transbordadores (ej. Conectividad Hornopirén-Leptepu)
  way(area.comuna)["route"="ferry"];
  relation(area.comuna)["route"~"ferry|road|tourism"];
);

out geom;
```


