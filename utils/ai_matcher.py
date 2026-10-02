import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_job_match(user_skills, df):
    """Calculates match percentage between user skills and job requirements using TF-IDF & Cosine Similarity."""
    if not user_skills or df.empty:
        df['match_percentage'] = 0
        return df

    documents = [user_skills] + df['skills'].tolist()
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)

    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    df_result = df.copy()
    df_result['match_percentage'] = (cosine_sim * 100).round(1)
    return df_result.sort_values(by='match_percentage', ascending=False)

def analyze_skill_gap(user_skills, target_job_title, df):
    """Identifies matching skills and missing skills required for a target job role."""
    user_skills_set = set([s.strip().lower() for s in user_skills.split(",") if s.strip()])
    
    target_jobs = df[df['title'].str.lower() == target_job_title.lower()]
    if target_jobs.empty:
        return [], []
    
    # Collect all unique required skills for target job
    required_skills_raw = target_jobs['skills'].str.cat(sep=',').split(',')
    required_skills_set = set([s.strip().lower() for s in required_skills_raw if s.strip()])
    
    matched = list(user_skills_set.intersection(required_skills_set))
    missing = list(required_skills_set.difference(user_skills_set))
    
    return [m.title() for m in matched], [m.title() for m in missing]
