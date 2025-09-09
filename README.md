# 📄 Resume & Job Description Analyzer

A Streamlit app that analyzes your resume against a job description using AI.  
It extracts skills, computes match percentages, highlights missing skills, and gives actionable resume improvement suggestions.

---

## Features

- Upload your **resume** (PDF only).  
- Paste **job description**.  
- AI-powered **skills extraction and match analysis**.  
- Enter **GROQ API key** in the sidebar to enable AI analysis.  

---

## Tech Stack

- **Python 3.11+**  
- **Streamlit** – for the web interface  
- **LangChain** – for AI and LLM handling  
- **LangChain-Groq** – for connecting to Groq LLM  
- **LangChain-Community** – for PDF loader (PyPDFLoader)  
- **Matplotlib** – optional, if you add visualizations later  

---

## How to Run Locally

1. **Clone this repository**:

```bash
git clone https://github.com/your-username/resume-jd-analyzer.git
cd resume-jd-analyzer
