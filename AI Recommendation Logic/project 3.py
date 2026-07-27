"""
╔══════════════════════════════════════════════════════════════════════╗
║               🤖 AI RECOMMENDATION SYSTEM 🎬                        ║
╠══════════════════════════════════════════════════════════════════════╣
║ 👩‍💻 Developed By : Bhaumik Bisht                               ║
║ 🏢 Internship   : DecodeLabs Artificial Intelligence Internship     ║
║ 📚 Project      : Project 3 - AI Recommendation Logic               ║
║ 🐍 Language     : Python 3                                          ║
║ 🚀 Version      : 1.0                                               ║
╠══════════════════════════════════════════════════════════════════════╣
║ Description:                                                        ║
║ A Rule-Based AI Recommendation System that suggests movies          ║
║ based on user preferences using similarity matching.                ║
║                                                                      ║
║ Features:                                                           ║
║ ✅ User Preference Input                                             ║
║ ✅ Similarity Score Calculation                                      ║
║ ✅ Top 5 AI Recommendations                                          ║
║ ✅ Recommendation History                                            ║
║ ✅ User Rating System                                                ║
║ ✅ CSV File Handling                                                 ║
║ ✅ Error Handling                                                    ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import csv
import os
from datetime import datetime

# -----------------------------
# Dataset File
# -----------------------------
DATA_FILE = "movies.csv"
HISTORY_FILE = "recommendation_history.csv"

# -----------------------------
# Create Default Dataset
# -----------------------------
def create_dataset():

    if os.path.exists(DATA_FILE):
        return

    movies = [
        ["Movie","Genre","Language","Mood","Rating"],
        ["Inception","Sci-Fi","English","Exciting",8.8],
        ["Interstellar","Sci-Fi","English","Inspirational",8.7],
        ["Avatar","Sci-Fi","English","Adventure",7.9],
        ["Titanic","Romance","English","Emotional",7.8],
        ["3 Idiots","Comedy","Hindi","Inspirational",8.4],
        ["PK","Comedy","Hindi","Funny",8.1],
        ["Dangal","Sports","Hindi","Motivational",8.5],
        ["Bahubali","Action","Hindi","Adventure",8.2],
        ["KGF","Action","Hindi","Exciting",8.3],
        ["RRR","Action","Hindi","Exciting",8.1],
        ["Frozen","Animation","English","Happy",7.8],
        ["Toy Story","Animation","English","Happy",8.2],
        ["Coco","Animation","English","Emotional",8.4],
        ["Doctor Strange","Sci-Fi","English","Adventure",7.9],
        ["The Dark Knight","Action","English","Thriller",9.0],
        ["Avengers Endgame","Action","English","Exciting",8.4],
        ["Spider-Man No Way Home","Action","English","Exciting",8.3],
        ["Parasite","Thriller","Korean","Suspense",8.6],
        ["Your Name","Animation","Japanese","Romantic",8.4],
        ["Shershaah","Drama","Hindi","Motivational",8.4],
        ["Taare Zameen Par","Drama","Hindi","Emotional",8.4],
        ["Chhichhore","Comedy","Hindi","Inspirational",8.3]
    ]

    with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(movies)


# -----------------------------
# Load Dataset
# -----------------------------
def load_movies():

    movies = []

    with open(DATA_FILE, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            row["Rating"] = float(row["Rating"])
            movies.append(row)

    return movies


# -----------------------------
# Display Header
# -----------------------------
def header():

    print("\n" + "🌟" * 25)
    print("🤖 AI MOVIE RECOMMENDATION SYSTEM 🎬")
    print("🌟" * 25)

    print(f"📅 Date : {datetime.now().strftime('%d-%m-%Y')}")
    print("👩‍💻 Developed By : Bhaumik Bisht")
    print("🏢 Internship : DecodeLabs Artificial Intelligence Internship")
    print("🎯 Project : AI Recommendation Logic")
    print("🌟" * 25)

# -----------------------------
# Menu
# -----------------------------
def menu():

    print("\n1. Get Recommendations")
    print("2. View Dataset")
    print("3. Recommendation History")
    print("4. About Project")
    print("5. Exit")


# -----------------------------
# View Dataset
# -----------------------------
def view_dataset():

    movies = load_movies()

    print("\nAvailable Movies\n")

    for movie in movies:

        print(f"{movie['Movie']:25} "
              f"{movie['Genre']:12} "
              f"{movie['Language']:10} "
              f"{movie['Mood']:15} "
              f"⭐ {movie['Rating']}")


# -----------------------------
# User Preferences
# -----------------------------
def user_preferences():

    print("\n🎬 Enter Your Preferences\n")

    genre = input("🎭 Preferred Genre : ").strip().title()

    language = input("🌍 Preferred Language : ").strip().title()

    mood = input("😊 Preferred Mood : ").strip().title()

    while True:

        try:
            rating = float(input("⭐ Minimum IMDb Rating : "))
            break

        except ValueError:
            print("❌ Please enter a valid rating.")

    # Always return values
    return genre, language, mood, rating


# ----------------------------------------------------
# Calculate Similarity Score
# ----------------------------------------------------
def calculate_score(movie, genre, language, mood, rating):

    score = 0

    if movie["Genre"].lower() == genre.lower():
        score += 40

    if movie["Language"].lower() == language.lower():
        score += 25

    if movie["Mood"].lower() == mood.lower():
        score += 20

    if movie["Rating"] >= rating:
        score += 15

    return score


# ----------------------------------------------------
# Save Recommendation History
# ----------------------------------------------------
def save_history(movie_name, similarity, user_rating):

    file_exists = os.path.exists(HISTORY_FILE)

    with open(HISTORY_FILE, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Date",
                "Movie",
                "Similarity",
                "User Rating"
            ])

        writer.writerow([
            datetime.now().strftime("%d-%m-%Y %I:%M %p"),
            movie_name,
            f"{similarity}%",
            user_rating
        ])


# ----------------------------------------------------
# Recommendation Engine
# ----------------------------------------------------
def recommend_movies():

    movies = load_movies()

    genre, language, mood, rating = user_preferences()

    recommendations = []

    for movie in movies:

        similarity = calculate_score(
            movie,
            genre,
            language,
            mood,
            rating
        )

        if similarity > 0:
            recommendations.append((movie, similarity))

    recommendations.sort(
        key=lambda x: x[1],
        reverse=True
    )

    print("\n" + "=" * 60)
    print("🤖 TOP AI RECOMMENDATIONS 🎬")
    print("=" * 60)

    if len(recommendations) == 0:

        print("❌ No recommendations found.")
        return

    top = recommendations[:5]

    for i, (movie, similarity) in enumerate(top, start=1):

        print(f"""
{i}. 🎬 {movie['Movie']}
   🎭 Genre      : {movie['Genre']}
   🌍 Language   : {movie['Language']}
   😊 Mood       : {movie['Mood']}
   ⭐ IMDb       : {movie['Rating']}
   💯 Similarity : {similarity}%
