__author__ = 'arpeetkale1'

from googleapiclient.discovery import build
import time


def getGoogleImagesURL(query):
    """
    :param query: keyword for retrieving urls
    """
    try:
        # customer search api endpoint
        service = build("customsearch", "v1", developerKey="AIzaSyCGFvvA8ewR4Q2AhH9BK3QavFvW8x1n5Yw")
        file = open(query + ".txt", "a")
        res = service.cse().list(
            q=query,
            cx='002561766668253956288:p4ojtzv0fco',  # search engine id
            searchType='image'
        ).execute()

        for item in res['items']:   # iterate over links
            print(item['link'])
            file.write("\n" + item['link'])

        for i in range(50):
            start = res['queries']['nextPage'][0]['startIndex']     # pagination
            print(start)
            res = service.cse().list(
                q=query,
                cx='002561766668253956288:p4ojtzv0fco',
                searchType='image',
                start=start
            ).execute()

            if 'items' not in res:
                print('No result !!\nres is: {}'.format(res))
            else:
                for item in res['items']:     # iterate over links
                    print(item['link'])
                    file.write("\n" + item['link'])

            time.sleep(5)

        file.close()
    except Exception as e:
        print(e)
    except KeyboardInterrupt as e:
        print(e)


if __name__ == '__main__':

    getGoogleImagesURL("Baia do Sancho")