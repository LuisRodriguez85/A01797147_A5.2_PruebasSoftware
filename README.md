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

