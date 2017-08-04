import scraper
from bs4 import BeautifulSoup

all_links = []
output_file = "problems.txt"


def first_page_links():
    data = scraper.get_data("http://codingbat.com/java", 'temp.txt')
    soup = BeautifulSoup(data, 'lxml')

    categories = soup.find_all('div', attrs={'class': 'summ'})

    rel_links = ['http://codingbat.com'+item.a['href'] for item in categories]
    return rel_links


def find_links():
    for link in first_page_links():

        data = scraper.get_data(link, 'test.txt')
        soup = BeautifulSoup(data, 'lxml')

        td = soup.find("div", class_="indent").table.find_all('td')
        for item in td:
            temp = item.find_all('a')
            for link in temp:
                all_links.append(('http://codingbat.com' + link['href']))


def write_output():
    output = open(output_file, "a+")

    for link in all_links:
        main_string = []

        data = scraper.get_data(link, 'temp.txt')
        soup = BeautifulSoup(data, 'lxml')

        main = soup.find("div", class_="minh")
        main_string.append(str(main.string) + "\n")
        for br_tag in main.parent.find_all('br'):
            main_string.append(str(br_tag.next_sibling))

        del main_string[-1]
        for item in main_string:
            output.write(item)
            output.write("\n")
        output.write("\n\n")

    output.close()


if __name__ == "__main__":
    find_links()
    write_output()
