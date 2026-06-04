import pandas as pd
import numpy as np

def clasificacion_genes(data_csv, umbral_padj=0.05, umbral_lfc=1.0):
    """Clasifica cada gen en una de tres categorías: `upregulated`, `downregulated` o `no_change`.

    Esta función toma un DataFrame con los datos de expresión génica y clasifica cada gen
    según los umbrales configurables para el valor ajustado (`padj`) y el cambio logarítmico
    en la expresión (`log2FoldChange`).

    Args:
        data_csv (pd.DataFrame): DataFrame que contiene las columnas `gene_id`, `log2_fold_change` y `p_value`.
        umbral_padj (float, opcional): Umbral para el valor ajustado (`padj`). Por defecto es 0.05.
        umbral_lfc (float, opcional): Umbral para el cambio logarítmico en la expresión (`log2FoldChange`). Por defecto es 1.0.

    Returns:
        pd.DataFrame: Un nuevo DataFrame con una columna adicional `category` que indica la categoría de cada gen.
    """
    try:
        # Clasificar los genes según los umbrales
        condiciones = [
            (data_csv['p_value'] < umbral_padj) & (data_csv['log2_fold_change'] >= umbral_lfc),
            (data_csv['p_value'] < umbral_padj) & (data_csv['log2_fold_change'] <= -umbral_lfc)
        ]
        
        opciones = ['upregulated', 'downregulated']
        
        data_csv['category'] = np.select(condiciones, opciones, default='no_change')

        return data_csv

    except Exception as e:
        if isinstance(e, FileNotFoundError):
            print(f"Error: Archivo no encontrado - {e}")
        if isinstance(e, pd.errors.EmptyDataError):
            print(f"Error: Archivo vacío - {e}")
        if isinstance(e, pd.errors.ParserError):
            print(f"Error: Error de análisis - {e}")
        if isinstance(e, ValueError):
            print(f"Error de valor: {e}")
        if isinstance(e, KeyError):
            print(f"Error de clave: {e}")
        if isinstance(e, Exception):
            print(f"Error al clasificar los genes: {e}")
        return None