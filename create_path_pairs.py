import glob

with open('pairs.tsv', 'w') as w:
	for i, c1 in enumerate(glob.glob('output/nested/medium/*.txt')):
		for j, c2 in enumerate(glob.glob('output/nested/medium/*.txt')):
			if i!=j:
				node1='CLUS' + c1.split('/')[-1][:-4]
				node2='CLUS' + c2.split('/')[-1][:-4]
				w.write(node1.strip() + '\t' + node2.strip() + '\n')
	print('Cartesian product ready')


