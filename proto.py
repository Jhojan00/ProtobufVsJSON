from pathlib import Path

import object_pb2


def create_coll(objs: list):
    coll = object_pb2.ObjectColl()
    for idx, obj in enumerate(objs):
        protobj = coll.objects.add()

        protobj.object_id = idx + 1
        protobj.title = obj["title"]
        protobj.description = obj["description"]
        protobj.time_start = obj["time_start"]
        protobj.time_end = obj["time_end"]
        protobj.price = obj["price"]
        protobj.url = obj["url"]

    return coll


def save_to_file(coll, file_path: Path):

    with open(file_path, "wb") as f:
        f.write(coll.SerializeToString())


def read_from_file(file_path: Path):
    coll = object_pb2.ObjectColl()
    with open(file_path, "rb") as f:
        coll.ParseFromString(f.read())

    return coll
