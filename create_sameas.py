from glob import glob

rel='connected_component'

with open('output/sameas.tsv', 'w') as w:
	w.write('id\tnode1\trelation\tnode2\n')
	for filename in glob('output/nested/medium/*.txt'):
		with open(filename, 'r') as f:
			cluster_id='CLUS' + filename.split('/')[-1][:-4]
			print(cluster_id)
			for line in f:
				node=line.strip()
				edge_id='%s-%s-%s' % (node, rel, cluster_id)
				row=[edge_id, node, rel, cluster_id]
				w.write('\t'.join(row) + '\n')
