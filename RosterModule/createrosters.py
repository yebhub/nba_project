from bs4 import BeautifulSoup
from requests import get

class RosterCreator():

    def __init__(self, url, filename):
        self.url = url
        self.filename = filename



    def scrape_playernames(self):
        names = []
        response = get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")
        scraped_names = soup.find_all(attrs={"class": "sortcell"})

        for name in scraped_names:
            names.append(name.text)
        return(names)


    def create_roster(self, scraped_names):
        with open(self.filename, "w") as rosterfile_object:
            for name in scraped_names:
                rosterfile_object.write(name.title() + "\n")
