import time
import string

# Linear Congruential Generator
def pseudo_random(a, b, seed):
    m = 2**32
    a_const = 1664525
    c_const = 1013904223
    
    # LCG formula
    seed = (a_const * seed + c_const) % m
    
    # Normalized within [a, b]
    normalized_number = a + seed % (b - a + 1)
    
    return int(normalized_number)

def random_choice(sequence, seed):
    index = pseudo_random(0, len(sequence) - 1, seed)
    return sequence[index]

# Fisher–Yates shuffle
def random_shuffle(sequence, seed):
    shuffled_list = sequence[:]
    n = len(shuffled_list)
    for i in range(n - 1, 0, -1):
        j = pseudo_random(0, i, seed)
        # Swap elements
        shuffled_list[i], shuffled_list[j] = shuffled_list[j], shuffled_list[i]
    return shuffled_list

def GeneratePassword(password_range, min_uppercase, min_lowercase, min_digits, min_symbols):
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    
    # List of characters to choose from
    characters = s1 + s2 + s3 + s4
    
    password = []
    seed = int(time.time() * 1000)  
    
    min_length, max_length = password_range
    total_min_required = min_uppercase + min_lowercase + min_digits + min_symbols
    
    # Ensuring the minimum length is sufficient
    if total_min_required < min_length:
        raise ValueError("Total required characters are less than the minimum password length.")
    
    # Ensuring the password length is sufficient
    if total_min_required > max_length:
        raise ValueError("Total required characters exceed the maximum password length.")
    
    # Randomly select a length within the specified range
    length = pseudo_random(min_length, max_length, seed)
    seed += 1
    
    for i in range(min_uppercase):
        chosen_char = random_choice(s1, seed)
        password.append(chosen_char)
        seed += 1  
    
    for i in range(min_lowercase):
        chosen_char = random_choice(s2, seed)
        password.append(chosen_char)
        seed += 1  
    
    for i in range(min_digits):
        chosen_char = random_choice(s3, seed)
        password.append(chosen_char)
        seed += 1  
    
    for i in range(min_symbols):
        chosen_char = random_choice(s4, seed)
        password.append(chosen_char)
        seed += 1  
    
    remaining_length = length - len(password)
    for i in range(remaining_length):
        chosen_char = random_choice(characters, seed)
        password.append(chosen_char)
        seed += 1  
    
    # Shuffling the password
    seed = int(time.time() * 1000) + length - 1
    password = ''.join(random_shuffle(password, seed))
    
    return password

password_range = [int(x) for x in input("Enter password length range [a b]: ").split()]

min_uppercase = int(input("Minimum uppercase letters: "))

min_lowercase = int(input("Minimum lowercase letters: "))

min_digits = int(input("Minimum digits: "))

min_symbols = int(input("Minimum symbols: "))

try:
    password = GeneratePassword(password_range, min_uppercase, min_lowercase, min_digits, min_symbols)
    #print(len(password))
    print("Generated password:", password)
except ValueError as e:
    print(e)
