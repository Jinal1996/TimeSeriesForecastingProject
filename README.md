# Time Series Forecasting Project
A comprehensive time series analysis and forecasting project focusing on production patterns of various goods. Includes exploratory data analysis, correlation analysis, and predictions using methods like Moving Average, Exponential Smoothing, and Facebook Prophet. Interactive visualizations and insights included.

## Overview
This project analyzes and forecasts the production patterns of various goods using time series techniques. It explores similarities between goods, handles missing values, and predicts production values for the next six months using multiple forecasting methods.

## Objectives
1. Identify production trends and similarities between goods.
2. Handle missing values to ensure data consistency.
3. Forecast production for the next six months using:
   * Moving Average
   * Exponential Smoothing
   * Facebook Prophet

## Repository Structure
TimeSeriesForecastingProject/
├── datasets/
│   ├── Tomatoes.csv
│   ├── Sorghum.csv
│   └── ...
├── scripts/
│   ├── forecasting_script.py
│   └── forecasting_notebook.ipynb
├── visualizations/
│   ├── heatmap_correlation.png
│   ├── moving_avg_forecast.png
│   └── ...
├── README.md
└── LICENSE (optional)

## Methods Used
### 1. Data Preprocessing
* **Handling Missing Values:** Linear interpolation to preserve trends.
* **Similarity Analysis:** Correlation matrix and heatmap visualization.

### 2. Forecasting Techniques
 * **Moving Average:** Forecast based on a 3-month and 6-month moving average.
 * **Exponential Smoothing:** Trend-adjusted smoothing to predict future production.
 * **Facebook Prophet:** Advanced model accounting for trends and seasonality.
    
## Results
1. **Correlation Analysis:**
   - Most Similar Pair of Goods: Peas (fresh) and Potatoes (Irish) with a correlation of 0.74
   - Visualized through a heatmap.
2. **Forecasting:**
   - Predictions for the next 6 months using all methods.
     - Moving Average Forecast for Next 6 Months: [383.0909041058931, 383.0909041058931, 383.0909041058931, 383.0909041058931, 383.0909041058931, 383.0909041058931]
     - Exponential Smoothing Forecast for Next 6 Months: [2016-01-01  368.303280, 2016-02-01  368.803712, 2016-03-01  369.304144, 2016-04-01  369.804576, 2016-05-01  370.305008,  2016-06-01  370.805440]
     - Prophet Forecast for Next 6 Months: [96  2015-12-31  388.284137, 97  2016-01-31  495.980508, 98  2016-02-29  400.669893, 99  2016-03-31  434.920036, 100 2016-04-30  431.211122, 101 2016-05-31  417.236700]
   - Visualized with interactive Plotly graphs and static Seaborn plots.

## Requirements
- Python 3.8+, Google Colab
- Libraries:
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `statsmodels`
  - `prophet`
  - `plotly`

## How to Run
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Jinal1996/TimeSeriesForecastingProject.git
   cd TimeSeriesForecastingProject
2. **Install Dependencies:**
   pip install -r requirements.txt
   * **Dependencies:**
      * pandas: Data manipulation and analysis.
      * matplotlib: Plotting static visualizations like line charts and decomposition.
      * seaborn:	Creating heatmaps and styled plots for correlation analysis.
      * plotly: Interactive visualizations with range sliders and custom backgrounds.
      * statsmodels:	Statistical models for time series analysis (e.g., Exponential Smoothing, decomposition).
      * prophet:	Advanced forecasting for trends and seasonality (formerly fbprophet).
3. **Run the Analysis:**
   * Jupyter Notebook: jupyter notebook forecasting_notebook.ipynb
   * Python Script: python scripts/forecasting_script.py

## Visualizations
* Correlation Heatmap: Highlights relationships between goods.
* Forecasting Plots: Moving average, exponential smoothing, and Prophet forecasts visualized with Pyplot, Plotly with range slider and Seaborne.

## License
This project is licensed under the MIT License.

## Contact
For questions or contributions, feel free to reach out:
* Name: Jinal Patel
* Email: jinalpat06@gmail.com
* GitHub: Jinal1996
