from behave import *

use_step_matcher("cfparse")


@given("some user wants to delete a contact")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when('she want to delete contact with id {contact_id}')
def step_impl(context, contact_id):
    """
    :param contact_id:
    :type context: behave.runner.Context
    """
    context.response = context.client.delete(f"/contacts/{contact_id}/")


@then("their desired contact should delete successfully")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 200


@given("some user wants to delete a contact that does not exist")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass

@then("their desired contact does not exist and should show error code 404")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 404
