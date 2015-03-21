__author__ = 'arpeetkale1'

from bs4 import BeautifulSoup
from http.cookiejar import CookieJar
import urllib
import re

cj = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

startingLink = 'http://www.absolutevisit.com'
top100 = []


def getAbsoluteVisitTop100():

    """
    This function scrapes absolutevisit.com and retrieves the top 100
    places mentioned on the site.

    :return:
    """
    try:
        file = open("AbsoluteVisitTopList.txt", "w")    # open file for writing
        sourceCode = opener.open(startingLink).read()   # read the source code of the html page

        soup = BeautifulSoup(sourceCode)
        tags = soup.find_all('a', attrs={"class": "top100"}, text=True)  # find the element where top 100 places are listed

        for node in tags:

            nodeContent = str(node.findAll(text=True))
            cleanedContent = ''.join(re.findall('[a-zA-Z ]', nodeContent))  # extract only words
            file.write("\n" + cleanedContent)                               # write to file
            top100.append(cleanedContent)                                   # append in array

        file.close()                                                        # close file after writing
        return top100

    except Exception as e:
        print(str(e))
        print('error in main')


if __name__ == '__main__':
    getAbsoluteVisitTop100()
