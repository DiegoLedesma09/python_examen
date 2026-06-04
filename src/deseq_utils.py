"""Utilities para ejecutar el flujo de análisis diferencial (DESeq-like).

Este módulo agrupa la lógica principal del script de alto nivel: parseo de
argumentos de línea de comandos, carga de datos (CSV/TSV y GFF), depuración de
atributos GFF, clasificación de genes según umbrales y escritura de los
resultados de salida con descripciones cuando están disponibles.

Funciones principales:
- ``main()``: punto de entrada que orquesta la ejecución completa del análisis.

Dependencias esperadas (módulos del paquete):
- ``cli.parse_arguments``: parseo de argumentos de entrada.
- ``load_data.load_data``: carga de archivos CSV/TSV y GFF (retorna ``data_csv, data_gff``).
- ``depuramiento_gff.parse_attributes``: parsea columna ``attributes`` del GFF y construye diccionarios.
- ``clasificacion.clasificacion_genes``: clasifica genes en categorías según umbrales.
- ``description_for_gene.agregar_descripcion``: añade la columna ``description`` al DataFrame.
- ``output.imprimir_resultados*``: funciones para imprimir y escribir resultados.
"""

import pandas as pd
from pathlib import Path
from cli import parse_arguments
from load_data import load_data
from depuramiento_gff import parse_attributes
from description_for_gene import agregar_descripcion
from clasificacion import clasificacion_genes
from output import imprimir_resultados_con_descripcion, imprimir_resultados


def main():
    """Ejecuta el flujo completo de análisis diferencial.

    Lee los argumentos de la línea de comandos, carga los datos de entrada,
    extrae anotaciones del GFF, clasifica los genes según los umbrales
    proporcionados y guarda/imprime los resultados.
    """
    args = parse_arguments()
    input_csv = args.input_csv
    input_gff = args.input_gff
    output_dir = args.output_dir
    umbral_padj = args.umbral_padj
    umbral_lfc = args.umbral_lfc

    data_csv, data_gff = load_data(input_csv, input_gff)
    if data_csv is None or data_gff is None:
        print("Error al cargar los datos.")
        exit(1)

    dict_name = parse_attributes(data_gff)
    data_clasificada = clasificacion_genes(data_csv, umbral_padj, umbral_lfc)
    if data_clasificada is None:
        print("Error al clasificar los genes.")
        exit(1)

    data_con_descripcion = agregar_descripcion(data_clasificada, dict_name)
    if data_con_descripcion is None:
        print("Error al agregar descripciones.")
        exit(1)

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    file_path_upregulated = output_path / "upregulated_genes.tsv"
    file_path_downregulated = output_path / "downregulated_genes.tsv"
    file_output_summary = output_path / "summary_report.txt"

    imprimir_resultados_con_descripcion(
        data_con_descripcion,
        dict_name,
        str(file_path_upregulated),
        str(file_path_downregulated),
        str(file_output_summary),
    )
    imprimir_resultados(
        data_con_descripcion,
        dict_name,
        input_csv,
        input_gff,
        umbral_padj,
        umbral_lfc,
        str(file_output_summary),
    )
    