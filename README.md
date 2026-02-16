# Actividad 5.2 – Ejercicio de Programación 2 y Análisis Estático

**Materia:** Pruebas de Software y Aseguramiento de la Calidad  
**Actividad:** 5.2  
**Alumno:** José Luis Rodríguez Leyva  
**Matrícula:** A01797147  
**Lenguaje:** Python  

---

## Descripción del programa

El programa `computeSales.py` calcula el total de ventas a partir de dos archivos en formato JSON:

- Un catálogo de precios de productos (`priceCatalogue.json`)
- Un registro de ventas con productos y cantidades (`salesRecord.json`)

El sistema:

- Recibe ambos archivos como parámetros desde la línea de comandos.
- Calcula el total general de ventas considerando los precios del catálogo.
- Muestra los resultados en consola.
- Genera un archivo de salida llamado `SalesResults.txt`.
- Mide e incluye el tiempo de ejecución.
- Maneja datos inválidos mostrando el error en consola sin detener la ejecución.

Los resultados se almacenan automáticamente en la carpeta `results`, la cual es creada por el programa en caso de no existir, asegurando organización y reproducibilidad.

---

## Forma de ejecución

El programa se ejecuta desde línea de comandos con el siguiente formato:

```bash
python computeSales.py priceCatalogue.json salesRecord.json
```

Ejemplo:

```bash
python computeSales.py testfiles/priceCatalogue.json testfiles/salesRecord.json
```

---

## Pruebas dinámicas

Se realizaron pruebas ejecutando el programa con distintos archivos JSON de prueba.

El programa:

- Procesa correctamente los datos válidos.
- Ignora registros inválidos mostrando el error en consola.
- Continúa la ejecución conforme al requerimiento.
- Calcula correctamente el total de ventas.
- Mide el tiempo de ejecución.

Los resultados se almacenan en:

```bash
results/SalesResults.txt
```

Estas pruebas corresponden a pruebas dinámicas, ya que implican la ejecución del programa para validar su comportamiento.

---

## Análisis Estático – Flake8

Se instaló y verificó la herramienta Flake8 mediante:

```bash
python -m flake8 --version
```

Durante el análisis inicial se detectaron observaciones relacionadas con:

- Longitud de línea
- Formato del archivo
- Convenciones de estilo

Todas las observaciones fueron corregidas.

El análisis final no arrojó errores ni advertencias, confirmando el cumplimiento del estándar PEP-8.

Los resultados se almacenaron en la carpeta `results`.


---

## Análisis Estático – Pylint

Se ejecutó la herramienta Pylint sobre el archivo `computeSales.py`, conforme al nombre especificado en el documento oficial de la actividad.

Después de corregir las observaciones iniciales, el resultado final fue:

```bash
Your code has been rated at 10.00/10
```

Esto confirma:

- Cumplimiento de estándares de codificación.
- Buena estructura del código.
- Correcta organización y mantenibilidad.

Los resultados del análisis fueron almacenados en la carpeta `results`.

---

## Relación con Pruebas Estáticas y Dinámicas

En esta actividad se aplicaron ambos enfoques de calidad:

`Pruebas Dinámicas`

Consisten en ejecutar el programa con datos reales para verificar su comportamiento y resultados.

`Pruebas Estáticas`

Se realizaron mediante herramientas como Flake8 y Pylint, las cuales analizan el código fuente sin ejecutarlo, permitiendo detectar:

- Violaciones de estilo
- Problemas de diseño
- Posibles defectos
- Complejidad innecesaria

El uso combinado de pruebas dinámicas y estáticas permite mejorar la calidad del software desde etapas tempranas del desarrollo.

---

## Conclusión

El programa computeSales.py cumple con todos los requisitos establecidos en la actividad:

- Correcta ejecución desde línea de comandos.
- Manejo adecuado de errores sin interrumpir la ejecución.
- Generación de archivo de resultados.
- Inclusión del tiempo de ejecución.
- Cumplimiento del estándar PEP-8.
- Cero errores reportados por Flake8.
- Calificación perfecta (10/10) en Pylint.

La actividad permitió experimentar directamente con herramientas de análisis estático y reforzar la importancia de las buenas prácticas de calidad en el desarrollo de software.