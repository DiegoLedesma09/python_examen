# Casos de prueba

## 1. Entrada valida con genes regulados al alza y a la baja
- CSV con columnas `gene_id`, `log2_fold_change`, `p_value`.
- GFF con atributos `Name=` y `description=`.
- Umbrales estandar `0.05` y `1.0`.
- Verificar que se generan `upregulated_genes.tsv`, `downregulated_genes.tsv` y `summary_report.txt`.

## 2. Genes sin descripcion en el GFF
- CSV valido.
- GFF con algunos genes sin campo `description=`.
- Verificar que esos genes reciben `sin anotacion` en la salida.

## 3. Umbrales limite exactos
- CSV con valores de `log2_fold_change` exactamente iguales a `umbral_lfc` y `p_value` exactamente igual a `umbral_padj`.
- Verificar clasificacion correcta segun la logica del script.

## 4. Sin genes significativos
- CSV valido donde ninguno cumple `p_value < umbral_padj`.
- Verificar que todos los genes queden en `no_change` y que el resumen lo refleje.

## 5. Atributos GFF mal formados
- GFF con lineas de atributos que no contienen `Name=` o no siguen el formato `key=value;...`.
- Verificar que el script maneja la excepcion sin detenerse y continua con los demas genes.

## 6. CSV con columnas faltantes
- CSV que no contiene `log2_fold_change` o `p_value`.
- Verificar que el script detecta el error y no genera resultados incorrectos.

## 7. Archivo CSV vacio
- CSV con encabezado pero sin filas de datos.
- Verificar que el script maneja el DataFrame vacio y no intenta escribir resultados invalidos.

## 8. Archivo GFF inexistente
- Ruta invalida para el archivo GFF.
- Verificar que el script informa de archivo no encontrado y termina correctamente.

## 9. Valores no numericos en el CSV
- CSV con valores de `log2_fold_change` o `p_value` no convertibles a numero.
- Verificar que el script detecta la falla de parsing o bloquea el calculo.

## 10. Directorio de salida no existente
- Proporcionar un `output_dir` que no existe.
- Verificar si el script crea los archivos o muestra un mensaje de error apropiado segun la implementacion actual.
