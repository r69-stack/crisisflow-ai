import streamlit as st

st.title("CrisisFlow AI")

incident = st.text_area("Enter Incident")

if st.button("Analyze"):
    st.success("Incident processed")
