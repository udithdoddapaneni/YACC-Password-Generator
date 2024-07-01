from RandomNumberGenerator import Randint

def RandomChoice(s):
	try:
		if not isinstance(s, list):
			raise TypeError("only list is expected")
		if not s:
			raise ValueError("list should not be empty")
		index = Randint(0, len(s) - 1)
		return s[index]
	except ValueError as v:
		print(f"Error occurred : {v}")
		return None
	except TypeError as t:
		print(f"Error occurred : {t}")
		return None



def RandomShuffle(s: list):
	try:
		if not isinstance(s, list):
			raise TypeError("only list is expected")
		if len(s) <= 1:
			return
		n = len(s)
		for i in range(n - 1, 0, -1):
			j = Randint( 0, i)
			s[i], s[j] = s[j], s[i]
	except TypeError as t:
		print(f"Error: {t}")
		return None
