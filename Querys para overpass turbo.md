https://overpass-turbo.eu/

QUERY 1: Datos generales de la comunda de hualaihué

[out:json][timeout:900][maxsize:2000000000];

// 1. Definir el área de búsqueda (Reemplaza por tu región si no usas el mapa visual)
// area["ISO3166-1"="CL"]->.searchArea; // Ejemplo para Chile entero

(
  // Ciudades, pueblos y subdivisiones (Polígonos si existen, o nodos)
  node["place"~"city|town|village|suburb"]({{bbox}});
  way["place"~"city|town|village|suburb"]({{bbox}});
  rel["place"~"city|town|village|suburb"]({{bbox}});
  
  // Límites administrativos (Provincias, comunas, regiones)
  boundary["administrative"]({{bbox}});

  // Rutas de transporte y turismo (Líneas y Relaciones)
  way["highway"~"motorway|trunk|primary|secondary|tertiary"]({{bbox}});
  relation["route"~"road|hiking|bicycle|tourism|bus"]({{bbox}});
);

// Salida optimizada con geometría incluida
out geom;



