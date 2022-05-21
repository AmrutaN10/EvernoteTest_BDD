Feature: Evernote feature
  Background: common feature steps
    Given Launch Firefox browser
    When Open Evernote website
    And Click on login for already registered user
    And Enter valid registered "naikamruta43@gmail.com" and "123456"
    And click on sign button

  Scenario: Successful login using email
    Then verify successful login
    And signout from the account
    And close the browser


  Scenario: Login and write a note followed by a logout
    Then click on new create note button and write note
    And signout from the account
    And close the browser


  Scenario: Login again and make sure you open the note created
     Then Successfully Open created note from previouse scenario
     And signout from the account
     And close the browser


