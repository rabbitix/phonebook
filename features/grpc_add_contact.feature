Feature: add a contact with gRPC
  as a microservice in the system i want to be able to create a contact
  using and calling to gRPC service

  Scenario: make a new contact
    Given some service wants to add a new contact
    When the service call the ContactService to use AddContact service and provide some data
    Then the contact should be added successfully and gives back a message
