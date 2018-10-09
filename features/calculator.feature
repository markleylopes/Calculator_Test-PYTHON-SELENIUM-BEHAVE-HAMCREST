Feature: Calculator

Scenario: Adding numbers

When I click in the number 9
Then I see number 9 in viewer

When I click on [+]
Then I see number 9 in viewer, too

When I click in the number 8
Then I see number 8 in viewer

When I click on [=]
Then The system returns 17


Scenario: Subtracting numbers

When I click in the number 1 and 0
Then I see number 10 in viewer

When I click on [-]
Then I see number 10 in viewer, too

When I click in the number 7
Then I see number 7 in viewer

When I click on [=] button
Then The system returns 3


Scenario: Dividing numbers

When I click on the numbers 1, 5, 5
Then I see number 155 in viewer

When I click on [/]
Then I see number 155 in viewer, too

When I click in the number 5
Then I see number 5 in viewer

When I click on [ = ] button
Then The system returns 31


Scenario: Multiplying numbers

When I click on the numbers 1, 5, 3
Then I see number 153 in viewer

When I click on [*]
Then I see number 153 in viewer, too

When I click in the number 6
Then I see number 6 in viewer

When I click on [ =] button
Then The system returns 918



