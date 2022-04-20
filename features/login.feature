@smoke

Feature: Login Page

  Background:
    Given Open the browser

  Scenario: Need to verify login

    When Enter username "Deepak" and email "Deepak.147392@gmail.com"
    And Click submit
    Then Verify message

  Scenario: Need to verify login

    When Enter username "Akshay" and email "Askshay.147392@gmail.com"
    And Click submit
    Then Verify message

