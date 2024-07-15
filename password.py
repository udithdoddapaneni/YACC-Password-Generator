import random
import string
import streamlit as st
import time


def generate_password(
    password_range: list, min_uppercase, min_lowercase, min_digits, min_symbols
):
    """
    password_range is list of two integers
    this function returns a string following the above parameters
    """

    min_length, max_length = password_range
    total_min_required = min_uppercase + min_lowercase + min_digits + min_symbols

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
    upper_chars = "".join(
        random.choices(string.ascii_letters[26:], k=min_uppercase)
    )  # used string slicing to get characters
    lower_chars = "".join(random.choices(string.ascii_letters[:26], k=min_lowercase))
    digit_chars = "".join(random.choices(string.digits, k=min_digits))
    symbol_chars = "".join(random.choices(string.punctuation, k=min_symbols))
    total_min_required = len(upper_chars + lower_chars + symbol_chars + digit_chars)

    # Ensure remaining characters are randomly chosen from all pools
    remaining_length = password_length - total_min_required
    all_chars = string.ascii_letters + string.digits + string.punctuation
    remaining_chars = "".join(random.choices(all_chars, k=remaining_length))

    # Combine all characters and shuffle them to ensure randomness
    password_list = list(
        upper_chars + lower_chars + digit_chars + symbol_chars + remaining_chars
    )
    random.shuffle(password_list)
    password = "".join(password_list)
    # Return the password
    return password


# print(generate_password([10,20],2,2,2,2))

# VERSION 1

# st.set_page_config(layout="centered", initial_sidebar_state="collapsed")
# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Go to", ["Password Generator", "About"])

# if page == "Password Generator":
#     st.title("Password Generator")
#     st.header("Generate a Secure Password")
#     with st.expander("Adjust Password Parameters"):
#         col1, col2 = st.columns(2)
#         with col1:
#             min_upper = int(
#                 st.number_input(
#                     "Min UpperCase Characters",
#                     min_value=3.0,
#                     max_value=30.0,
#                     value=3.0,
#                     step=1.0,
#                     help="Minimum number of uppercase letters in the password",
#                 )
#             )
#             min_lower = int(
#                 st.number_input(
#                     "Min Lowercase Characters",
#                     min_value=3.0,
#                     max_value=30.0,
#                     value=3.0,
#                     step=1.0,
#                     help="Minimum number of lowercase letters in the password",
#                 )
#             )
#         with col2:
#             min_digit = int(
#                 st.number_input(
#                     "Min digits",
#                     min_value=3.0,
#                     max_value=30.0,
#                     value=3.0,
#                     step=1.0,
#                     help="Minimum number of digits in the password",
#                 )
#             )
#             min_symbol = int(
#                 st.number_input(
#                     "Min symbols",
#                     min_value=3.0,
#                     max_value=30.0,
#                     value=3.0,
#                     step=1.0,
#                     help="Minimum number of symbols in the password",
#                 )
#             )

#     total_min_required = min_upper + min_lower + min_digit + min_symbol

#     min_length = st.slider(
#         "password min Length", min_value=total_min_required, max_value=32
#     )
#     max_length = st.slider(
#         "password max Length", min_value=min_length + 1, max_value=32
#     )

#     if st.button("Generate Password"):
#         password = generate_password(
#             [min_length, max_length], min_upper, min_lower, min_digit, min_symbol
#         )  # password generating function is being called
#
#         st.text("Generated Password: ")
#         st.code(password, language="")
#         #st.markdown(password)

#         succ = st.success("Password Successfully Generated")
#         time.sleep(10)
#         succ.empty()


# elif page == "About":
#     st.header("About Us")
#     st.write("This is a Simple Password generator apo using Streamlit")


# VERSION 2

tab1, tab2 = st.tabs(["Password Generator", "About Us"])

with tab1:
    st.title("Password Generator")
    with st.expander("Adjust Password Parameters"):
        col1, col2 = st.columns(2)
        with col1:
            min_upper = int(
                st.number_input(
                    "Min UpperCase Characters",
                    min_value=3.0,
                    max_value=30.0,
                    value=3.0,
                    step=1.0,
                    help="Minimum number of uppercase letters in the password",
                )
            )
            min_lower = int(
                st.number_input(
                    "Min Lowercase Characters",
                    min_value=3.0,
                    max_value=30.0,
                    value=3.0,
                    step=1.0,
                    help="Minimum number of lowercase letters in the password",
                )
            )
        with col2:
            min_digit = int(
                st.number_input(
                    "Min digits",
                    min_value=3.0,
                    max_value=30.0,
                    value=3.0,
                    step=1.0,
                    help="Minimum number of digits in the password",
                )
            )
            min_symbol = int(
                st.number_input(
                    "Min symbols",
                    min_value=3.0,
                    max_value=30.0,
                    value=3.0,
                    step=1.0,
                    help="Minimum number of symbols in the password",
                )
            )

    total_min_required = min_upper + min_lower + min_digit + min_symbol

    min_length = st.slider(
        "password min Length", min_value=total_min_required, max_value=32
    )
    max_length = st.slider(
        "password max Length", min_value=min_length, max_value=32
    )

    if st.button("Generate Password"):
        password = generate_password(
            [min_length, max_length], min_upper, min_lower, min_digit, min_symbol
        )  # password generating function is being called

        st.text("Generated Password: ")

        # Various Options for Displaying Password
        st.code(password, language="")
        # st.markdown(password)

        succ = st.success("Password Successfully Generated")
        time.sleep(10)
        succ.empty()

with tab2:
    st.header("About Us")
    st.write("This is a Simple Password Generator app using Streamlit")
