import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain




# ---------------------------
st.set_page_config(page_title="Resume & JD Matcher", layout="wide")
st.title("📄 Resume & Job Description Analyzer")

# 2. File Uploads

st.header("Upload Resume")
uploaded_resume = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

resume_text = ""
if uploaded_resume:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_resume.read())
    loader = PyPDFLoader("temp_resume.pdf")
    docs = loader.load()
    resume_text = " ".join([doc.page_content for doc in docs])
    st.success("✅ Resume uploaded and text extracted.")

# 3. Job Description
st.header("Upload / Paste Job Descritpion")
job_description = st.text_area("Paste Job Description here:")

# uploaded_jd = st.file_uploader("Or Upload JD (PDF/TXT)", type=["pdf", "txt"])
# if uploaded_jd:
#     if uploaded_jd.type == "application/pdf":
#         with open("temp_jd.pdf", "wb") as f:
#             f.write(uploaded_jd.read())
#         loader = PyPDFLoader("temp_jd.pdf")
#         docs = loader.load()
#         job_description = " ".join([doc.page_content for doc in docs])
#     else:  # txt
#         job_description = uploaded_jd.read().decode("utf-8")
#     st.success("✅ Job description uploaded and extracted.")

# 4. Display extracted text

if resume_text and job_description:
    st.subheader("📑 Extracted Documents")
    col1, col2 = st.columns(2)

    with col1:
        st.write("### Resume")
        st.write(resume_text[:1200] + "..." if len(resume_text) > 1200 else resume_text)

    with col2:
        st.write("### Job Description")
        st.write(job_description[:1200] + "..." if len(job_description) > 1200 else job_description)

# 4. LLM Setup

st.sidebar.header("🔑 API Key Settings")
groq_api_key = st.sidebar.text_input("Enter your GROQ API Key:", type="password")

if groq_api_key:
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=groq_api_key,
        temperature=0.2
    )

    prompt_template = PromptTemplate(
        input_variables=["resume", "job"],
        template="""
You are a smart career assistant 🤖.

Given the following Resume and Job Description:
---
Resume: {resume}
---
Job Description: {job}
---

1. Extract top **skills** from the resume.
2. Extract key **requirements** from the job description.
3. Show **skills match %** between resume and JD.
4. List **missing skills** (resume doesn’t have but JD requires).
5. Give 3 **actionable improvements** to make the resume better.

Respond in a structured way with bullet points.
        """
    )

    chain = LLMChain(llm=llm, prompt=prompt_template)

    # ---------------------------
    # 6. Run Analysis
    # ---------------------------
    if st.button("🚀 Analyze Resume vs JD"):
        with st.spinner("Analyzing with AI..."):
            result = chain.run({"resume": resume_text, "job": job_description})
        st.subheader("📊 AI Analysis Result")
        st.write(result)


    
