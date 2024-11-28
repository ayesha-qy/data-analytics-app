from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'templates'))  # Explicit template folder

def run_analysis(file_path):
    data = pd.read_csv('data/hi.csv')  # Use a relative path
    if 'Age' in data.columns:
        mean_value = data['Age'].mean()
        return {'mean': mean_value}
    else:
        return {'error': 'Column "Age" not found in the dataset.'}

@app.route('/')
def index():
    results = run_analysis('data/hi.csv')
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
