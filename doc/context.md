# Contexto del proyecto

Este proyecto analiza resultados de expresión génica diferencial y enriquece los genes con anotaciones extra�das de un archivo GFF.

- Entrada principal:
  - Un archivo TSV/CSV con los resultados de DESeq2 (o datos similares) que incluye identificadores de genes, log2FoldChange y p-value ajustado.
  - Un archivo GFF con anotaciones genómicas, cuya columna `attributes` contiene los campos `Name=` y `description=`.

- Objetivo:
  - Clasificar genes en tres categorías: `upregulated`, `downregulated` y `no_change`.
  - Añadir descripciones de genes desde el GFF cuando están disponibles.
  - Generar resultados de salida en archivos TSV, un informe de resumen y un volcano plot.

- Grupo de usuarios:
  - Bioinformáticos y biólogos que desean filtrar y explorar genes diferencialmente expresados a partir de resultados de análisis de expresión génica.

- Motivación:
  - Facilitar la interpretación biológica de los resultados al a�adir anotaciones de gen desde el archivo GFF.
  - Proveer una salida clara de genes regulados al alza y a la baja, junto con un informe resumen.
