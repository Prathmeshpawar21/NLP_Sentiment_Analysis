import streamlit as st
import re
import pickle
import nltk
from nltk.tokenize import word_tokenize
from css import get_custom_css 

# Download necessary NLTK data only if not available
nltk.download('punkt', quiet=True)

# Load the trained TF-IDF vectorizer and Logistic Regression model
try:
    with open("./Model/TFIDF_vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)

    with open("./Model/logistic_regression_model.pkl", "rb") as f:
        log_reg_model = pickle.load(f)

except FileNotFoundError:
    st.error("🚨 Model or vectorizer file is missing. Please check the './Model/' directory.")
    st.stop()

# Function to preprocess and predict sentiment
def predict_sentiment(text):
    # Compile regex pattern once for efficiency
    clean_text = re.compile('[^A-Za-z0-9:)()]+').sub(' ', text).lower()
    
    # Convert text to TF-IDF features
    text_vector = vectorizer.transform([clean_text])

    # Predict sentiment
    prediction = log_reg_model.predict(text_vector)[0]

    # Convert prediction to label
    return "😊 Positive" if prediction == 1 else "😞 Negative"

# Streamlit UI
st.markdown(get_custom_css(), unsafe_allow_html=True)  # Inject CSS

st.title("🔍 Sentiment Analysis App")
st.write("Enter a review, and the model will predict if it's **positive** or **negative**.")

# User input text box
user_input = st.text_area("Enter your review here:", "")

# Predict button (centered)
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
if st.button("Analyze Sentiment"):
    if user_input.strip():
        result = predict_sentiment(user_input)
        st.write("### Prediction:", result)
    else:
        st.warning("⚠️ Please enter some text before analyzing.")
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("💡 *Developed By Prathamesh J Pawar | Date - 19 March*")
