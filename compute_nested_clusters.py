from graph_tool import Graph,load_graph_from_csv
import graph_tool.all as gt

# TSV file that contains the graph
filename='input/clean_result.tsv'

# Load the TSV in graph tool
g=load_graph_from_csv(filename, 
                      skip_first=True, # skip the header
                      directed=True, 
                      ecols=(0,2), # column ids of the subject and the object
                      eprop_names='p', # how to call the other columns (in this case, the property column)
                      csv_options={'delimiter':'\t'}) # specify the delimiter

state = gt.minimize_nested_blockmodel_dl(g) # run the nested clustering method from GT

state.print_summary() # print number of clusters in each nesting iteration

lstate = state.levels[0] # take the result of the first clustering iteration
b = lstate.get_blocks() # take the blocks/clusters from it

# Iterate through the nodes, and write their cluster ID to disk
with open('output/nested_clusters.tsv', 'w') as w:
    for v in g.vertices():
        w.write('%s\t%d\n' % (g.vp['name'][v], b[v])) 
