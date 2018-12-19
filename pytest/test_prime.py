
import pytest
import prime
import time

def test_prime_positive():
	
	assert prime.isprime(2) == True
	assert prime.isprime(20) == False	
	assert prime.isprime(3)
	assert not prime.isprime(4)

def test_prime_negative():
	assert not prime.isprime(4012311) == False
	assert not prime.isprime(4012310) == True

	
def test_prime_type_exception():
	with pytest.raises(TypeError):
		prime.isprime('h')
		
def test_prime_value_exception():
	with pytest.raises(ValueError):
		prime.isprime(-3)
def test_check_prime_test():
	assert prime.isprime(200) == False
	
def test_check_range_of_prime():
	with pytest.raises(TypeError):
		prime.isprime(False)
def test_missing_param():
	
	with pytest.raises(ValueError) as ex_info:
		prime.isprime(-2)
	assert ex_info.type == ValueError
def test_time_taken_to_calculate():
	
	t0 = time.time()
	for i in range(2,100000):
		prime.isprime(i)
	t1 = time.time()
	t = t1-t0
	assert t < 0.4
	
