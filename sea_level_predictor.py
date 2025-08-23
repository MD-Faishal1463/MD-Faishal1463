import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Step 1: Read the data
    df = pd.read_csv("epa-sea-level.csv")

    # Step 2: Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Step 3: Create first line of best fit (all data)
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = range(1880, 2051)
    plt.plot(years_extended, intercept + slope * pd.Series(years_extended), 'r', label="Fit: 1880-2050")

    # Step 4: Create second line of best fit (data from year 2000 onward)
    df_recent = df[df["Year"] >= 2000]
    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent_extended = range(2000, 2051)
    plt.plot(years_recent_extended, intercept_recent + slope_recent * pd.Series(years_recent_extended), 'green', label="Fit: 2000-2050")

    # Step 5: Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Step 6: Save and return plot
    plt.savefig("sea_level_plot.png")
    return plt.gca()
