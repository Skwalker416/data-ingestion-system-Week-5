
# **NER for Amharic Telegram Messages using XLM-Roberta**

This repository contains the implementation of a Named Entity Recognition (NER) system for extracting key entities (e.g., products, prices, locations) from Amharic Telegram messages. The project leverages **XLM-Roberta**, a multilingual transformer model, to address challenges related to low-resource languages like Amharic.

---

## **Project Overview**
### **Problem Statement**
Over 350 million people in Africa remain unbanked due to barriers like lack of credit history, limited financial literacy, and high fees. Extracting structured information from unstructured Amharic text (e.g., Telegram messages) is crucial for improving access to financial and e-commerce services.

### **Objective**
To develop and fine-tune an NER model that can:
1. Extract entities like **products**, **prices**, and **locations**.
2. Handle noisy, user-generated Amharic text.
3. Provide transparency through interpretability tools like SHAP and LIME.

---

## **Folder Structure**
```plaintext
.
├── data/
│   ├── raw/                    # Raw Telegram messages
│   ├── processed/              # Preprocessed and labeled datasets
│       ├── preprocessed_data.json
│       ├── labeled_data.conll
│
├── models/
│   ├── fine_tuned_xlm_roberta/ # Fine-tuned model checkpoint
│
├── results/
│   ├── logs/                   # Training and evaluation logs
│   ├── evaluation_results.json # Evaluation metrics
│
├── scripts/
│   ├── data_ingestion.py       # Collects messages from Telegram channels
│   ├── preprocess_data.py      # Cleans and tokenizes raw messages
│   ├── label_data.py           # Annotates data in CoNLL format
│   ├── fine_tune_ner.py        # Fine-tunes XLM-Roberta for NER
│   ├── compare_models.py       # Evaluates and compares models
│   ├── interpret_model.py      # Provides model interpretability with SHAP & LIME
```

---

## **How to Run the Project**
### **1. Environment Setup**
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

- Optional: Use a virtual environment:
  ```bash
  python -m venv env
  source env/bin/activate  # Linux/MacOS
  env\Scripts\activate   # Windows
  ```

### **2. Data Collection**
- Collect Telegram messages using `data_ingestion.py`:
  ```bash
  python scripts/data_ingestion.py
  ```

### **3. Preprocess Data**
- Clean and tokenize the raw messages:
  ```bash
  python scripts/preprocess_data.py
  ```

### **4. Label the Dataset**
- Annotate the dataset in CoNLL format:
  ```bash
  python scripts/label_data.py
  ```

### **5. Fine-Tune the Model**
- Fine-tune XLM-Roberta for NER:
  ```bash
  python scripts/fine_tune_ner.py
  ```

### **6. Evaluate and Compare Models**
- Compare performance metrics across models:
  ```bash
  python scripts/compare_models.py
  ```

### **7. Interpret the Model**
- Use SHAP and LIME for interpretability:
  ```bash
  python scripts/interpret_model.py
  ```

---

## **Key Results**
### **Fine-Tuned XLM-Roberta Metrics**
| Metric       | Value (%) |
|--------------|-----------|
| Precision    | 94        |
| Recall       | 93        |
| F1-Score     | 93.5      |

### **Model Comparison**
| **Model**        | **Precision (%)** | **Recall (%)** | **F1-Score (%)** | **Inference Time** |
|-------------------|-------------------|----------------|-------------------|---------------------|
| **XLM-Roberta**   | 94                | 93             | 93.5             | 0.4s/text           |
| **DistilBERT**    | 90                | 89             | 89.5             | 0.3s/text           |
| **mBERT**         | 88                | 87             | 87.5             | 0.5s/text           |

---

## **Future Work**
- Expand the dataset to include more diverse entities.
- Implement real-time NER for Telegram messages.
- Optimize the model for deployment on low-resource devices.

---

## **Contact**
For questions or collaborations, feel free to contact:  
**Amanuel Legesse**  
ese.amanuel.legesse@gmail.com

---
