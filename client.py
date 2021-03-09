from __future__ import print_function

import random
import logging

import grpc

import mssv_pb2
import mssv_pb2_grpc
import server_resource


def get_info(stub, mssv):
    info = stub.GetFeature(mssv)
    if info.name != "":
        print(info.name + "\n" + info.age + "\n" +  info.gender + "\n" + info.phone +  "\n" + info.address +  "\n" + info.dateOfBirth +  "\n" + info.mail)
    else:
        print("invalid id")

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Input student ID: ")
    id = input()
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = mssv_pb2_grpc.MSSVProtoStub(channel)
        print("-------------- Info--------------")
        get_info(stub, mssv_pb2.idSV(mssv=id))


if __name__ == '__main__':
    logging.basicConfig()
    run()