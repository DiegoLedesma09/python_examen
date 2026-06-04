import pandas as pd

def load_data(file_path_csv, file_path_gff):
    """Carga los datos de entrada desde un archivo TSV de genes y un archivo GFF.

    Esta función lee el archivo CSV/TSV con los identificadores de genes y el archivo GFF
    con las anotaciones genómicas. Devuelve dos DataFrames de pandas: uno con la columna
    `gene_id` extraída del TSV y otro con la columna `attributes` extraída del GFF.

    Args:
        file_path_csv (str): Ruta al archivo TSV/CSV que contiene los identificadores de genes.
        file_path_gff (str): Ruta al archivo GFF con las anotaciones genómicas.

    Returns:
        tuple[pd.DataFrame, pd.DataFrame]: Una tupla con los DataFrames `data_csv` y `data_gff`.
    """
    try:
        
        data_csv = pd.read_csv(file_path_csv, sep='\t', header=0, names=['gene_id', 'log2_fold_change', 'p_value'], usecols=[0, 2, 6])
        data_gff = pd.read_csv(file_path_gff, sep='\t', comment='#', header=None, names=['attributes'], usecols=[8])
        return data_csv, data_gff
    
    except Exception as e:
        if isinstance(e, FileNotFoundError):
            print(f"Error: Archivo no encontrado - {e}")
        if isinstance(e, pd.errors.EmptyDataError):
            print(f"Error: Archivo vacío - {e}")
        if isinstance(e, pd.errors.ParserError):
            print(f"Error: Error de análisis - {e}")
        if isinstance(e, Exception):
            print(f"Error inesperado: {e}")
        return None, None