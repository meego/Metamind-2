__author__ = 'arpeetkale1'

from Utilities import getMergedArray
import requests


def getInstagramTagsCount(tagNameArray):
    """
    :param tagNameArray: hashtag array
    """

    try:
        file = open("InstagramTagsCount.txt", "w")

        print("Tag  \t\t\t\t\t Count")
        print("------------------------------")

        for tag_name in tagNameArray:

            # create url for each hashtag
            url = "https://api.instagram.com/v1/tags/" + tag_name + "?client_id=6cd753ceba494a209edf8459f42f9a37"

            # read the response
            response = requests.get(url).json()

            # extract the count
            data = tag_name + "-" + str(response['data']['media_count'])

            print(data)
            file.write("\n" + data)

        file.close()

    except Exception as e:
        file.close()
        print(e)
    except KeyboardInterrupt as e:
        file.close()
        print(e)


if __name__ == '__main__':

    taggedArray = getMergedArray()          # get the top places from both absolute visit and trip advisor
    getInstagramTagsCount(taggedArray)