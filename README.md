# Email Categorization and PII Masking

This project is a machine learning-based email classification system that categorizes emails into predefined categories (such as Incident, Request, Problem, Change) and applies PII (Personally Identifiable Information) masking to sensitive parts of the email. It uses Gradio for the web interface and scikit-learn for machine learning-based classification.

## 📋 Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)

## 🛠 Installation

Follow these steps to set up the project and install the necessary dependencies:

```bash
git clone https://github.com/aveshkh1/Email-Categorization-and-PII-Masking.git
cd Email-Categorization-and-PII-Masking
pip install -r requirements.txt
```

## 🚀 Usage

Run the Gradio interface:

```bash
python app.py
```

Then open the provided local URL in your browser to interact with the interface.

## 🧠 Model Details

- **Classifier**: RandomForestClassifier
- **Vectorizer**: TF-IDF
- **Libraries**: Scikit-learn, pandas, numpy, joblib
- **Interface**: Gradio

## ✨ Features

- PII Masking (Email, Phone Numbers, Names, etc.)
- Email Text Classification into categories
- Easy-to-use web interface built with Gradio

## 🤝 Contributing

Contributions are welcome! If you’d like to improve the project, please fork the repository and submit a pull request.

## 📜 License

This project is licensed under the MIT License.

## 👨‍💻 Authors

- Avesh Kharani
