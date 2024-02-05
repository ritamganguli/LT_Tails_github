from behave import given
from features.data_seed.provider_state_seeds import *


@given('Add fixed revenue for dataseed pet')
def _(context):
    set_quote_for_subscription(context.customer_id)
