from behave import given, when, then


@given('Open the main page')
def open_main_page(context):
    context.app.main_page.open_main()


@when('Click on "Connect the developer"')
def click_connect_developer(context):
    context.app.main_page.click_connect_developer_and_wait_new_tab(expected_windows_count=2)


@when('Switch the new tab')
def switch_new_tab(context):
    context.app.main_page.switch_to_new_tab()


@then('Verify the right tab opens')
def verify_right_tab(context):
    context.app.developer_page.verify_join_waitlist_visible()
