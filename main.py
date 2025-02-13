import streamlit as st
st.title("Welome to Wingo Tech")
st.header("Python")

name=st.text_input("Enter Your Name:")
fname=st.text_input("Enter Your Father Name:")
adr=st.text_area("Enter Your Text:")
classdata=st.selectbox("Enter Your Graduation:",("B.Sc.","BA","B.Tech","B.Com","M.Tech",""))
classdata=st.selectbox("Enter Your Class:",("1,2,3,4,5,6,7,8,9,10,11,12"))

button=st.button("Done")
if button :
 st.markdown(f"""
    Name : {name}
    Father Name : {fname}
    address : {adr}
    class  : {classdata}""")
   