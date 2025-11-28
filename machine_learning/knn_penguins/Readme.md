# KNN with Scaling and Cross-Validation

This project demonstrates how to apply the **k-Nearest Neighbors (KNN)** algorithm to the `penguins` dataset and explores the effects of **feature scaling** and **cross-validation**.

---

## 📊 Background

- **KNN** classifies data points based on the nearest neighbors in the feature space.
- Since KNN relies on **distances**, it is important that all features are comparable.
- **Scaling** (StandardScaler) ensures that each feature has mean = 0 and standard deviation = 1.
- **Cross-validation** checks the stability of the model across multiple data splits.

---

## ⚙️ Approach

1. **Tutorial Basis**  
   - The first version with `n=3` was built following a YouTube tutorial by **Fabian Rappert**.  
   - It refers to the **last chapter** of the tutorial.  
   - Link: [Fabian Rappert – Python Tutorial Deutsch | Komplettkurs für Anfänger](https://www.youtube.com/watch?v=e6vPt_e9sRw&t=21600s)

2. **Testing Different Neighbor Values**  
   - The values `n=1, 2, 3, 5, and 10` were tested to compare the impact of neighbor count on accuracy.

3. **Scaling**  
   - With `n=3`, the model was trained once **without scaling** and once **with StandardScaler**.

4. **Cross-Validation**  
   - Additionally, with `n=3`, a **10-fold cross-validation** was performed, combined with StandardScaler.

---

## 📈 Results

### 🔹 Accuracy without Scaling (Train/Test Split)
- n=1  → ~ 88%  
- n=2  → ~ 88%  
- n=3  → ~ 88%  
- n=5  → ~ 81%  
- n=10 → ~ 78%   

### 🔹 Accuracy with StandardScaler (Train/Test Split)
- n=3 → 100%  

### 🔹 Accuracy with StandardScaler + Cross-Validation (10-fold)
- n=3 → Average Accuracy: ~**98%**  
- Standard Deviation: ~**0.025**  

---

## 🧪 Conclusion

- Scaling is crucial for KNN, otherwise features with larger numeric ranges dominate the distance calculation.  
- Cross-validation is essential to ensure that high accuracy is not just due to a lucky split.  
- 100% accuracy is rarely sustainable – the goal is a **stable model** with high average accuracy.  

---

# Deutsch

---
# KNN mit Skalierung und Cross-Validation

Dieses Projekt zeigt, wie man den **k-Nearest Neighbors (KNN)** Algorithmus auf den `penguins`-Datensatz anwendet und dabei die Effekte von **Feature-Skalierung** und **Cross-Validation** untersucht.

---

## 📊 Hintergrund

- **KNN** klassifiziert Datenpunkte basierend auf den nächsten Nachbarn im Merkmalsraum.
- Da KNN auf **Abständen** basiert, ist es wichtig, dass alle Features vergleichbar sind.
- **Skalierung** (StandardScaler) sorgt dafür, dass jedes Feature Mittelwert = 0 und Standardabweichung = 1 hat.
- **Cross-Validation** prüft die Stabilität des Modells über mehrere Datenaufteilungen hinweg.

---

## ⚙️ Vorgehensweise

1. **Tutorial-Basis**  
   - Die erste Version mit `n=3` wurde nach einem YouTube-Tutorial von **Fabian Rappert** gebaut.  
   - Es handelt sich um das **letzte Kapitel** des Tutorials.  
   - Link: [Fabian Rappert – Python Tutorial Deutsch | Komplettkurs für Anfänger](https://www.youtube.com/watch?v=e6vPt_e9sRw&t=21600s)

2. **Tests mit verschiedenen Nachbarn**  
   - Anschließend wurden die Werte `n=1, 2, 3, 5 und 10` getestet, um die Auswirkungen der Nachbaranzahl auf die Genauigkeit zu vergleichen.

3. **Skalierung**  
   - Mit `n=3` wurde das Modell einmal **ohne Skalierung** und einmal **mit StandardScaler** trainiert.  

4. **Cross-Validation**  
   - Zusätzlich wurde mit `n=3` eine **10-fache Cross-Validation** durchgeführt, kombiniert mit StandardScaler.  

---

## 📈 Ergebnisse

### 🔹 Genauigkeit ohne Skalierung (Train/Test-Split)
- n=1  → ca. 88%  
- n=2  → ca. 88%  
- n=3  → ca. 88%  
- n=5  → ca. 81%  
- n=10 → ca. 78%  

### 🔹 Genauigkeit mit StandardScaler (Train/Test-Split)
- n=3 → 100%  

### 🔹 Genauigkeit mit StandardScaler + Cross-Validation (10-fach)
- n=3 → Durchschnittliche Accuracy: ca. **98%**  
- Standardabweichung: ca. **0.025**  

---

## 🧪 Fazit

- Skalierung ist bei KNN entscheidend, da sonst Features mit großen Zahlenwerten dominieren.  
- Cross-Validation ist wichtig, um sicherzustellen, dass die hohe Genauigkeit nicht nur Zufall bei einem Split ist.  
- 100% Accuracy ist selten dauerhaft erreichbar – Ziel ist ein **stabiles Modell** mit hoher Durchschnittsgenauigkeit.  

---