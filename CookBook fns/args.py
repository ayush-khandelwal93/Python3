def fn(a, *args):
	print(a)
	for i in args:
		print (i)

fn('a','b','c','d')
fn('a','b','c')
