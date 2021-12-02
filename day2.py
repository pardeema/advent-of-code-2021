FILE1 = "input2_1.txt"

with open(FILE1) as f:
    lines = [line.strip() for line in f]

x = 0
y = 0
pt1 = 0 

#pt2
aim = 0
y2 = 0
pt2 = 0

for line in lines:
    if 'forward' in line:
        num = int(line.strip('forward').strip())
        x+= num
        y2 += aim * num 

    if 'up' in line:
        num = int(line.strip('up').strip())
        y-= num
        aim -= num
    if 'down' in line:
        num = int(line.strip('down').strip())
        y+= num
        aim += num

pt1 = x * y
print (pt1)
pt2 = x * y2 
print (pt2)

