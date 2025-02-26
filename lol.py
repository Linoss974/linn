from future.backports import count

import streamlit as st

def check(password):
    count_spec_symbol = 0
    count_numbers = 0
    count_upper = 0
    count_lower = 0
    count_eng = 0
    for symbol in password:
        if symbol in 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm':
            count_eng += 1
        if symbol in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ':
            count_upper += 1
        if symbol in 'йцукенгшщзхъёфывапролджэячсмитьбю':
            count_lower += 1
        if symbol in '!@#$%^&*()_-+={}[]"/\|><~:;':
            count_spec_symbol += 1
        if symbol in '1234567890':
            count_numbers += 1

    if len(password) < 5:
        st.text('Пароль должен содержать как минимум 5 символов')
    elif '_' in password:
        st.text('Пароль должен содержать символ "_"')
    elif ',' in password:
        st.text('Пароль не должен содержать символ "."')
    elif '12345' not in password:
        st.text('Пароль должен содержать символы "25"')
    elif '0801' not in password:
        st.text('Пароль должен содержать эту дату "0801"')
    elif '!' not in password:
        st.text('Пароль должен содержать синвол "!"')
    elif count_eng > 0:
        st.text('not english')
    else:
        st.text('Ваш пароль подходит!')
        st.text('YOU WIN, DUDE')


st.title("The password game")
st.subheader("you need to guess the password")
st.markdown(':violet[Password should have at least 5 elements]')
p = st.text_input('Enter a password')

st.markdown('Welcome in FPI.LINN!')
check(p)