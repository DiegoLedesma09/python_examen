def genes_significativos(data_csv):
    '''Identifica los genes más significativos según los criterios establecidos y los reporta en pantalla.
    
    Esta función toma un DataFrame con la clasificación de genes y sus estadísticas, identifica el gen más inducido, el más reprimido y el más estadísticamente confiable, y luego imprime esta información en pantalla.
    
    Args:
        data_csv (pd.DataFrame): DataFrame que contiene la clasificación de cada gen y sus estadísticas.
    Returns:
        gen_max_log2fc (str): Identificador del gen con el mayor log2FoldChange.
        gen_min_log2fc (str): Identificador del gen con el menor log2FoldChange.
        gen_min_padj (str): Identificador del gen con el menor padj.
    '''
    try:
        gen_max_log2fc = data_csv.loc[data_csv['log2_fold_change'].idxmax()]['gene_id']
        gen_min_log2fc = data_csv.loc[data_csv['log2_fold_change'].idxmin()]['gene_id']
        gen_min_padj = data_csv.loc[data_csv['p_value'].idxmin()]['gene_id']

        print(f"Gen más inducido: {gen_max_log2fc}")
        print(f"Gen más reprimido: {gen_min_log2fc}")
        print(f"Gen más estadísticamente confiable: {gen_min_padj}")

        return gen_max_log2fc, gen_min_log2fc, gen_min_padj

    except Exception as e:
        if isinstance(e, KeyError):
            print(f"Error de clave: {e}")
        if isinstance(e, ValueError):
            print(f"Error de valor: {e}")
        if isinstance(e, Exception):
            print(f"Error al identificar los genes significativos: {e}")
        return None, None, None


def imprimir_resultados(data_csv, dict_name, file_path_csv, file_path_gff, umbral_padj, umbral_lfc, file_output_summary):
    """Imprime en pantalla el conteo de genes en cada categoría, los porcentajes sobre el total, el archivo analizado y los umbrales utilizados.

    Esta función toma un DataFrame con la clasificación de genes y la ruta del archivo CSV analizado. Calcula el conteo de genes en cada categoría (`upregulated`, `downregulated`, `no_change`), los porcentajes correspondientes sobre el total de genes, y luego imprime esta información junto con la ruta del archivo y los umbrales utilizados para la clasificación.

    Args:
        data_csv (pd.DataFrame): DataFrame que contiene la columna `category` con la clasificación de cada gen.
        dict_name (dict): Diccionario que mapea IDs de genes a sus nombres.
        file_path_csv (str): Ruta al archivo CSV que fue analizado.
        file_path_gff (str): Ruta al archivo GFF utilizado.
        umbral_padj (float): Umbral para el p-value ajustado.
        umbral_lfc (float): Umbral para el log2FoldChange.
        file_output_summary (str): Ruta al archivo de resumen de salida.
    Returns:
        None: Esta función no devuelve ningún valor, solo imprime los resultados en pantalla.  
    """
    try:
        
        total_genes_csv = len(data_csv)
        total_genes_gff = len(dict_name) if dict_name is not None else 0
        max_gene, min_gene, min_padj = genes_significativos(data_csv)
        conteo_categorias = data_csv['category'].value_counts()
        
        porcentajes = (conteo_categorias / total_genes_csv) * 100 if total_genes_csv else {}

        print("====================================\n")
        print("  Analisis de DESEq2: IAV vs Mock\n")
        print(f"  Archivo analizado: {file_path_csv}")
        print(f"  Archivo GFF utilizado: {file_path_gff}")
        print(f"  Umbral p-value ajustado: {umbral_padj}")
        print(f"  Umbral log2FoldChange: {umbral_lfc}")
        print("====================================\n")
        print(f"Genes cargados del archivo CSV: {total_genes_csv}")
        print(f"Genes cargados del archivo GFF: {total_genes_gff}\n")
        print("-----Clasificacion------\n")
        print(f"  upregulated: {conteo_categorias.get('upregulated', 0)} genes (porcentaje: {porcentajes.get('upregulated', 0):.2f}%)")
        print(f"  downregulated: {conteo_categorias.get('downregulated', 0)} genes (porcentaje: {porcentajes.get('downregulated', 0):.2f}%)")
        print(f"  no_change: {conteo_categorias.get('no_change', 0)} genes (porcentaje: {porcentajes.get('no_change', 0):.2f}%)\n")
        print("-----Genes mas significativos------\n")
        print(f"  Gen mas inducido: {max_gene}")
        print(f"  Gen mas reprimido: {min_gene}")
        print(f"  Gen mas estadisticamente confiable: {min_padj}\n")
        print(f"Archivos guardados en: {file_output_summary}\n")

    except Exception as e:
        if isinstance(e, KeyError):
            print(f"Error de clave: {e}")
        if isinstance(e, ValueError):
            print(f"Error de valor: {e}")
        if isinstance(e, Exception):
            print(f"Error al imprimir los resultados: {e}")

    
