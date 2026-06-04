def parse_attributes(data_gff):
    """Parsea la columna `attributes` del DataFrame del GFF para extraer descripciones."""

    name_dict = {}
    for _, row in data_gff.iterrows():
        try:
            attributes = row['attributes']
            if not isinstance(attributes, str):
                continue

            fields = [field for field in attributes.split(';') if field]
            parsed = {}
            for item in fields:
                if '=' in item:
                    key, value = item.split('=', 1)
                    parsed[key] = value

            gene_name = parsed.get('Name')
            if not gene_name:
                gene_name = parsed.get('gene_id') or parsed.get('ID')

            description = parsed.get('description')
            if gene_name:
                name_dict[gene_name] = description if description else None
        except Exception as e:
            if isinstance(e, IndexError):
                print(f"Error de indice al parsear la fila: {e}")
            elif isinstance(e, KeyError):
                print(f"Error de clave al parsear la fila: {e}")
            else:
                print(f"Error al parsear la fila: {e}")
    return name_dict