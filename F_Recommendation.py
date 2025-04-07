import pandas as pd
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ================================ Recommendation Function =============================================
def recommend_freelancers(job, top_n=5):

    tfidf = TfidfVectorizer()
    skill_matrix_f = tfidf.fit_transform(df_freelancers["skills"])
    skill_matrix_j = tfidf.transform([job["required_skills"]])

    similarities = cosine_similarity(skill_matrix_j, skill_matrix_f).flatten()
    
    top_indices = similarities.argsort()[::-1][:top_n]
    recommendations = df_freelancers.loc[top_indices].copy()
    recommendations["match_score"] = similarities[top_indices].round(3)
    
    return recommendations[["id", "name", "skills", "hourly_rate", "experience_years", "match_score"]].to_dict(orient='records')


# =====================  Creating Dummy freelancer ==========================
skills = [ "python", "machine learning", "deep learning", "data analysis", "api development", "react", "node.js", "flask", "django", "sql", "mongodb", "tensorflow", "keras", "natural language processing", "computer vision", "docker", "aws", "gcp", "linux", "devops"]

freelancers = []
for i in range(1, 108):
    freelancer = {
        "id": i,
        "name": f"Freelancer_{i}",
        "skills": ", ".join(random.sample(skills, k=random.randint(3, 6))),
        "experience_years": random.randint(1, 10),
        "hourly_rate": random.randint(10, 100),
        "past_projects": random.randint(1, 20)
    }
    freelancers.append(freelancer)

df_freelancers = pd.DataFrame(freelancers)