# Created by ali at 8/21/23
Feature: see contacts info
  as a user i want to be able to see all of my contacts
  which i saved sofar as a list

  Scenario: get list of contacts
    Given some user wants to see all of her contacts
    When she ask for contact list
    Then she shall see a list of contacts