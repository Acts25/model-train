from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

#LOad diabetes dataset
x,y = load_diabetes(return_x_y=True)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

#train model
model = LinearRegression()
model.fit(x_train, y_train)

#save model to file
joblib.dump(model, "model.pkl")
print("Training complete. Model saved to  model.pkl")
