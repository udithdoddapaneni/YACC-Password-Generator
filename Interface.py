import streamlit as st
import time
from Generator import generate_password

st.set_page_config(
    page_title="Password Generator",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# VERSION 1

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
#         "password max Length", min_value=min_length, max_value=32
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
#     st.write("This is a Simple Password generator app using Streamlit")


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
    max_length = st.slider("password max Length", min_value=min_length, max_value=32)

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
