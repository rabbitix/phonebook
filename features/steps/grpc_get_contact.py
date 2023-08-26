from behave import *

from gRPCpb import phonebook_pb2_grpc, phonebook_pb2

use_step_matcher("cfparse")


@given("some service wants to retrieve a contact")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("the service call the ContactService to use GetContact service and provide contact_id {contact_id}")
def step_impl(context, contact_id):
    """
    :type context: behave.runner.Context
    """
    context.contact_id = int(contact_id)
    context.stub: phonebook_pb2_grpc.ContactServiceStub
    context.response = context.stub.GetContact(phonebook_pb2.ReteriveContactRequest(contact_id=context.contact_id))


@then("the service should be able to see the contact information")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.first_name == "grpc_user"
    assert context.response.message == "here you are :)"
