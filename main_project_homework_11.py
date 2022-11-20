from utils_homework_11 import get_candidate, get_candidates_by_name, get_candidates_by_skill, load_candidates_from_json
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    candidates = load_candidates_from_json()
    result = '<h1> Все кандидаты </h1>'
    for candidate in candidates:
        result += '<p> <a href="/candidate/<id>">' + candidate['name'] + '</a></p>'
    return result


@app.route("/candidate/<int:id>")
def get_candidate_by_id(id):
    candidate = get_candidate(id)
    result = ''
    if candidate == "Mistake":
        return f"Not found candidate with id {id}"
    else:
        result = '<br>'
        result += '<h1>' + candidate['name'] + '</h1>'
        result += '<p>' + candidate['position'] + '</p>'
        result += '<img src = ' + candidate['picture'] + ' width=200/>'
        result += '<p>' + candidate['skills'] + '</p>'
        result += '<br>'
        return result


app.run(debug=True, host='0.0.0.0', port=8000)
