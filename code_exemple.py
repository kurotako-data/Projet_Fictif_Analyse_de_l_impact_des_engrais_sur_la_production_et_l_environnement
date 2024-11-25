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

