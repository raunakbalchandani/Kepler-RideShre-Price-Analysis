
# RideShare Price Analysis and Visualization with Kepler.gl

## Overview
This project analyzes and visualizes ride-sharing data from Uber and Lyft to predict prices and explore geospatial patterns using **Kepler.gl**. The project integrates machine learning models to predict fares and provides interactive maps to visualize pricing trends, surge areas, and trip routes.

---

## Features
1. Predict fare prices for Uber and Lyft rides using machine learning models.
2. Visualize geospatial patterns such as:
   - Pickup/Drop-off density.
   - Surge pricing zones.
   - Trip routes.
3. Analyze factors affecting ride fares, including distance, time, weather, and traffic.
4. Export results for interactive visualizations using Kepler.gl.

---

## Technologies Used
- **Data Processing**: Python (pandas, geopandas, NumPy).
- **Visualization**: Kepler.gl, Matplotlib.
- **Machine Learning**: Scikit-learn, XGBoost.
- **Geospatial Queries**: PostgreSQL with PostGIS.
- **APIs**: OpenWeatherMap, Google Maps API (traffic data).
- **Interactive Visualization**: Kepler.gl.

---

## Project Structure
```
RideShare_Price_Analysis_Kepler/
│
├── data/                  # Raw and processed data files
│   ├── raw_rides.csv      # Input dataset
│   ├── processed_rides.csv# Preprocessed dataset
│
├── notebooks/             # Jupyter notebooks for experimentation
│   ├── analysis.ipynb     # Data analysis and insights
│
├── src/                   # Source code for models and visualization
│   ├── preprocessing.py   # Data preprocessing scripts
│   ├── modeling.py        # Machine learning models
│   ├── visualization.py   # Kepler.gl visualization logic
│
├── results/               # Exported results and visualizations
│   ├── kepler_map.html    # Interactive visualization
│
├── config.json            # Configuration file for API keys and database credentials
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
```

---

## Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/RideShare_Price_Analysis_Kepler.git
cd RideShare_Price_Analysis_Kepler
```

### 2. Install Required Libraries
Install the dependencies listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 3. Prepare Data
- Place your raw dataset (e.g., `raw_rides.csv`) in the `data/` folder. Ensure it includes the following fields:
  - `pickup_lat`, `pickup_lon`: Pickup location coordinates.
  - `dropoff_lat`, `dropoff_lon`: Drop-off location coordinates.
  - `timestamp`: Trip time.
  - `fare`: Fare price.

### 4. Configure API Keys
- Obtain API keys for:
  - **OpenWeatherMap** for weather data.
  - **Google Maps API** for traffic data.
- Update the `config.json` file with your API keys and database credentials:
```json
{
    "openweathermap_api_key": "YOUR_API_KEY",
    "google_maps_api_key": "YOUR_API_KEY",
    "db_config": {
        "host": "localhost",
        "port": 5432,
        "user": "postgres",
        "password": "yourpassword",
        "database": "rideshare"
    }
}
```

---

## How to Run
### 1. Preprocess Data
Run the preprocessing script to clean and prepare data:
```bash
python src/preprocessing.py
```
This generates `processed_rides.csv` in the `data/` folder.

### 2. Train the Model
Train a machine learning model to predict ride fares:
```bash
python src/modeling.py
```
This outputs the model's performance metrics (e.g., MSE).

### 3. Create Visualizations
Generate interactive visualizations with Kepler.gl:
```bash
python src/visualization.py
```
This creates an HTML file (e.g., `kepler_map.html`) in the `results/` folder. Open it in your browser to explore the map.

---

## Sample Visualizations
1. **Heatmap of Pickup/Drop-off Locations**:
   ![Heatmap Example](results/heatmap_example.png)

2. **Trip Routes with Fare Pricing**:
   ![Routes Example](results/routes_example.png)

---

## Key Scripts
1. **preprocessing.py**: Cleans raw data, computes distance, and extracts time-based features.
2. **modeling.py**: Trains machine learning models for fare prediction.
3. **visualization.py**: Generates interactive visualizations using Kepler.gl.

---

## Extensions
- Add real-time predictions using live data from APIs.
- Include additional layers in Kepler.gl for weather or traffic conditions.
- Develop a web app for end-user interaction with maps and predictions.

---

## License
This project is licensed under the MIT License.

---

## Acknowledgments
- Data sourced from public ride-sharing datasets.
- Inspired by [Kepler.gl](https://github.com/keplergl/kepler.gl) for interactive visualizations.
