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

# Scenariu 1: username corect + parola corecta

@invalid_login1
  Scenario: Succes login
    Given I am on the saucedemo login page
    When I insert the correct username and correct password
    And I click the login button
    Then I can login into the application and see the list of products

# Scenariu 2: username corect + parola incorecta

@invalid_login2
  Scenario: Check login functionality when username is valid but password is invalid
    Given I am on the saucedemo login page
    When I insert the correct username and incorrect password
    And I click the login button
    Then I can't login into the application and receive error Epic sadface: Username and password do not match any user in this service

# Scenariu 3: username incorect + parola corecta

@invalid_login3
  Scenario: Check login functionality when username is invalid but password is valid
    Given I am on the saucedemo login page
    When I insert the incorrect username and correct password
    And I click the login button
    Then I can't login into the application and receive error Epic sadface: Username and password do not match any user in this service

# Scenariu 4: username corect + parola none

@invalid_login4
  Scenario: Check login functionality when username is valid but password is none
  Given I am on the saucedemo login page
  When I insert the valid username and  no password
  And I click the login button
  Then I can't login into the application and receive error Epic sadface: Password is required

# Scenario 5: username none + parola corecta

@invalid_login5
  Scenario: Check login functionality when username is none and password is valid
  Given I am on the saucedemo login page
  When I insert username none and a valid password
  And I click the login button
  Then I can't login into the application and receive error Epic sadface: Username is required

# Scenariu 6: username none + parola none

@invalid_login6
  Scenario: Check login functionality when username is none and password is none
  Given I am on the saucedemo login page
  When I insert username none and password none
  And I click the login button
  Then I can't login into the application and receive error Epic sadface: Username is required

# Scenariu 7: username incorect + parola none

@invalid_login7
  Scenario: Check login functionality when username is incorrect and password is none
  Given I am on the saucedemo login page
  When I insert incorrect username and password is none
  And I click the login button
  Then I can't login into the application and receive error Epic sadface: Password is required