# Created by kusia at 4/8/21
Feature: Account Lost Password Test

  Scenario: Lost Password form has correct UI elements (input field, header, CTA, etc.)
    Given Open Lost Password page
    Then Verify page has correct UI elements


  Scenario: User can see Best Selling, Latest, Top Rated blocks
    Given Open Lost Password page
    Then Verify user can see Best Selling, Latest, Top Rated blocks


  Scenario: Resetting a password for non-existing user "test" displays a correct error message
    Given Open Lost Password page
    When Enter "test" for non-existing user in the input field
    And Click on Reset Password button
    Then Verify a correct error message is displayed


  Scenario: Resetting a password for existing user "admin" displays correct confirmation message
    Given Open Lost Password page
    When Enter "admin" for existing user in the input field
    And Click on Reset Password button
    Then Verify a correct confirmation message is displayed
