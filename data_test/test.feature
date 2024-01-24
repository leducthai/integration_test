# content of publish_article.feature

Feature: report excel
    report excel file.

    Scenario: get excel report file failed
        Given I do notthing

        When I go to the API "http://stage.gah.gbcvn2.local:4481/excel/export"

        Then The status code should be 500