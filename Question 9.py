# Question 9 - Extract tabular data from a webpage and store it in a structured format.

# ***(currently not outputting the right result.)***
#=======================================================================================

from bs4  import BeautifulSoup
import requests
import csv


def load_soup(data_url):
    # Scraps the wiki website and puts the data into a "soup".
    headers = {"User-Agent": "Mozilla/5.0"}
    wiki_contents = requests.get(data_url, headers=headers)

    return BeautifulSoup(wiki_contents.text, "html.parser")


def extract_table(soup):
    # Finds the first table that has more than three rows.
    wiki_content = soup.find("div", id="mw-content-text")
    tables = wiki_content.find_all("table")

    for table in tables:
        rows = table.find_all("tr")

        data_rows_count = 0
        for row in rows:
            if row.find_all("td"):
                data_rows_count += 1

        if data_rows_count >= 3:

            return table


def parse_table(table):
    # Prepares the table so it could be created as a csv file.
    rows = table.find_all("tr")

    extracted_rows = []

    for row in rows:
        cells = row.find_all(["td", "th"])
        row_data = [cell.get_text(strip=True) for cell in cells]
        if row_data:
            extracted_rows.append(row_data)

    max_columns = max(len(r) for r in extracted_rows)

    header_cells = rows[0].find_all("th")

    if header_cells:
        headers = [cell.get_text(strip=True) for cell in header_cells]
        extracted_rows = extracted_rows[1:]
    else:
        headers = [f"col{i+1}" for i in range(max_columns)]

    padded_rows = []
    for row in extracted_rows:
        while len(row) < max_columns:
            row.append("")
        padded_rows.append(row)

    return headers, padded_rows


def create_wiki_table_csv(headers, rows):
    # Creates the table csv from the header list and row list.
    with open("wiki_table.csv", "w", newline="") as table_file:
        table_writer = csv.writer(table_file)
        table_writer.writerow(headers)
        table_writer.writerows(rows)

# ================================================================================

def main():
    wiki_page = "https://en.wikipedia.org/wiki/Machine_learning"

    machine_learning_soup = load_soup(wiki_page)

    machine_learning_table = extract_table(machine_learning_soup)

    table_headers, padded_rows = parse_table(machine_learning_table)

    create_wiki_table_csv(table_headers, padded_rows)

main()




