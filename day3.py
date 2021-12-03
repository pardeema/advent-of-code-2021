import collections

FILE1="input3_1.txt"
g=''
e=''

with open(FILE1) as f:
	lines = f.readlines()
	lines = [line.strip() for line in lines]

def return_min_max(items, depth=1):
	tmp = [line[depth] for line in items]
	counter = collections.Counter(tmp)

	max = counter.most_common()[0][0]
	min = counter.most_common()[-1][0]
	no_max = counter.most_common()[0][1]
	no_min = counter.most_common()[-1][1]

	if no_max == no_min:
		max='1'
		min='0'

	return min, max 


cols = [list(line) for line in lines] #split into columns

length = len(lines[0])

o_candidates = lines.copy()
o2 = lines.copy()
o_ct = 0
c_candidates = lines.copy()
c_ct = 0

#pt1
for i in range(length):
	min, max = return_min_max(cols, i)
	g+=max
	e+=min

#pt2
def pt2(candidates, ct, value='o'):
	while (len(candidates)> 1):
		new_cands = candidates.copy()
		cols  = [ list(line) for line in candidates]
		min, max = return_min_max(cols, ct)

		#look for max
		if value=='o':
			for item in candidates:
				if item[ct] != max:
					new_cands.remove(item)
			candidates=new_cands.copy()
		#min
		if value =='c':
			# print(candidates)
			# print("MIN: {}".format(min))
			for item in candidates:
				# print(item)
				if item[ct] != min:
					new_cands.remove(item)
			candidates = new_cands.copy() 	
		ct += 1

	return candidates

#converts binary to int
pt1 = int(g,2) * int(e, 2)
print(pt1)

o2 = pt2(o_candidates, o_ct, 'o')[0]
c2 = pt2(c_candidates, c_ct, 'c')[0]
a2 = int(o2, 2) * int(c2, 2)
print(a2)

