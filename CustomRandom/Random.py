from RandomNumberGenerator import Randint

def RandomChoice(s):
	try:
		if not isinstance(s, list):
			raise TypeError("Expected a list")
		if not s:
			raise ValueError("List v must not be empty")
		index = Randint(0, len(s) - 1)
		return s[index]
	except ValueError as s:
		print(f"Error occurred : {s}")
		return None
	except TypeError as t:
		print(f"Error occurred : {s}")
		return None



def RandomShuffle(s: list):
	try:
		if not isinstance(s, list):
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
