__author__ = 'arpeetkale1'

from AbsoluteVisitScraper import getAbsoluteVisitTop100
from TripAdvisorScraper import getTripAdvisorTopPlaces
import re
import pandas as p


def convertToTag(array):
    """
    :param array: array to convert into hashtag
    """
    tagsArray = []
    for element in array:
        if ',' in element:
            # extract text before comma if comma present in the string
            cleanedElement = ''.join(re.findall("[a-zA-z]", element.split(",", 1)[0]))
        else:
            cleanedElement = ''.join(re.findall("[a-zA-z]", element))

        tagsArray.append(cleanedElement)  # append in the array

    return tagsArray


def getMergedArray():
    """
    This function merges the two arrays of top place from absolutevisit.com
    and tripadvisor

    """
    finalAllPlacesArray = []

    absoluteVisitPlacesArray = getAbsoluteVisitTop100()     # get top 100 places from absolute visit
    tripAdvisorPlacesArray = getTripAdvisorTopPlaces()      # get top places from trip advisor

    finalAllPlacesArray.extend(absoluteVisitPlacesArray)    # merge the two arrays
    finalAllPlacesArray.extend(tripAdvisorPlacesArray)

    taggedArray = convertToTag(finalAllPlacesArray)         # convert array elements to hashtag format

    return taggedArray


def readTop100List():
    """
    This function reads the final rank formulated
    list of top 100 places
    """

    data = p.read_csv("/Users/arpeetkale1/Documents/Metamind/top100.csv")

    top100 = data['PLACE']

    return top100