# -*- coding: utf-8 -*-
"""Jinal Final Exam Fall 2024.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1j62OZhrGjWTGN3d2Is_ryHf8vm-sPqzV
"""

# prompt: connect to google drive

from google.colab import drive
drive.mount('/content/drive')

"""# Task 1: Combine CSV Files into a Single DataFrame

**Objective:** Consolidate data from multiple CSV files into a single DataFrame
indexed by date, with each column representing the values for a specific
good.

**Instructions:**
* **You are provided with the following CSV files:**
 * Tomatoes.csv
 * Sorghum.csv
 * Potatoes (Irish).csv
 * Peas (fresh).csv
 * Oranges (big size).csv
 * Maize.csv
 * Chili (red).csv
 * Cassava.csv
 * Beans (dry).csv

* **Each file contains two columns:**
 * The first column is the date.
 * The second column represents the monthly production values for the
respective good.

* **Steps:**
 1. Load all the CSV files into separate DataFrames.
 2. Extract the name of the good from the file name (e.g., "Tomatoes"
from Tomatoes.csv ).
 3. Ensure the date column is parsed correctly as a datetime object.
 4. Combine all DataFrames into a single DataFrame: Use the date as the index,
  Each good should appear as a separate column.
 5. Align dates across all goods (fill any missing values with NaN ).
"""

# Commented out IPython magic to ensure Python compatibility.
# %cd "/content/drive/MyDrive/Final Exam 2024"

# Import Required Libraries
import pandas as pd
import glob
import os

ls

!unzip 'data.zip' -d 'data'

ls

"""## Define File Paths"""

#Define File Paths

file_paths = [
    '/content/drive/MyDrive/Final Exam 2024/data/data/Chili (red).csv',
    '/content/drive/MyDrive/Final Exam 2024/data/data/Tomatoes.csv',
    '/content/drive/MyDrive/Final Exam 2024/data/data/Beans (dry).csv',
    '/content/drive/MyDrive/Final Exam 2024/data/data/Cassava.csv',
    '/content/drive/MyDrive/Final Exam 2024/data/data/Maize.csv',
    '/content/drive/MyDrive/Final Exam 2024/data/data/Oranges (big size).csv',
    '/content/drive/MyDrive/Final Exam 2024/data/data/Peas (fresh).csv',
    '/content/drive/MyDrive/Final Exam 2024/data/data/Potatoes (Irish).csv',
    '/content/drive/MyDrive/Final Exam 2024/data/data/Sorghum.csv',
]

"""## Initialize an Empty List to Store Processed DataFrames"""

#Initialize an Empty List to Store Processed DataFrames
dataframes = []

"""## Process Each File"""

#Process Each File
for file in file_paths:
    # Load the CSV file
    df = pd.read_csv(file)

    # Extract the commodity name from the file name
    good_name = os.path.basename(file).split(".csv")[0]

    # Create a 'Date' column by combining 'mp_year' and 'mp_month'
    df['Date'] = pd.to_datetime(df['mp_year'].astype(str) + '-' + df['mp_month'].astype(str) + '-01')

    # Extract relevant columns: 'Date' and 'mp_price'
    df = df[['Date', 'mp_price']]

    # Rename 'mp_price' column to the commodity name
    df.rename(columns={'mp_price': good_name}, inplace=True)

    # Handle duplicates by grouping by 'Date' and averaging prices for the same date
    df = df.groupby('Date').mean()

    # Append the processed DataFrame to the list
    dataframes.append(df)

"""## Combine All DataFrames"""

# Combine All DataFrames
# Merge all DataFrames on the 'Date' index
combined_df = pd.concat(dataframes, axis=1)

"""## Display the Combined DataFrame"""

# Display the Combined DataFrame
# Show the first few rows of the combined DataFrame
print(combined_df.head())

"""## Save the Combined DataFrame to a CSV File"""

# Save the Combined DataFrame to a CSV File
combined_df.to_csv('Combined_Production_Data.csv')

"""# Task 2: Explore the Consolidated Data

**Objective:** Analyze the structure, quality, and patterns of the consolidated
DataFrame created in Task 1.

**Instructions:** Perform the following exploratory steps:
1. Data Overview
 * Display the shape of the DataFrame (number of rows and
columns).
 * List the column names and their respective data types.
 * Verify the date range of the index and check if it is continuous.
2. Missing Values
 * Identify missing values for each good.
 * Summarize the percentage of missing values per column.
3. Descriptive Statistics
 * Generate summary statistics for each column (mean, median, min,
max, and standard deviation).
4. Time Series Visualizations
 * Plot the time series for each good to identify trends, seasonality,
and anomalies.
 * Overlay multiple time series in a single plot to explore relationships
between goods.

## Data Overview
"""

