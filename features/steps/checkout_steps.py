from behave import given, when, then


@given(u'I am on the homepage')
def step_impl(context):
    pass


@when(u'I search for a product by name or category')
def step_impl(context):
    pass


@when(u'I select a product from the search results')
def step_impl(context):
    pass


@when(u'I view the product details page')
def step_impl(context):
    pass


@when(u'I add the product to my cart')
def step_impl(context):
    pass


@when(u'I view my shopping cart')
def step_impl(context):
    pass


@when(u'I proceed to checkout as a guest')
def step_impl(context):
    pass


@when(u'I enter my personal information (name, email, phone)')
def step_impl(context):
    pass


@when(u'I enter my delivery address')
def step_impl(context):
    pass


@when(u'I choose Debit Card as the payment method')
def step_impl(context):
    pass


@when(u'I enter valid Debit Card details')
def step_impl(context):
    pass


@when(u'I review my order summary')
def step_impl(context):
    pass


@when(u'I place the order')
def step_impl(context):
    pass


@then(u'I should be redirected to the order confirmation page')
def step_impl(context):
    pass


@when(u'I choose PayPal as the payment method')
def step_impl(context):
    pass


@when(u'I enter valid PayPal details')
def step_impl(context):
    pass


@when(u'I choose Finance as the payment method')
def step_impl(context):
    pass


@when(u'I enter valid Finance details')
def step_impl(context):
    pass
