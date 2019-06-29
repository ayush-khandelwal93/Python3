a= {'a':1,'b':2}
#print(a['c']) Will throw error

# Method 1
if 'c' in a:
	print(a['c'])
else:
	print(None)

# Method 2
print(a.get('c', None))
