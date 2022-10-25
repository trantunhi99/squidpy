from anndata import AnnData
import plotly.graph_objects as go
import numpy as np

def pl_spatial_de(adata: AnnData):
    adata.uns["design_matrix_DEGs"]['log_pval'] = np.log2(adata.uns["design_matrix_DEGs"]['p-val_adj']) * -1
    fig = go.Figure()
    trace1 = go.Scatter(
    x=adata.uns["design_matrix_DEGs"]['lfc'],
    y=adata.uns["design_matrix_DEGs"]['log_pval'],
    mode='markers',
    hovertext=list(adata.uns["design_matrix_DEGs"]['gene'])
    )
    fig.add_trace(trace1)
    fig.update_layout(title='Volcano plot for spatial DEGs')
    fig.show()