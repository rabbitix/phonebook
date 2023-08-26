from behave import *
from gRPCpb import phonebook_pb2, phonebook_pb2_grpc

use_step_matcher("cfparse")


@given("some service wants to delete a contact")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("the service call the ContactService to use DeleteContact service and provide contact id {contact_id}")
def step_impl(context, contact_id):
    """
    :type context: behave.runner.Context
    """
    data = {"contact_id": int(contact_id)}
    context.contact_id = contact_id
    context.stub: phonebook_pb2_grpc.ContactServiceStub
    context.response = context.stub.DeleteContact(phonebook_pb2.ReteriveContactRequest(**data))


@then("the contact should be deleted successfully and gives back a message")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.message == f"your contact with id {context.contact_id} deleted!"
