from flask import Flask, render_template, request


# Initialize Flask app
app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

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


