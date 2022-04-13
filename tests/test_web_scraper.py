from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report
import re


URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'


def test_citations():
    actual = get_citations_needed_count(URL)
    expected = 4
    assert actual == expected


def test_number_of_citation_in_page():
    paragraphs = get_citations_needed_report(URL)
    reg = r'\[((\w+).(\w+))\]'

    actual = len(re.findall(reg, paragraphs))
    expected = 5
    assert actual == expected
