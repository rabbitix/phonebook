from behave import *

use_step_matcher("cfparse")


@given("some user wants to add a number to a contact")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("she want to add a new number to cantact with id {contact_id}")
def step_impl(context, contact_id):
    """
    :type context: behave.runner.Context
    """
    data = {
        "label": "test",
        "phone": "09154231243"
    }
    context.response = context.client.post(f'/contacts/{contact_id}/numbers/', json=data)


@then("their number will added to contact successfully")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 200


@when("she wants to add number to contact with id {contact_id} and only provide phone as '{phone}'")
def step_impl(context, contact_id, phone):
    """
    :type context: behave.runner.Context
    """
    data = {'phone': phone}
    context.response = context.client.post(f'/contacts/{contact_id}/numbers/', json=data)


@then("their number will add with a default label")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    res = context.response.json()
    assert context.response.status_code == 200
    assert res['numbers'][-1]['label'] == 'phone'


@when(
    "she wants to add a number to contact with id {contact_id} and she provide a number like '{phone}' which is incomplete")
def step_impl(context, contact_id, phone):
    """
    :type context: behave.runner.Context
    """
    data = {'phone': phone}
    context.response = context.client.post(f'/contacts/{contact_id}/numbers/', json=data)


@then("their number should not add and they get an error")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 422
    assert context.response.json()['detail'][0]['type'] == "string_pattern_mismatch"
