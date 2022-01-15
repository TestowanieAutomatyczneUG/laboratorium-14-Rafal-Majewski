from behave import *
from src.validateIsbnNumber import validateIsbnNumber

use_step_matcher("re")


@given("there is a function validating ISBN number")
def step_impl(context):
	pass


@when("the ISBN number is (?P<isbnNumber>.+)")
def step_impl(context, isbnNumber):
	context.isbnNumber = isbnNumber

@then("the ISBN number is (?P<validity>(?:in)?valid)")
def step_impl(context, validity):
	assert validateIsbnNumber(context.isbnNumber) == (validity == "valid")
