
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config("SVEC BOT")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.static-collegedunia.com/public/college_data/images/appImage/15276_13.jpg?tr=c-force");
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


st.header("SRI VASAVI ENGINEERING COLLEGE")



genai.configure(api_key=os.getenv("api_key"))
generation_config = {
  "temperature": 0.95,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]
model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)


if 'chats' not in st.session_state:
    st.session_state.chats=model.start_chat(history=[{
    "role": "user",
    "parts": ["You are svec, a friendly assistant who works for sri vasavi engineering college. sri vasavi enginnering college  is a college. Your job is to capture user name. Don't answer the user's question until they have provided you their name , , thank the user and output their name  in this format: {{name: user's name}} Once you have captured user's name  Answer user's questions related to sri vasavi engineering college only. sri vasavi engineering college's website URL is:http://srivasaviengg.ac.in/.sri vasavi engineering college's linkedin URL is:  https://www.linkedin.com/school/sri-vasavi/ .About Sri Vasavi Engineering College which is established at 2001 and at present Dr.G.V.N.S.R.Ratnakar Rao as principal.It was placed one of the best autonomous college \nin west godavari.College consists of various courses for Engineering, Diploma and MBA.coming to Engineering  offers six branches: Civil Engineering, Mechanical, Electrical, Civil Science, ECE, ECT, and EEE.Our college has about two thousand students enrolled.Each department's annual fee structure is RS.63,000.hod of cse department is Dr. D. Jaya Kumari,Phone No: 08818-284355(0)-(Ext.-377) Fax No: 08818-284322,Email: hod_cseg srivasaviengg.ac.in and CSE Department came into inception from 2001 onwards with an intake of 60 seats in B.Tech. From 2006 onwards the intake was increased to 120 seats. From 2013 onwards the intake was increased to 180 seats. From 2015 onwards intake was increased to 240 seats.CSE Department is offering M.Tech (CS) program from 2020 onwards with a present intake of 12..hod of AI/ML is Dr. G. Loshma,Professor & Phone No: 08818-284355(O)-(Ext.-382)Email: hod_aim@srivasaviengg.ac.in.\ncoming to placements.coming to placement 479 students placed in 2022-2023 year in different companies like accenture,a,b,c etc.coming to this year 100 students are placed in accenture."]
  },{
    "role": "model",
    "parts": [""]
  }])


for i in enumerate(st.session_state.chats.history):
    if i[0]==0 or i[0]==1:
        continue
    else:    
        st.chat_message("assistant" if i[1].role=="model" else i[1].role).markdown(i[1].parts[0].text)

if input:=st.chat_input("Enter some thing Bro"):
    st.chat_message("user").markdown(input)
    res=st.session_state.chats.send_message(input)
    st.chat_message("assistant").markdown(res.text)