""")

    choice = input("⭐ Would you like to rate these recommendations? (y/n): ").lower()

    if choice == "y":

        for movie, similarity in top:

            while True:

                try:

                    user_rating = int(
                        input(f"🌟 Rate '{movie['Movie']}' (1-5): ")
                    )

                    if 1 <= user_rating <= 5:

                        save_history(
                            movie["Movie"],
                            similarity,
                            user_rating
                        )

                        break

                    else:
                        print("❌ Rating must be between 1 and 5.")

                except ValueError:
                    print("❌ Invalid input.")


# ----------------------------------------------------
# Recommendation History
# ----------------------------------------------------
def view_history():

    print("\n📜 Recommendation History\n")

    if not os.path.exists(HISTORY_FILE):

        print("⚠ No recommendation history available.")

        return

    with open(HISTORY_FILE, "r", encoding="utf-8") as file:

        reader = csv.reader(file)

        for row in reader:
            print("{:<20} {:<30} {:<12} {}".format(*row))


# ----------------------------------------------------
# About Project
# ----------------------------------------------------
def about():

    print("\n" + "=" * 60)
    print("📌 PROJECT INFORMATION")
    print("=" * 60)

    print("🤖 Project      : AI Recommendation System")
    print("🏢 Internship   : DecodeLabs AI Internship")
    print("👩‍💻 Developer   : Bhaumik Bisht")
    print("🐍 Language     : Python")
    print("🎯 Method       : Similarity Matching")
    print("📂 Dataset      : Movies")
    print("🚀 Version      : 1.0")

    print("=" * 60)


# ----------------------------------------------------
# Main Function
# ----------------------------------------------------
def main():

    create_dataset()

    while True:

        header()

        menu()

        choice = input("\n👉 Enter your choice : ")

        if choice == "1":

            recommend_movies()

        elif choice == "2":

            view_dataset()

        elif choice == "3":

            view_history()

        elif choice == "4":

            about()

        elif choice == "5":

            print("\n👋 Thank you for using AI Recommendation System!")
            print("🌟 Have a wonderful day!")
            break

        else:

            print("❌ Invalid choice. Please try again.")

        input("\n🔹 Press Enter to continue...")


# ----------------------------------------------------
# Program Starts Here
# ----------------------------------------------------
if __name__ == "__main__":
    main()
