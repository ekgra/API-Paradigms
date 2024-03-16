# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import people_pb2 as people__pb2


class PeopleServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPeople = channel.unary_unary(
                '/PeopleService/GetPeople',
                request_serializer=people__pb2.GetPeopleRequest.SerializeToString,
                response_deserializer=people__pb2.GetPeopleResponse.FromString,
                )
        self.GetPerson = channel.unary_unary(
                '/PeopleService/GetPerson',
                request_serializer=people__pb2.GetPersonRequest.SerializeToString,
                response_deserializer=people__pb2.Person.FromString,
                )
        self.AddPerson = channel.unary_unary(
                '/PeopleService/AddPerson',
                request_serializer=people__pb2.AddPersonRequest.SerializeToString,
                response_deserializer=people__pb2.AddPersonResponse.FromString,
                )
        self.UpdatePerson = channel.unary_unary(
                '/PeopleService/UpdatePerson',
                request_serializer=people__pb2.UpdatePersonRequest.SerializeToString,
                response_deserializer=people__pb2.UpdatePersonResponse.FromString,
                )
        self.DeletePerson = channel.unary_unary(
                '/PeopleService/DeletePerson',
                request_serializer=people__pb2.DeletePersonRequest.SerializeToString,
                response_deserializer=people__pb2.DeletePersonResponse.FromString,
                )


class PeopleServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetPeople(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPerson(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddPerson(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdatePerson(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeletePerson(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PeopleServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetPeople': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPeople,
                    request_deserializer=people__pb2.GetPeopleRequest.FromString,
                    response_serializer=people__pb2.GetPeopleResponse.SerializeToString,
            ),
            'GetPerson': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPerson,
                    request_deserializer=people__pb2.GetPersonRequest.FromString,
                    response_serializer=people__pb2.Person.SerializeToString,
            ),
            'AddPerson': grpc.unary_unary_rpc_method_handler(
                    servicer.AddPerson,
                    request_deserializer=people__pb2.AddPersonRequest.FromString,
                    response_serializer=people__pb2.AddPersonResponse.SerializeToString,
            ),
            'UpdatePerson': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdatePerson,
                    request_deserializer=people__pb2.UpdatePersonRequest.FromString,
                    response_serializer=people__pb2.UpdatePersonResponse.SerializeToString,
            ),
            'DeletePerson': grpc.unary_unary_rpc_method_handler(
                    servicer.DeletePerson,
                    request_deserializer=people__pb2.DeletePersonRequest.FromString,
                    response_serializer=people__pb2.DeletePersonResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'PeopleService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PeopleService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetPeople(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PeopleService/GetPeople',
            people__pb2.GetPeopleRequest.SerializeToString,
            people__pb2.GetPeopleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPerson(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PeopleService/GetPerson',
            people__pb2.GetPersonRequest.SerializeToString,
            people__pb2.Person.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddPerson(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PeopleService/AddPerson',
            people__pb2.AddPersonRequest.SerializeToString,
            people__pb2.AddPersonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdatePerson(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PeopleService/UpdatePerson',
            people__pb2.UpdatePersonRequest.SerializeToString,
            people__pb2.UpdatePersonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeletePerson(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PeopleService/DeletePerson',
            people__pb2.DeletePersonRequest.SerializeToString,
            people__pb2.DeletePersonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
