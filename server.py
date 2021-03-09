from concurrent import futures
import time
import math
import logging

import grpc

import mssv_pb2
import mssv_pb2_grpc
import server_resource


def get_info(info_db, mssv):
    """Returns Feature at given location or None."""
    for info in info_db:
        if info.id == mssv:
            return info
    return None


class MSSVProtoServicer(mssv_pb2_grpc.MSSVProtoServicer):
    """Provides methods that implement functionality of route guide server."""

    def __init__(self):
        self.db = server_resource.read_database()

    def GetFeature(self, request, context):
        info = get_info(self.db, request)
        if info is None:
            print("invalid")
            return mssv_pb2.infoSV(name="", id = request, phone = "", address = "", dateOfBirth = "", age = "", gender = "", mail = "")
        else:
            print(info.name + "\n" + info.age + "\n" +  info.gender + "\n" + info.phone +  "\n" + info.address +  "\n" + info.dateOfBirth +  "\n" + info.mail)
            return info

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mssv_pb2_grpc.add_MSSVProtoServicer_to_server(
        MSSVProtoServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()