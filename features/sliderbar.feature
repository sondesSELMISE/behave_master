Feature: progress bar

  Scenario: progress succesffully
    Given Then user navigate to the URL https://qavbox.github.io/demo/dragndrop/
    When he move the slider bar to 100
    Then he see the message success progress!
