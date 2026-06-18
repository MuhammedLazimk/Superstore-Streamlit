import streamlit as st


st.title("Hai , Muhammed Lazim")


st.header("About Me",divider="blue")
st.write('My name is Muhammed Lazim. I am a student at Medhavi Skill University. I am interested in technology, coding, and data analysis. I enjoy learning new skills and completing academic projects. I am hardworking, dedicated, and always eager to improve my knowledge and achieve my career goals successfully.')
st.markdown("---")


st.header("Skills",divider="green")
st.markdown(
"- **Python** — pandas, NumPy, Matplotlib"
"\n- Streamlit dashboard development"
"\n- SQL and database design")
st.markdown("---")


st.header("Contact ",divider="orange")
st.write("""
Email: mhdlzm@gmail.com

Phone: +91 1234567890
""")
st.markdown("---")

st.subheader('Favourite Snippet', help='A pattern I use often')
st.code("""
import pandas as pd
df = pd.read_csv("data.csv")
print(df.describe())
""", language="python")

st.latex(r'E = mc^{2}')

st.markdown('---')
st.caption('Built with Streamlit · Day 1 Project · 2024')