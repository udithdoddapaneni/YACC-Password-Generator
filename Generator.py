import random
import string
def generate_password(password_range : list , min_uppercase , min_lowercase, min_digits, min_symbols):
    
    """
    password_range is list of two integers
    this function returns a string following the above parameters
    """

    min_length, max_length = password_range
    
    total_min_required = min_uppercase + min_lowercase  + min_digits + min_symbols
    
    # Ensure the password length is sufficient
    if total_min_required > max_length:
        raise ValueError("The maximum length is too short for the given requirements.")
    
    # Determine the length of the password within the provided range
    password_length = random.randint(min_length, max_length)
    
    # Create pools of characters create upper_chars , lower_chars , digit_chars , symbol_chars , remaining_chars
    
    upper_chars="".join(random.choices(string.ascii_letters[26:],k=min_uppercase))    #used string slicing to get characters
    lower_chars="".join(random.choices(string.ascii_letters[:26],k=min_lowercase))
    digit_chars="".join(random.choices(string.digits,k=min_digits))
    symbol_chars="".join(random.choices(string.punctuation,k=min_symbols))
    total_min_required=len(upper_chars+lower_chars+symbol_chars+digit_chars)    
    # Ensure remaining characters are randomly chosen from all pools
    remaining_length = password_length - total_min_required
    all_chars = string.ascii_letters + string.digits + string.punctuation       
    remaining_chars = "".join(random.choices(all_chars, k=remaining_length))
    
    # Combine all characters and shuffle them to ensure randomness
    password=upper_chars+lower_chars+symbol_chars+digit_chars+remaining_chars

    random.shuffle(list(password))    #converting to list to shuffle
    password="".join(password)        #back to a string
    # Join the list to form the final password string
    return password
    
# define the main function and print the final output
