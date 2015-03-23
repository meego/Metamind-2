from Utilities import convertToTag, readTop100List, getPhotosFromUrls

__author__ = 'arpeetkale1'

import math
import flickr
import urllib
import os
import time


def get_urls_for_tags(tag, number):
    """
    :param tag: the for which to fetch the url for photos
    :param number: the number of photo urls to fetch
    :return: urls array
    """
    try:
        urls = []
        i = 0
        path_to_directory = "ImageFiles"

        if not os.path.exists(path_to_directory):
            os.makedirs(path_to_directory)

        file = open(path_to_directory + "/" + tag + ".txt", "w")    # open file for writing urls
        photos = flickr.photos_search(tags=tag, per_page=number)    # call the api function

        for photo in photos:
            i += 1
            url = photo.getURL(size='Medium', urlType='source')     # specify the size and source for url
            print("\n" + url)
            file.write("\n" + url)                                  # write url in file
            urls.append(url)                                        # append in array

        file.close()
        return urls

    except Exception as e:
        print(e)
    except KeyboardInterrupt as e:
        print(e)


def photos_required(screen, size=(100, 100)):
    """screen is tuple (width, height)
    :param screen:
    :param size:
    """
    width = int(math.ceil(float(screen[0]) / size[0]))
    height = int(math.ceil(float(screen[1]) / size[1]))
    return width * height


if __name__ == '__main__':

    #taggedArray = convertToTag(readTop100List())
    #print(taggedArray)

    #for tag in taggedArray:
    #    get_urls_for_tags(tag, 500)

    getPhotosFromUrls("ImageFiles")