# Second Brain con LLM

Un **"second brain"** (o segundo cerebro) ==es un sistema digital externo que te permite guardar, organizar y recuperar la información que aprendes para no depender solo de tu memoria==.

==**Regla base: el humano agrega fuentes y hace preguntas; el LLM escribe y mantiene todo el wiki.**==

![[Captura de Pantalla 2026-09-22 a la(s) 14.24.14.png]]

Primeramente, para preparar el cerebro digital, se le indican al Claude los prompts que determinan el comportamiento, el cómo se van haciendo la ingesta incremental de las fuentes, y actualizando el wiki.


Para el MVP Se cargaron 3 geojson obtenidos de OSM a través de overpass-turbo: 

Query 1: Áreas Naturales, Bosques y Parques (Polígonos Grandes) de Chile

Query 2: Ciudades, Pueblos, Turismo y Puntos de Interés (POIs) de la comuna de Hualaihué

Query 3: Conectividad (Carretera Austral, Rutas Marítimas y Senderos)

  
![[Captura de Pantalla 2026-09-22 a la(s) 14.17.41.png]]
Luego las consultas al LLM vía promt relacionado a los datos fuentes entregados,.

  

Para el MVP se realizan al menos 2 preguntas:

¿Qué rutas hay para ir al río blanco?

¿Qué rutas hay para ir al mirador del río blanco desde Contao?


Ejemplo de respuesta:
![[Captura de Pantalla 2026-09-22 a la(s) 14.18.46.png]]




![[Captura de Pantalla 2026-09-22 a la(s) 14.19.03.png]]


![[Captura de Pantalla 2026-09-22 a la(s) 14.19.26.png]]


![[Captura de Pantalla 2026-09-22 a la(s) 14.19.47.png]]



Para más detalles de como se configura el modelo, ver https://github.com/alfredoeganah/mvpUsachIA2026/blob/main/CLAUDE.md