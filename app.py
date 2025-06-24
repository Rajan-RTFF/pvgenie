import streamlit as st
from crew import build_crew

st.title("PVGenie - AI Assistant for Pharmacovigilance Setup")

if st.button("Generate PV Setup Kit"):
    crew = build_crew()
    results = crew.kickoff()
    st.write("✅ Results:")
    st.write(results)
