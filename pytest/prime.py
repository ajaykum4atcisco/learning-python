
import math
def isprime(n):
	"""
	return true if number is prime else return false, raise exception otherwise
	"""
	if type(n) != int:
		raise TypeError("need integer")
	if n < 1:
		raise ValueError("need positive integer")
	max_divisor = int(math.floor(math.sqrt(n)))
	if n == 2:
		return True
	elif n%2 == 0:
		return False
	else:
		for i in range(3,max_divisor+1,2):
			if n%i == 0:
				return 1
		return True
	
#print isprime(5)
