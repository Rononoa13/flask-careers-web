from flask import Flask, jsonify, render_template
import database


app = Flask(__name__)


@app.route("/")
def index():
    jobs = database.load_jobs()
    return render_template("home.html", jobs=jobs, company_name="Bell")


@app.route("/api/jobs")
def list_jobs():
    jobs = database.load_jobs()
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(debug=True)

# Functional and aesthetic improvement form jovian flask