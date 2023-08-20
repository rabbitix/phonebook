# Created by ali at 8/20/23
Feature: add a new contact
  as a user i want to create a contact with first-name, last-name and nick-name
  so that later i can see them and have them.

  Scenario: successful contact creation
    Given some user wants to add a new contact to their phonebook
    When she provide first-name last-name and nick-name
    Then their contact should successfully added to the phonebook

  Scenario: unsuccessful contact creation
    Given some user wants to add a new contact to their phonebook
    When she do not provide first-name of the contact
    Then their contact should not added to the phonebook