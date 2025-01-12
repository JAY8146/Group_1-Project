from flask import Flask, render_template, request
from joblib import load
import nltk
import re
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Initialize Flask app
app = Flask(__name__)



# Preprocessing function for user input
def preprocess_text(text):
    """
    Clean and preprocess input text for prediction.
    """
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    # Lowercase the text
    text = text.lower()
    # Remove special characters and numbers
    text = re.sub(r'[^a-z\s]', '', text)
    # Remove stopwords and lemmatize words
    text = ' '.join(
        lemmatizer.lemmatize(word)
        for word in text.split()
        if word not in stop_words
    )
    return text


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        # Get the input from the user
        user_message = request.form['message']
        
        # Preprocess the input text
        clean_message = preprocess_text(user_message)
        
        # Vectorize the cleaned message
        vectorized_message = vectorizer.transform([clean_message]).toarray()
        
        # Predict the vulnerability type using the model
        prediction = model.predict(vectorized_message)[0]
        
        # Decode the label to get the vulnerability type
        vulnerability_type = label_encoder.inverse_transform([prediction])[0]

        # Return the result to the admin template
        return render_template('admin.html', result=f"Detected Vulnerability Type: {vulnerability_type}")

    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)


