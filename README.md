# UX-AlejandroNunez

Proyecto de Blender de Alejandro Nuñez Pardo


# Addon de Herramientas para Artistas 3D - Blender
[cite_start]**Proyecto de UI: UX, Interfaces de Usuario y Herramientas** [cite: 1, 2]
[cite_start]**Grado en Ingeniería en Tecnologías para Animación y Videojuegos** [cite: 3]

## [cite_start]Objetivos SMART (Operadores) [cite: 12]
1. [cite_start]**Mover Origen al Mundo:** Implementar un operador que mueva el origen del objeto al (0,0,0)[cite: 16].
2. [cite_start]**Limpieza de Materiales:** Operador para eliminar slots vacíos en un clic[cite: 17].
3. [cite_start]**Reset de Transformaciones:** Limpiar posición, rotación y escala a la vez[cite: 17].
4. [cite_start]**Modo Esculpido Rápido:** Configurar visor y modo de edición automáticamente[cite: 17].
5. [cite_start]**Material Emisivo Aleatorio:** Generar materiales con nodos (funcionalidad no vista en clase)[cite: 25, 26].

## [cite_start]Guía de Instalación 
1. Descargar el archivo `addon_proyecto_ui.py`.
2. En Blender: `Edit > Preferences > Add-ons > Install`.
3. Seleccionar el archivo y activar la casilla de verificación.

## [cite_start]Decisiones de Diseño (Ciclo UI) [cite: 11, 20]
- [cite_start]**Proximidad:** Los botones de "Origen" y "Reset" están juntos porque ambos gestionan transformaciones[cite: 19, 21, 22].
- [cite_start]**Simetría:** Se utiliza un diseño de columna alineada para reducir el esfuerzo visual.
- [cite_start]**Accesibilidad:** Se incluye un **Pie Menu** (Shift + X) para los operadores más usados.
