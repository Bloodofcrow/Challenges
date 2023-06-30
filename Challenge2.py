l = [-6, -5, 0, 5, 6]
l = [(entry**2) for entry in l]
s = 4
s = int(str(s)+str(s))
l = [entry for entry in l if entry <= s]

for iteration in range(0, len(l)-1):	
	for i in range(0, len(l)-1):
	    if (l[i]>= l[i+1]):
	        temporal = l[i+1]
	        l[i+1] = l[i]
	        l[i] = temporal
        

print(l)