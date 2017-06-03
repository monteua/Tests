# Created by VadymStavskyi at 5/22/2017
Feature: Checking search


  Scenario: Enter some text to search box
    Given website "http://google.com/"
    When website is open
    Then enter the "Python" into search box