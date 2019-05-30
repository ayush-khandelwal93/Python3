def fn(a, **kwargs):
	print(a)
	for key,value in kwargs.items():
		print(key, value)

fn('a',last='one',trap='two',sig='nin')
