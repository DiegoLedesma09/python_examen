
def volcano_plot(data_csv, umbral_padj=0.05, umbral_lfc=1.0, output_dir="results"):
    """Genera un volcano plot a partir de los datos de expresión génica.

    Esta función crea un volcano plot utilizando `matplotlib`, donde el eje X representa el `log2FoldChange` y el eje Y representa el `-log10(padj)`. Los puntos se colorean según su categoría (`upregulated`, `downregulated`, `no_change`). Se agregan líneas punteadas para indicar los umbrales de significancia y se etiquetan los 5 genes más significativos. Finalmente, el gráfico se guarda en el directorio especificado.

    Args:
        data_csv (pd.DataFrame): DataFrame que contiene las columnas `gene_id`, `log2_fold_change`, `p_value` y `category`.
        umbral_padj (float, opcional): Umbral para el p-value ajustado. Por defecto es 0.05.
        umbral_lfc (float, opcional): Umbral para el log2FoldChange. Por defecto es 1.0.
        output_dir (str, opcional): Directorio donde se guardará el gráfico. Por defecto es "results".
    Returns:
        None: Esta función no devuelve ningún valor, solo genera y guarda el gráfico.  
    """
    
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        import os

        # Crear el directorio de salida si no existe
        os.makedirs(output_dir, exist_ok=True)

        # Calcular -log10(padj)
        data_csv['neg_log10_padj'] = -np.log10(data_csv['p_value'])

        # Colores para cada categoría
        colores = {'upregulated': 'red', 'downregulated': 'blue', 'no_change': 'grey'}
        data_csv['color'] = data_csv['category'].map(colores)

        # Crear el volcano plot
        plt.figure(figsize=(10, 6))
        plt.scatter(data_csv['log2_fold_change'], data_csv['neg_log10_padj'], c=data_csv['color'], alpha=0.7, edgecolors='w', linewidth=0.5)

        # Agregar líneas de umbral
        plt.axhline(-np.log10(umbral_padj), color='black', linestyle='dashed')
        plt.axvline(umbral_lfc, color='black', linestyle='dashed')
        plt.axvline(-umbral_lfc, color='black', linestyle='dashed')

        # Etiquetar los 5 genes más significativos
        top_genes = data_csv.nsmallest(5, 'p_value')
        for _, row in top_genes.iterrows():
            plt.text(row['log2_fold_change'], row['neg_log10_padj'], row['gene_id'], fontsize=8)

        # Configurar el gráfico
        plt.title('Volcano Plot')
        plt.xlabel('log2FoldChange')
        plt.ylabel('-log10(padj)')
        plt.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) for color in colores.values()], labels=colores.keys())
        
        # Guardar el gráfico
        output_path = os.path.join(output_dir, 'volcano_plot.png')
        plt.savefig(output_path)
        plt.close()
        
    except ImportError as e:
        print(f"Error: Librería no encontrada - {e}")
    except Exception as e:
        if isinstance(e, KeyError):
            print(f"Error de clave: {e}")
        if isinstance(e, ValueError):
            print(f"Error de valor: {e}")
        if isinstance(e, FileNotFoundError):
            print(f"Error: Archivo no encontrado - {e}")
        if isinstance(e, OSError):
            print(f"Error de sistema operativo: {e}")
        if isinstance(e, Exception):
            print(f"Error al generar el volcano plot: {e}")
