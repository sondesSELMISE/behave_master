
from behave import when,then
from numpy.testing import assert_equal
from selenium.webdriver.common.action_chains import ActionChains

@when(u'he move the slider bar to 100')
def step_impl(context):
    context.dd.slide()


@then(u'he see the message success progress!')
def step_impl(context):
    context.dd.message()
    ms = context.dd.msg_slide()
    assert_equal(ms,"100")