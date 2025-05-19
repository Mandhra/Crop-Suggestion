# 🌾 Crop Suggestion System

A machine learning-based Crop Suggestion System that recommends the most suitable crop to grow based on environmental conditions like Nitrogen, Phosphorous, Potassium, Temperature, Humidity, pH, and Rainfall.

## 🚀 Project Overview

This project uses a pre-trained classification model to analyze various soil and climate parameters and suggest the most appropriate crop for cultivation. It's useful for farmers, agricultural students, and researchers to make data-driven agricultural decisions.

## 🧠 How It Works

The model is trained on an agricultural dataset containing different features such as:

- Nitrogen
- Phosphorus
- Potassium
- Temperature
- Humidity
- pH
- Rainfall

Based on these inputs, the system predicts the most suitable crop.

## 📦 Features

- Input form to provide environmental parameters.
- Predicts the best crop using a machine learning model.
- Clean and minimal UI using Streamlit.
- Easy to deploy and use.

## 🛠 Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit

## 📁 Directory Structure

```

Crop-Suggestion/
├── crop\_recommendation\_model.pkl   # Trained model
├── Crop\_recommendation.ipynb       # Notebook with model training
├── app.py                          # Streamlit web app
└── README.md                       # Project documentation

````

## 🧑‍💻 Installation and Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Mandhra/Crop-Suggestion.git
   cd Crop-Suggestion
````

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   streamlit run app.py
   ```

## 📊 Example Input

| Nitrogen | Phosphorus | Potassium | Temperature (°C) | Humidity (%) | pH  | Rainfall (mm) |
| -------- | ---------- | --------- | ---------------- | ------------ | --- | ------------- |
| 90       | 40         | 40        | 25.5             | 80           | 6.5 | 200           |

## 🎯 Output

`Suggested Crop: rice`

## 📌 Future Enhancements

* Add fertilizer recommendation based on crop.
* Include real-time weather API integration.
* User login and input history tracking.

## 📃 License

This project is licensed under the MIT License.

## 🙋‍♂️ Author

Developed by [Mandhra](https://github.com/Mandhra)

---

Feel free to contribute or raise issues to improve this project!

```

---

Let me know if you want a version with a badge, deployment instructions (e.g., Streamlit Cloud or Hugging Face), or if you want to turn this into a full project page with images.
```
