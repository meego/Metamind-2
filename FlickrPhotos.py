
from Utilities import getMergedArray

__author__ = "James Clarke <james@jamesclarke.info>"
__version__ = "$Rev$"
__date__ = "$Date$"
__copyright__ = "Copyright 2004-5 James Clarke"

import math
import flickr


def get_urls_for_tags(tag, number):
    """
        author: Arpeet Kale
    :param tag: the for which to fetch the url for photos
    :param number: the number of photo urls to fetch
    :return: urls array
    """
    try:
        urls = []

        file = open("ImageFiles/" + tag + ".txt", "w")              # open file for writing urls
        photos = flickr.photos_search(tags=tag, per_page=number)    # call the api function

        for photo in photos:
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


# def create_wallpaper(screen, urls, size=(100, 100), randomise=False):
#     if randomise:
#         random.shuffle(urls)
#
#     wallpaper = Image.new("RGB", screen, "blue")
#
#     width = int(math.ceil(float(screen[0]) / size[0]))
#     height = int(math.ceil(float(screen[1]) / size[1]))
#
#     offset = [0,0]
#     for i in xrange(height):
#         y = size[1] * i
#         for j in xrange(width):
#             x = size[0] * j
#             photo = load_photo(urls.pop())
#             if photo.size != size:
#                 photo = photo.resize(size, Image.BICUBIC)
#             wallpaper.paste(photo, (x, y))
#             del photo
#     return wallpaper


# def load_photo(url):
#     file, mime = urllib.urlretrieve(url)
#     photo = Image.open(file)
#     return photo
#
#
# def main(*argv):
#     from getopt import getopt, GetoptError
#
#     try:
#         (opts, args) = getopt(argv[1:], 'w:h:f', ['width', 'height', 'file'])
#     except GetoptError as e:
#         print(e)
#         print(__doc__)
#         return 1
#
#     width = 1024
#     height = 768
#     file = 'wallpaper.jpg'
#
#     for o, a in opts:
#         if o in ('-w', '--width'):
#             width = a
#         elif o in ('-h', '--height'):
#             height = a
#         elif o in ('-f' '--file'):
#             file = a
#         else:
#             print("Unknown argument: %s" % o)
#             print(__doc__)
#             return 1
#
#     if len(args) == 0:
#         print("You must specify at least one tag")
#         print(__doc__)
#         return 1
#
#     tags = [item for item in args]
#
#     screen = (width, height)
#
#     n = photos_required(screen)
#     urls = get_urls_for_tags(tags, n)
#     wallpaper = create_wallpaper(screen, urls, randomise=True)
#     wallpaper.save(file)

if __name__ == '__main__':

    taggedArray = getMergedArray()      # get the top places from both absolute visit and trip advisor

    for tag in taggedArray:
        get_urls_for_tags(tag, 500)
