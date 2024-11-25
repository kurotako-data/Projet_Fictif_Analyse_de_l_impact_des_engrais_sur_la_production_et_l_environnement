# Importation des bibliothèques nécessaires
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---- 1. Simulation des données ----
# Création de données fictives pour simuler les impacts des engrais
# Les colonnes incluent : type de culture, type d'engrais, rendement, émissions de CO₂, consommation d'eau
data = {
    "Type_de_Culture": ["Blé", "Maïs", "Soja"] * 4,
    "Type_d_Engrais": ["Organique", "Azoté", "Phosphoré", "Mixte"] * 3,
    "Rendement_kg_par_ha": [3500, 4000, 3700, 4200, 4500, 5000, 4700, 5200, 3000, 3500, 3200, 3800],
    "Emissions_CO2_kg_par_ha": [50, 120, 100, 80, 70, 180, 150, 120, 30, 90, 70, 60],
    "Consommation_Eau_m3_par_ha": [300, 500, 450, 400, 350, 600, 550, 500, 200, 400, 350, 300],
}

# Conversion en DataFrame
df = pd.DataFrame(data)

# ---- 2. Visualisation : Rendement par type d'engrais ----
# Création d'un graphique montrant les rendements pour chaque type de culture et d'engrais
plt.figure(figsize=(10, 6))
for culture in df["Type_de_Culture"].unique():
    subset = df[df["Type_de_Culture"] == culture]
    plt.plot(subset["Type_d_Engrais"], subset["Rendement_kg_par_ha"], marker='o', label=culture)

plt.title("Rendement par type d'engrais et de culture")
plt.xlabel("Type d'engrais")
plt.ylabel("Rendement (kg/ha)")
plt.legend(title="Type de Culture")
plt.grid()
plt.show()

# ---- 3. Visualisation : Émissions de CO₂ par type d'engrais ----
# Création d'un graphique montrant les émissions de CO₂ pour chaque culture et type d'engrais
plt.figure(figsize=(10, 6))
for culture in df["Type_de_Culture"].unique():
    subset = df[df["Type_de_Culture"] == culture]
    plt.plot(subset["Type_d_Engrais"], subset["Emissions_CO2_kg_par_ha"], marker='o', label=culture)

plt.title("Émissions de CO₂ par type d'engrais et de culture")
plt.xlabel("Type d'engrais")
plt.ylabel("Émissions CO₂ (kg/ha)")
plt.legend(title="Type de Culture")
plt.grid()
plt.show()

# ---- 4. Visualisation : Consommation d'eau par type d'engrais ----
# Création d'un graphique montrant la consommation d'eau pour chaque culture et type d'engrais
plt.figure(figsize=(10, 6))
for culture in df["Type_de_Culture"].unique():
    subset = df[df["Type_de_Culture"] == culture]
    plt.plot(subset["Type_d_Engrais"], subset["Consommation_Eau_m3_par_ha"], marker='o', label=culture)

plt.title("Consommation d'eau par type d'engrais et de culture")
plt.xlabel("Type d'engrais")
plt.ylabel("Consommation d'eau (m³/ha)")
plt.legend(title="Type de Culture")
plt.grid()
plt.show()

# ---- 5. Résumé des performances optimales ----
# Création d'un résumé des résultats optimisés par région
resume_optimisation = pd.DataFrame({
    "Region": ["Aride", "Fertile", "Tempérée"],
    "Engrais_Optimal": ["Organique", "Mixte", "Phosphoré"],
    "Augmentation_Rendement_%": [15, 25, 20],
    "Reduction_CO2_%": [30, 20, 15],
    "Economie_Eau_%": [40, 15, 10]
})

# Affichage du résumé
print("Résumé des recommandations optimisées :")
print(resume_optimisation)

# ---- 6. Visualisation des résultats optimaux ----
# Graphique en barres montrant les améliorations de performance par région
plt.figure(figsize=(10, 6))
categories = resume_optimisation["Region"]
augmentation_rendement = resume_optimisation["Augmentation_Rendement_%"]
reduction_co2 = resume_optimisation["Reduction_CO2_%"]
economie_eau = resume_optimisation["Economie_Eau_%"]

x = np.arange(len(categories))  # Position des étiquettes
width = 0.2  # Largeur des barres

# Création des barres
plt.bar(x - width, augmentation_rendement, width, label="Augmentation du rendement (%)")
plt.bar(x, reduction_co2, width, label="Réduction du CO₂ (%)")
plt.bar(x + width, economie_eau, width, label="Économie d'eau (%)")

# Mise en forme
plt.xlabel("Régions")
plt.ylabel("Améliorations des performances (%)")
plt.title("Améliorations des performances par choix d'engrais optimal")
plt.xticks(x, categories)
plt.legend()
plt.grid(axis="y")
plt.show()

