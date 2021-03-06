import requests
from bs4 import BeautifulSoup


class GoogleNews:

    def __init__(self, userAgent):
        """
        ### GoogleNews
        Create new instance of google news.
        """
        self.header = {"User-Agent": userAgent}

    def getTopStories(self):
        """
        ### getTopStories( )
        return top stores headlines from google news.
        #### Return Type : `list()`
        """
        content = requests.get('https://rb.gy/ndlov9', headers=self.header).content
        pageSource = BeautifulSoup(content, "html.parser")
        newsList = []
        for i in pageSource.find_all(class_='DY5T1d'):
            newsList.append(i.get_text())
        return newsList

    def getForYou(self):
        """
        ### getTopStories( )
        return headlines recommended based on your interests.
        #### Return Type : `list()`
        """
        content = requests.get('https://rb.gy/cj4y19', headers=self.header).content
        page_source = BeautifulSoup(content, "html.parser")
        newsList = []
        for i in page_source.find_all(class_='DY5T1d'):
            newsList.append(i.get_text())
        return newsList

    def getCoronaNews(self):
        """
        ### getCoronaNews( )
        return headlines of corona news.
        #### Return Type : `list()`
        """
        content = requests.get('https://rb.gy/qcr9hl', headers=self.header).content
        pageSource = BeautifulSoup(content, "html.parser")
        newsList = []
        for i in pageSource.find_all(class_='DY5T1d'):
            newsList.append(i.get_text())
        return newsList

    def getCountryNews(self):
        """
        ### getCountryNews( )
        return headlines of your country.
        #### Return Type : `list()`
        """
        content = requests.get('https://rb.gy/wasqbr', headers=self.header).content
        pageSource = BeautifulSoup(content, "html.parser")
        newsList = []
        for i in pageSource.find_all(class_='DY5T1d'):
            newsList.append(i.get_text())
        return newsList

    def getWorldNews(self):
        """
        ### getWorldNews( )
        return headlines of world.
        #### Return Type : `list()`
        """
        content = requests.get('https://rb.gy/al7v06', headers=self.header).content
        pageSource = BeautifulSoup(content, "html.parser")
        newsList = []
        for i in pageSource.find_all(class_='DY5T1d'):
            newsList.append(i.get_text())
        return newsList

    def getTechnologyNews(self):
        """
        ### getTechnologyNews( )
        return headlines of technology.
        #### Return Type : `list()`
        """
        content = requests.get('https://rb.gy/m4jclu', headers=self.header).content
        pageSource = BeautifulSoup(content, "html.parser")
        newsList = []
        for i in pageSource.find_all(class_='DY5T1d'):
            newsList.append(i.get_text())
        return newsList

    def getEntertainmentNews(self):
        """
        ### getEntertainmentNews( )
        return headlines of entertainment.
        #### Return Type : `list()`
        """
        content = requests.get('https://rb.gy/s78u6n', headers=self.header).content
        pageSource = BeautifulSoup(content, "html.parser")
        newsList = []
        for i in pageSource.find_all(class_='DY5T1d'):
            newsList.append(i.get_text())
        return newsList

    def getSportsNews(self):
        """
        ### getSportsNews( )
        return headlines of sports.
        #### Return Type : `list()`
        """
        content = requests.get('https://rb.gy/nyv5as', headers=self.header).content
        pageSource = BeautifulSoup(content, "html.parser")
        newsList = []
        for i in pageSource.find_all(class_='DY5T1d'):
            newsList.append(i.get_text())
        return newsList

    def getScienceNews(self):
        """
        ### getScienceNews( )
        return headlines of science.
        #### Return Type : `list()`
        """
        content = requests.get('https://rb.gy/9r5k0w', headers=self.header).content
        pageSource = BeautifulSoup(content, "html.parser")
        newsList = []
        for i in pageSource.find_all(class_='DY5T1d'):
            newsList.append(i.get_text())
        return newsList

    def getHealthNews(self):
        """
        ### getHealthNews( )
        return headlines of health.
        #### Return Type : `list()`
        """
        content = requests.get('https://rb.gy/ee2r4a', headers=self.header).content
        pageSource = BeautifulSoup(content, "html.parser")
        newsList = []
        for i in pageSource.find_all(class_='DY5T1d'):
            newsList.append(i.get_text())
        return newsList
