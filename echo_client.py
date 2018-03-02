import grpc
from concurrent import futures

import helloworld_pb2
import helloworld_pb2_grpc

channels = [ 
    grpc.insecure_channel('localhost:27885')
]
stubs = [ 
    helloworld_pb2_grpc.GreeterStub(channels[0])
]


def run():
    p = futures.ThreadPoolExecutor(max_workers=50)
    data_set = range(10000, 0, -1)
    p.map(make_req_and_get_response, data_set)


def make_req_and_get_response(i):
    response = stubs[0].sayHello(helloworld_pb2.HelloRequest(
            name="JayD + Req {}".format(i)
        ))
    print("Greeter client received :: {}".format(
            response.message
        ))


if __name__ == "__main__":
    run()