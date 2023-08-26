# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import phonebook_pb2 as phonebook__pb2


class ContactServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetContact = channel.unary_unary(
                '/ContactService/GetContact',
                request_serializer=phonebook__pb2.ReteriveContactRequest.SerializeToString,
                response_deserializer=phonebook__pb2.ContactResponse.FromString,
                )
        self.AddContact = channel.unary_unary(
                '/ContactService/AddContact',
                request_serializer=phonebook__pb2.ContactRequest.SerializeToString,
                response_deserializer=phonebook__pb2.ContactResponse.FromString,
                )
        self.EditContact = channel.unary_unary(
                '/ContactService/EditContact',
                request_serializer=phonebook__pb2.EditContactRequest.SerializeToString,
                response_deserializer=phonebook__pb2.ContactResponse.FromString,
                )
        self.DeleteContact = channel.unary_unary(
                '/ContactService/DeleteContact',
                request_serializer=phonebook__pb2.ReteriveContactRequest.SerializeToString,
                response_deserializer=phonebook__pb2.ContactDeleteResponse.FromString,
                )


class ContactServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetContact(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddContact(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EditContact(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteContact(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ContactServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetContact': grpc.unary_unary_rpc_method_handler(
                    servicer.GetContact,
                    request_deserializer=phonebook__pb2.ReteriveContactRequest.FromString,
                    response_serializer=phonebook__pb2.ContactResponse.SerializeToString,
            ),
            'AddContact': grpc.unary_unary_rpc_method_handler(
                    servicer.AddContact,
                    request_deserializer=phonebook__pb2.ContactRequest.FromString,
                    response_serializer=phonebook__pb2.ContactResponse.SerializeToString,
            ),
            'EditContact': grpc.unary_unary_rpc_method_handler(
                    servicer.EditContact,
                    request_deserializer=phonebook__pb2.EditContactRequest.FromString,
                    response_serializer=phonebook__pb2.ContactResponse.SerializeToString,
            ),
            'DeleteContact': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteContact,
                    request_deserializer=phonebook__pb2.ReteriveContactRequest.FromString,
                    response_serializer=phonebook__pb2.ContactDeleteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ContactService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ContactService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetContact(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ContactService/GetContact',
            phonebook__pb2.ReteriveContactRequest.SerializeToString,
            phonebook__pb2.ContactResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddContact(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ContactService/AddContact',
            phonebook__pb2.ContactRequest.SerializeToString,
            phonebook__pb2.ContactResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EditContact(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ContactService/EditContact',
            phonebook__pb2.EditContactRequest.SerializeToString,
            phonebook__pb2.ContactResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteContact(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ContactService/DeleteContact',
            phonebook__pb2.ReteriveContactRequest.SerializeToString,
            phonebook__pb2.ContactDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class NumberServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddNumber = channel.unary_unary(
                '/NumberService/AddNumber',
                request_serializer=phonebook__pb2.NumberRequest.SerializeToString,
                response_deserializer=phonebook__pb2.NumberResponse.FromString,
                )


class NumberServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddNumber(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NumberServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddNumber': grpc.unary_unary_rpc_method_handler(
                    servicer.AddNumber,
                    request_deserializer=phonebook__pb2.NumberRequest.FromString,
                    response_serializer=phonebook__pb2.NumberResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'NumberService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NumberService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddNumber(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NumberService/AddNumber',
            phonebook__pb2.NumberRequest.SerializeToString,
            phonebook__pb2.NumberResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
