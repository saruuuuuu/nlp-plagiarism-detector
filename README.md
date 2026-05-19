# NLP-Based Multilingual Plagiarism Detection System

An AI-powered plagiarism detection system designed to identify similarities across code files, English text documents, and Telugu language text using NLP techniques, TF-IDF vectorization, and cosine similarity.

## Features

* Code plagiarism detection using token-based similarity analysis
* English text plagiarism detection using NLP preprocessing
* Telugu multilingual plagiarism detection support
* TF-IDF vectorization for feature extraction
* Cosine similarity-based plagiarism scoring
* New file comparison against existing datasets
* Automated similarity analysis across multiple document types

---

## Project Structure

```bash
.
├── code_data/          # Code files dataset
├── telugu_text/        # Telugu text dataset
├── text_data/          # English text dataset
├── code_plag.py        # Code plagiarism checker
├── telugu_plag.py      # Telugu plagiarism checker
├── text_plag.py        # English text plagiarism checker
├── new_file_input/     # Input folder for new files
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* NLP
* Scikit-learn
* TF-IDF Vectorization
* Cosine Similarity
* Machine Learning
* pandas
* NumPy

---

## How It Works

### TF-IDF Vectorization

The system converts text and source code into numerical vectors using TF-IDF to capture important tokens and word frequency patterns.

### Cosine Similarity

Similarity between files is calculated using cosine similarity scores to detect plagiarism levels.

### Multilingual Support

The system supports plagiarism detection for Telugu text using multilingual tokenization and preprocessing techniques.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/saruuuuuu/nlp-plagiarism-detector.git
cd nlp-plagiarism-detector
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### Code Plagiarism Detection

```bash
python code_plag.py
```

### Telugu Text Plagiarism Detection

```bash
python telugu_plag.py
```

### English Text Plagiarism Detection

```bash
python text_plag.py
```

---

## Future Enhancements

* Deep Learning-based semantic similarity
* Transformer-based embeddings
* Real-time plagiarism dashboard
* Support for additional regional languages
* AI-generated plagiarism reports

---

## Applications

* Academic plagiarism detection
* Code similarity analysis
* Multilingual text verification
* AI-assisted content validation
* Educational analytics systems
