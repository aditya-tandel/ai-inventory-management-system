from sklearn.linear_model import LinearRegression
import numpy as np

def predict_demand(quantity_sold):
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array(quantity_sold)

    model = LinearRegression()
    model.fit(X, y)

    return int(model.predict([[6]])[0])
