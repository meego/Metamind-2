__author__ = 'arpeetkale1'

from PIL import Image
from AbsoluteVisitScraper import getAbsoluteVisitTop100
from TripAdvisorScraper import getTripAdvisorTopPlaces
import re
import pandas as p
import os
import urllib
import time
import numpy as np


def getPhotosFromUrls(path_to_directory):
    """
    This function saves image from url
    :param path_to_directory: directory in which to save image
    """
    try:

        if not os.path.exists(path_to_directory):
            print("Directory does not exists")

        files = os.listdir(path_to_directory + "/")
        print(files)

        i = 0
        for file in files:
            if file.endswith(".txt"):  # get all the text files in directory

                imageDirectory = path_to_directory + "/" + os.path.basename(
                    path_to_directory + "/" + file.split(".")[0])
                print(imageDirectory)
                os.makedirs(imageDirectory)

                fileHandler = open(path_to_directory + "/" + file, encoding='utf-8')  # open each file in read mode

                urls = fileHandler.readlines()  # load all the lines in file in an array

                for url in urls:  # retrieve image from each url and save it
                    if url.strip():
                        print(url)
                        i += 1
                        try:
                            urllib.request.urlretrieve(url, imageDirectory + "/" + str(i) + ".jpg")
                        except urllib.error.HTTPError as e:
                            print(e)
                            pass
                        except urllib.error.URLError as e:
                            print(e)
                            pass

                        time.sleep(1)
            i = 0

    except NotADirectoryError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)
    except KeyboardInterrupt as e:
        print(e)


def imageResize(filename, width, height):
    """
    takes a filename and turns it into a numpy array of RGB pixels
    :param height:
    :param width:
    :param filename:
    """
    STANDARD_SIZE = (width, height)
    img = Image.open(filename)
    img = img.resize(STANDARD_SIZE)
    img.save(filename.split('.')[0] + str(STANDARD_SIZE) + ".jpg")
    return img


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

    absoluteVisitPlacesArray = getAbsoluteVisitTop100()  # get top 100 places from absolute visit
    tripAdvisorPlacesArray = getTripAdvisorTopPlaces()  # get top places from trip advisor

    finalAllPlacesArray.extend(absoluteVisitPlacesArray)  # merge the two arrays
    finalAllPlacesArray.extend(tripAdvisorPlacesArray)

    taggedArray = convertToTag(finalAllPlacesArray)  # convert array elements to hashtag format

    return taggedArray


def readTop100List():
    """
    This function reads the final rank formulated
    list of top 100 places
    """

    data = p.read_csv("/Users/arpeetkale1/Documents/Metamind/top100.csv")

    top100 = data['PLACE']

    return top100


def directoryMetaData(path_to_directory):
    """
    counts the number of sub-directories and files under
    the specified directory
    :param path_to_directory:
    """
    for information in os.walk(path_to_directory):
        print(information[0] + "---" + str(len(information[2])))


if __name__ == '__main__':
    directoryMetaData("path/to/directory")


