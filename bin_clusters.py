from glob import glob
from collections import defaultdict, Counter

for f in glob('output/*.*'):
	clusters=defaultdict(list)
	with open(f, 'r') as lines:
		for line in lines:
			data=line.split()
			if len(data)!=2:
				print(data)
				continue
			clusters[data[1]].append(data[0])
	sizes=[]
	less25=0
	from25to200=0
	over200=0
	for c, l in clusters.items():
		sizes.append(len(l))
		if len(l)<25:
			less25+=1
			filename='%s/small/%s.txt' % (f.split('_')[0], c)
		elif len(l)<=200:
			from25to200+=1
			filename='%s/medium/%s.txt' % (f.split('_')[0], c)
		else:
			over200+=1
			filename='%s/large/%s.txt' % (f.split('_')[0], c)
		with open(filename, 'w') as w:
			for node in l:
				w.write(node + '\n')
	#print(dict(Counter(sizes).most_common()))
	print('less than 25: %d, 25-200: %d, 201+: %d' % (less25, from25to200, over200))
