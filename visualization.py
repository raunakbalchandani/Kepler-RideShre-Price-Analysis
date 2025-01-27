from keplergl import KeplerGl
import pandas as pd

def create_visualization(data_path, output_file):
    data = pd.read_csv(data_path)
    map_ = KeplerGl(height=600)
    map_.add_data(data=data, name="Rides")
    map_.save_to_html(file_name=output_file)

if __name__ == "__main__":
    create_visualization("../data/processed_rides.csv", "../results/kepler_map.html")
