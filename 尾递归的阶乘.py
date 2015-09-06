def fact(n):
	return fact_iter(n, 1)

def fact_iter(n, product):
	if n==1:
		return product
	else:
		return fact_iter(n-1, product*n)
n=7
print('fact(%d) =%d' % (n, fact(n)) ) 