import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.set_page_config(
    page_title="Email Spam Detector",
    page_icon="📧"
)

st.title("📧 Intelligent Email Spam Detection System")

st.write("Enter an email message below and click Analyze.")

message = st.text_area(
    "Email Content",
    height=200
)

if st.button("Analyze Email"):

    if message.strip() == "":
        st.warning("Please enter an email message.")
    else:

        data = vectorizer.transform([message])

        prediction = model.predict(data)

        if prediction[0] == 1:
            st.error("🚨 SPAM EMAIL DETECTED")
        else:
            st.success("✅ NOT SPAM EMAIL")