# Data Overview
# Display the shape of the DataFrame
print(f"Shape of the DataFrame: {combined_df.shape}")

# List the column names and their respective data types
print("\nColumn Names and Data Types:")
print(combined_df.dtypes)

#Verify the date range of the index
print("\nDate Range of the Index:")
print(f"Start Date: {combined_df.index.min()}")
print(f"End Date: {combined_df.index.max()}")

# Check if the date index is continuous
print("\nIs the Date Index Continuous?")
date_diff = pd.date_range(start=combined_df.index.min(), end=combined_df.index.max(), freq='MS')
is_continuous = combined_df.index.equals(date_diff)
print("Continuous" if is_continuous else "Not Continuous")

"""## Missing Values"""

# Identify missing values for each good
print("\nMissing Values Count per Column:")
print(combined_df.isnull().sum())

# Summarize the percentage of missing values per column
missing_percentage = combined_df.isnull().mean() * 100
print("\nPercentage of Missing Values per Column:")
print(missing_percentage)

"""## Descriptive Statistics"""

# Descriptive Statistics
# Generate summary statistics for each column
print("\nDescriptive Statistics for Each Good:")
print(combined_df.describe())

"""## Time Series Visualizations

### Using Pyplot
"""

# Time Series Visualizations
import matplotlib.pyplot as plt

# Plot time series for each good to identify trends, seasonality, and anomalies
combined_df.plot(subplots=True, figsize=(15, 20), title="Time Series of Monthly Production Values for Each Good")
plt.tight_layout()
plt.show()

