# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
from bs4 import BeautifulSoup as bs

URL = "https://helpix.ru/currency/"


def parse_site():
    list_elements = []
    page = requests.get(URL)
    soup = bs(page.content, "html.parser")
    elements = soup.find_all("tr", class_="b-tabcurr__tr")
    for i in range(9):
        for element in elements:
            for y in range(2):
                if element =
            list_elements.append(element)

    for i in range(2):

    print(list_elements)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parse_site()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
