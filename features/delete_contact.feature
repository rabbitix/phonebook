# Created by ali at 8/20/23
Feature: delete a contact
  as a user of system i want to be able to delete a contact so it no longer show in my list

  Scenario: deleting a contact
    Given some user wants to delete a contact
    When she want to delete contact with id 2
    Then their desired contact should delete successfully

  Scenario: deleting a non existing contact
    Given some user wants to delete a contact that does not exist
    When she want to delete contact with id 80
    Then their desired contact does not exist and should show error code 404