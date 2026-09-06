import os
from pathlib import Path
from time import perf_counter

import json_s
import proto
from proto import create_coll
from utils import get_dummies

json_path = Path("json_serialized.json")
proto_path = Path("proto_serialized.pb")
DUMMIED_AMOUNT = 10000


def process_json(objs: list[dict]):
    objs = json_s.add_id(objs)

    print(f"\nSaving to file: {json_path}")
    json_s.save_to_file(objs, json_path)
    print("Saved!")

    print(f"\nLoading from file: {json_path}")
    objs = json_s.read_from_file(json_path)
    print("Done.")

    del objs


def process_proto(objs: list[dict]):
    coll = create_coll(objs)

    print(f"\nSaving to file: {proto_path}")
    proto.save_to_file(coll, proto_path)
    print("Saved!")

    print(f"\nLoading from file: {proto_path}")
    coll = proto.read_from_file(proto_path)
    print("Done.")

    del coll


def time_fn(fn, *args, **kwargs):
    a = perf_counter()
    _ = fn(*args, **kwargs)
    b = perf_counter()

    return b - a


def print_stats(json_objs: list, protobuf_objs: list):
    print("=== JSON VS Protobuf ===\n")

    print("--- JSON ---")

    time_json = time_fn(process_json, json_objs)

    print("\n--- Protobuf ---")

    time_proto = time_fn(process_proto, protobuf_objs)

    print("\n--- Final Stats ---")

    print("Time:")
    print(f"\tJSON: {time_json} s.")
    print(f"\tProtobuf: {time_proto} s.")
    print(f"\tJSON is {(time_json / time_proto):.3f} slower tan Protobuf.")

    json_size = os.path.getsize(json_path)
    proto_size = os.path.getsize(proto_path)
    print("\nSize:")
    print(f"\tJSON: {json_size} bytes.")
    print(f"\tProtobuf: {proto_size} bytes.")
    print(f"\tJSON is {(json_size / proto_size):.3f} bigger tan Protobuf.")


def main():

    dummies = get_dummies(DUMMIED_AMOUNT)
    dummies = list(dummies)

    protobuf = dummies[:]

    json = dummies[:]

    print_stats(json, protobuf)


if __name__ == "__main__":
    main()
