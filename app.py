from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # This will render the HTML form

@app.route('/generate-graph', methods=['POST'])
def generate_graph():
    # Placeholder for the code that handles form input and generates the graph
    return "Graph generation not yet implemented."

if __name__ == "__main__":
    app.run(debug=True)
