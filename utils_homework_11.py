import json


def load_candidates_from_json():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_candidate(id_candidate):
    data_candidates = load_candidates_from_json()
    for candidate in data_candidates:
        if candidate['id'] == int(id_candidate):
            return candidate

    return "Mistake"


def get_candidates_by_name(candidate_name):
    data_candidates = load_candidates_from_json()
    for candidate in data_candidates:
        if candidate['name'].lower() == candidate_name.lower():
            return candidate
        else:
            return f"Not found candidate with name {candidate_name}"


def get_candidates_by_skill(skill_name):
    data_candidates = load_candidates_from_json()
    for candidate in data_candidates:
        if skill_name.lower() in candidate['skill'].lower().split(','):
            return candidate
        else:
            return f"Not found candidate with skill {skill_name}"