import grpc

import object_pb2
import object_pb2_grpc


def main():

    channel = grpc.insecure_channel("localhost:50051")

    stub = object_pb2_grpc.ObjectServiceStub(channel)

    obj = object_pb2.Object(
        object_id=1,
        title="Evento musical",
        description="Concierto de música",
        time_start="2026-09-06 18:00:00",
        time_end="2026-09-06 20:00:00",
        price=500,
        url="https://ejemplo.com"
    )

    response = stub.SendObject(obj)

    print("Respuesta del servidor:")
    print(response.message)


if __name__ == "__main__":
    main()