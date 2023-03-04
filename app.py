from flask import Flask, jsonify, render_template
import database


app = Flask(__name__)


@app.route("/")
def index():
    jobs = database.load_jobs()
    return render_template("home.html", jobs=jobs, company_name="Bells")


@app.route("/api/jobs")
def list_jobs():
    jobs = database.load_jobs()
    return jsonify(jobs)


@app.route("/job/<id>")
def show_job(id):
    job = database.load_job(id)
    if not job:
        return "Not Found", 404
    return render_template("job_page.html", company_name="Bells", job=job)


if __name__ == "__main__":
    app.run(debug=True)

# Functional and aesthetic improvement form jovian flask