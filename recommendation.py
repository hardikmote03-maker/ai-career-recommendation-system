import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = BASE_DIR / "data" / "careers.csv"


def load_careers():

    careers = []

    with open(DATA_FILE, newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            row["skills"] = [
                skill.strip()
                for skill in row["skills"].split("|")
            ]

            careers.append(row)

    return careers


def recommend_careers(profile, top_n=3):

    careers = load_careers()

    results = []

    for career in careers:

        required_skills = career["skills"]

        scores = []

        missing_skills = []

        for skill in required_skills:

            score = profile.get(skill, 0)

            scores.append(score)

            if score < 60:

                missing_skills.append(
                    skill.replace("_", " ").title()
                )

        if scores:

            match_percentage = round(
                sum(scores) / len(scores)
            )

        else:

            match_percentage = 0

        results.append({

            "career": career["career"],

            "description": career["description"],

            "match": match_percentage,

            "missing": missing_skills,

            "roadmap": career["roadmap"].split("|")

        })

    results.sort(
        key=lambda item: item["match"],
        reverse=True
    )

    return results[:top_n]