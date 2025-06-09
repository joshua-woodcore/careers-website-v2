from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Scientist',
        'location': 'New York, NY',
        'salary': '$120,000'
    },
    {
        'id': 2,
        'title': 'Web Developer',
        'location': 'San Francisco, CA',
        'salary': '$110,000'
    },
    {
        'id': 3,
        'title': 'Software Engineer',
        'location': 'Austin, TX',
        'salary': '$100,000'
    },
    {
        'id': 4,
        'title': 'Product Manager',
        'location': 'Seattle, WA',
        'salary': '$130,000'
    },
    {
        'id': 5,
        'title': 'UX Designer',
        'location': 'Los Angeles, CA',
        'salary': '$95,000'
    }
]


@app.route('/')
def hello_world():
    return render_template('home.html',
                           jobs=JOBS)


@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)