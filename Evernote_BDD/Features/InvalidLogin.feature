Feature: Evernote feature
  Scenario: Unsuccessful login using email
    Given Launch Firefox browser
    When Open Evernote website
    And Click on login for already registered user
    And Enter Invalid not registered "na43@gmail.com"
    Then Click on continue and verify unsuccessful login
    And close the browser

