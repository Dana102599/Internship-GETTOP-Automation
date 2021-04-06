# Created by kusia at 4/2/21
Feature: Product test
  # Enter feature description here

  Scenario: Product has image, name, price, description
    Given Open Gettop product page
    Then Verify product has 6 images
    Then Verify product has name
    Then Verify product has price
    Then Verify product has description


  Scenario: User can zoom in product image, scroll thru images and close them (by clicking X)
    Given Open Gettop product page
    When Click on zoom icon
    And Scroll thru images
    Then Close zoomed image by clicking X


  Scenario: User can add product to wishlist by hovering over product image and clicking on the heart icon
    Given Open Gettop product page
    When Hover over product image
    And Click on heart icon
    Then Verify item added to wishlist


  Scenario: "Home" link takes user to Home Page
    Given Open Gettop product page
    When Click on "Home" link
    Then Verify Home Page is displayed


  Scenario: Category link takes users to correct category page
    Given Open Gettop product page
    When Click on product category name
    Then Verify correct category page is displayed


  Scenario: Social network logos are present: FB, Twitter, Email, Pinterest LinkedIn
    Given Open Gettop product page
    Then Verify there are 5 social logos present


  Scenario: Clicking on a social network link opens a new window to login to social network
    Given Open Gettop product page
    When Click on a social network link
    When Switch to the newly opened window
    Then Verify new window to login to social network is open
    Then User can close new window and switch back to original