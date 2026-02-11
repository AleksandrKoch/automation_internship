Feature: Connect developer flow
"""
To run this scenario do the next steps:
Run → Edit Configurations → Behave → Environment variables:
REELLY_EMAIL=put_my_email_here
REELLY_PASSWORD=Put_my_password_here
"""
  Scenario: The user can click on “Connect the company” on the left side of the main page
    Given Open the main page
    And Log in to the page
    When Click on "Connect the developer"
    And Switch the new tab
    Then Verify the right tab opens
