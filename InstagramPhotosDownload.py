__author__ = 'arpeetkale1'

import requests
import time
import os


def getInstagramPhotoURL(tag_name):

    """
    :param tag_name: tag for which to fetch the urls
    """
    try:
        # instagram api endpoint
        url = "https://api.instagram.com/v1/tags/" + tag_name + "/media/recent?client_id=6cd753ceba494a209edf8459f42f9a37"

        # read the response
        response = requests.get(url).json()

        count = 0

        # create directory to store location url files
        if not os.path.exists("InstagramImageURLFiles"):
            os.makedirs("InstagramImageURLFiles")

        # create a text file for each location to store its urls
        file = open("InstagramImageURLFiles/" + tag_name + ".txt", "w")

        while True:
            # fetch 500 urls
            if 'next_url' in response['pagination'] and count < 500:

                url = response['pagination']['next_url']
                response = requests.get(url).json()

                for item in response['data']:
                    url = item['images']['standard_resolution']['url']
                    print(url)
                    file.write("\n" + url)  # write the url in file
                    count += 1

                time.sleep(2)

            else:
                break

        file.close()
        print("Total Count: " + str(count))

    except Exception as e:
        file.close()
        print("Total Count: " + str(count))
        print(e)
    except KeyboardInterrupt as e:
        file.close()
        print("Total Count: " + str(count))
        print(e)
    except KeyError as e:
        file.close()
        print("Total Count: " + str(count))
        print(e)

if __name__ == '__main__':

    getInstagramPhotoURL("AntarticaCruise")


