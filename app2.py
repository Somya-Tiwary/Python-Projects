import streamlit as st
import json
import PyPDF2
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load job data
with open("jobs.json", "r") as f:
    jobs = json.load(f)

def extract_text(pdf_file):
    text = ""
    reader = PyPDF2.PdfReader(pdf_file)
    for page in reader.pages:
        text += page.extract_text()
    return text.lower()

def extract_skills(text):
    keywords = ["python", "java", "machine learning", "sql", "html", "css", "javascript", "react", "excel", "powerbi"]
    return [k for k in keywords if k in text]

def evaluate(resume_text):
    resume_skills = extract_skills(resume_text)
    results = []
    for job in jobs:
        required = " ".join(job["skills"])
        vectorizer = CountVectorizer().fit_transform([required, " ".join(resume_skills)])
        score = cosine_similarity(vectorizer)[0][1] * 100
        results.append((job["title"], round(score, 2), job["location"]))
    results.sort(key=lambda x: x[1], reverse=True)
    return resume_skills, results

st.set_page_config(page_title="AI Resume Evaluator & Placement Portal", page_icon="🤖")
st.title("🎓 AI Resume Evaluator & Placement Portal")
st.write("Upload your resume (PDF), and I'll analyze your skills & suggest suitable job roles!")

uploaded_file = st.file_uploader("📄 Upload Resume", type=["pdf"])

if uploaded_file:
    resume_text = extract_text(uploaded_file)
    resume_skills, job_results = evaluate(resume_text)

    st.subheader("✅ Extracted Skills")
    st.write(", ".join(resume_skills))

    st.subheader("💼 Recommended Job Matches")
    for job, score, loc in job_results:
        st.write(f"**{job}** ({loc}) — Match Score: {score}%")
        st.progress(int(score))
