# Question 8 - Extracting structured heading information from webpage.

from bs4  import BeautifulSoup
import requests

def load_soup(data_url):
    # Scraps the wiki and combines all the data into a "soup".
    headers = {"User-Agent": "Mozilla/5.0"}
    wiki_contents = requests.get(data_url, headers=headers)

    return BeautifulSoup(wiki_contents.text, "html.parser")


def extract_headings(soup):
    # Finds the headings from the soup, and puts them into a list.
    headings_content = soup.find("div", id="mw-content-text")

    headings = []

    for h2 in headings_content.find_all("h2"):
        heading_text = h2.get_text(strip=True)

        headings.append(heading_text)

    return headings


def clean_headings(unclean_headings):
    # Cleans the headings from excluded words.
    excluded_words = ["References", "External links", "See also", "Notes"]
    final_headings = []

    for heading in unclean_headings:
        heading = heading.replace("[edit]", "").strip()

        if heading in excluded_words:
            continue

        final_headings.append(heading)

    return final_headings


def create_headings_file(headings_list):
    # Creates a file with the headings in the file in order.
    with open("headings.txt", "w") as headings_file:
        for heading in headings_list:
            headings_file.write(heading + "\n")

# =======================================================================================

def main():
    wiki_page = "https://en.wikipedia.org/wiki/Data_science"

    data_science_soup = load_soup(wiki_page)

    unclean_headings = extract_headings(data_science_soup)

    final_headings = clean_headings(unclean_headings)

    create_headings_file(final_headings)


main()