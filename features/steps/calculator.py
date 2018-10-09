from hamcrest import *
import unittest
from selenium import webdriver
import behave

driver = webdriver.Firefox()
driver.get("https://walissonmarkley.000webhostapp.com/")

""" Adding numbers """

@when('I click in the number 9')
def step_insert_number9(context):
        elem = driver.find_element_by_css_selector('[data-num="9"]').click()

@then('I see number 9 in viewer')
def step_viewer_number9(context):

        elem = driver.find_element_by_id("viewer").get_property("innerHTML")
        print(elem)
        assert_that(elem, equal_to("9"))

@when('I click on [+]')
def step_insert_number9(context):
        elem = driver.find_element_by_css_selector('[data-ops="plus"]').click()
        print("Clicked!")

@then('I see number 9 in viewer, too')
def step_viewer_number9(context):

        elem = driver.find_element_by_id("viewer").get_property("innerHTML")
        print(elem)
        assert_that(elem, equal_to("9"))

@when('I click in the number 8')
def step_insert_number9(context):
        elem = driver.find_element_by_css_selector('[data-num="8"]').click()

@then('I see number 8 in viewer')
def step_viewer_number9(context):

        elem = driver.find_element_by_id("viewer").get_property("innerHTML")
        print(elem)
        assert_that(elem, equal_to("8"))

@when('I click on [=]')
def step_insert_number9(context):
        elem = driver.find_element_by_id('equals').click()
        print("Clicked!")

@then('The system returns 17')
def step_viewer_number9(context):

        elem = driver.find_element_by_id("viewer").get_property("innerHTML")
        print(elem)
        assert_that(elem, equal_to("17"))

""" Subtracting numbers """

@when('I click in the number 1 and 0')
def step_insert_number9(context):
        elem = driver.find_element_by_css_selector('[data-num="1"]').click()
        elem = driver.find_element_by_css_selector('[data-num="0"]').click()

@then('I see number 10 in viewer')
def step_viewer_number9(context):

        elem = driver.find_element_by_id("viewer").get_property("innerHTML")
        print(elem)
        assert_that(elem, equal_to("10"))

@when('I click on [-]')
def step_insert_number9(context):
        elem = driver.find_element_by_css_selector('[data-ops="minus"]').click()
        print("Clicked!")

@then('I see number 10 in viewer, too')
def step_viewer_number9(context):

        elem = driver.find_element_by_id("viewer").get_property("innerHTML")
        print(elem)
        assert_that(elem, equal_to("10"))

@when('I click in the number 7')
def step_insert_number9(context):
        elem = driver.find_element_by_css_selector('[data-num="7"]').click()

@then('I see number 7 in viewer')
def step_viewer_number9(context):

        elem = driver.find_element_by_id("viewer").get_property("innerHTML")
        print(elem)
        assert_that(elem, equal_to("7"))

@when('I click on [=] button')
def step_insert_number9(context):
        elem = driver.find_element_by_id('equals').click()
        print("Clicked!")

@then('The system returns 3')
def step_viewer_number9(context):

        elem = driver.find_element_by_id("viewer").get_property("innerHTML")
        print(elem)
        assert_that(elem, equal_to("3"))

""" Dividing numbers """

@when('I click on the numbers 1, 5, 5')
def step_insert_number9(context):
        elem = driver.find_element_by_css_selector('[data-num="1"]').click()
        elem = driver.find_element_by_css_selector('[data-num="5"]').click()
        elem = driver.find_element_by_css_selector('[data-num="5"]').click()

@then('I see number 155 in viewer')
def step_viewer_number9(context):

        elem = driver.find_element_by_id("viewer").get_property("innerHTML")
        print(elem)
        assert_that(elem, equal_to("155"))

@when('I click on [/]')
def step_insert_number9(context):
        elem = driver.find_element_by_css_selector('[data-ops="divided by"]').click()
        print("Clicked!")

@then('I see number 155 in viewer, too')
def step_viewer_number9(context):

        elem = driver.find_element_by_id("viewer").get_property("innerHTML")
        print(elem)
        assert_that(elem, equal_to("155"))

@when('I click in the number 5')
def step_insert_number9(context):
        elem = driver.find_element_by_css_selector('[data-num="5"]').click()

@then('I see number 5 in viewer')
def step_viewer_number9(context):

        elem = driver.find_element_by_id("viewer").get_property("innerHTML")
        print(elem)
        assert_that(elem, equal_to("5"))

@when('I click on [ = ] button')
def step_insert_number9(context):
        elem = driver.find_element_by_id('equals').click()
        print("Clicked!")

@then('The system returns 31')
def step_viewer_number9(context):

        elem = driver.find_element_by_id("viewer").get_property("innerHTML")
        print(elem)
        assert_that(elem, equal_to("31"))

""" Multiplying numbers """

@when('I click on the numbers 1, 5, 3')
def step_insert_number9(context):
        elem = driver.find_element_by_css_selector('[data-num="1"]').click()
        elem = driver.find_element_by_css_selector('[data-num="5"]').click()
        elem = driver.find_element_by_css_selector('[data-num="3"]').click()

@then('I see number 153 in viewer')
def step_viewer_number9(context):

        elem = driver.find_element_by_id("viewer").get_property("innerHTML")
        print(elem)
        assert_that(elem, equal_to("153"))

@when('I click on [*]')
def step_insert_number9(context):
        elem = driver.find_element_by_css_selector('[data-ops="times"]').click()
        print("Clicked!")

@then('I see number 153 in viewer, too')
def step_viewer_number9(context):

        elem = driver.find_element_by_id("viewer").get_property("innerHTML")
        print(elem)
        assert_that(elem, equal_to("153"))

@when('I click in the number 6')
def step_insert_number9(context):
        elem = driver.find_element_by_css_selector('[data-num="6"]').click()

@then('I see number 6 in viewer')
def step_viewer_number9(context):

        elem = driver.find_element_by_id("viewer").get_property("innerHTML")
        print(elem)
        assert_that(elem, equal_to("6"))

@when('I click on [ =] button')
def step_insert_number9(context):
        elem = driver.find_element_by_id('equals').click()
        print("Clicked!")

@then('The system returns 918')
def step_viewer_number9(context):

        elem = driver.find_element_by_id("viewer").get_property("innerHTML")
        print(elem)
        assert_that(elem, equal_to("918"))