from RandomNumberGenerator import Randint

def RandomChoice(s):
    """
    replicate choice function from the inbuilt random module using
    the Randint fuction

    s is a non-empty sequence
    """

    if not s:
        raise IndexError("Cannot choose from an empty sequence")
    index = Randint(0, len(s) - 1)
    return s[index]

def RandomShuffle(s: list):
    """
    replicate shuffle function from the inbuilt random module using
    the Randint function

    s is a list
    """

    n = len(s)
    for i in range(n - 1, 0, -1):
        j = Randint(0, i)
        s[i], s[j] = s[j], s[i]

'''


def test_random_choice():
    sequence = [1, 2, 3, 4, 5]
    chosen_elements = [RandomChoice(sequence) for _ in range(10)]
    print("RandomChoice test:")
    print("Sequence:", sequence)
    print("Chosen elements:", chosen_elements)

def test_random_shuffle():
    sequence = [1, 2, 3, 4, 5]
    print("RandomShuffle test:")
    print("Original sequence:", sequence)
    RandomShuffle(sequence)
    print("Shuffled sequence:", sequence)

if __name__ == "__main__":
    test_random_choice()
    test_random_shuffle()
    
    '''