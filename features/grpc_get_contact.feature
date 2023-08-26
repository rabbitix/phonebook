Feature: get a contact with gRPC
  as a microservice in the system i want to be able to retrieve a contact
  calling a gRPC service

  Scenario: retrieve a contact
    Given some service wants to retrieve a contact
    When the service call the ContactService to use GetContact service and provide contact_id 2
    Then the service should be able to see the contact information
