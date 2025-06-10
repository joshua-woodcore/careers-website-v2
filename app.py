from flask import Flask, render_template, jsonify
from database import fetch_all_jobs, fetch_jobs

app = Flask(__name__)



@app.route('/')
def hello_world():
    jobs = fetch_all_jobs()
    return render_template('home.html',
                           jobs=jobs)


@app.route('/job/<id>')
def show_job(id):
    job = fetch_jobs(id)
    if not job:
        return "Job not found", 404
    return render_template('jobpage.html',
                           job=job)


@app.route('/api/jobs')
def list_jobs():
    jobs = fetch_all_jobs()
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)