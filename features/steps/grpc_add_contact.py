from behave import *
import grpc
from gRPCpb import phonebook_pb2, phonebook_pb2_grpc

use_step_matcher("cfparse")


@given("some service wants to add a new contact")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("the service call the ContactService to use AddContact service and provide some data")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    data = {"first_name": "grpc_user",
            "last_name": "booo",
            "nick_name": "haaaa"
            }
    context.stub: phonebook_pb2_grpc.ContactServiceStub
    context.response = context.stub.AddContact(phonebook_pb2.ContactRequest(**data))


@then("the contact should be added successfully and gives back a message")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.message == 'seems like contact added! hooray!'
    assert context.response.first_name == "grpc_user"
