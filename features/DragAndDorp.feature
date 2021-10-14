@Severity(SeverityLevel.MINOR)
Feature: drag and drop

  Scenario: dropped succesffully
    Given Then user navigate to the URL https://qavbox.github.io/demo/dragndrop/
    When he move the drag box to drop box
    Then he see the message change to Dropped!



