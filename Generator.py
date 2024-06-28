import random
import string 


def GeneratePassword(password_range, min_uppercase, min_lowercase, min_digits, min_symbols):
    """
    password_range is list of two integers
    this function returns a string following the above parameters
    """
    length_of_password=(range_password[0]+range_password[1])/2
    length_req=minCount_upper+minCount_lower+minCount_digits+minCount_symbols

    if length_of_password<length_req:
        return "Password length insufficient"
    
    remaining_length=abs(length_of_password-length_req)

    upper=string.ascii_uppercase
    lower=string.ascii_lowercase
    punctuations=string.punctuation
    digits=string.digits

    mixture=upper+lower+punctuations+digits

    list_mixture=list(mixture)
    random.shuffle(list_mixture)
    shuffled_mixture="".join(list_mixture)

    list_pass=random.choices(shuffled_mixture,k=length_req)
    list_pass.extend(random.choices(shuffled_mixture,k=int(remaining_length)))
    password="".join(list_pass)

    return password
