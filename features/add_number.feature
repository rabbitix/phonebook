
Feature: add a number to a contact
  as a user i want to be able to add a number to one of my contacts
  so i have that number in list of numbers for that contact

  Scenario: add a full number to a contact
    Given some user wants to add a number to a contact
    When she want to add a new number to cantact with id 1
    Then their number will added to contact successfully

  Scenario: add a number to contact with only phone number
    Given some user wants to add a number to a contact
    When she wants to add number to contact with id 1 and only provide phone as '09123456789'
    Then their number will add with a default label

