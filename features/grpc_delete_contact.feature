Feature: delete a contact with gRPC
  as a microservice in the system i want to be able to delete a contact
  calling the gRPC service for it

  Scenario: delete a contact
    Given some service wants to delete a contact
    When the service call the ContactService to use DeleteContact service and provide contact id 2
    Then the contact should be deleted successfully and gives back a message
