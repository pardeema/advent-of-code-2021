FILE1 = 'input1_1.txt'

pt1 = 0
pt2 = 0 

with open(FILE1, 'r') as f:
    lines = f.readlines()

for i in range(len(lines)-1):
    if int(lines[i+1]) > int(lines[i]):
        pt1+=1
for i in range(len(lines)-3):
    sum_A = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
    sum_B = int(lines[i+1]) + int(lines[i+2]) + int(lines[i+3])
    if sum_B > sum_A:
        pt2+=1

print(pt1)
print(pt2)
