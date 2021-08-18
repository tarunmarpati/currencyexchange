import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('model.pkl','rb'))
def predict(df):
    data= np.array(df[["Open", "High", "Low"]])
    print(np.shape(data))
    data = np.reshape(data,(-1, 3))
    print(np.shape(data))
    predictions = model.predict(data)
    return list(predictions)
