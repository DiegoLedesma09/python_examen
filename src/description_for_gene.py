
def agregar_descripcion(data_csv, name_dict):
    """Agrega la descripción de cada gen al DataFrame de clasificación.

    Esta función toma un DataFrame que contiene la clasificación de genes y un diccionario que mapea los identificadores de genes a sus descripciones. Agrega una nueva columna `description` al DataFrame con la descripción correspondiente para cada gen. Si un gen no tiene una descripción en el diccionario, se asigna el valor `"sin anotación"`.

    Args:
        data_csv (pd.DataFrame): DataFrame que contiene la columna `gene_id` con los identificadores de genes.
        name_dict (dict): Diccionario que mapea los identificadores de genes a sus descripciones.

    Returns:
        pd.DataFrame: Un nuevo DataFrame con una columna adicional `description` que contiene la descripción de cada gen.
    """
    try:
        data_csv['description'] = data_csv['gene_id'].map(name_dict).fillna('sin anotación')
        return data_csv

    except Exception as e:
        if isinstance(e, KeyError):
            print(f"Error de clave: {e}")
        if isinstance(e, ValueError):
            print(f"Error de valor: {e}")
        if isinstance(e, Exception):
            print(f"Error al agregar las descripciones: {e}")
        return None