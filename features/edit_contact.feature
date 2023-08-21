# Created by ali at 8/20/23
Feature: edit a contact
  as a user i want to change and update some part of a contact
  so it be updated with new data

  Scenario: edit contact successfully
    Given some user wants to edit a contact
    When she wants to update contact with id 1 and set first-name to "Reza"
    Then their contact should be updated successfully