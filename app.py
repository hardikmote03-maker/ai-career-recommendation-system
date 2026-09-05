from flask import Flask, render_template, request
from utils.recommendation import recommend_careers

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = None

    if request.method == "POST":
        profile = {
            "python": int(request.form.get("python", 0)),
            "sql": int(request.form.get("sql", 0)),
            "excel": int(request.form.get("excel", 0)),
            "statistics": int(request.form.get("statistics", 0)),
            "machine_learning": int(request.form.get("machine_learning", 0)),
            "web_development": int(request.form.get("web_development", 0)),
            "communication": int(request.form.get("communication", 0))
        }

        recommendations = recommend_careers(profile)

    return render_template(
        "index.html",
        recommendations=recommendations
    )


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=True)