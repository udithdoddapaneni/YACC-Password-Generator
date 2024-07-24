import streamlit as st
import time
from Generator import generate_password

st.set_page_config(
    page_title="Password Generator",
    layout="centered",
    initial_sidebar_state="collapsed",
)

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
                    min_value=0,
                    max_value=25,
                    value=3,
                    step=1,
                    help="Minimum number of uppercase letters in the password",
                )
            )
            min_lower = int(
                st.number_input(
                    "Min Lowercase Characters",
                    min_value=0,
                    max_value=25,
                    value=3,
                    step=1,
                    help="Minimum number of lowercase letters in the password",
                )
            )
        with col2:
            min_digit = int(
                st.number_input(
                    "Min digits",
                    min_value=0,
                    max_value=25,
                    value=3,
                    step=1,
                    help="Minimum number of digits in the password",
                )
            )
            min_symbol = int(
                st.number_input(
                    "Min symbols",
                    min_value=0,
                    max_value=25,
                    value=3,
                    step=1,
                    help="Minimum number of symbols in the password",
                )
            )

    total_min_required = min_upper + min_lower + min_digit + min_symbol

    if total_min_required < 100:
        min_length = st.slider(
            "Password Min Length", min_value=total_min_required, max_value=100
        )

        if min_length == 100:
            st.warning(
                "Maximum length of password is 100. Max Lenth Slider has been disabled."
            )
            max_length = 100
        else:
            max_length = st.slider(
                "Password Max Length",
                min_value=min_length,
                max_value=100,
            )
    else:
        min_length = max_length = 100
        st.warning("Maximum length of password is 100. Sliders have been disabled.")

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
    st.write("Welcome to the 𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐨𝐫 app!")
    st.write(
        "This application was developed by 𝐘𝐞𝐭 𝐀𝐧𝐨𝐭𝐡𝐞𝐫 𝐂𝐨𝐝𝐢𝐧𝐠 𝐂𝐥𝐮𝐛 (𝐘𝐀𝐂𝐂) at 𝐈𝐈𝐓 𝐏𝐚𝐥𝐚𝐤𝐤𝐚𝐝."
    )
    st.write(
        "We welcome any questions, feedback, or suggestions you might have. Your input helps us improve and innovate.\nContact us at yacc@iitpkd.ac.in"
    )
    st.write(
        "Thank you for using our Password Generator app. We hope it serves you well in generating secure and reliable passwords!"
    )
