import pickle
import numpy as np
load=pickle.load(open('trained_model.sav','rb'))
input_data=(5,166,72,19,175,25.8,0.587,51)
input_data_as_numpy_array=np.asarray(input_data)
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
pred=load.predict(input_data_reshaped)
print(pred)