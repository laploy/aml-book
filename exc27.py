import pandas as pd

def replace_gender(x):
    gender = x['Gender']
    if gender in ['Male', '0', 'M', 'm', 'A']:
        return 'male'
    if gender in ['Female', '1', 'F', 'f', 'B']:
        return 'female'

def azureml_main(dataframe1 = None, dataframe2 = None):
    dataframe1['Sex'] = dataframe1.apply(replace_gender, axis=1)
    return dataframe1,
