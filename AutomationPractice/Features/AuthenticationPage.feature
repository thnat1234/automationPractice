Feature: Login Page
  Tests login existing and registering new users

  Background:
    Given I open website

  Scenario: Register user
    Given I navigate to login page
    When I enter email test12493@test.com
    And I click on create account button
    Then I am redirected to create an account page
    When I fill my personal information:
      | Title | FirstName | LastName | Email              | Password              | DateOfBirth |
      | Mr.   | John      | Doe      | test12493@test.com | automationPractice123 | 01/02/1990  |
    And I click register
    Then I am redirected to my account screen
    And I validate banner with successful registration
    When I click on my personal information
    Then I validate my personal information:
      | Title | FirstName | LastName | Email             | DateOfBirth |
      | Mr.   | John      | Doe      | test12493@test.com | 01/02/1990 |