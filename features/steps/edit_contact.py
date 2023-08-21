from behave import *

use_step_matcher("cfparse")


@given("some user wants to edit a contact")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when('she wants to update contact with id {contact_id} and set first-name to "{text}"')
def step_impl(context, contact_id, text):
    """
    :param text:
    :param contact_id:
    :type context: behave.runner.Context
    """
    data = {
        "first_name": text
    }
    context.user_data = text
    context.response = context.client.patch(f'/contacts/{contact_id}/', json=data)


@then("their contact should be updated successfully")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.json()['first_name'] == context.user_data
    assert context.response.status_code == 200
