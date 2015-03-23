# Metamind

Project to get top tourist places around the world and get photos of these sights.

Requirements:

1. Python 3.x+
2. BeautifulSoup    -   pip3 install beautifulsoup4
3. Pillow           -   pip3 install Pillow
4. googleapiclient  -   pip3 install --upgrade google-api-python-client
5. pandas           -   pip3 install pandas


1. AbsoluteVisitScraper.py	    - Code to scrape www.absolutevisit.com and get their list of top 100 tourist sights

2. FlickrPhotos.py	            - Code to retrieve urls for images and then download images using those urls

3. GoogleImages.py	            - Code to retrieve urls using google's custom search api

4. InstagramPhotosDownload.py	  - Code to retrieve urls for images using Instagram api

5. InstagramTagsCount.py	      - Code to retrieve #hashtag count using Instagram api

6. TripAdvisorScraper.py	      - Code to scrape www.tripadvisor.com/TravelersChoice page and retrieve top tourist                                     sights

7. TwitterHashTagCount.py	      - Code to retrieve #hashtag count using Twitter api

8. flickr.py                    - Code for using flickr api endpoints
