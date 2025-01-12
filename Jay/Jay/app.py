from flask import Flask, render_template, request
from joblib import load



# Load the saved model, vectorizer, and label encoder
model = load("models/best_model.pkl")
vectorizer = load("models/vectorizer.pkl")
label_encoder = load("models/label_encoder.pkl")

