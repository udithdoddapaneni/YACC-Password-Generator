from RandomNumberGenerator import Randint

def RandomChoice(v):
	try:
		if not isinstance(v, list):
			raise TypeError("Expected a list")
		if not v:
			raise ValueError("List v must not be empty")
		index = Randint(0, len(v) - 1)
		return v[index]
	except ValueError as v:
		print(f"Error occurred : {v}")
		return None
	except TypeError as t:
		print(f"Error occurred : {v}")
		return None



def RandomShuffle(s: list):
	try:
		if not isinstance(v, list):
			raise TypeError("Expected a list")
		if len(s) <= 1:
			return
		n = len(s)
		for i in range(n - 1, 0, -1):
			j = Randint( 0, i)
			s[i], s[j] = s[j], s[i]
	except TypeError as t:
		print(f"Error occurred : {v}")
		return None
