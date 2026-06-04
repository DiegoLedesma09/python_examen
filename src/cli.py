import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Analiza la regulación génica a partir de archivos CSV y GFF.")
    parser.add_argument('input_csv', required=True, help='Ruta al archivo CSV/TSV con los identificadores de genes y datos de expresión.')
    parser.add_argument('input_gff', required=True, help='Ruta al archivo GFF')
    parser.add_argument('output_dir', required=True, help='Ruta al directorio de salida')
    parser.add_argument('umbral_padj', type=float, default=0.05, help='Umbral para el p-valor ajustado')
    parser.add_argument('umbral_lfc', type=float, default=1.0, help='Umbral para la diferencia de expresión logarítmica')
    return parser.parse_args()