def imprimir_resultados_con_descripcion(data_csv, dict_name, file_path_upregulated, file_path_downregulated, file_output_summary):
    '''Crea los archivos de salida con los genes inducidos, reprimidos y el resumen completo.'''
    if not file_output_summary:
        raise ValueError("La ruta del archivo de salida no puede estar vacía.")
    if not file_path_upregulated:
        raise ValueError("La ruta del archivo de genes inducidos no puede estar vacía.")
    if not file_path_downregulated:
        raise ValueError("La ruta del archivo de genes reprimidos no puede estar vacía.")
    if data_csv.empty:
        raise ValueError("El DataFrame de genes está vacío.")
    if dict_name is None:
        raise ValueError("El diccionario de nombres de genes no puede ser None.")
    if 'gene_id' not in data_csv.columns:
        raise KeyError("El DataFrame debe contener la columna 'gene_id'.")
    if 'log2_fold_change' not in data_csv.columns:
        raise KeyError("El DataFrame debe contener la columna 'log2_fold_change'.")
    if 'p_value' not in data_csv.columns:
        raise KeyError("El DataFrame debe contener la columna 'p_value'.")
    if 'category' not in data_csv.columns:
        raise KeyError("El DataFrame debe contener la columna 'category'.")

    try:
        data_csv['description'] = data_csv['gene_id'].map(dict_name).fillna(data_csv.get('description', 'sin anotacion'))

        with open(file_output_summary, 'w', encoding='utf-8') as summary_file:
            summary_file.write(f"Total de genes analizados: {len(data_csv)}\n")
            gen_max_log2fc, gen_min_log2fc, gen_min_padj = genes_significativos(data_csv)
            summary_file.write(f"Gen mas inducido: {gen_max_log2fc}\n")
            summary_file.write(f"Gen mas reprimido: {gen_min_log2fc}\n")
            summary_file.write(f"Gen mas estadisticamente confiable: {gen_min_padj}\n\n")
            summary_file.write("Conteo de genes por categoria:\n")
            for categoria in ['upregulated', 'downregulated', 'no_change']:
                conteo = data_csv['category'].value_counts().get(categoria, 0)
                porcentaje = (conteo / len(data_csv)) * 100 if len(data_csv) else 0
                summary_file.write(f"  {categoria}: {conteo} genes ({porcentaje:.2f}%)\n")
            summary_file.write("\nLista de genes DE con descripcion:\n")
            for _, row in data_csv.iterrows():
                if row['category'] in ['upregulated', 'downregulated', 'no_change']:
                    summary_file.write(f"{row['gene_id']}\t{row['log2_fold_change']}\t{row['p_value']}\t{row['description']}\n")

        for path, category in [(file_path_upregulated, 'upregulated'), (file_path_downregulated, 'downregulated')]:
            with open(path, 'w', encoding='utf-8') as out_file:
                out_file.write("gene_id\tlog2FoldChange\tp_value\tdescription\n")
                for _, row in data_csv[data_csv['category'] == category].iterrows():
                    out_file.write(f"{row['gene_id']}\t{row['log2_fold_change']}\t{row['p_value']}\t{row['description']}\n")

    except Exception as e:
        if isinstance(e, FileNotFoundError):
            print(f"Error: Archivo no encontrado - {e}")
        elif isinstance(e, IOError):
            print(f"Error de entrada/salida: {e}")
        elif isinstance(e, KeyError):
            print(f"Error de clave: {e}")
        elif isinstance(e, ValueError):
            print(f"Error de valor: {e}")
        else:
            print(f"Error al imprimir los resultados con descripcion: {e}")
    