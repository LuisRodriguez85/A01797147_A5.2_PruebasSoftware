# Actividad 5.2 – Ejercicio de Programación 2 y Análisis Estático

**Materia:** Pruebas de Software y Aseguramiento de la Calidad  
**Actividad:** 5.2  
**Alumno:** José Luis Rodríguez Leyva  
**Matrícula:** A01797147  
**Lenguaje:** Python  

---

## Descripción del programa

El programa implementado permite calcular el total de ventas a partir de dos archivos en formato JSON:
- Un catálogo de precios de productos.
- Un registro de ventas con productos y cantidades.

El sistema valida la información de entrada, maneja errores sin interrumpir la ejecución y genera los resultados tanto en consola como en un archivo de salida, cumpliendo con buenas prácticas de calidad y estilo de codificación.

Los resultados de ejecución se almacenan automáticamente en la carpeta `results`, la cual es creada por el programa en caso de no existir, asegurando organización y reproducibilidad de los resultados.

---

## Pruebas dinámicas

El programa fue ejecutado exitosamente utilizando archivos de prueba proporcionados, generando el cálculo correcto del total de ventas y midiendo el tiempo de ejecución.  
Los resultados se almacenan en el archivo `SalesResults.txt`.

---

## Análisis Estático – Flake8

Se verificó la instalación correcta de la herramienta de análisis estático **Flake8** mediante el comando:

```bash
python -m flake8 --version

Obteniendo la versión 7.3.0, junto con los módulos pycodestyle, pyflakes y mccabe, lo cual confirma que la herramienta está lista para analizar código fuente Python conforme al estándar PEP-8 y detectar problemas de calidad estática.

Durante el análisis se detectaron advertencias relacionadas con la longitud de línea y el formato del archivo, las cuales fueron corregidas. Posteriormente, el análisis se ejecutó nuevamente sin detectar errores ni advertencias.

Los resultados del análisis se almacenaron en la carpeta results.

Análisis Estático – Pylint

Se ejecutó la herramienta Pylint sobre el archivo compute_sales.py.
Inicialmente se detectó una advertencia de convención relacionada con el nombre del módulo.

Después de corregir el nombre del archivo conforme al estándar snake_case, el análisis se ejecutó nuevamente sin observaciones, obteniendo una calificación final de:

10.00 / 10

El resultado del análisis se almacenó en el archivo correspondiente dentro de la carpeta results.

Conclusión

El programa fue validado mediante pruebas dinámicas y análisis estático.
Las herramientas Flake8 y Pylint no detectaron errores ni advertencias tras la corrección de los hallazgos iniciales, confirmando el cumplimiento del estándar PEP-8 y la correcta aplicación de buenas prácticas de calidad de software.

