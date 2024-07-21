from CustomRandom.Random import Randint, RandomChoice, RandomChoices, RandomShuffle
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
        
    # If minimum length is less than other requirements
    if total_min_required > min_length:
        raise ValueError("The minimum length is too short for the given requirements.")
    
    # Determine the length of the password within the provided range
    password_length = Randint(max(total_min_required, min_length), max_length)
    
    # Create pools of characters create upper_chars , lower_chars , digit_chars , symbol_chars , remaining_chars
    upper_chars="".join(RandomChoices(string.ascii_letters[26:],k=min_uppercase))    #used string slicing to get characters
    lower_chars="".join(RandomChoices(string.ascii_letters[:26],k=min_lowercase))
    digit_chars="".join(RandomChoices(string.digits,k=min_digits))
    symbol_chars="".join(RandomChoices(string.punctuation,k=min_symbols))
    total_min_required=len(upper_chars+lower_chars+symbol_chars+digit_chars)  
    
    # Ensure remaining characters are randomly chosen from all pools
    remaining_length = password_length - total_min_required
    all_chars = string.ascii_letters + string.digits + string.punctuation       
    remaining_chars = "".join(RandomChoices(all_chars, k=remaining_length))
    
    # Combine all characters and shuffle them to ensure randomness
    password_list = list(upper_chars + lower_chars + digit_chars + symbol_chars + remaining_chars)
    RandomShuffle(password_list)
    password = "".join(password_list)
    # Return the password
    return password

#Getting the input from the user
def get_user_input():
    """
    Collects user input for password constraints and validates it.
    Returns:
    tuple: A tuple containing length_range, min_upper, min_lower, min_digits, min_symbols.
    """
    while True:
        try:
            min_length = int(input("Enter the lower bound for password length: "))
            max_length = int(input("Enter the upper bound for password length: "))
            if min_length > max_length:
                raise ValueError("Minimum length cannot be greater than maximum length.")
            
            length_range = (min_length, max_length)
            
            min_upper = int(input("Enter the minimum number of uppercase characters: "))
            min_lower = int(input("Enter the minimum number of lowercase characters: "))
            min_digits = int(input("Enter the minimum number of digits: "))
            min_symbols = int(input("Enter the minimum number of symbols: "))
            
            if any(x < 0 for x in [min_upper, min_lower, min_digits, min_symbols]):
                raise ValueError("Minimum values cannot be negative.")
            
            return length_range, min_upper, min_lower, min_digits, min_symbols
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

# Defining the main function
def main():
    length_range, min_upper, min_lower, min_digits, min_symbols = get_user_input()
    
    try:
        password = generate_password(length_range, min_upper, min_lower, min_digits, min_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
