from Utilities import getMergedArray

__author__ = 'arpeetkale1'

from twython import Twython
import time

consumer_key = "0s0g1AjSdS8y3AoUqtFfIQzzR"
consumer_secret = "NXA5iCPvjdleQNcQoy1v2ChxyDVF0BnRXfxT377zaMQucx3oOA"
access_token = "549310508-tmb13czuhJcaPThryxs0owx1ie0Hu8Lbyr6EmSm1"
access_token_secret = "XWRjdQRFjHr5dPPcXBiDsp3rqsAN50G0Jvj7kxZf9EbYC"

file = open("TwitterHashTagCount.txt", "w")
twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)


def getTwitterHashTagCount(tag):
    """
    :param tag: the tag for which to fetch the count
    """
    next_max_id = 0
    count = 0
    max_id = 0
    hashtag = "#" + tag.lower()

    results = twitter.search(q=hashtag, lang="en", count='100')

    # search_metadata json object has the id from which to start the fetching the next set of tweets
    if 'next_results' in results['search_metadata']:
        max_id = (results['search_metadata']['next_results']).split('max_id=')[1].split('&')[0]     # get only the value of max_id

    count += len(results['statuses'])   # count the tweets returned

    try:

        while True:

            if max_id != next_max_id:   # if there are still more tweets then fire the query again

                next_max_id = max_id    # set the new max_id

                results = twitter.search(q=hashtag, lang="en", count='100', max_id=next_max_id)     # query with new max_id

                count += len(results['statuses'])   # count the tweets returned

                key = 'next_results'
                keys = results['search_metadata']

                if key in keys:     # check if there are more results

                    # get the new max_id
                    max_id = (results['search_metadata']['next_results']).split('max_id=')[1].split('&')[0]

                else:
                    break

                time.sleep(2)   # sleep to not exceed the limit of requests per second

            else:
                break

        file.write("\n" + hashtag + "---" + str(count))     # write the tag and count in file
        print("Total Count: " + str(count))

        print("\n-----------------------------------------------------------------------------------------------------------\n")

    except Exception as e:
        print("Total Count: " + str(count))
        print(e)
    except KeyboardInterrupt as e:
        print("Total Count: " + str(count))
        print(e)
        file.close()
    except KeyError as e:
        pass


if __name__ == '__main__':

    taggedArray = getMergedArray()

    for tag in taggedArray:
        getTwitterHashTagCount(tag)
    file.close()