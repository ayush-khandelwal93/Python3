a = ['a','b','c']

b = [1,2,3]

c = zip(a,b)
print(type(c))         # zip object
print(type(list(c)))   # list

for i in c:
	print(type(i))     # tuple
	print(i)


