import json
from pathlib import Path


def add_id(objs: list):
    for idx, obj in enumerate(objs):
        obj["id"] = idx + 1

    return objs


def save_to_file(objs: list[dict], file_path: Path):
    with open(file_path, "w") as f:
        json.dump(objs, f)


def read_from_file(file_path: Path):
    with open(file_path, "r") as f:
        coll = json.load(f)
    return coll
