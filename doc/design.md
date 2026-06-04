# Diseño de la solución

## Arquitectura general

El proyecto está organizado en módulos Python dentro de `src/` que dividen el flujo de análisis en responsabilidades claras:

- `src/cli.py`: parseo de argumentos de línea de comandos.
- `src/load_data.py`: carga el archivo TSV/CSV con datos de expresión y el archivo GFF.
- `src/depuramiento_gff.py`: parsea la columna `attributes` del GFF para extraer `gene_id` y `description`.
- `src/clasificacion.py`: clasifica los genes según umbrales de `p_value` y `log2_fold_change`.
- `src/description_for_gene.py`: agrega la descripción del GFF al DataFrame de genes clasificados.
- `src/output.py`: imprime el resumen y crea los archivos de salida.
- `src/volcano.py`: genera un volcano plot de los resultados de expresión diferencial.
- `src/deseq_utils.py`: orquesta el flujo completo de ejecución.

## Flujo de datos

1. El usuario invoca el script con:
   - `input_csv` (archivo de expresión génica)
   - `input_gff` (archivo GFF)
   - `output_dir` (directorio de salida)
   - `umbral_padj` y `umbral_lfc`

2. `load_data.load_data()` lee el archivo CSV/TSV y el archivo GFF.
3. `depuramiento_gff.parse_attributes()` construye un diccionario de descripciones por `gene_id`.
4. `clasificacion.clasificar_genes()` etiqueta cada gen como `upregulated`, `downregulated` o `no_change`.
5. `description_for_gene.agregar_descripcion()` anexa las anotaciones de descripción al DataFrame.
6. `output.imprimir_resultados_con_descripcion()` escribe los archivos de salida y `output.imprimir_resultados()` imprime un resumen por consola.

## Entradas

- Archivo TSV/CSV con los campos esperados:
  - `gene_id`
  - `log2_fold_change`
  - `p_value`
- Archivo GFF con la columna de atributos que contiene `Name=` y `description=`.

## Salidas

- `upregulated_genes.tsv`
- `downregulated_genes.tsv`
- `summary_report.txt`
- `volcano_plot.png`
- Resumen impreso en consola

## Suposiciones y notas

- El archivo CSV/TSV se lee con separador de tabulador y columnas especificas.
- El archivo GFF se parsea desde la columna `attributes`, esperando el formato estándar de atributos separados por `;`.
- Si un gen no tiene descripcion en el GFF, se marca como `sin anotación`.
- El umbral `umbral_padj` controla el valor ajustado y `umbral_lfc` controla la magnitud m�nima del cambio logar�tmico.

## Consideraciones de diseño

- El flujo modular facilita la extensión y el mantenimiento.
- Cada módulo encapsula una responsabilidad única: entrada, carga, depuración, clasificación, enriquecimiento y salida.
- El diseño actual permite cambiar fácilmente los criterios de clasificación o el formato de salida sin modificar todo el pipeline.