# Overlay multiple time series in a single plot to explore relationships between goods
combined_df.plot(figsize=(15, 8), title="Overlay of Time Series for All Goods")
plt.xlabel("Date")
plt.ylabel("Monthly Production Values")
plt.legend(title="Goods", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

"""### Using Plotly"""

# Import required libraries
import plotly.express as px
import plotly.graph_objects as go

# Define a professional color palette, replacing yellow with a more visible color
colors = [
    "#636EFA",  # Blue
    "#EF553B",  # Red
    "#00CC96",  # Green
    "#AB63FA",  # Purple
    "#FFA15A",  # Orange
    "#19D3F3",  # Cyan
    "#FF6692",  # Pink
    "#B6E880",  # Lime Green (replacing Yellow)
    "#FF97FF",  # Magenta
    "#FECB52",  # Golden Yellow (optional)
]

# Define a professional background color
background_color = "#f9f9f9"

# Individual Time Series Plot for Each Good with Unique Colors and Background
for i, column in enumerate(combined_df.columns):
    fig = px.line(
        combined_df,
        x=combined_df.index,
        y=column,
        title=f"Time Series for {column}",
        labels={"x": "Date", "y": "Monthly Production Value"},
        color_discrete_sequence=[colors[i % len(colors)]]  # Cycle through updated colors
    )
    fig.update_traces(line=dict(width=2))  # Increase line width
    fig.update_layout(
        xaxis=dict(rangeslider=dict(visible=True), title="Date"),
        yaxis=dict(title="Production Value"),
        plot_bgcolor=background_color,  # Background for the plot
        paper_bgcolor=background_color,  # Background for the entire figure
        font=dict(size=14),  # Professional font size
        title_font=dict(size=16, color="black"),  # Title font styling
        legend=dict(bgcolor=background_color),  # Legend background
        template="plotly_white"
    )
    fig.show()

# Overlayed Time Series Plot for All Goods with Unique Colors and Background
fig = go.Figure()

# Overlayed Time Series Plot for All Goods with Unique Colors and Background
fig = go.Figure()

# Use different colors for each line and increase line width
for i, column in enumerate(combined_df.columns):
    fig.add_trace(go.Scatter(
        x=combined_df.index,
        y=combined_df[column],
        mode='lines',
        name=column,
        line=dict(color=colors[i % len(colors)], width=2)  # Updated color and thicker lines
    ))

fig.update_layout(
    title="Overlay of Time Series for All Goods",
    xaxis=dict(rangeslider=dict(visible=True), title="Date"),
    yaxis=dict(title="Production Value"),
    plot_bgcolor=background_color,  # Background for the plot
    paper_bgcolor=background_color,  # Background for the entire figure
    font=dict(size=14),
    title_font=dict(size=18, color="black"),
    legend=dict(bgcolor=background_color),
    template="plotly_white",
    height=600,
    width=1000
)
fig.show()

"""### Using Seaborn"""

import seaborn as sns
import matplotlib.pyplot as plt

# Set Seaborn style
sns.set_theme(style="whitegrid")

# Define the background color
background_color = "#f9f9f9"

# Plot Individual Time Series
for column in combined_df.columns:
    plt.figure(figsize=(12, 6))
    plt.gca().set_facecolor(background_color)  # Set background color for the plot area
    plt.title(f"Time Series for {column}", fontsize=16)
    plt.xlabel("Date", fontsize=14)
    plt.ylabel("Monthly Production Value", fontsize=14)
    sns.lineplot(x=combined_df.index, y=combined_df[column], label=column, linewidth=2)
    plt.tight_layout()
    plt.show()

# Overlay All Time Series
plt.figure(figsize=(14, 8))
plt.gca().set_facecolor(background_color)  # Set background color for the plot area
plt.title("Overlay of Time Series for All Goods", fontsize=18)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Monthly Production Value", fontsize=14)

# Plot each time series with unique colors
for column in combined_df.columns:
    sns.lineplot(x=combined_df.index, y=combined_df[column], label=column, linewidth=2)

# Add legend and finalize the plot
plt.legend(title="Goods", fontsize=12)
plt.tight_layout()
plt.show()

"""## Seasonal Decompose"""

from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

# Step 1: Select a column (good) to decompose
# Replace 'Your_Column_Name' with the name of the column you want to analyze
column_to_decompose = 'Chili (red)'  # Example column; replace as needed

# Ensure the selected column is not null
ts = combined_df[column_to_decompose].dropna()

# Step 2: Perform Seasonal Decomposition
# The frequency is set to 12 for monthly data (12 months in a year)
decompose_result = seasonal_decompose(ts, model='additive', period=12)

# Step 3: Plot the Decomposed Components
plt.figure(figsize=(12, 10))

# Original Time Series
plt.subplot(411)
plt.plot(ts, label='Original', color='blue')
plt.title(f'Seasonal Decomposition of {column_to_decompose}')
plt.legend(loc='upper left')

# Trend Component
plt.subplot(412)
plt.plot(decompose_result.trend, label='Trend', color='orange')
plt.legend(loc='upper left')

# Seasonal Component
plt.subplot(413)
plt.plot(decompose_result.seasonal, label='Seasonality', color='green')
plt.legend(loc='upper left')

# Residual Component
plt.subplot(414)
plt.plot(decompose_result.resid, label='Residuals', color='red')
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()

"""# Task 3: Handle Missing Values

**Objective:** Ensure the data is complete and consistent for analysis by handling missing values appropriately.

**Instructions:**
 * Identify columns with missing values and the total number of missing
entries for each.
 * Apply an appropriate method to fill or interpolate missing values, such as:
  * Forward-fill ( ffill ).
  * Backward-fill ( bfill ).
  * Linear interpolation.
 * Justify your choice of method for handling missing data.
Task
"""

# Step 1: Identify Missing Values
# Count total missing values for each column
missing_counts = combined_df.isnull().sum()
print("Missing Values Count per Column:")
print(missing_counts)

# Calculate percentage of missing values for each column
missing_percentage = (missing_counts / len(combined_df)) * 100
print("\nPercentage of Missing Values per Column:")
print(missing_percentage)

# Handle Missing Values
  # Choice of Method:
    # - Forward-fill: Propagates the last valid observation forward.
    # - Backward-fill: Propagates the next valid observation backward.
    # - Linear interpolation: Fills missing values using linear interpolation.

# Apply linear interpolation to fill missing values
# Interpolation is chosen as it maintains data trends and smoothness
filled_df = combined_df.interpolate(method='linear', limit_direction='both', axis=0)

# Verify if all missing values are filled
print("\nMissing Values Count after Interpolation:")
print(filled_df.isnull().sum())

"""**Justification for Linear Interpolation**

Given the nature of the data (monthly production values for goods), linear interpolation is the best choice because:

1. **Preservation of Trends:** Monthly production values typically follow trends over time. Interpolation maintains these trends better than forward-fill or backward-fill.
2. **Continuity:** Linear interpolation provides a smooth transition between data points, avoiding abrupt jumps in values.
3. **Symmetry:** Unlike ffill or bfill, interpolation considers both past and future data, ensuring a balanced estimation for missing values.
4. **Applicability to Time Series:** Time series data often requires methods that preserve continuity and trends, making interpolation ideal.

Linear Interpolation is used for this dataset because:

* The data likely follows consistent trends.
* It ensures smooth, trend-preserving estimations without introducing significant biases.

# Task 4: Analyze Similarities Between Products

**Objective:** Identify which two goods have the most similar production patterns over time.

**Instructions:**
* Calculate the correlation matrix for the goods in the DataFrame.
* Identify the pair of goods with the highest correlation value.
* Provide a visualization (e.g., a heatmap of the correlation matrix) to
support your analysis.
* Justify why correlation is a meaningful metric for this comparison.
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

"""### Calculate the Correlation Matrix



"""

# Calculate the Correlation Matrix
correlation_matrix = filled_df.corr()

# Display the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

"""### Pair of Goods with the Highest Correlation"""

# Identify the Pair of Goods with the Highest Correlation
# Find the pair with the highest correlation value (excluding self-correlations)
correlation_values = correlation_matrix.unstack()
correlation_values = correlation_values[correlation_values.index.get_level_values(0) != correlation_values.index.get_level_values(1)]
most_similar_pair = correlation_values.idxmax()
highest_correlation = correlation_values.max()

print("\nMost Similar Pair of Goods:")
print(f"{most_similar_pair[0]} and {most_similar_pair[1]} with a correlation of {highest_correlation:.2f}")

"""### Visualize the Correlation Matrix (Heatmap)"""

# Step 3: Visualize the Correlation Matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", cbar=True)
plt.title("Heatmap of Correlation Matrix", fontsize=16)
plt.show()

"""### Justify Why Correlation is a Meaningful Metric for this Comparison.

**Why Use Correlation as a Metric?**

1. **Quantitative Measure of Similarity:**
 * Correlation quantifies how two goods' production values change together over time.
 * A high correlation (close to +1) indicates similar production patterns, while a low or negative correlation suggests dissimilarity.
2. **Handles Linear Relationships:** Correlation is well-suited for time series data where trends and seasonal variations are expected.
3. **Interpretability:** Correlation values provide a clear and interpretable metric to compare production patterns.

**Output:**
1. **Correlation Matrix:** Printed in the console.
2. **Most Similar Pair:** The pair of goods with the highest correlation and the correlation value.
3. **Heatmap:** Visual representation of the correlation matrix.

# Task 5: Forecasting for the Next 6 Months

**Objective:** Use different forecasting methods to predict production values for the next 6 months for a selected good.

**Instructions:**
* Select one good from the DataFrame (e.g., Tomatoes).
* Implement the following forecasting methods:
 1. **Moving Average**
   * Calculate and plot the moving average for different window sizes
(e.g., 3 months, 6 months).
   * Use the results to predict the next 6 months.
 2. **Exponential Smoothing**
   * Apply exponential smoothing methods (Simple, Holt, or Holt-
Winters, depending on the data's trend/seasonality).
   * Predict the next 6 months.
 3. **Facebook Prophet**
   * Prepare the data for Prophet by converting it to the required format
(columns: ds for date and y for values).
   * Fit a Prophet model and forecast the next 6 months.
* Visualize the forecasted results for all three methods alongside the actual
time series.
"""

# Install fbprophet (required for forecasting)
!pip install prophet

# Import Necessary Libraries
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from prophet import Prophet

"""## Moving Average Forecasting

"""

# Select a good (e.g., Tomatoes)
good_to_forecast = 'Tomatoes'

# Extract the time series for the selected good
ts = filled_df[good_to_forecast].dropna()

# Plot Moving Average for different window sizes
plt.figure(figsize=(12, 6))
plt.plot(ts, label='Original Data', color='blue')
for window in [3, 6]:
    moving_avg = ts.rolling(window=window).mean()
    plt.plot(moving_avg, label=f'{window}-Month Moving Average')
plt.title(f'Moving Average Forecasting for {good_to_forecast}')
plt.legend()
plt.show()

# Predict the next 6 months using the last moving average value
last_moving_avg = ts.rolling(window=6).mean().iloc[-1]
moving_avg_forecast = [last_moving_avg] * 6
print("Moving Average Forecast for Next 6 Months:")
print(moving_avg_forecast)

"""## Exponential Smoothing"""

# Exponential Smoothing Forecast
from statsmodels.tsa.holtwinters import ExponentialSmoothing

model = ExponentialSmoothing(ts, trend='add', seasonal=None, seasonal_periods=12).fit()
exp_forecast = model.forecast(steps=6)

# Plot with Plotly
fig = go.Figure()

# Original data
fig.add_trace(go.Scatter(
    x=ts.index, y=ts, mode='lines', name='Original Data', line=dict(color='blue', width=2)
))

# Fitted values
fig.add_trace(go.Scatter(
    x=ts.index, y=model.fittedvalues, mode='lines', name='Fitted Values', line=dict(color='orange', width=2)
))

# Forecast
forecast_dates = pd.date_range(ts.index[-1], periods=6, freq='M')
fig.add_trace(go.Scatter(
    x=forecast_dates, y=exp_forecast, mode='lines', name='Exponential Smoothing Forecast', line=dict(color='red', dash='dot', width=2)
))

fig.update_layout(
    title=f'Exponential Smoothing Forecast for {good_to_forecast}',
    xaxis=dict(rangeslider=dict(visible=True), title='Date'),
    yaxis=dict(title='Monthly Production Value'),
    plot_bgcolor='#FFF9C4',  # Light yellow background
    paper_bgcolor='#FFF9C4',
    height=600,
    width=1000
)
fig.show()

print("Exponential Smoothing Forecast for Next 6 Months:")
print(exp_forecast)

"""## Facebook Prophet

"""

# Prepare data for Prophet
prophet_df = ts.reset_index()
prophet_df.columns = ['ds', 'y']  # Prophet requires 'ds' for date and 'y' for values

# Fit the Prophet Model
model_prophet = Prophet()
model_prophet.fit(prophet_df)

# Create a future DataFrame for the next 6 months
future = model_prophet.make_future_dataframe(periods=6, freq='M')
forecast = model_prophet.predict(future)

# Plot the Forecast
fig = model_prophet.plot(forecast)
plt.title(f'Facebook Prophet Forecast for {good_to_forecast}')
plt.show()

# Display the Forecasted Values
print("Prophet Forecast for Next 6 Months:")
print(forecast[['ds', 'yhat']].tail(6))

"""##  Combine All Forecasts"""

# Combine all forecasts into a single DataFrame
forecast_dates = pd.date_range(ts.index[-1], periods=6, freq='M')
combined_forecasts = pd.DataFrame({
    'Date': forecast_dates,
    'Moving Average': moving_avg_forecast,
    'Exponential Smoothing': exp_forecast.values,
    'Prophet': forecast.loc[forecast['ds'].isin(forecast_dates), 'yhat'].values
})

print("Combined Forecasts for the Next 6 Months:")
print(combined_forecasts)

# Plot All Forecasts Together
plt.figure(figsize=(12, 6))
plt.plot(ts, label='Original Data', color='blue')
plt.plot(pd.date_range(ts.index[-1], periods=6, freq='M'), moving_avg_forecast, label='Moving Average Forecast', linestyle='--', color='green')
plt.plot(pd.date_range(ts.index[-1], periods=6, freq='M'), exp_forecast, label='Exponential Smoothing Forecast', linestyle='--', color='red')
plt.plot(pd.date_range(ts.index[-1], periods=6, freq='M'), forecast.loc[forecast['ds'].isin(forecast_dates), 'yhat'].values, label='Prophet Forecast', linestyle='--', color='purple')
plt.title(f'Forecast Comparison for {good_to_forecast}')
plt.legend()
plt.show()

"""### Using Plotly"""

import plotly.graph_objects as go
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from prophet import Prophet

# Select the good to forecast
good_to_forecast = 'Tomatoes'
ts = filled_df[good_to_forecast].dropna()

# Moving Average Forecast
window_size = 6  # Use a 6-month moving average
last_moving_avg = ts.rolling(window=window_size).mean().iloc[-1]
ma_forecast_dates = pd.date_range(ts.index[-1], periods=6, freq='M')
ma_forecast_values = [last_moving_avg] * 6

# Exponential Smoothing Forecast
exp_model = ExponentialSmoothing(ts, trend='add', seasonal=None, seasonal_periods=12).fit()
exp_forecast_values = exp_model.forecast(steps=6)

# Prophet Forecast
# Prepare data for Prophet
prophet_df = ts.reset_index()
prophet_df.columns = ['ds', 'y']
prophet_model = Prophet()
prophet_model.fit(prophet_df)

# Create future DataFrame for Prophet
prophet_future = prophet_model.make_future_dataframe(periods=6, freq='M')
prophet_forecast = prophet_model.predict(prophet_future)
prophet_forecast_values = prophet_forecast.loc[prophet_forecast['ds'].isin(ma_forecast_dates), 'yhat']

# Plotly Visualization
fig = go.Figure()

# Original Data
fig.add_trace(go.Scatter(
    x=ts.index, y=ts, mode='lines', name='Original Data', line=dict(color='blue', width=2)
))

# Moving Average Forecast
fig.add_trace(go.Scatter(
    x=ma_forecast_dates, y=ma_forecast_values, mode='lines', name='Moving Average Forecast', line=dict(color='green', dash='dot', width=2)
))

# Exponential Smoothing Forecast
fig.add_trace(go.Scatter(
    x=ma_forecast_dates, y=exp_forecast_values, mode='lines', name='Exponential Smoothing Forecast', line=dict(color='red', dash='dot', width=2)
))

# Prophet Forecast
fig.add_trace(go.Scatter(
    x=ma_forecast_dates, y=prophet_forecast_values, mode='lines', name='Prophet Forecast', line=dict(color='purple', dash='dot', width=2)
))

# Update layout with range slider and background
fig.update_layout(
    title=f'Combined Forecasts for {good_to_forecast}',
    xaxis=dict(rangeslider=dict(visible=True), title='Date'),
    yaxis=dict(title='Monthly Production Value'),
    plot_bgcolor='#FFF9C4',  # Light yellow background
    paper_bgcolor='#FFF9C4',
    font=dict(size=14),
    height=600,
    width=1000
)

fig.show()

"""### Using Seaborne"""

import seaborn as sns
import matplotlib.pyplot as plt

# Define a professional background color
background_color = "#f0fff0"

# Prepare forecast data
dates = pd.date_range(ts.index[-1], periods=6, freq='M')
moving_avg_forecast = pd.Series(moving_avg_forecast, index=dates, name="Moving Average Forecast")
exp_forecast = pd.Series(exp_forecast.values, index=dates, name="Exponential Smoothing Forecast")
prophet_forecast = pd.Series(
    forecast.loc[forecast['ds'].isin(dates), 'yhat'].values,
    index=forecast.loc[forecast['ds'].isin(dates), 'ds'],
    name="Prophet Forecast"
)

# Combine data for plotting
forecast_df = pd.DataFrame({
    "Original Data": ts,
    "Moving Average Forecast": moving_avg_forecast,
    "Exponential Smoothing Forecast": exp_forecast,
    "Prophet Forecast": prophet_forecast
})

# Plot the forecasts
plt.figure(figsize=(14, 8))
plt.gca().set_facecolor(background_color)  # Set the background color
sns.lineplot(data=forecast_df["Original Data"], label="Original Data", color="blue", linewidth=2)
sns.lineplot(data=forecast_df["Moving Average Forecast"], label="Moving Average Forecast", color="green", linestyle='--')
sns.lineplot(data=forecast_df["Exponential Smoothing Forecast"], label="Exponential Smoothing Forecast", color="red", linestyle='-.')
sns.lineplot(data=forecast_df["Prophet Forecast"], label="Prophet Forecast", color="purple", linestyle=':')

# Add title and labels
plt.title(f"Forecasting for {good_to_forecast}", fontsize=16)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Production Value", fontsize=14)
plt.legend(title="Forecast Methods", fontsize=12, loc='upper left')
plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray', alpha=0.5)
plt.tight_layout()

# Show the plot
plt.show()

"""## Task 6: Organize and Share the Project on GitHub

**Objective:** Consolidate all work and datasets into a GitHub repository to share the project.

**Instructions:** Follow these steps to create and upload the project to GitHub:

1. Create a GitHub Repository:
 * Go to GitHub.
 * Log in to your account.
 * Click on the + button in the top right corner and select New
repository.
 * Name the repository (e.g., TimeSeriesForecastingProject ).
 * Add a description.
 * Choose visibility (public or private).
 * Click Create repository.

2. Add Files via GitHub Web App:
 * Open the newly created repository on GitHub.
 * Click on the Add file button and choose Upload files.
 * Upload the following files:
  * All datasets ( Tomatoes.csv , Sorghum.csv , etc.).
  * Your Python notebook or script files.
  * Any additional documentation (e.g., README.md).
 * Commit the changes by adding a commit message and clicking
Commit changes.

# Final Deliverable

Final Deliverable: Share the GitHub repository link with me. It should have the data, .ipynb and markdown/html.
"""