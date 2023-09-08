from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
import os  # Add this import

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # This will render the HTML form

@app.route('/generate-graph', methods=['POST'])
def generate_graph():
    # Placeholder for the code that handles form input and generates the graph
    return "Graph generation not yet implemented."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable if it's there
    app.run(host="0.0.0.0", port=port, debug=True)
