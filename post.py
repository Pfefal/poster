
import requests
import streamlit as st

url = 'https://httpbin.org/anything'

with st.form("my_form"):
   st.write("Magic Form")
   customMessage = st.text_input("Magic Message")
   submitted = st.form_submit_button("Submit")

   if submitted:
        data = {'name': 'Alice', 'message': 'Hello', 'customMessage': customMessage}
        response = requests.post(url, data=data)
        st.write(response.text)