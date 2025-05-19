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
- Clean and minimal UI using Flask.
- Easy to deploy and use.

## 🛠 Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Flask

## 📁 Directory Structure

```

Crop-Suggestion/
├── templates/index.html             #HTML file for frontend
├── Vizualization                    #Folder contraining information about plots and vizualization
├── app.py                           # Flask web app
├── Crop_recommendation.pkl          # Trained model
├── encoder.pkl                      #Label encoder model
├── Crop_Recommendation.ipynb        # Notebook with model training
├── app.py                           # Streamlit web app
├── requirements.txt                 # To install dependencies
└── README.md                        # Project documentation

````

## 🧑‍💻 Installation and Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Mandhra/Crop-Suggestion.git
   cd Crop-Suggestion
   ```
   
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
   python app.py
   ```

## 📊 Example Input

| Nitrogen | Phosphorus | Potassium | Temperature (°C) | Humidity (%) | pH  | Rainfall (mm) |
| -------- | ---------- | --------- | ---------------- | ------------ | --- | ------------- |
| 90       | 40         | 40        | 25.5             | 80           | 6.5 | 200           |

## 🎯 Output

`Suggested Crop: jute`

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
