

# AI-Recommendation-Logic
# 🎬 AI Movie Recommendation System 

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/AI-Recommendation-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Project-DecodeLabs-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">
  <img src="https://img.shields.io/github/license/vaishnavibansal222-ctrl/AI-Recommendation-System?style=for-the-badge">
</p>

<p align="center">
An intelligent movie recommendation system built using <b>Python</b> that recommends movies based on
<b>Genre, Language, Mood, and IMDb Rating</b> using a rule-based AI similarity matching algorithm.
</p>

---

# 📖 Overview

Finding the perfect movie can be difficult.

This project implements a simple **Artificial Intelligence Recommendation System** that understands a user's preferences and recommends the most suitable movies using a similarity scoring algorithm.

The system also stores recommendation history and allows users to rate the recommended movies.

---

# ✨ Features

✅ Rule-Based AI Recommendation Logic

✅ Similarity Score Calculation

✅ Personalized Movie Suggestions

✅ Top 5 AI Recommendations

✅ Movie Dataset using CSV

✅ Recommendation History

✅ User Rating System

✅ Error Handling

✅ Interactive Console Interface

✅ Clean and Modular Python Code

---

# 🧠 AI Recommendation Logic

The recommendation score is calculated using four user preferences.

| Preference | Score |
|------------|-------|
| Genre Match | +40 |
| Language Match | +25 |
| Mood Match | +20 |
| IMDb Rating Match | +15 |

Maximum Similarity Score

```text
40 + 25 + 20 + 15 = 💯 100%
```

Movies with higher similarity scores are ranked first.

---

## 📂 Project Structure

```mermaid
flowchart TD

    A["📁 AI-Recommendation-System"] --> B["🐍 PROJECT 3 AI RECOMMENDATION LOGIC.py"]
    A --> C["🎬 movies.csv"]
    A --> D["📜 recommendation_history.csv"]
    A --> E["📖 README.md"]
    A --> F["📷 screenshots/"]

    F --> G["🏠 home.png"]
    F --> H["🤖 recommendation.png"]
    F --> I["📜 history.png"]

    B --> J["📂 Dataset Management"]
    B --> K["🎯 Recommendation Engine"]
    B --> L["📝 History Management"]
    B --> M["🖥️ Console Menu"]

    J --> J1["Create Dataset"]
    J --> J2["Load Movies"]

    K --> K1["User Preferences"]
    K --> K2["Similarity Score"]
    K --> K3["Top 5 Recommendations"]

    L --> L1["Save Recommendation History"]
    L --> L2["View Recommendation History"]

    M --> M1["Get Recommendations"]
    M --> M2["View Dataset"]
    M --> M3["About Project"]
    M --> M4["Exit"]
```

# 🎥 Sample Dataset

| Movie | Genre | Language | Mood | IMDb |
|--------|--------|-----------|------|------|
| Inception | Sci-Fi | English | Exciting | ⭐ 8.8 |
| Interstellar | Sci-Fi | English | Inspirational | ⭐ 8.7 |
| Titanic | Romance | English | Emotional | ⭐ 7.8 |
| Dangal | Sports | Hindi | Motivational | ⭐ 8.5 |
| Avengers Endgame | Action | English | Exciting | ⭐ 8.4 |
| Coco | Animation | English | Emotional | ⭐ 8.4 |

---

# ⚙️ How It Works

```
User Input
     │
     ▼
Enter Preferences
     │
     ▼
Load Dataset
     │
     ▼
Calculate Similarity Score
     │
     ▼
Sort Movies
     │
     ▼
Top 5 Recommendations
     │
     ▼
User Rating
     │
     ▼
Save Recommendation History
```

---

# 🚀 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/vaishnavibansal222-ctrl/AI-Recommendation-System.git
```

## 2️⃣ Navigate to the Project Directory

```bash
cd AI-Recommendation-System
```
## 3️⃣ Run the Application

```bash
python "PROJECT 3 AI RECOMMENDATION LOGIC.py"
```

# 🖥️ Application Menu

```
1. Get Recommendations

2. View Dataset

3. Recommendation History

4. About Project

5. Exit
```

---

# 🎯 Example

### User Preferences

```
Genre      : Action

Language   : English

Mood        : Exciting

Minimum Rating : 8
```

### AI Output

```
1. Avengers Endgame
Similarity : 100%

2. Spider-Man No Way Home
Similarity : 100%

3. The Dark Knight
Similarity : 80%

4. Doctor Strange
Similarity : 65%

5. Avatar
Similarity : 55%
```

---

# 📊 Recommendation Process

```mermaid
flowchart LR

A[User Input] --> B[Load Dataset]

B --> C[Calculate Similarity]

C --> D[Sort by Score]

D --> E[Top 5 Movies]

E --> F[User Rating]

F --> G[Save History]
```

---

# 🛠️ Technologies Used

- 🐍 Python 3
- 📄 CSV
- 📅 Datetime Module
- 📂 OS Module
- 🤖 Rule-Based AI
- 📊 Similarity Matching Algorithm

---

# 📈 Future Improvements

- Machine Learning Recommendation Engine

- Collaborative Filtering

- Content-Based Recommendation

- Hybrid Recommendation System

- Movie Posters

- GUI using Tkinter

- Streamlit Web App

- Flask API

- Database Integration (SQLite/MySQL)

- User Login System

---

# 📷 Screenshots



# RECOMMENDATION 
<img width="1382" height="995" alt="Screenshot 2026-07-27 103626" src="https://github.com/user-attachments/assets/30d866ed-db10-4341-8629-fbd9312e5121" />
<img width="1241" height="992" alt="Screenshot 2026-07-27 103648" src="https://github.com/user-attachments/assets/09c52186-de1c-4f3d-9535-38d72beec4c7" />


# RECOMMDNDATION HISTORY 

<img width="1110" height="996" alt="Screenshot 2026-07-27 103751" src="https://github.com/user-attachments/assets/63921362-c606-4cc1-ad2f-fc098f7a9085" />

# 🌟 Highlights

- Beginner Friendly
- Modular Code
- AI-Based Logic
- Real Dataset
- Easy to Customize
- Good for College Projects
- Internship Ready

---

# 👩‍💻 Developer

**Bhaumik Bisht**

🎓 DecodeLabs Artificial Intelligence Internship

🤖 AI & Machine Learning Enthusiast


# 📜 License

This project is created under MIT licence

---

# ⭐ Support

If you found this project useful,

⭐ Star this repository

🍴 Fork it

📢 Share it with others

---

<p align="center">

## ⭐ "Artificial Intelligence is not replacing humans, it is empowering them."

</p>
