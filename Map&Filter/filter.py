a = [1,2,3,4,5]

a1 = filter(lambda x: x>2, a)
for i in a1:
	print(i)


#-----------------------------------

def large(x):
	if x>2:
		return True

a2 = filter(lambda x: large(x),a)

for i in a2:
	print(i)
