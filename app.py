import streamlit as st
from predict import predict_case

st.title("POCSO Case Analysis Chatbot")

st.write("Enter case facts to predict section and outcome")

facts = st.text_area("Case Facts")

if st.button("Analyse Case"):

    section, outcome, reasons = predict_case(facts)

    st.subheader("Prediction Result")

    st.write("Predicted Section:", section)
    st.write("Predicted Outcome:", outcome)

    st.subheader("Reasons")

    for r in reasons:
        st.write("-", r)
