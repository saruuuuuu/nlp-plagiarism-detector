
# Plagiarism Checker

This project is a plagiarism detection tool that checks for plagiarism within files located in different data folders. It supports checking plagiarism for code files, Telugu text files, and English text files using **TF-IDF vectorization** and **cosine similarity**. The system allows users to input new files, and the tool will check the new file for plagiarism against the existing database of files in the respective folders.

## Folder Structure

The project has the following folder structure:

```
.
├── code_data       # Folder containing code files for code plagiarism checking
├── telugu_text     # Folder containing Telugu text files for Telugu text plagiarism checking
├── text_data       # Folder containing English text files for English text plagiarism checking
├── code_plag       # Python code for detecting plagiarism in code files
├── telugu_plag     # Python code for detecting plagiarism in Telugu text files
├── text_plag       # Python code for detecting plagiarism in English text files
├── new_file_input  # Input folder where new files are placed for checking plagiarism
└── README.md       # Project documentation
```

## Models Used

This plagiarism checker uses:
- **TF-IDF (Term Frequency - Inverse Document Frequency) Vectorization** to convert text and code into numerical features.
- **Cosine Similarity** to measure the similarity between files.

## Features

- Plagiarism detection for **code files** in `code_data` using `code_plag`.
- Plagiarism detection for **Telugu text files** in `telugu_text` using `telugu_plag`.
- Plagiarism detection for **English text files** in `text_data` using `text_plag`.
- **New file support**: You can input a new file into the appropriate folder, and the system will check for plagiarism against all existing files in that folder.

## How to Use

1. Clone this repository:

   ```bash
   git clone https://github.com/your-repo/plagiarism-checker.git
   cd plagiarism-checker
   ```

2. Place the new file you want to check in the appropriate folder (`code_data`, `telugu_text`, or `text_data`).

3. Run the respective plagiarism checker script for the file type:

   - For code files (stored in `code_data`):
     ```bash
     python code_plag.py
     ```

   - For Telugu text files (stored in `telugu_text`):
     ```bash
     python telugu_plag.py
     ```

   - For English text files (stored in `text_data`):
     ```bash
     python text_plag.py
     ```

4. **New File Support**: 
   If you have a new file to check for plagiarism:
   
   - Place the new file in the appropriate folder (e.g., `code_data` for code, `telugu_text` for Telugu text, or `text_data` for English text).
   - Run the corresponding script as mentioned above.
   - The script will compare the new file against all other files in the respective folder and output plagiarism detection results.

## Dependencies

This project requires the following Python libraries:

- `scikit-learn`
- `numpy`
- `pandas`

You can install the dependencies using pip:

```bash
pip install -r requirements.txt
```

## How It Works

1. **TF-IDF Vectorization**: 
   The text or code files are converted into vectors using the TF-IDF vectorizer, which helps in representing the importance of each word or token across the files.
   
2. **Cosine Similarity**:
   The vectors of files are compared using cosine similarity to calculate the degree of similarity between them.

3. **New File Checking**:
   When a new file is added to the appropriate folder, the system updates its model and checks the new file for plagiarism by calculating its similarity to all other files in the folder. The results will indicate the similarity score, allowing for the detection of plagiarism.

## Example

For example, to check plagiarism in a new code file:

1. Place the new code file in the `code_data` folder.
2. Run the `code_plag.py` script:

   ```bash
   python code_plag.py
   ```

3. The script will output the plagiarism results, showing the similarity between the new code file and the existing code files in `code_data`.

