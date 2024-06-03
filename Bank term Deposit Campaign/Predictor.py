#import liraries
import pandas as pd

def wrangle(filepath):
    df = pd.read_csv(filepath, delimiter=";")
    
    df.drop(columns="duration", inplace=True)
    
    return df

def make_my_prediction(data_filepath, model_filepath):
    #Wrangle data file
    X_test = wrangle(data_filepath)
    
    #Load model
    with open("GSclassificaiton_model.pkl", "rb") as f:
        model = pickle.load(f)
        
    #Generate Predictions
    y_test_pred = model.predict(X_test)
    
    y_test_pred = pd.Series(y_test_pred, index=X_test.index, name="Subscribed to Campaign")
    return y_test_pred
