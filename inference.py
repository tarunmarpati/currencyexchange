import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

model = pickle.load(open('model.pkl','rb'))
def predict(df):
    data= np.array(df[["Open", "High", "Low"]])
    predictions = model.predict(data)
    output = model.predict(predictions)
    return list(output)
