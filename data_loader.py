import os
import pandas as pd

DATA_PATH = os.path.join("data", "jobs_dataset.csv")

def generate_sample_dataset():
    """Generates a realistic tech job dataset if not present."""
    if os.path.exists(DATA_PATH):
        return
    
    data = [
        {"job_id": 101, "title": "Data Scientist", "company": "TechCorp", "location": "Bangalore", "salary_lpa": 14.5, "skills": "Python, Machine Learning, SQL, Pandas, Scikit-learn", "experience_yrs": 3, "job_type": "Full-time"},
        {"job_id": 102, "title": "AI Engineer", "company": "InnovateAI", "location": "Remote", "salary_lpa": 18.0, "skills": "Python, Deep Learning, TensorFlow, PyTorch, LLMs", "experience_yrs": 4, "job_type": "Full-time"},
        {"job_id": 103, "title": "Data Analyst", "company": "AnalyticsHub", "location": "Mumbai", "salary_lpa": 8.0, "skills": "SQL, Excel, Tableau, Power BI, Python", "experience_yrs": 1, "job_type": "Full-time"},
        {"job_id": 104, "title": "Frontend Developer", "company": "WebCraft", "location": "Hyderabad", "salary_lpa": 10.5, "skills": "React, JavaScript, HTML, CSS, Tailwind", "experience_yrs": 2, "job_type": "Full-time"},
        {"job_id": 105, "title": "Backend Developer", "company": "CloudSystems", "location": "Pune", "salary_lpa": 13.0, "skills": "Python, Django, FastAPI, PostgreSQL, Docker", "experience_yrs": 3, "job_type": "Full-time"},
        {"job_id": 106, "title": "Machine Learning Engineer", "company": "NextGen ML", "location": "Bangalore", "salary_lpa": 20.0, "skills": "Python, Scikit-learn, MLOps, Docker, AWS", "experience_yrs": 5, "job_type": "Full-time"},
        {"job_id": 107, "title": "Full Stack Engineer", "company": "DevStudio", "location": "Remote", "salary_lpa": 16.0, "skills": "React, Node.js, Python, MongoDB, AWS", "experience_yrs": 4, "job_type": "Full-time"},
        {"job_id": 108, "title": "Business Intelligence Analyst", "company": "DataVision", "location": "Delhi NCR", "salary_lpa": 9.5, "skills": "SQL, Power BI, Python, Excel, Data Warehousing", "experience_yrs": 2, "job_type": "Full-time"},
        {"job_id": 109, "title": "DevOps Engineer", "company": "InfraScale", "location": "Bangalore", "salary_lpa": 15.0, "skills": "Docker, Kubernetes, AWS, CI/CD, Python", "experience_yrs": 3, "job_type": "Full-time"},
        {"job_id": 110, "title": "Junior Python Developer", "company": "StartUpX", "location": "Remote", "salary_lpa": 6.5, "skills": "Python, Django, Git, SQL, REST API", "experience_yrs": 0, "job_type": "Internship"}
    ]
    
    df = pd.DataFrame(data)
    os.makedirs("data", exist_ok=True)
    df.to_csv(DATA_PATH, index=False)
    print("Sample dataset created successfully at data/jobs_dataset.csv")

def load_data():
    """Loads the dataset into a pandas DataFrame."""
    generate_sample_dataset()
    return pd.read_csv(DATA_PATH)

if __name__ == "__main__":
    df = load_data()
    print("Dataset Preview:")
    print(df.head())