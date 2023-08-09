# Author: Pari Malam

import requests
import os
import random
import urllib3
import warnings
from sys import stdout
from bs4 import BeautifulSoup
from colorama import Fore

FY = Fore.YELLOW
FG = Fore.GREEN
FR = Fore.RED
FW = Fore.WHITE
FC = Fore.CYAN
RC = Fore.RESET

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def traffic():
    clear()
    stdout.write("                                                                                         \n")
    stdout.write(""+Fore.LIGHTRED_EX +"██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗███████╗ ██████╗ ██████╗  ██████╗███████╗   ██╗ ██████╗ \n")
    stdout.write(""+Fore.LIGHTRED_EX +"██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝   ██║██╔═══██╗\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║     █████╗     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██║     ╚██████╔╝██║  ██║╚██████╗███████╗██╗██║╚██████╔╝\n")
    stdout.write(""+Fore.LIGHTRED_EX +"╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝╚═╝ ╚═════╝ \n")
    stdout.write(""+Fore.YELLOW +"═════════════╦═════════════════════════════════╦════════════════════════════════════════════════════════════\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════╩═════════════════════════════════╩═════════════════════════════╗\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"AUTHOR             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   PARI MALAM                                    "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"GITHUB             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   GITHUB.COM/PARI-MALAM                         "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════════════════════════════════════════════════════════════════════╝\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"OFFICIAL FORUM     "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   DRAGONFORCE.IO                                "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"OFFICIAL TELEGRAM  "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   @DRAGONFORCE.IO                               "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╚════════════════════════════════════════════════════════════════════════════╝\n") 
    print(f"{FY}[SEO] - {FG}Perform with Mass Traffic Seo Checkers!\n")
traffic()

BASE_URL = "https://www.scrolltotop.com/MozRank-Domain-Authority-Checker.php"
BASE_URL_TRAFFIC = "http://www.statshow.com/www/{site}"

def create_results_directory():
    if not os.path.exists('Results'):
        os.mkdir('Results')

def read_user_agents():
    with open("lib/ua.txt", "r") as ua_file:
        user_agents = [ua.strip() for ua in ua_file.readlines() if ua.strip()]
    return user_agents

def add_https_prefix(domain):
    if not domain.startswith("https://"):
        return f"https://{domain}"
    return domain

def get_valid_filename():
    while True:
        filename = input(f"{FY}[Filename]: {FG}")
        if not filename.endswith(".txt"):
            print(f"{FR}Please enter a valid .txt file.")
        elif not os.path.exists(filename):
            print(f"{FR}Invalid filename. Please enter a valid filename.")
        else:
            return filename

def read_domains_from_file(filename):
    with open(filename, "r") as file:
        domains = [domain.strip() for domain in file.readlines() if domain.strip()]
    return domains

def check_mozrank(site, headers):
    user_agents = read_user_agents()
    headers = {'user-agent': random.choice(user_agents)}
    try:
        payload = {"url_form": site}
        response_mozrank = requests.post(BASE_URL, headers=headers, data=payload, verify=True)
        response_mozrank.raise_for_status()

        if response_mozrank.status_code == 200:
            soup = BeautifulSoup(response_mozrank.text, "html.parser")
            table = soup.select_one('div[style*="margin: auto; width: 75%; min-width: 400px"] table')
            if table:
                table_rows = table.select('tbody tr')
                if table_rows:
                    row_data = [cell.text.strip() for cell in table_rows[0].find_all('td')]
                    return row_data
                else:
                    print(f"{FY}[SEO] - {FW}No table rows found for MozRank data - {FR}[Failed]")
            else:
                print(f"{FY}[SEO] - {FW}Cannot Extract MozRank Domain Authority - {FR}[Failed]")
        else:
            print(f"{FY}[SEO] - {FW}Get Ranked & DA for URL: {site} - {FR}[Failed]")
    except requests.exceptions.RequestException as e:
        print(f"{FY}[SEO] - {FR}An error occurred while making the MozRank request: {e}")

    return None

def check_site_traffic(site, headers):
    response_traffic = requests.get(BASE_URL_TRAFFIC.format(site=site), headers=headers, verify=True)
    if response_traffic.status_code == 200:
        content = response_traffic.text
        try:
            content_one = content.split('Daily Pageviews: <span class="red_bold">')[1].split('</span>')[0]
            content_two = content.split('Monthly Pageviews: <span class="red_bold">')[1].split('</span>')[0]
            content_three = content.split('Monthly Visitors: <span class="red_bold">')[1].split('</span>')[0]
            return content_one, content_two, content_three
        except IndexError:
            print(f"{FY}[SEO] - {FR}Failed to extract data for site: {site}")

    print(f"{FR}Failed to get data for site: {site}")
    return None, None, None

def write_print(site, mozrank_data):
    filename = f"Results/Traffics.txt"
    with open(filename, "a") as file:
        file.write(f"Domain                : {site}\n")
        file.write(f"ID                    : {mozrank_data[0]}\n")
        file.write(f"Domain Authority      : {mozrank_data[2]}\n")
        file.write(f"Page Authority        : {mozrank_data[3]}\n")
        file.write(f"MozRank               : {mozrank_data[4]}\n")
        file.write(f"BackLinks             : {mozrank_data[5]}\n")

    print(f"{FW}ID                    : {FG}{mozrank_data[0]}")
    print(f"{FW}Domain                : {FG}{mozrank_data[1]}")
    print(f"{FW}Domain Authority      : {FG}{mozrank_data[2]}")
    print(f"{FW}Page Authority        : {FG}{mozrank_data[3]}")
    print(f"{FW}MozRank               : {FG}{mozrank_data[4]}")
    print(f"{FW}BackLinks             : {FG}{mozrank_data[5]}\n")

def writes_prints(site, content_one, content_two, content_three):
    filename = f"Results/Traffics.txt"
    with open(filename, "a") as file:
        file.write(f"Domain                : {site}\n")
        file.write(f"Daily visitor         : {content_one}\n")
        file.write(f"Monthly Page Visitor  : {content_two}\n")
        file.write(f"Monthly Visitors      : {content_three}\n")
        file.write(".++========================================++.\n")

    print(f"{FW}Daily visitor         : {FG}{content_one}")
    print(f"{FW}Monthly Page Visitor  : {FG}{content_two}")
    print(f"{FW}Monthly Visitors      : {FG}{content_three}\n")
    print(f"{FR}.++========================================++.\n")

def main():
    create_results_directory()
    filename = get_valid_filename()
    sites_to_check = read_domains_from_file(filename)
    user_agents = read_user_agents()

    if sites_to_check:
        headers = {'user-agent': random.choice(user_agents)}
        for site in sites_to_check:
            site = add_https_prefix(site)
            print(f"{FY}[SEO] - {FW}{site} - {FG}[CHECKING]\n")
            mozrank_data = check_mozrank(site)
            if mozrank_data:
                write_print(site, mozrank_data)
            content_one, content_two, content_three = check_site_traffic(site, headers)
            if content_one and content_two and content_three:
                writes_prints(site, content_one, content_two, content_three)

if __name__ == "__main__":
    main()
