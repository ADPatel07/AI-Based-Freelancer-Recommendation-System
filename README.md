# 🚀 Freelancer Recommendation System

An AI-powered recommendation engine that suggests the **top 5 freelancers** for a given job based on **skills**.

---

## 📌 Features

- 🔍 Skill-based freelancer matching using **TF-IDF** & **cosine similarity**
- ⚡ Fast API built with **FastAPI**

---

## 🧠 How It Works

### ✨ Matching Logic

- Vectorizes freelancer and job skills using **TF-IDF**
- Computes similarity between job and freelancer vectors
- Ranks freelancers and returns the **top 5** best fits

---

## 📁 Project Structure

```
AI-Based-Freelancer-Recommendation-System/
├── controller.py
├── F_Recommendation.py
├── requirements.txt
└── README.md
```

---

## ⚙️ API Usage

### 🔗 Endpoint: `/recommend`

**Method**: `POST`  
**URL**: `/recommend`

### ✅ Input (JSON)
```json
{
  "required_skills": "django, keras, api development, devops",
  "budget": 300,
  "timeline_days": 10
}
```

### 📤 Output
```json
[
    {
        "id": 78,
        "name": "Freelancer_78",
        "skills": "django, keras, api development, devops",
        "hourly_rate": 62,
        "experience_years": 8,
        "match_score": 1.0
    },
    {
        "id": 85,
        "name": "Freelancer_85",
        "skills": "mongodb, docker, aws, django, api development, keras",
        "hourly_rate": 83,
        "experience_years": 8,
        "match_score": 0.645
    },
    {
        "id": 44,
        "name": "Freelancer_44",
        "skills": "keras, node.js, api development, django, tensorflow, mongodb",
        "hourly_rate": 16,
        "experience_years": 10,
        "match_score": 0.619
    },
    {
        "id": 84,
        "name": "Freelancer_84",
        "skills": "api development, devops, docker",
        "hourly_rate": 43,
        "experience_years": 8,
        "match_score": 0.619
    },
    {
        "id": 91,
        "name": "Freelancer_91",
        "skills": "linux, django, react, devops, api development, computer vision",
        "hourly_rate": 64,
        "experience_years": 3,
        "match_score": 0.595
    }
]
```

---

## ▶️ Running the Project Locally

1. **Clone the repo**
```bash
git clone https://github.com/ADPatel07/AI-Based-Freelancer-Recommendation-System.git
cd AI-Based-Freelancer-Recommendation-System
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the API**
```bash
fastapi dev controller.py
```

4. Open your browser or Postman:
```
http://127.0.0.1:8000/recommend/
```

---

## 🧪 Model Details

- **Skills**: TF-IDF vectorized
- **Matching**: Cosine similarity
- **Scoring**: skill similarity
- **Data**: Synthetic dataset of 108 freelancers

---

## 👨‍💻 Author

**Akhil Dhaduk**  
