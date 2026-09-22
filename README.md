# Second Brain con LLM

Un **"second brain"** (o segundo cerebro) **es un sistema digital externo que te permite guardar, organizar y recuperar la información que aprendes para no depender solo de tu memoria**.

**Regla base: el humano agrega fuentes y hace preguntas; el LLM escribe y mantiene todo el wiki.**


<img width="859" height="740" alt="Captura de Pantalla 2026-09-22 a la(s) 14 24 14" src="https://github.com/user-attachments/assets/551916fc-3cb6-44de-b271-f0fd3ad44981" />


Primeramente, para preparar el cerebro digital, se le indican al Claude los prompts que determinan el comportamiento, el cómo se van haciendo la ingesta incremental de las fuentes, y actualizando el wiki.


Para el MVP Se cargaron 3 geojson obtenidos de OSM a través de overpass-turbo: 


Query 1: Áreas Naturales, Bosques y Parques (Polígonos Grandes) de Chile

Query 2: Ciudades, Pueblos, Turismo y Puntos de Interés (POIs) de la comuna de Hualaihué

Query 3: Conectividad (Carretera Austral, Rutas Marítimas y Senderos)

  
<img width="1021" height="666" alt="Captura de Pantalla 2026-09-22 a la(s) 14 17 41" src="https://github.com/user-attachments/assets/260cc800-be7c-40ad-92d3-8b52bfd23934" />


Luego las consultas al LLM vía promt relacionado a los datos fuentes entregados,.

  

Para el MVP se realizan al menos 2 preguntas:

¿Qué rutas hay para ir al río blanco?

¿Qué rutas hay para ir al mirador del río blanco desde Contao?


Ejemplo de respuesta:
<img width="883" height="476" alt="Captura de Pantalla 2026-09-22 a la(s) 14 18 46" src="https://github.com/user-attachments/assets/425690ee-a2b4-476f-9184-a0ae38413146" />
<img width="876" height="618" alt="Captura de Pantalla 2026-09-22 a la(s) 14 19 03" src="https://github.com/user-attachments/assets/6b125480-c21e-486e-aa3d-8a8857803225" />
<img width="876" height="618" alt="Captura de Pantalla 2026-09-22 a la(s) 14 19 26" src="https://github.com/user-attachments/assets/6a14af80-c06f-408b-be96-92f95a2e8485" />
<img width="876" height="618" alt="Captura de Pantalla 2026-09-22 a la(s) 14 19 47" src="https://github.com/user-attachments/assets/b6c87979-164e-4682-8608-b05feec7a9ca" />



Para más detalles de como se configura el modelo, ver https://github.com/alfredoeganah/mvpUsachIA2026/blob/main/CLAUDE.md
