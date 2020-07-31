from graph_tool.topology import label_components
from graph_tool import load_graph, GraphView, Graph,load_graph_from_csv

import graph_tool.all as gt

filename='input/clean_result.tsv'
#filename='test_data.tsv'

g=load_graph_from_csv(filename, 
                      skip_first=True, 
                      directed=True, 
                      ecols=(0,2), 
                      eprop_names='p', 
                      csv_options={'delimiter':'\t'})

state = gt.minimize_blockmodel_dl(g)

#state.print_summary()

b = state.get_blocks()

with open('output/nonnested_clusters.tsv', 'w') as w:
    for v in g.vertices():
        w.write('%s\t%d\n' % (g.vp['name'][v], b[v]))
