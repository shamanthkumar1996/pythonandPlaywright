Feature: Order Transcations
    Tests related to order Transcations

Scenario: Create an order Transcations
    Given place the item order with user1 and pass1
    And the user is on landing page
    When I Login to portal with user1 and pass1
    And navigate to orders page
    And select the orderId

