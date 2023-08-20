from behave import *

use_step_matcher("re")


@given("some user wants to add a new contact to their phonebook")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("she provide first-name last-name and nick-name")
def step_impl(context):
    data = {
        "first_name": "ali",
        "last_name": "fazeli",
        "nick_name": "alex",
    }

    response = context.client.post('/contacts/', json=data)
    context.response = response


@when("she do not provide first-name of the contact")
def step_impl(context):
    data = {

        "last_name": "fazeli",
        "nick_name": "alex",
    }

    response = context.client.post('/contacts/', json=data)
    context.response = response


@then("their contact should successfully added to the phonebook")
def step_impl(context):
    assert context.response.status_code == 200


@then("their contact should not added to the phonebook")
def step_impl(context):
    assert context.response.status_code == 422
    assert context.response.is_error is True
