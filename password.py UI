import random
import string
import streamlit as st
import time

def generate_password(password_range : list , min_uppercase , min_lowercase, min_digits, min_symbols):
    
    """
    password_range is list of two integers
    this function returns a string following the above parameters
    """

    min_length, max_length = password_range
    total_min_required = min_uppercase + min_lowercase  + min_digits + min_symbols
    
    # Ensure the password length is sufficient
    if total_min_required > max_length:
        st.error("The maximum length is too short for the given requirements.")
        # raise ValueError("The maximum length is too short for the given requirements.")
        
    # If minimum length is less than other requirements
    if total_min_required > min_length:
        st.error("The maximum length is too short for the given requirements.")
        # raise ValueError("The minimum length is too short for the given requirements.")
    
    # Determine the length of the password within the provided range
    password_length = random.randint(max(total_min_required, min_length), max_length)
    
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
    password_list = list(upper_chars + lower_chars + digit_chars + symbol_chars + remaining_chars)
    random.shuffle(password_list)
    password = "".join(password_list)
    # Return the password
    return password

print(generate_password([10,20],2,2,2,2))


st.sidebar.title("Navigation")
page=st.sidebar.radio("Go to",["Password Generator","About"])

if page=="Password Generator":
    st.title("Password Generator")
    st.header('Generate a Secure Password')
    min_length=st.slider("password min Length",min_value=8,max_value=32,value=12)
    max_length=st.slider("password max Length",min_value=8,max_value=32,value=12)
    min_upper=int(st.number_input("Min UpperCase Characters",min_value=3.0,max_value=30.0,value=3.0,step=1.0))
    min_lower=int(st.number_input("Min Lowercase Characters",min_value=3.0,max_value=30.0,value=3.0,step=1.0))
    min_digit=int(st.number_input("Min digits",min_value=3.0,max_value=30.0,value=3.0,step=1.0))
    min_symbol=int(st.number_input("Min symbols",min_value=3.0,max_value=30.0,value=3.0,step=1.0))

    if st.button("Generate Password"):
        password=generate_password([min_length,max_length],min_upper,min_lower,min_digit,min_symbol)  #password generating function is being called
        # st.markdown
        st.text("Generated Password: ")
        # st.code(password)
        st.markdown(password)
        succ=st.success("password Successfully generated")
        time.sleep(10)
        succ.empty()


elif page=="About":
    st.header("About Us")
    st.write("This is a Simple Password generator apo using Streamlit")



