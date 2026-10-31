import json

from models.control import Control


def save_project(filename, controls):

    data = []

    for control in controls:
        data.append(control.to_dict())

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def load_project(filename):

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    controls = []

    for item in data:
        controls.append(Control(**item))

    return controls