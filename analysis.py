# analysis.py
# ============================================================================
# Analyzing & Visualizing Synthetic Data (2000–2025) with Pandas & Matplotlib
#
# This script:
#  1. Generates a synthetic monthly passengers dataset for 2000–2025
#  2. Saves it to data/flights.csv (if not already present)
#  3. Loads, explores & cleans the data
#  4. Computes basic statistics and group-wise summaries
#  5. Produces FOUR distinct visualizations:
#     • Line chart (time series)
#     • Bar chart (category comparison)
#     • Histogram (distribution)
#     • Scatter plot (numerical relationship)
#  6. Prints findings & observations
#
# To run:
#  $ python analysis.py
#  (Ensure pandas, numpy, matplotlib installed.)
# ============================================================================

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------
# 1. Setup: synthetic data generation for 2000–2025
# ----------------------------------------------------------------------------

# Ensure data folder exists
os.makedirs('data', exist_ok=True)
csv_path = os.path.join('data', 'flights.csv')

# If the CSV doesn't exist, generate it
if not os.path.exists(csv_path):
    print("➤ Generating synthetic data for 2000–2025 → 'data/flights.csv'…")

    # 1.1 Create a date range: first of each month
    dates = pd.date_range(start='2000-01-01', end='2025-12-01', freq='MS')
    
    # 1.2 Build synthetic passenger numbers:
    #      - linear upward trend
    #      - seasonal variation (monthly sine wave)
    #      - random noise
    base = 200
    trend_per_month = 2.5
    seasonal_amplitude = 80
    noise_std = 20

    idx = np.arange(len(dates))
    trend = base + trend_per_month * idx
    # seasonal pattern: peak around mid-year
    seasonal = seasonal_amplitude * np.sin(2 * np.pi * (dates.month - 1) / 12)
    noise = np.random.normal(scale=noise_std, size=len(dates))

    passengers = (trend + seasonal + noise).round().astype(int)

    # 1.3 Assemble DataFrame
    df0 = pd.DataFrame({
        'year': dates.year,
        'month': dates.month_name(),
        'passengers': passengers
    })

    # 1.4 Save to CSV
    df0.to_csv(csv_path, index=False)
    print("✅ Synthetic flights.csv generated: "
          f"{df0.shape[0]} rows ({dates.min().date()}→{dates.max().date()})\n")

# ----------------------------------------------------------------------------
# 2. Load & Explore the Dataset (Task 1)
# ----------------------------------------------------------------------------

def load_data(path: str) -> pd.DataFrame:
    """
    Loads a CSV into a pandas DataFrame with error handling.
    """
    try:
        df = pd.read_csv(path)
        print(f"✅ Loaded '{path}': {df.shape[0]} rows, {df.shape[1]} columns\n")
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"❌ File not found: {path}")
    except pd.errors.EmptyDataError:
        raise ValueError(f"❌ No data: '{path}' is empty")
    except pd.errors.ParserError as e:
        raise ValueError(f"❌ Parsing error in '{path}': {e}")

# 2.1 Load
df = load_data(csv_path)

# 2.2 Inspect first few rows
print(">>> First 5 rows:")
print(df.head(), "\n")   # .head()

# 2.3 Structure, dtypes & missing values
print(">>> DataFrame info:")
df.info()
print("\n>>> Missing values by column:")
print(df.isnull().sum(), "\n")

# 2.4 Clean (no missing in our synthetic data, but demonstrate dropna())
df = df.dropna()
print(f"After cleaning: {df.shape[0]} rows, {df.shape[1]} columns\n")

# ----------------------------------------------------------------------------
# 3. Basic Data Analysis (Task 2)
# ----------------------------------------------------------------------------

# 3.1 Descriptive stats for 'passengers'
print(">>> Descriptive statistics (passengers):")
print(df['passengers'].describe(), "\n")

# 3.2 Group by year → compute mean, median, std
avg_by_year = (
    df
    .groupby('year')['passengers']
    .agg(['mean', 'median', 'std', 'count'])
    .rename(columns={'mean': 'avg', 'std': 'std_dev'})
    .reset_index()
)
print(">>> Yearly summary:")
print(avg_by_year, "\n")

# 3.3 Observations from grouping
print("▶️ Observation: 'avg' rises nearly linearly from 2000 to 2025, reflecting our trend.")
print("▶️ Observation: 'std_dev' shows consistent seasonal variability (~60–90 passengers).\n")

# ----------------------------------------------------------------------------
# 4. Data Visualization (Task 3)
# ----------------------------------------------------------------------------

# Prepare datetime index for time-series plotting
df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month'])
df.set_index('date', inplace=True)

# ---- 4.1 Line chart: monthly trend ----
plt.figure()
plt.plot(df.index, df['passengers'], marker='o', linewidth=1)
plt.title('Synthetic Monthly Passengers (2000–2025)')
plt.xlabel('Date')
plt.ylabel('Passengers')
plt.tight_layout()
plt.show()

# ---- 4.2 Bar chart: average per year ----
plt.figure()
plt.bar(avg_by_year['year'].astype(str), avg_by_year['avg'])
plt.title('Average Monthly Passengers by Year (2000–2025)')
plt.xlabel('Year')
plt.ylabel('Average Passengers')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---- 4.3 Histogram: distribution ----
plt.figure()
plt.hist(df['passengers'], bins=20, edgecolor='black')
plt.title('Histogram of Monthly Passenger Counts')
plt.xlabel('Passengers')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# ---- 4.4 Scatter: year vs. passengers ----
plt.figure()
scatter_df = df.reset_index()
plt.scatter(scatter_df['year'], scatter_df['passengers'], alpha=0.6)
plt.title('Scatter Plot: Year vs. Monthly Passengers')
plt.xlabel('Year')
plt.ylabel('Passengers')
plt.tight_layout()
plt.show()

# ----------------------------------------------------------------------------
# 5. Findings & Observations
# ----------------------------------------------------------------------------

print("===== Findings & Observations =====")
print("1. Upward Trend: Average monthly passengers increase steadily from 2000 → 2025.")
print("2. Seasonality: Histogram and std_dev confirm regular peaks & troughs each year.")
print("3. Variability: Scatter plot shows spread around the trend line due to seasonal + noise.")
print("====================================")
