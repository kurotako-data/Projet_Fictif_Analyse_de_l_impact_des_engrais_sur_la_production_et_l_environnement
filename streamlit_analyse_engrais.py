import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ---- 1. Préparation des données ----
# Données fictives
# Ces données sont créées dans le but de simuler une étude sur l'impact de différents types d'engrais
# sur les rendements agricoles, les émissions de CO₂ et la consommation d'eau.
# Ce projet sert de modèle et pourrait être appliqué à des cas réels avec des données concrètes.
data = {
    "Type de Culture": ["Blé", "Maïs", "Soja"] * 4,
    "Type d'Engrais": ["Organique", "Azoté", "Phosphoré", "Mixte"] * 3,
    "Rendement (kg/ha)": [3500, 4000, 3700, 4200, 4500, 5000, 4700, 5200, 3000, 3500, 3200, 3800],
    "Émissions CO₂ (kg/ha)": [50, 120, 100, 80, 70, 180, 150, 120, 30, 90, 70, 60],
    "Consommation Eau (m³/ha)": [300, 500, 450, 400, 350, 600, 550, 500, 200, 400, 350, 300],
}

# Création du DataFrame principal pour l'analyse
df = pd.DataFrame(data)

# Données pour les recommandations optimisées par région
optimized_results = pd.DataFrame({
    "Région": ["Aride", "Fertile", "Tempérée"],
    "Engrais Optimal": ["Organique", "Mixte", "Phosphoré"],
    "Augmentation Rendement (%)": [15, 25, 20],
    "Réduction CO₂ (%)": [30, 20, 15],
    "Économie Eau (%)": [40, 15, 10]
})

# ---- 2. Configuration Streamlit ----
# Titre de l'application et introduction
st.title("Analyse et Optimisation des Engrais")
st.markdown("""
Bienvenue dans cette application de simulation. **Notez que les données utilisées sont fictives** 
et sont conçues pour illustrer une approche d'analyse des performances agricoles et environnementales.
Ces principes peuvent être appliqués à des cas réels pour des décisions data-driven.
""")

# ---- 3. Visualisation interactive ----
# Visualisation du rendement par type de culture
st.header("Rendement par Type d'Engrais et de Culture")
# Sélection dynamique pour choisir une culture
culture = st.selectbox("Choisissez une culture", df["Type de Culture"].unique())

# Filtrage des données pour la culture sélectionnée
subset = df[df["Type de Culture"] == culture]

# Création du graphique des rendements avec Matplotlib
fig, ax = plt.subplots()
ax.plot(subset["Type d'Engrais"], subset["Rendement (kg/ha)"], marker='o', label="Rendement")
ax.set_title(f"Rendement pour la culture : {culture}")
ax.set_xlabel("Type d'Engrais")
ax.set_ylabel("Rendement (kg/ha)")
ax.grid()

# Affichage du graphique dans Streamlit
st.pyplot(fig)

# ---- 4. Tableau de recommandations ----
# Affichage des recommandations optimisées
st.header("Recommandations par Région")
st.markdown("""
Le tableau ci-dessous présente les recommandations optimales par région pour maximiser le rendement 
tout en réduisant les impacts environnementaux.
""")
st.dataframe(optimized_results)

# ---- 5. Visualisation des performances optimisées ----
# Graphique comparatif des améliorations des performances
st.header("Améliorations de Performance par Région")

# Préparation des données pour le graphique
categories = optimized_results["Région"]
yield_increase = optimized_results["Augmentation Rendement (%)"]
co2_reduction = optimized_results["Réduction CO₂ (%)"]
water_saving = optimized_results["Économie Eau (%)"]

x = np.arange(len(categories))  # Position des étiquettes
width = 0.2  # Largeur des barres

# Création du graphique
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x - width, yield_increase, width, label="Augmentation du rendement (%)")
ax.bar(x, co2_reduction, width, label="Réduction du CO₂ (%)")
ax.bar(x + width, water_saving, width, label="Économie d'eau (%)")

# Mise en forme du graphique
ax.set_xlabel("Régions")
ax.set_ylabel("Améliorations des performances (%)")
ax.set_title("Améliorations des performances par choix d'engrais optimal")
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
ax.grid(axis="y")

# Affichage du graphique dans Streamlit
st.pyplot(fig)

# ---- 6. Conclusion ----
# Résumé de l'application
st.markdown("""
### Conclusion
Cette simulation montre comment les données peuvent être utilisées pour optimiser les décisions 
agricoles en équilibrant les besoins de production avec des objectifs environnementaux. 

Avec des données réelles, cette approche pourrait guider les acteurs agricoles à choisir des solutions 
plus durables et efficaces, tout en améliorant les rendements. 
N'hésitez pas à explorer plus loin et à adapter cette méthodologie à des contextes spécifiques.
""")

