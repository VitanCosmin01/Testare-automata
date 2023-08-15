Feature: Check the functionality of login page
  # Scenariu 1: username corect + parola corecta
  # Scenariu 2: username corect + parola incorecta
  # Scenariu 3: username incorect + parola corecta
  # Scenariu 4: username corect + parola none
  # Scenariu 5: username none + parola corecta
  # Scenariu 6: username none + parola none
  # Scenariu 7: username incorect + parola none
  # Scenariu 8: username none + parola incorecta
  # Scenariu 9: username incorect + parola incorecta
  # Scenariu 10: username blocat + parola corecta

  @valid_login
  Scenario: Succes login
    Given I am on the saucedemo login page
    When I insert the correct username and correct password
    And I click the login button
    Then I can login into the application and see the list of products

  @invalid_login
  Scenario: Check login functionality when username is valid but password is invalid
    Given I am on the saucedemo login page
    When I insert the correct username and incorrect password
    And I click the login button
    Then I can't login into the application and receive error Epic sadface: Username and password do not match any user in this service
    