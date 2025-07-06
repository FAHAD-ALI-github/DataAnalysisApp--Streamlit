
# 📊 Data Analysis Web App

An interactive and intuitive web application built with **Streamlit** for performing quick, insightful data analysis. Whether you're exploring built-in datasets or uploading your own, this app helps you visualize and understand your data with ease.

---

## 🚀 Features

- 📂 Upload your own `.csv` or `.xlsx` dataset
- 📦 Choose from popular sample datasets (Iris, Titanic, Tips, Diamonds)
- 🧼 Automatic null value detection
- 📊 Summary statistics table
- 🔁 Pairplot visualization with `seaborn`
- 🔥 Interactive correlation heatmap with `plotly`

---

## 🛠 Installation

1. Clone the repository:

```bash
git clone https://github.com/FAHAD-ALI-github/DataAnalysisApp--Streamlit.git
cd DataAnalysisApp--Streamlit
```

2. (Optional but recommended) Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Start the app by running:

```bash
streamlit run app.py
```

Then open your browser and go to `http://localhost:8501`.

---

## 📦 Requirements

Make sure these Python packages are listed in your `requirements.txt`:

```txt
streamlit
pandas
numpy
seaborn
matplotlib
plotly
openpyxl  # for reading .xlsx files
```

---

## 👨‍💻 Author

**Fahad Ali**  
🔗 [LinkedIn](https://www.linkedin.com/in/fahadali1078) • [GitHub](https://github.com/FAHAD-ALI-github)

---

## 🙏 Acknowledgments

Thank you for using the Data Analysis Web App! We hope it helps streamline your data exploration process.
