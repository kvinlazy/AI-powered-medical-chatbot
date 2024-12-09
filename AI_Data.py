import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import requests
from datetime import datetime

# Mock data for demonstration purposes
def generate_mock_data():
    # Get today's date and generate dates from 30 days ago to today
    today = pd.to_datetime('today')
    dates = pd.date_range(start=today - pd.Timedelta(days=30), end=today)
    
    # Create random data for Message Volume, Response Time, and Referrals Processed
    data = {
        "Date": dates,
        "Message Volume": np.random.randint(50, 200, len(dates)),
        "Response Time (minutes)": np.random.randint(5, 30, len(dates)),
        "Referrals Processed": np.random.randint(10, 50, len(dates)),
    }
    return pd.DataFrame(data)

# Load data
data = generate_mock_data()

# Streamlit app
st.title("Communication Data Dashboard")

# Create three tabs: Metrics, AI Doctor, and Referrals
tab1, tab2, tab3 = st.tabs(["AI Doctor", "Referrals","Metrics"])

# Metrics tab
with tab3:

    # Message Volume
    st.subheader("Message Volume Over Time")
    fig_volume = px.line(data, x="Date", y="Message Volume", title="Message Volume Over Time")
    st.plotly_chart(fig_volume, use_container_width=True)

    # Response Times
    st.subheader("Response Times")
    fig_response = px.bar(data, x="Date", y="Response Time (minutes)", title="Average Response Times")
    st.plotly_chart(fig_response, use_container_width=True)

    # Referrals Processed
    st.subheader("Number of Referrals Processed")
    fig_referrals = px.scatter(
        data, x="Date", y="Referrals Processed", size="Referrals Processed",
        title="Referrals Processed Over Time", color="Referrals Processed"
    )
    st.plotly_chart(fig_referrals, use_container_width=True)

    # Display the data table at the bottom of the app
    st.subheader("Data Set")
    st.dataframe(data)

    # Display Summary Statistics at the bottom using an expander
    with st.expander("Summary Statistics"):
        summary = data[["Message Volume", "Response Time (minutes)", "Referrals Processed"]].describe()
        st.dataframe(summary)

# AI Doctor tab
with tab1:
    st.header("AI Doctor Chatbot")
    st.markdown("Ask any medical question, and I'll try my best to assist!")

    # Hugging Face API details
    API_URL = "https://api-inference.huggingface.co/models/distilgpt2"
    headers = {"Authorization": f"Bearer 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"}

    # Function to query Hugging Face model
    def query_huggingface(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    # Initialize session state for chat history if not already initialized
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # User input with a unique key to avoid StreamlitDuplicateElementId error
    user_input = st.text_input("Your Question:", key="user_input")  # Use a unique key for the user input box

    if user_input:
        # Add user input to session state messages
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Send input to Hugging Face model
        result = query_huggingface({"inputs": user_input})
        
        # Accessing the response safely (handling list structure)
        if isinstance(result, list) and len(result) > 0:
            ai_response = result[0].get("generated_text", "I'm not sure about that.")
        else:
            ai_response = "Sorry, something went wrong."
        
        # Add AI response to session state messages
        st.session_state.messages.append({"role": "assistant", "content": ai_response})

    # Display the chat history
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.write(f"**You:** {msg['content']}")
        else:
            st.write(f"**AI Doctor:** {msg['content']}")

    st.markdown("### Medical Disclaimer")
    st.markdown("This is an AI tool and **not a substitute for professional medical advice**.")

# Referrals tab
with tab2:
    st.header("Referral Management")
    st.markdown("Here, you can submit and manage patient referrals.")

    # Initialize session state for referrals if not already initialized
    if "referrals" not in st.session_state:
        st.session_state.referrals = []

    # Referral form
    with st.form(key="referral_form"):
        st.subheader("New Referral")
        
        name = st.text_input("Patient's Name")
        dob = st.date_input("Date of Birth", min_value=datetime(1900, 1, 1))
        hospital_number = st.text_input("Hospital Number")
        reason = st.text_area("Reason for Referral")
        
        submit_button = st.form_submit_button(label="Submit Referral")
        
        if submit_button:
            if name and dob and hospital_number and reason:
                referral = {
                    "Name": name,
                    "Date of Birth": dob,
                    "Hospital Number": hospital_number,
                    "Reason for Referral": reason,
                    "Status": "Incomplete",  # Referral starts as "Incomplete"
                    "Date Submitted": datetime.now()
                }
                st.session_state.referrals.append(referral)
                st.success("Referral submitted successfully!")
            else:
                st.error("Please fill in all fields.")

    # Display list of referrals in a table
    if st.session_state.referrals:
        st.subheader("Referral List")

        # Convert referral data into a DataFrame for display in a table
        referral_data = pd.DataFrame(st.session_state.referrals)
        
        # Display the DataFrame as a table
        st.dataframe(referral_data)

        # Option to mark referrals as "Complete"
        for idx, referral in enumerate(st.session_state.referrals):
            if referral["Status"] == "Incomplete":
                if st.button(f"Mark Referral {idx + 1} as Complete"):
                    st.session_state.referrals[idx]["Status"] = "Complete"
                    st.rerun()  # Refresh to show updated status
