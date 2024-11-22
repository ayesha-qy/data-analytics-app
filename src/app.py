from flask import Flask, render_template
import pandas as pd


app = Flask(__name__, template_folder='C:/Users/500225906/data-analytics-app/templates') 

def run_analysis(file_path):
	data = pd.read_csv('C:/Users/500225906/data-analytics-app/data/hi.csv')
	if 'Age' in data.columns:
		mean_value = data['Age'].mean()
		return {'mean': mean_value}
	else:
		return {'error': 'Column "Age" not found in the dataset.'}


@app.route('/')
def index():
	results = run_analysis('C:/Users/500225906/data-analytics-app/data/hi.csv')
	return render_template('index.html', results=results)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
 