import requests
from bs4 import BeautifulSoup
from lxml import etree

def scrape(id):
    url = f"https://cameochemicals.noaa.gov/chemical/{id}"
    response = requests.get(url = url)
    if response.status_code != 404:  
        soup = BeautifulSoup(response.content, 'html5lib')
        dom = etree.HTML(str(soup))
        name_xpath = "/html/body/div[2]/table[1]/tbody/tr/td[1]/h1"
        cas_num_xpath = "/html/body/div[2]/table[2]/tbody[1]/tr/td[1]/ul/li"
        if dom.xpath(name_xpath):
            name = str(dom.xpath(name_xpath)[0].text)
        else:
            name = None
        if dom.xpath(cas_num_xpath):
            cas_number = str(dom.xpath(cas_num_xpath)[0].text).split(" ")[0]
        else:
            cas_number = None

        chemical = {
            "name": name,
            "cas_number": cas_number
        }
        return chemical
    else:
        print(f"Page not found on page id: {id}")
        return None