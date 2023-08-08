import streamlit as st
import pandas as pd
import random as rm

alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = [0,1,2,3,4,5,6,7,8,9]
passwd = []
login = {
    "usn": [],
    "password":[]
}



def generate_password():
    pass_ = []
    for j in range(passwd_length):
        key = rm.randint(0,1)
        if key == 0:
            pass_.append(rm.choice(alphabets))
        else:
            pass_.append(rm.choice(numbers))
            
    pass_ = ''.join(map(str,pass_))
            
    return pass_



st.header("Login password Generator")
st.subheader("Unleash Unique Passwords")
st.divider()
prefix = st.text_input("Enter prefex of USN",placeholder='1ms21ci',max_chars=7)
students = st.slider('Number of Students', 0, 300, 75)
password_length = st.slider('Length of password',0,10,5)
st.divider()
if st.button("Generate"):
    number_of_passwords = students
    department_usn = prefix
    passwd_length = password_length


    for k in range(0,number_of_passwords):
        pass_ = generate_password()
        while pass_  in passwd:
            pass_ = generate_password()
        passwd.append(pass_)
        i=k+1
        if i < 10:
            login["usn"].append(department_usn+'00'+str(i))
        elif i >=10 and i<100:
            login["usn"].append(department_usn + '0' + str(i))
        else:
            login["usn"].append(department_usn + str(i))
        
    for i in range(number_of_passwords):
        password = rm.choice(passwd)
        login["password"].append(password)
        passwd.remove(password)
    df = pd.DataFrame(login)
    st.write("Generated Passwords")
    st.write(df)

    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')


    csv = convert_df(df)

    st.download_button(
        "Download CSV",
        csv,
        "file.csv",
        "text/csv",
        key='download-csv'
    )
        
