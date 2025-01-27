import pandas as pd
from geopy.distance import geodesic

def preprocess_data(file_path):
    data = pd.read_csv(file_path)
    data['distance'] = data.apply(
        lambda row: geodesic((row['pickup_lat'], row['pickup_lon']), (row['dropoff_lat'], row['dropoff_lon'])).km, axis=1
    )
    data['hour'] = pd.to_datetime(data['timestamp']).dt.hour
    return data

if __name__ == "__main__":
    data = preprocess_data("../data/raw_rides.csv")
    data.to_csv("../data/processed_rides.csv", index=False)
