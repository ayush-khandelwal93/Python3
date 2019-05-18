# MAP is a transformer function

a1 = [1,2,3]

a2 = map(lambda x: 2*x, a1)

for i in a2:
	print(i)



#---------------------------------------------------#

small = ['usa','ind']

def capital(x):
	return x.upper()

cap = map(lambda x: capital(x), small)
for i in cap:
	print(i)
