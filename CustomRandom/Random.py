from datetime import datetime
from RandomNumberGenerator import *

def RandomChoice(s):
    """
    Replicate choice function from the inbuilt random module using
    the Randint function.

    s is a non-empty sequence.
    """
    if not s:
        raise IndexError("Cannot choose from an empty sequence")
    index = Randint(0, len(s) - 1)
    return s[index]

def RandomShuffle(s: list):
    """
    Replicate shuffle function from the inbuilt random module using
    the Randint function.

    s is a list.
    """
    n = len(s)
    for i in range(n - 1, 0, -1):
        j = Randint(0, i)
        s[i], s[j] = s[j], s[i]

def generate_sequence_from_time():
    """
    Generate a sequence based on the current time (year, month, day, hour, minute, second, microsecond).
    """
    now = datetime.now()
    sequence = [
        now.year, now.month, now.day,
        now.hour, now.minute, now.second,
        now.microsecond
    ]
    # Extend the sequence by adding numbers derived from the microsecond
    sequence.extend([int(digit) for digit in str(now.microsecond)])
    return sequence

def test_random_choice():
    sequence = generate_sequence_from_time()
    chosen_elements = [RandomChoice(sequence) for _ in range(10)]
    # print("RandomChoice test:")
    # print("Sequence:", sequence)
    # print("Chosen elements:", chosen_elements)

def test_random_shuffle():
    sequence = generate_sequence_from_time()
    # print("RandomShuffle test:")
    # print("Original sequence:", sequence)
    RandomShuffle(sequence)
    # print("Shuffled sequence:", sequence)

if __name__ == "__main__":
    test_random_choice()
    test_random_shuffle()
    print(generate_password(20))

