# AI powered medical chatbot

## **Overview**
The **Communication Data Dashboard** is a Streamlit-based application designed to visualize communication metrics, provide an AI-powered medical chatbot, and manage patient referrals. It combines interactive data visualization, AI capabilities, and streamlined referral management into a single platform.

## **Key Features**

### 1. **Metrics Dashboard**
Visualize trends in communication data:
- **Message Volume Over Time:** Line chart displaying message traffic trends.
- **Response Times:** Bar chart showing average response times in minutes.
- **Referrals Processed:** Scatter plot illustrating processed referrals over time.
- **Summary Statistics:** Statistical insights (mean, median, standard deviation, etc.) for all metrics.

### 2. **AI Doctor Chatbot**
- Provides an AI-driven medical assistant powered by the Hugging Face `distilgpt2` model.
- Accepts user input and generates AI responses for medical inquiries.
- Displays a chat history between the user and the AI.
- Includes a **Medical Disclaimer** emphasizing that the chatbot is not a substitute for professional medical advice.

### 3. **Referral Management**
- Allows users to submit and track patient referrals.
- **Referral Form:** Collects patient details (name, date of birth, hospital number, reason for referral).
- Displays a **Referral List** with submission status.
- Enables marking referrals as "Complete" with a simple button click.

## **Technical Details**

### **Technology Stack**
- **Python:** Core programming language.
- **Streamlit:** Framework for building the web interface.
- **Plotly Express:** Data visualization library for creating interactive charts.
- **NumPy and Pandas:** Used for data manipulation and statistical analysis.
- **Hugging Face API:** Powers the AI chatbot.

### **Code Organization**
1. **Data Generation:**
   - Mock data simulates real-world communication metrics for demonstration purposes.
   - Includes dates, message volume, response time, and referrals processed.

2. **Streamlit Tabs:**
   - **Metrics Tab:** Visualizes communication data.
   - **AI Doctor Tab:** Facilitates interaction with the AI medical assistant.
   - **Referrals Tab:** Handles patient referral management.

3. **User Interaction:**
   - Persistent session state (`st.session_state`) ensures data (chat history and referrals) is retained across app interactions.
   - Intuitive forms and buttons for user inputs and actions.

4. **APIs and Authentication:**
   - Utilizes Hugging Face API with a token-based authentication mechanism for querying the chatbot.

## **How to Run the Application**

### **Prerequisites**
1. Install Python 3.7 or later.
2. Install the required libraries:
   ```bash
   pip install streamlit pandas plotly numpy requests
   ```

### **Running the App**
1. Save the code in a file named `app.py`.
2. Run the app with the command:
   ```bash
   streamlit run app.py
   ```
3. Access the app in your web browser at `http://localhost:8501`.


## **Future Enhancements**
- Integrate real-world data sources for live metrics.
- Add role-based access control for sensitive information.
- Enhance AI chatbot responses with domain-specific fine-tuning.
- Expand referral management features to include detailed analytics.


## **Disclaimer**
This application is for demonstration purposes only. The AI Doctor chatbot is not intended to provide professional medical advice and should not be relied upon as such. Always consult a qualified medical professional for health-related concerns.
