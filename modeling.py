from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd

def train_model(data_path):
    data = pd.read_csv(data_path)
    X = data[['distance', 'hour']]
    y = data['fare']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = GradientBoostingRegressor()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Model MSE: {mse}")

    return model

if __name__ == "__main__":
    model = train_model("../data/processed_rides.csv")
