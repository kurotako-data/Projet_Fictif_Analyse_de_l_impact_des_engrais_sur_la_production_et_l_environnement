import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ---- 1. Préparation des données ----
# Données fictives
data = {
    "Type de Culture": ["Blé", "Maïs", "Soja"] * 4,
    "Type d'Engrais": ["Organique", "Azoté", "Phosphoré", "Mixte"] * 3,
    "Rendement (kg/ha)": [3500, 4000, 3700, 4200, 4500, 5000, 4700, 5200, 3000, 3500, 3200, 3800],
    "Émissions CO₂ (kg/ha)": [50, 120, 100, 80, 70, 180, 150, 120, 30, 90, 70, 60],
    "Consommation Eau (m³/ha)": [300, 500, 450, 400, 350, 600, 550, 500, 200, 400, 350, 300],
}

df = pd.DataFrame(data)

# Résumé des performances optimales par région
optimized_results = pd.DataFrame({
    "Région": ["Aride", "Fertile", "Tempérée"],
    "Engrais Optimal": ["Organique", "Mixte", "Phosphoré"],
    "Augmentation Rendement (%)": [15, 25, 20],
    "Réduction CO₂ (%)": [30, 20, 15],
    "Économie Eau (%)": [40, 15, 10]
})

# ---- 2. Configuration Streamlit ----
st.title("Analyse et Optimisation des Engrais")
st.markdown("""
Cette application présente une simulation d'analyse des performances agricoles et environnementales 
pour différents types d'engrais. Les résultats incluent des recommandations pour maximiser le rendement 
tout en réduisant l'impact environnemental.
""")

# ---- 3. Visualisation interactive ----
st.header("Rendement par Type d'Engrais et de Culture")
culture = st.selectbox("Choisissez une culture", df["Type de Culture"].unique())

subset = df[df["Type de Culture"] == culture]

# Graphique matplotlib pour les rendements
fig, ax = plt.subplots()
ax.plot(subset["Type d'Engrais"], subset["Rendement (kg/ha)"], marker='o', label="Rendement")
ax.set_title(f"Rendement pour la culture : {culture}")
ax.set_xlabel("Type d'Engrais")
ax.set_ylabel("Rendement (kg/ha)")
ax.grid()
st.pyplot(fig)

# ---- 4. Tableau de recommandations ----
st.header("Recommandations par Région")
st.dataframe(optimized_results)

# ---- 5. Visualisation des performances optimisées ----
st.header("Améliorations de Performance par Région")

# Graphique interactif matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
categories = optimized_results["Région"]
yield_increase = optimized_results["Augmentation Rendement (%)"]
co2_reduction = optimized_results["Réduction CO₂ (%)"]
water_saving = optimized_results["Économie Eau (%)"]

x = np.arange(len(categories))  # Position des étiquettes
width = 0.2  # Largeur des barres

ax.bar(x - width, yield_increase, width, label="Augmentation du rendement (%)")
ax.bar(x, co2_reduction, width, label="Réduction du CO₂ (%)")
ax.bar(x + width, water_saving, width, label="Économie d'eau (%)")

# Mise en forme
ax.set_xlabel("Régions")
ax.set_ylabel("Améliorations des performances (%)")
ax.set_title("Améliorations des performances par choix d'engrais optimal")
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
ax.grid(axis="y")

st.pyplot(fig)
