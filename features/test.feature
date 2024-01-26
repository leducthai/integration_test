# content of publish_article.feature

Feature: report excel
    report excel file.

    Scenario: get excel report file failed
        Given I create an API POST request
        And the endpoint is '/excel/export'
        And the headers are:
        | Key         | Value                    |
        | Content-Type | application/json         |
        | Authorization| token goes here if exist   |
        And the request params are:
        | year | 2023 |
        | week | 23 |

        When I send request

        Then The status code should be 500