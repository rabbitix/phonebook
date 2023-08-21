from behave import *

use_step_matcher("cfparse")


@given("some user wants to see all of her contacts")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass

@when("she ask for contact list")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.response = context.client.get('/contacts/')


@then("she shall see a list of contacts")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 200
    assert isinstance(context.response.json(),list)
