import grpc

import rx
import helloworld_pb2
import helloworld_pb2_grpc

import logging
from cython import nogil

channels = [ 
    grpc.insecure_channel('localhost:27885')
]
stubs = [ 
    helloworld_pb2_grpc.GreeterStub(channels[0])
]

logging.getLogger().setLevel(logging.INFO)

pooled_scheduler = rx.concurrency.ThreadPoolScheduler(max_workers=80)


def run():
    rx.Observable.from_(range(10000, 0, -1)) \
        .subscribe_on(pooled_scheduler) \
        .subscribe(on_next=lambda x: make_req_and_get_response(x))


def make_req_and_get_response(i):
    response = stubs[0].sayHello(helloworld_pb2.HelloRequest(
            name="JayD + Req {}".format(i)
        ))
    logging.info("Greeter client received :: %s", response.message)


if __name__ == "__main__":
    with nogil:
        run()
