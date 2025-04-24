import streamlit as st
import os
import pandas as pd
from resume_parser import extract_text_from_pdf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("Resume Screening System")

# Load job description
with open("job_description.txt", "r", encoding="utf-8") as f:
    job_description = f.read()

uploaded_files = st.file_uploader("Upload PDF Resumes", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    texts = []
    filenames = []

    for uploaded_file in uploaded_files:
        file_path = os.path.join("resumes", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())
        text = extract_text_from_pdf(file_path)
        texts.append(text)
        filenames.append(uploaded_file.name)

    # Add job description to list
    docs = [job_description] + texts

    # TF-IDF and similarity
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(docs)
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    results = pd.DataFrame({
        "Resume": filenames,
        "Match Score": cosine_similarities
    }).sort_values(by="Match Score", ascending=False)

    st.subheader("Ranked Resumes")
    st.dataframe(results, use_container_width=True)

    # Save results
    results.to_csv("results.csv", index=False)
    st.download_button("Download Results as CSV", data=results.to_csv(index=False), file_name="results.csv")
