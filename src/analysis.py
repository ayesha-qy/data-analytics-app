import pandas as pd

def run_analysis():
    # Load data
    data = pd.read_csv('C:/Users/500225906/data-analytics-app/data/hi.csv')
    
    mean_value = data['Age'].mean()   	
    

    return {'mean': mean_value}