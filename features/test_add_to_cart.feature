Feature: Shopping Cart

  Scenario: Add a single item to the cart
    Given the user is logged in
    When the user adds an item "Sauce Labs Backpack" to the cart
    And the user opens the cart page
    Then the cart contains the item "Sauce Labs Backpack"

  Scenario Outline: Add multiple items to the cart
    Given the user is logged in
    When the user adds an item "<item_name>" to the cart
    And the user opens the cart page
    Then the cart contains the item "<item_name>"

    Examples:
      | item_name    |
      | Sauce Labs Bolt T-Shirt  |
      | Sauce Labs Bike Light |
