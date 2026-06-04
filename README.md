# Python Examen Final

## Versión 1.1
- Se añadió generación automática de `volcano_plot.png` en el directorio de salida.
- El pipeline ahora incluye el módulo `src/volcano.py`.
- Se conservan los archivos de salida existentes: `upregulated_genes.tsv`, `downregulated_genes.tsv` y `summary_report.txt`.

## Descripción
Proyecto para el examen final de Python, que procesa resultados de expresión génica diferencial y enriquece los genes con anotaciones GFF.

## Estructura
- `data/`: datos de entrada
- `doc/`: documentación
- `results/`: resultados del análisis
- `src/`: código fuente
- `tests/`: pruebas unitarias

## Instalación
1. Crear y activar un entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instalar dependencias:

```powershell
pip install pandas matplotlib pytest
```

## Uso
```powershell
python main.py data/iav_deseq2_results.tsv data/human_genes.gff results 0.05 1.0
```

## Salidas
- `results/upregulated_genes.tsv`
- `results/downregulated_genes.tsv`
- `results/summary_report.txt`
- `results/volcano_plot.png`
