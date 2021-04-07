# Created by kusia at 4/6/21
Feature: Sort by latest test

  Scenario: User can sort products by Latest, query “orderby=date“ will appear in page URL after products are sorted
    Given Open shop page
    When Select sort by latest
    Then Verify query “orderby=date“ will appear in page URL


  Scenario: User can go through all product pages after they sorted by Latest (1, 2, > buttons under product catalog)
    Given Open shop page
    When Select sort by latest
    Then Verify user can go through all product pages after they sorted by Latest


  Scenario: After user sorts products by Latest, they can then reset to Default Sorting
    Given Open shop page
    When Select sort by latest
    Then Verify user can reset to Default Sorting


  Scenario: Url https://gettop.us/shop/?orderby=date opens the page with products sorted by Latest
    Given Open given URL
    Then Verify given URL opens the page with products sorted by Latest




