__author__ = 'arpeetkale1'

from bs4 import BeautifulSoup
from http.cookiejar import CookieJar
import urllib

cj = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

startingLink = 'http://www.tripadvisor.com'


def getTripAdvisorTopPlaces():

    """
    This function scrapes tripadvisor.com and retrieves the top places

    :return: array of top places
    """
    try:
        file = open("TripAdvisorTopList.txt", "w")
        topPlaces = []
        categoryArray = ['TravelersChoice-Beaches-cTop-g1', 'TravelersChoice-Destinations-cTop-g1',
                         'TravelersChoice-Attractions-cTop-g1', 'TravelersChoice-Islands-cTop-g1',
                         'TravelersChoice-DestinationsontheRise-cTop-g1']

        for category in categoryArray:

            file.write('\n' + category)     # write the category in file

            categorySourceCode = opener.open(startingLink + '/' + category).read()  # read the source code for each category

            soup = BeautifulSoup(categorySourceCode)
            tags = soup.find_all('a', attrs={"target": "_blank"}, text=True)    # find the right html element

            for node in tags:
                htmlElementClass = node.parent.attrs

                if 'mainName' in htmlElementClass['class']:
                    place = ''.join(node.findAll(text=True))    # extract text from the html element which is a place name
                    file.write("\n" + place)    # write the place name in file
                    topPlaces.append(place)     # append to the array

            file.write("\n")

        file.close()
        return topPlaces

    except Exception as e:
        print(str(e))
        print('error in main')

if __name__ == '__main__':
    getTripAdvisorTopPlaces()