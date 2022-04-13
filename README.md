# Lab 17: Web scraping

## Challenge
  - Feature and tasks
     - Scrape a Wikipedia page and record which passages need citations.
     - Your web scraper should report the number of citations needed.
     - Your web scraper should identify those cases AND include the relevant passage.
       - E.g. Citation needed for “lorem spam and impsum eggs”
       - Consider the “relevant passage” to be the parent element that contains the passage, often a paragraph element. 


## Implementation
  - Create a count function named **get_citations_needed_count**
    - get_citations_needed takes in a url and returns an integer of citations needed
  - Create function named **get_citations_needed_report**
    - get_citations_needed_report takes in a url and returns a string
    - the string should be formatted with each citation needed on own line, in order found.

## Pull Request
  - [PR]()