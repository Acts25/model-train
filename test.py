from sklearn.model_selection import train_test_split
from sklearn.datasets import  load_diabetes
from sklearn.metrics import mean_squared_error
import joblib
import pandas as pd

#load test data
x, y = load_diabetes(return_x_y= True)

_,x_test, _, y_test = train_test_split(x,y,test_size=0.2)

#load model
model = joblib.load("model.pkl")
y_pred = model.predict(x_test)

#Evaluate
mse = mean_squared_error(y_test, y_pred)
print(f"Model MSE: {mse:.2f}")

#print predicted versus actual
results_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(results_df.head(20))
print(f"\n... displaying {len(results_df)} total samples.")

