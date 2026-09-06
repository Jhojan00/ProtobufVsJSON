from concurrent import futures

import grpc

import object_pb2
import object_pb2_grpc


class ObjectService(object_pb2_grpc.ObjectServiceServicer):

    def SendObject(self, request, context):
        print("\nObjeto recibido:")
        print(request)

        return object_pb2.ObjectResponse(
            success=True,
            message=f"Objeto '{request.title}' recibido correctamente."
        )


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    object_pb2_grpc.add_ObjectServiceServicer_to_server(
        ObjectService(),
        server
    )

    server.add_insecure_port("[::]:50051")
    server.start()

    print("Servidor gRPC ejecutándose en el puerto 50051")

    server.wait_for_termination()


if __name__ == "__main__":
    main()