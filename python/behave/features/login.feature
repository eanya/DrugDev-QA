  Feature: Login
    As a user
    I want to Login
    So that I can use the app

    Background:
       Given the user is on the home page

    Scenario: Login Success
       When the user enters username as "test@drugdev.com"
       And the user enters password as "supers3cret"
       And clicks Login
       Then the user is presented with a welcome message as "Welcome Dr I Test"


    Scenario Outline: Login Incorrect credentials
        When the user enters username as "<email>"
        And the user enters password as "<password>"
        And clicks Login
        Then the user is presented with an error message as "<error_msg>"

    Examples: Login Incorrect credentials
      |email              |password    |error_msg                |
      |xtest@drugdev.com  |supers3cret |Credentials are incorrect|
      |test@drugdev.com   |xsupers3cret|Credentials are incorrect|
      |xtest@drugdev.com  |xsupers3cret|Credentials are incorrect|
      | empty             |empty       |Credentials are incorrect|
      | empty             |supers3cret |Credentials are incorrect|
      | test@drugdev.com  |  empty     |Credentials are incorrect|
      #|test=drugdev.com   |supers3cret |Credentials are incorrect|