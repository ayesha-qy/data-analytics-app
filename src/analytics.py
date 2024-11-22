import pandas as pd

def run_analysis():
    
    data = pd.read_csv('data/german_credit_data.csv')
    
    # Perform analysis (e.g., calculate mean)
    data = data.astype({'Sex': 'category',
                  'Housing': 'category',
                  'Saving accounts': 'category',
                  'Checking account': 'category',
                  'Purpose': 'category'})
    data.info()
    data.describe(include='category')

    return {'mean': mean_value}
