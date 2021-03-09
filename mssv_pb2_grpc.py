# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import mssv_pb2 as mssv__pb2


class MSSVProtoStub(object):
    """Interface exported by the server.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetFeature = channel.unary_unary(
                '/MSSV.MSSVProto/GetFeature',
                request_serializer=mssv__pb2.idSV.SerializeToString,
                response_deserializer=mssv__pb2.infoSV.FromString,
                )


class MSSVProtoServicer(object):
    """Interface exported by the server.
    """

    def GetFeature(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MSSVProtoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetFeature': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFeature,
                    request_deserializer=mssv__pb2.idSV.FromString,
                    response_serializer=mssv__pb2.infoSV.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MSSV.MSSVProto', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MSSVProto(object):
    """Interface exported by the server.
    """

    @staticmethod
    def GetFeature(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MSSV.MSSVProto/GetFeature',
            mssv__pb2.idSV.SerializeToString,
            mssv__pb2.infoSV.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
