from concurrent import futures
import time
import argparse
import grpc
from cython import nogil
import helloworld_pb2
import helloworld_pb2_grpc
import logging
import hashlib

PARALLEL = 50
executor = futures.ThreadPoolExecutor(max_workers=PARALLEL)
logging.getLogger().setLevel(logging.INFO)


class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def sayHello(self, request, context):
        logging.info("Processing sayHello for %s", request.name)
        return helloworld_pb2.HelloReply(
            message="Hello world .... {} ( Integrity: {})".format(
                request.name,
                hashlib.sha512(request.name.encode('utf-8')).hexdigest()
            )
        )


def app():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", default=28001)
    parser.add_argument("-a", "--address", default="localhost")
    cmd_args = parser.parse_args()

    server = grpc.server(executor, maximum_concurrent_rpcs=PARALLEL)
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    logging.info("Attempting to listen on %s:%s", cmd_args.address, cmd_args.port)
    server.add_insecure_port('{}:{}'.format(
        cmd_args.address, cmd_args.port
    ))

    server.start()
    try:
        while True:
            time.sleep(1)
    except Exception as e:
        server.stop(1)


if __name__ == "__main__":
    with nogil:
        app()