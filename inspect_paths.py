from tqdm import tqdm
from collections import Counter

count_rel={"0":0, "1":0}

current_path=''
all_paths=[]
with open('paths.tsv', 'r') as f:
	header = next(f)
	for line in tqdm(f, total=180000000):
		n1, rel, n2, eid=line.split('\t')
		count_rel[rel]+=1
		if rel=='0':
			if current_path:
				all_paths.append(current_path)
			current_path=n2.split('-')[1]
		else:
			current_path+='-%s' % n2.split('-')[1] 
	
	if current_path:
		all_paths.append(current_path)

print(count_rel)
print(Counter(all_paths))
