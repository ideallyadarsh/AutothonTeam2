@ActivateOffer

Feature: Activate an Offer
  	
  Scenario: Activate an Offer
    Given User logs into the application

    # Activate an Offer
    When User navigates to the Rewards section and click on For You tab
    And Validate if offer is activated 
    And Validate activated offers
    And Validate my activated offers in mycard section

    # Deactivate an Offer
    When User navigates to the Rewards section and click on For You tab
    And Validate if offer is deactivated
    And Validate deactivated offers
    And Validate my deactivated offers in mycard section