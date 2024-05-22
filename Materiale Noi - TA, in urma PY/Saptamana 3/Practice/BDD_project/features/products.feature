Feature: Check the functionality of item/product page
  # Scenariu 1: Check if clicking the item's name goes on the product page
  # Scenariu 2: Check if clicking on item's picture goes on the product page
  # Scenariu 3: Check the button "Add to cart"
  # Scenariu 4: Check the button "Remove"
Background:
  Given I am on the product's page

@name
Scenario: Checking the product's name
  When I click on the product's name
  Then I go to product's detailpage

@picture
Scenario: Checking the product's picture
  When I click on the product's picture
  Then I go to product's detailpage

@kart_in
Scenario: Adding to cart
  When I click the button Add to cart
  Then The product is added to the cart

@kart_out
Scenario: Deleting item
  When I click the button Remove
  Then The item is deleted from kart