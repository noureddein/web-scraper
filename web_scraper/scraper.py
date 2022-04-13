import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'


def get_site_data(URL):
    def _try_open_file():
        with open('page_content.html', 'r') as f:
            page_content = f.read()
            return page_content

    try:
        return _try_open_file()
    except FileNotFoundError:
        response = requests.get(URL)
        html = response.text
        with open('page_content.html', 'w') as f:
            f.write(html)
        return _try_open_file()


def get_paragraphs(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    content_container = soup.find('div', id='mw-content-text')
    all_paragraphs = content_container.find_all('p')
    return all_paragraphs


def get_paragraphs_citation_needed(paragraphs):
    paragraphs_need_citations = []

    for paragraph in paragraphs:
        has_citation = paragraph.find(
            'sup', class_='noprint Inline-Template Template-Fact')
        if has_citation:
            section = has_citation.find_previous_sibling(
                "span")
            print('Section', section)
            paragraphs_need_citations.append(paragraph.get_text())

    return paragraphs_need_citations


def get_citations_needed_count(URL):
    page_content = get_site_data(URL)
    all_paragraphs = get_paragraphs(page_content)
    citations_needed = get_paragraphs_citation_needed(all_paragraphs)

    return len(citations_needed)


def get_citations_needed_report(URL):
    page_content = get_site_data(URL)
    all_paragraphs = get_paragraphs(page_content)
    citations_needed = get_paragraphs_citation_needed(all_paragraphs)

    output = ''
    for paragraph in citations_needed:
        output += f'{paragraph}\n'
    print(output)


get_citations_needed_report(URL)

#! (\.\s\w+)\[((\w+).(\w+))\](\w+\.\s)

# site_data = get_site_data(URL)

# soup = BeautifulSoup(site_data, 'html.parser')

# h2_p = soup.find_all(['h2', 'p'])
# with open('test.html', 'w') as f:
#     f.write(str(h2_p))
