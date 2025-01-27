# Kepler-RideShre-Price-Analysis

## Overview
This project analyzes and visualizes ride-sharing data from Uber and Lyft to predict prices and explore geospatial patterns using **Kepler.gl**. The project integrates machine learning models to predict fares and provides interactive maps to visualize pricing trends, surge areas, and trip routes.

## Features
1. Predict fare prices for Uber and Lyft rides using machine learning models.
2. Visualize geospatial patterns like:
   - Pickup/Drop-off density.
   - Surge pricing zones.
   - Trip routes.
3. Analyze factors affecting ride fares such as distance, time, weather, and traffic.
4. Export and integrate results into interactive Kepler.gl visualizations.

## Technologies Used
- **Data Processing**: Python (pandas, geopandas, NumPy).
- **Visualization**: Kepler.gl, Matplotlib.
- **Machine Learning**: Scikit-learn, XGBoost.
- **Geospatial Queries**: PostgreSQL with PostGIS.
- **APIs**: OpenWeatherMap, Google Maps API (traffic data).
- **Interactive Visualization**: Kepler.gl.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Kepler-RideShre-Price-Analysis.git
   cd Kepler-RideShre-Price-Analysis
Install required Python packages:
bash
Copy
Edit
pip install -r requirements.txt

## Key Scripts

1. preprocessing.py: Cleans and preprocesses raw data.
2. modeling.py: Trains machine learning models to predict fares.
3. visualization.py: Integrates predictions into interactive Kepler.gl visualizations.


