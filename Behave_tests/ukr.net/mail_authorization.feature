# Created by VadymStavskyi at 5/23/2017
Feature: Log in into ukr.net account
  Trying to log in into ukr.net account
  using given credentials
  and check if the credentials is working

  Scenario: Log-in into ukr.net account
    Given website "https://mail.ukr.net/"
    When website is loaded
    Then enter the credentials into field e-mail: EMAIL password: PASS


  Scenario: Open the website
    Given website "http://mail.ukr.net/"
    When website is loaded
