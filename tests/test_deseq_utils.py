def test_classify_upregulated():
    """Un gen con padj=0.01 y lfc=3.5 debe ser upregulated."""
    import pandas as pd
    from src.clasificacion import clasificacion_genes

    df = pd.DataFrame([{'gene_id': 'G1', 'log2_fold_change': 3.5, 'p_value': 0.01}])
    out = clasificacion_genes(df.copy(), umbral_padj=0.05, umbral_lfc=1.0)
    assert out.loc[0, 'category'] == 'upregulated'

def test_classify_downregulated():
    """Un gen con padj=0.01 y lfc=-2.0 debe ser downregulated."""
    import pandas as pd
    from src.clasificacion import clasificacion_genes

    df = pd.DataFrame([{'gene_id': 'G2', 'log2_fold_change': -2.0, 'p_value': 0.01}])
    out = clasificacion_genes(df.copy(), umbral_padj=0.05, umbral_lfc=1.0)
    assert out.loc[0, 'category'] == 'downregulated'

def test_classify_no_change_by_padj():
    """Un gen con padj=0.8 aunque tenga lfc alto debe ser no_change."""
    import pandas as pd
    from src.clasificacion import clasificacion_genes

    df = pd.DataFrame([{'gene_id': 'G3', 'log2_fold_change': 5.0, 'p_value': 0.8}])
    out = clasificacion_genes(df.copy(), umbral_padj=0.05, umbral_lfc=1.0)
    assert out.loc[0, 'category'] == 'no_change'

def test_classify_no_change_by_lfc():
    """Un gen significativo pero con lfc=0.3 debe ser no_change."""
    import pandas as pd
    from src.clasificacion import clasificacion_genes

    df = pd.DataFrame([{'gene_id': 'G4', 'log2_fold_change': 0.3, 'p_value': 0.001}])
    out = clasificacion_genes(df.copy(), umbral_padj=0.05, umbral_lfc=1.0)
    assert out.loc[0, 'category'] == 'no_change'

def test_find_extremes_returns_correct_keys():
    """find_extremes debe retornar dict con las claves most_induced,
    most_repressed y most_significant."""
    import pandas as pd
    from src.output import genes_significativos

    df = pd.DataFrame([
        {'gene_id': 'A', 'log2_fold_change': 10.0, 'p_value': 0.01},
        {'gene_id': 'B', 'log2_fold_change': -8.0, 'p_value': 0.02},
        {'gene_id': 'C', 'log2_fold_change': 1.0, 'p_value': 0.0001},
    ])

    most_induced, most_repressed, most_significant = genes_significativos(df)
    assert most_induced == 'A'
    assert most_repressed == 'B'
    assert most_significant == 'C'