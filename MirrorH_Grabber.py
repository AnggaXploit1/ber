#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import cfscrape
from colorama import Fore, Style, init
from urlparse import urlparse

# Initialize Colorama
init(autoreset=True)

fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.WHITE
fg  =   Fore.GREEN
fm  =   Fore.MAGENTA


print(fm+'''
         ______      __             _       __               __               
        / ____/_  __/ /_  ___  ____| |     / /___ __________/ /__  ____  _____
       / /   / / / / __ \/ _ \/ ___/ | /| / / __ `/ ___/ __  / _ \/ __ \/ ___/
      / /___/ /_/ / /_/ /  __/ /   | |/ |/ / /_/ / /  / /_/ /  __/ / / (__  ) 
      \____/\__, /_.___/\___/_/    |__/|__/\__,_/_/   \__,_/\___/_/ /_/____/  
           /____/                                                             
                      '''+'\033[90m'+'''- Copyright '''+'\033[92m'+'''[2023]'''+'\033[91m'+''' [@ShiroMoriaty]'''+'\033[0m'+fc+''' [MirrorH_Grabber]\n''')

# Function to scrape websites from the specified page range of the archive
def scrape_websites(first_page, last_page):
    scraper = cfscrape.create_scraper()
    domains = set()

    print(Fore.CYAN + "\t\tScraping websites from pages {} to {}...".format(first_page, last_page) + Style.RESET_ALL)

    for page in range(first_page, last_page + 1):
        url = "https://mirror-h.org/archive/page/{}".format(page)
        response = scraper.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            rows = soup.select('tr')

            # Extract the website URLs from the HTML
            for row in rows[1:]:  # Skip the header row
                columns = row.select('td')
                if len(columns) >= 3:
                    web_url = columns[2].text.strip()
                    domain = urlparse(web_url).scheme + '://' + urlparse(web_url).netloc
                    domains.add(domain)

            print(Fore.GREEN + "\t\tScraped websites from page {}: {}".format(page, len(domains)) + Style.RESET_ALL)
        else:
            print(Fore.RED + "\t\tFailed to scrape websites from page {} of the archive.".format(page) + Style.RESET_ALL)

    return domains

# Function to write websites to a file
def write_websites_to_file(domains):
    with open('mirrorHwebsites.txt', 'w') as file:
        for domain in domains:
            file.write(domain + '\n')

# Main function
def main():
    print(Fore.BLUE + "\t\tWebsite Scraper for mirror-h.org Archive" + Style.RESET_ALL)

    # Get user input for page range
    first_page = int(raw_input("\t\tEnter the first page: "))
    last_page = int(raw_input("\t\tEnter the last page: "))

    print(Fore.CYAN + "\t\tScraping websites from the specified page range..." + Style.RESET_ALL)
    domains = scrape_websites(first_page, last_page)

    if domains:
        write_websites_to_file(domains)
        print(Fore.GREEN + "\t\tDomains saved to 'mirrorHwebsites.txt'." + Style.RESET_ALL)
    else:
        print(Fore.RED + "\t\tNo domains to process." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
