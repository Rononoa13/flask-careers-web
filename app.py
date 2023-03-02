from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'USA, Miami',
        'salary': '$64000 per year'
    },
    {
        'id': 2,
        'title': 'Data QA Engineer',
        'location': 'USA, Newyork',
        'salary': '$54000 per year'
    },
    {
        'id': 3,
        'title': 'Senior Data Engineer',
        'location': 'Remote'
    },
    {
        'id': 4,
        'title': 'Senior Backend Engineer',
        'location': 'Remote',
        'salary': '$84000 per year'
    }
]

@app.route("/")
def index():
    return render_template("home.html", jobs=JOBS, company_name="Bell")


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(debug=True)

# Functional and aesthetic improvement form jovian flask