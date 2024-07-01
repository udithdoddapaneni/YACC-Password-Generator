import time

def Linear_Congruential_Generator(seed, a=1664525, c=1013904223, m=2**32):
	while True:
		seed = (a * seed + c) % m
		yield seed

def Randint(a, b):
	try:
		if a > b:
			raise ValueError("Lower bound must be less than or equal to upper bound")
		current_time = time.time()
		seed = int(time.time() * 1000)	
		generator = Linear_Congruential_Generator(seed)
		range = b - a + 1
		rand_no = next(generator) % range + a
		return rand_no
	except ValueError as v:
		print(f"Error occurred : {v}")
		return None
