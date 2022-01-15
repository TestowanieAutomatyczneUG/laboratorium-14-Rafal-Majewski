from behave import *
from src.PasswordValidator import PasswordValidator

use_step_matcher("re")


@given("there is a password validator")
def step_impl(context):
	context.passwordValidator = PasswordValidator()


@given("the password requires a minimum length of (?P<minLettersCount>\d*) letters?")
def step_impl(context, minLettersCount):
	if minLettersCount:
		context.passwordValidator.minLettersCount = int(minLettersCount)

@given("the password requires a minimum length of (?P<minDigitsCount>\d*) digits?")
def step_impl(context, minDigitsCount):
	if minDigitsCount:
		context.passwordValidator.minDigitsCount = int(minDigitsCount)

@when("the password is (?P<password>.+)")
def step_impl(context, password):
	context.password = password

@then("the password is (?P<validity>(?:in)?valid)")
def step_impl(context, validity):
	assert context.passwordValidator.validate(context.password) == (validity == "valid")
