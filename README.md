# 🎬 Netflix Type Predictor

[![Streamlit App](https://static.streamlit.io/badge-github.svg)](https://netflix-type-finder.streamlit.app/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-red.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An interactive, Netflix-themed machine learning web application that predicts whether a title is a **Movie** or a **TV Show** using a **Random Forest Classifier**.

👉 **[Live Demo](https://netflix-type-finder.streamlit.app/)**

---

## ✨ Features

- **🔊 Immersive Netflix Intro**: Experience the iconic "TUDUM" intro sound and animation upon opening the app.
- **🎨 Cinematic Netflix UI**: Sleek dark mode styling matching Netflix's signature red (`#e50914`) and charcoal tones.
- **🎛️ Modern Interactive Controls**: Custom-designed pill-style selectors and increment/decrement steppers for a premium user experience.
- **🤖 Random Forest Model**: Instant predictions powered by a pre-trained Random Forest model based on:
  - **Release Year**
  - **Number of Genres**
  - **Title Word Count**
- **🎉 Celebratory Reveal**: Fun animations and balloons celebrate your prediction results.

---

## 🛠️ Tech Stack

- **Frontend / App Framework**: [Streamlit](https://streamlit.io/) (with custom HTML/CSS injection for Netflix styling)
- **Machine Learning**: [Scikit-Learn](https://scikit-learn.org/) (Random Forest Classifier)
- **Data Manipulation**: [NumPy](https://numpy.org/)
- **Audio Processing**: Base64 encoding for local MP3 playback

---

## 📁 Repository Structure

```text
├── app.py                  # Streamlit application entry point & UI code
├── netflix_intro.mp3       # Netflix intro audio file (TUDUM sound)
├── random_forest_model.pkl # Pre-trained Random Forest model
├── requirements.txt        # Python package dependencies
└── README.md               # Project documentation
```

---

## 🚀 Running Locally

To run the application on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/UDHAYA-UD/netflix_type_predictor.git
   cd netflix_type_predictor
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/UDHAYA-UD/netflix_type_predictor/issues).

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.
