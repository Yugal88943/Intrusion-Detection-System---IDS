# 🛡️ Intrusion Detection System using Soft Computing

AI-powered Intrusion Detection System (IDS) using Machine Learning and Soft Computing techniques to detect malicious network traffic in real time.

---

## 🚀 Project Overview

This project implements an intelligent Intrusion Detection System using:

- 📌 Logistic Regression
- 🧠 Artificial Neural Network (ANN)

The models are trained on the **NSL-KDD dataset** to classify network traffic as:

✅ Normal Traffic  
🚨 Attack Traffic  

An interactive **Streamlit Dashboard** is also developed for real-time predictions and model comparison.

---

# ✨ Features

- ✅ Real-time intrusion prediction
- ✅ ANN-based soft computing model
- ✅ Logistic Regression baseline model
- ✅ Interactive Streamlit dashboard
- ✅ Feature scaling & preprocessing
- ✅ Attack detection analysis
- ✅ Model comparison visualization

---

# 🛠️ Technology Stack

## 💻 Programming Language

- Python

---

## 📚 Libraries Used

### 📊 Data Processing
- pandas
- numpy

### 📈 Visualization
- matplotlib
- seaborn

### 🤖 Machine Learning
- scikit-learn
- joblib

### 🌐 Dashboard
- streamlit

---

# 🧰 Tools Used

- 📝 Jupyter Notebook
- 💻 VS Code
- 🌍 GitHub
- ☁️ Streamlit Cloud

---

# 📂 Project Structure

```text
Soft_Computing_Project/
│
├── IDS_Dashboard/
│   ├── app.py
│   ├── ann_model.pkl
│   ├── lr_model.pkl
│   ├── scaler.pkl
│   ├── columns.pkl
│
├── Project.ipynb
├── Documentation.pdf
├── requirements.txt
├── README.md
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Yugal88943/Intrusion-Detection-System---IDS
cd Soft_Computing_Project
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Run Streamlit Dashboard

```bash
streamlit run IDS_Dashboard/app.py
```

---

# 🧠 Machine Learning Models

## 📌 Logistic Regression

- Fast and efficient binary classifier
- Strong baseline performance
- High recall after threshold tuning

---

## 🧠 Artificial Neural Network (ANN)

- Soft computing approach
- Learns complex non-linear intrusion patterns
- Better attack detection capability
- Reduced false negatives

---

# 📊 Dataset

This project uses the **NSL-KDD Dataset** for intrusion detection research.

### 🚨 Attack Categories

- DoS
- Probe
- R2L
- U2R

---

# 📈 Results

| Metric | Logistic Regression | ANN |
|---|---|---|
| 🎯 Accuracy | 97.43% | 99.67% |
| 🔍 Recall | 97.53% | 99.58% |
| ❌ False Negatives | 291 | 49 |
| ⚠️ False Positives | 355 | 34 |
| 📉 AUC Score | 0.9959 | 0.9994 |

---

# 📊 Dashboard Features

- ✅ User-friendly interface
- ✅ Real-time predictions
- ✅ Model comparison
- ✅ Attack detection analysis
- ✅ Interactive visualizations

---

# 🔮 Future Improvements

- 🚀 Deep Learning-based IDS
- 🚀 Real-time packet monitoring
- 🚀 Cloud deployment
- 🚀 Explainable AI integration
- 🚀 Full 41-feature deployment

---

# 👨‍💻 Author

## Yugal  
M.Tech CSE, NIT Jalandhar

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub!