# Automated-Resume-Parsing-and-Classification
# Resume Screening Project (Mini Project)

This is a simple resume screening tool that matches PDF resumes against a given job description using NLP techniques.

## Features
- Upload multiple PDF resumes
- Automatically extract text
- Match with job description using TF-IDF and cosine similarity
- Display ranked results
- Export results as CSV

## How to Run

1. Clone this repo or unzip the folder
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the app:

```
streamlit run app.py
```

4. Upload PDF resumes and view results.

## Folder Structure
- `app.py`: Main Streamlit app
- `resume_parser.py`: PDF text extraction logic
- `job_description.txt`: Edit this to set your job description
- `resumes/`: Place uploaded resumes here
- `results.csv`: Output of ranked resumes

