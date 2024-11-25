import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulated data for the analysis
data = {
    "Crop_Type": ["Wheat", "Corn", "Soybean"] * 4,
    "Fertilizer_Type": ["Organic", "Nitrogen-based", "Phosphorus-based", "Mixed"] * 3,
    "Yield_kg_per_ha": [3500, 4000, 3700, 4200, 4500, 5000, 4700, 5200, 3000, 3500, 3200, 3800],
    "CO2_Emissions_kg_per_ha": [50, 120, 100, 80, 70, 180, 150, 120, 30, 90, 70, 60],
    "Water_Use_m3_per_ha": [300, 500, 450, 400, 350, 600, 550, 500, 200, 400, 350, 300],
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Plot 1: Yield by Fertilizer Type for each Crop
plt.figure(figsize=(10, 6))
for crop in df["Crop_Type"].unique():
    subset = df[df["Crop_Type"] == crop]
    plt.plot(subset["Fertilizer_Type"], subset["Yield_kg_per_ha"], marker='o', label=crop)

plt.title("Yield by Fertilizer Type for Different Crops")
plt.xlabel("Fertilizer Type")
plt.ylabel("Yield (kg/ha)")
plt.legend(title="Crop Type")
plt.grid()
plt.show()

# Plot 2: CO2 Emissions by Fertilizer Type for each Crop
plt.figure(figsize=(10, 6))
for crop in df["Crop_Type"].unique():
    subset = df[df["Crop_Type"] == crop]
    plt.plot(subset["Fertilizer_Type"], subset["CO2_Emissions_kg_per_ha"], marker='o', label=crop)

plt.title("CO2 Emissions by Fertilizer Type for Different Crops")
plt.xlabel("Fertilizer Type")
plt.ylabel("CO2 Emissions (kg/ha)")
plt.legend(title="Crop Type")
plt.grid()
plt.show()

# Plot 3: Water Usage by Fertilizer Type for each Crop
plt.figure(figsize=(10, 6))
for crop in df["Crop_Type"].unique():
    subset = df[df["Crop_Type"] == crop]
    plt.plot(subset["Fertilizer_Type"], subset["Water_Use_m3_per_ha"], marker='o', label=crop)

plt.title("Water Usage by Fertilizer Type for Different Crops")
plt.xlabel("Fertilizer Type")
plt.ylabel("Water Use (m³/ha)")
plt.legend(title="Crop Type")
plt.grid()
plt.show()


# Creating a summary table to synthesize the findings
summary_data = {
    "Fertilizer_Type": ["Organic", "Nitrogen-based", "Phosphorus-based", "Mixed"],
    "Average_Yield_kg_per_ha": df.groupby("Fertilizer_Type")["Yield_kg_per_ha"].mean().round(2).values,
    "Average_CO2_Emissions_kg_per_ha": df.groupby("Fertilizer_Type")["CO2_Emissions_kg_per_ha"].mean().round(2).values,
    "Average_Water_Use_m3_per_ha": df.groupby("Fertilizer_Type")["Water_Use_m3_per_ha"].mean().round(2).values,
}

# Convert to DataFrame for presentation
summary_df = pd.DataFrame(summary_data)

import ace_tools as tools; tools.display_dataframe_to_user(name="Fertilizer Impact Summary", dataframe=summary_df)

# Displaying the summary DataFrame
summary_df

# Example data for visualization of a methodology
# Creating a simple example for a dashboard-like overview of optimization

# Summary DataFrame as an example
optimized_results = pd.DataFrame({
    "Region": ["Arid", "Fertile", "Temperate"],
    "Optimal_Fertilizer": ["Organic", "Mixed", "Phosphorus-based"],
    "Yield_Increase_%": [15, 25, 20],
    "CO2_Reduction_%": [30, 20, 15],
    "Water_Saving_%": [40, 15, 10]
})

import ace_tools as tools; tools.display_dataframe_to_user(name="Optimized Fertilizer Recommendations", dataframe=optimized_results)

# Creating a bar chart to visualize the optimization results
plt.figure(figsize=(10, 6))
categories = optimized_results["Region"]
yield_increase = optimized_results["Yield_Increase_%"]
co2_reduction = optimized_results["CO2_Reduction_%"]
water_saving = optimized_results["Water_Saving_%"]

x = np.arange(len(categories))  # Label locations
width = 0.2  # Bar width

# Bars for each metric
plt.bar(x - width, yield_increase, width, label="Yield Increase (%)")
plt.bar(x, co2_reduction, width, label="CO2 Reduction (%)")
plt.bar(x + width, water_saving, width, label="Water Saving (%)")

# Add labels and formatting
plt.xlabel("Regions")
plt.ylabel("Performance Metrics (%)")
plt.title("Performance Improvements by Optimal Fertilizer Choice")
plt.xticks(x, categories)
plt.legend()
plt.grid(axis="y")
plt.show()
