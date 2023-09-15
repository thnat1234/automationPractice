Feature: Login Page
  Tests login existing and registering new users

  Background:
    Given I open website

  Scenario: Register user
    Given I navigate to login page
    When I enter email test1@test.com
    And I click on create account button
    Then I am redirected to create an account page
    #And Email {test1@test.com} is already pre-filled
    When I fill my personal information:
      | Title | FirstName | LastName | Email          | Password              | DateOfBirth |
      | Mr    | John      | Doe      | test1@test.com | automationPractice123 | 1/1/1990    |
    #And I click register
    #Then I am redirected to my account screen
    #And I validate banner with successful registration
    #When I click on my personal information
    #Then I validate my personal information
    #  | Title | FirstName | LastName | Email          | DateOfBirth |
    #  | Mr    | John      | Doe      | test1@test.com | 1/1/1990    |
    #When I sign out
    #Then I validate that I am signed out

  #Examples: PersonalInformation
  #  | Title |