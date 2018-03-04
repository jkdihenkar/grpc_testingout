from concurrent import futures
import time

import grpc

from cython import nogil
import helloworld_pb2
import helloworld_pb2_grpc
import logging
import hashlib

executor = futures.ThreadPoolExecutor(max_workers=50)


class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def sayHello(self, request, context):
        return helloworld_pb2.HelloReply(
            message="Hello world .... {} ( Integrity: {})".format(
                request.name,
                hashlib.sha512(request.name.encode('utf-8')).hexdigest()
            )
        )


def app():
    server = grpc.server(executor)
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('localhost:27885')
    server.start()
    try:
        while True:
            time.sleep(1)
    except Exception as e:
        server.stop(1)


if __name__ == "__main__":
    with nogil:
        app()