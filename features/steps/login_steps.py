from behave import given


@given('Log in to the page')
def login_to_page(context):
    context.app.login_page.open_sign_in()
    context.app.login_page.login()
