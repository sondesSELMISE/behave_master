import time

from behave import given,when,then
from selenium.webdriver import ActionChains
from numpy.testing import assert_equal


@given(u'Then user navigate to the URL https://qavbox.github.io/demo/dragndrop/')
def step_impl(context):

    #context.browser.get("https://qavbox.github.io/demo/dragndrop/")
    context.dd.setup("https://qavbox.github.io/demo/dragndrop/")


@when(u'he move the drag box to drop box')
def step_impl(context):
    context.dd.drag()

    time.sleep(2)

@then(u'he see the message change to Dropped!')
def step_impl(context):
    context.dd.message()
    msg = context.dd.message()
    assert_equal(msg,"Dropped!")


