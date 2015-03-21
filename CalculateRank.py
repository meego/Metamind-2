from Utilities import convertToTag

__author__ = 'arpeetkale1'

import pandas as p


def calculateRank():
    """
    This function calculates rank for top tourist sights
    using instagram count and tripadvisor and absolutevisit
    weights
    :rtype : object
    """

    data = p.read_csv('/Users/arpeetkale1/Documents/Metamind/Metamind_Data.csv')
    data.fillna(' ', inplace=True)
    instagramList = data['Instagram_List']
    instagramWeights = data['Instagram_Count']
    absoluteVisitList = data['Absolute_Visit']
    absoluteVisitWeights = data['AV_RANK_WEIGHT']
    tripAdvisorBeachesList = data['Trip_Advisor_Beaches']
    tripAdvisorBeachesWeights = data['TAB_RANK_WEIGHT']
    tripAdvisorDestinationsList = data['Trip_Advisor_Destinations']
    tripAdvisorDestinationsWeights = data['TAD_RANK_WEIGHT']
    tripAdvisorAttractionsList = data['Trip_Advisor_Attractions']
    tripAdvisorAttractionsWeights = data['TAA_RANK_WEIGHT']
    tripAdvisorIslandsList = data['Trip_Advisor_Islands']
    tripAdvisorIslandWeights = data['TAI_RANK_WEIGHT']
    tripAdvisorDestOnRiseList = data['Trip_Advisor_DestontheRise']
    tripAdvisorDestOnRiseWeights = data['TADR_RANK_WEIGHT']

    absoluteVisit = convertToTag(absoluteVisitList)
    tripAdvisorBeaches = convertToTag(tripAdvisorBeachesList)
    tripAdvisorDestinations = convertToTag(tripAdvisorDestinationsList)
    tripAdvisorAttractions = convertToTag(tripAdvisorAttractionsList)
    tripAdvisorIslands = convertToTag(tripAdvisorIslandsList)
    tripAdvisorDestOnRise = convertToTag(tripAdvisorDestOnRiseList)

    instagramPlaceRankArray = zip(instagramList, instagramWeights)
    absoluteVisitPlaceRankArray = zip(absoluteVisit, absoluteVisitWeights)
    tripAdvisorBeachesRankArray = zip(tripAdvisorBeaches, tripAdvisorBeachesWeights)
    tripAdvisorDestinationsRankArray = zip(tripAdvisorDestinations, tripAdvisorDestinationsWeights)
    tripAdvisorAttractionsRankArray = zip(tripAdvisorAttractions, tripAdvisorAttractionsWeights)
    tripAdvisorIslandsRankArray = zip(tripAdvisorIslands, tripAdvisorIslandWeights)
    tripAdvisorDestOnRiseRankArray = zip(tripAdvisorDestOnRise, tripAdvisorDestOnRiseWeights)

    instagramHashmap = {}
    absoluteVisitHashmap = {}
    tripAdvisorBeachHashMap = {}
    tripAdvisorDestinationsHashMap = {}
    tripAdvisorAttractionsHashMap = {}
    tripAdvisorIslandsHashMap = {}
    tripAdvisorDestOnRiseListHashMap = {}

    for row in instagramPlaceRankArray:
        k, v = row
        instagramHashmap[k] = v

    for row in absoluteVisitPlaceRankArray:
        k, v = row
        absoluteVisitHashmap[k] = v

    for row in tripAdvisorBeachesRankArray:
        k, v = row
        tripAdvisorBeachHashMap[k] = v

    for row in tripAdvisorDestinationsRankArray:
        k, v = row
        tripAdvisorDestinationsHashMap[k] = v

    for row in tripAdvisorAttractionsRankArray:
        k, v = row
        tripAdvisorAttractionsHashMap[k] = v

    for row in tripAdvisorIslandsRankArray:
        k, v = row
        tripAdvisorIslandsHashMap[k] = v

    for row in tripAdvisorDestOnRiseRankArray:
        k, v = row
        tripAdvisorDestOnRiseListHashMap[k] = v

    for item in absoluteVisitHashmap:
        if item in instagramHashmap:
            #weight = absoluteVisitHashmap.get(item) #+ instagramHashmap.get(item)
            print(item + "," + str(round(instagramHashmap.get(item))) + "," + str(absoluteVisitHashmap.get(item)))

    # for item in tripAdvisorBeachHashMap:
    #     if item in instagramHashmap:
    #         #print(item + "," + str(round(instagramHashmap.get(item))) + "," + str(tripAdvisorBeachHashMap.get(item)))
    #
    # for item in tripAdvisorDestinationsHashMap:
    #     if item in instagramHashmap:
    #         #print(item + "," + str(round(instagramHashmap.get(item))) + "," + str(tripAdvisorDestinationsHashMap.get(item)))
    #
    # for item in tripAdvisorAttractionsHashMap:
    #     if item in instagramHashmap:
    #         #print(item + "," + str(round(instagramHashmap.get(item)))+ "," + str(tripAdvisorAttractionsHashMap.get(item)))
    #
    # for item in tripAdvisorDestOnRiseListHashMap:
    #     if item in instagramHashmap:
    #         #print(item + "," + str(round(instagramHashmap.get(item)))+ "," + str(tripAdvisorDestOnRiseListHashMap.get(item)))
    #
    # for item in tripAdvisorIslandsHashMap:
    #     if item in instagramHashmap:
    #         #print(item + "," + str(round(instagramHashmap.get(item)))+ "," + str(tripAdvisorIslandsHashMap.get(item)))


if __name__ == '__main__':
    calculateRank()