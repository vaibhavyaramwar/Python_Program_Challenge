import requests
import json

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

from Utility import Constants

def get_ineuron_web_page_html():
    uClient = uReq(Constants.ineuronMainPageURL)
    iNeuronPage = uClient.read()
    iNeuron_html = bs(iNeuronPage, "html.parser")
    uClient.close()

    return iNeuron_html


def get_parent_data_dictionary(iNeuron_html):
    iNeuronHeader = iNeuron_html.find_all("body")
    scriptResult = iNeuronHeader[0].find("script", {"id": "__NEXT_DATA__"})
    scriptResultContent = scriptResult.contents[0]
    scriptDict = dict(json.loads(scriptResultContent))
    parentDataDict = scriptDict.get("props").get("pageProps").get("initialState").get("init").get("categories")

    return parentDataDict

def get_parent_course_url(parentDataDict,parentDataKey,categoryName):
    subCat = parentDataDict[parentDataKey]['subCategories']
    parentCourseResponse = requests.get(Constants.ineuronCourseDetailUrl + subCat[categoryName]['title'])
    parentCourseResponse.encoding = 'utf-8'
    parentcourseResponse_html = bs(parentCourseResponse.text, "html.parser")
    parentcourseResult = parentcourseResponse_html.find_all("script", {"id": "__NEXT_DATA__"})
    parentcourseResultContent = parentcourseResult[0].contents
    parentcourseDict = dict(json.loads(parentcourseResultContent[0]))
    #courseDetailDict = parentcourseDict['props']['pageProps']['initialState']['init']['categories']
    parentcourseUrl = parentcourseDict['page'].replace("[categorySlug]", parentcourseDict['query']['categorySlug'])
    courseUrl = Constants.ineuronMainPageURL + parentcourseUrl
    return courseUrl

def getCourseDetailsDict(courseUrl):
    courseDetailsResponse = requests.get(courseUrl)
    courseDetailsResponse.encoding = 'utf-8'
    courseDetailsResponse_html = bs(courseDetailsResponse.text, "html.parser")
    courseDetailsResponseResult = courseDetailsResponse_html.find_all("script", {"id": "__NEXT_DATA__"})
    courseDetailsResponseContent = courseDetailsResponseResult[0].contents
    courseDetailsDict = dict(json.loads(courseDetailsResponseContent[0]))
    return courseDetailsDict

def getFilteredCources(filteredCourses):
    try:
        filteredCoursesUrl = Constants.ineuronMainPageURL+filteredCourses
        print(filteredCoursesUrl)
        indcourseResponse = requests.get(filteredCoursesUrl)
        indcourseResponse.encoding = 'utf-8'
        indcourseResponse_html = bs(indcourseResponse.text, "html.parser")
        indcourseDetailsResponseResult = indcourseResponse_html.find_all("script", {"id": "__NEXT_DATA__"})
        indcourseDetailsResponseContent = indcourseDetailsResponseResult[0].contents
        indcourseDetailsDict = dict(json.loads(indcourseDetailsResponseContent[0]))
        return indcourseDetailsDict
    except Exception as e:
        print(e)

def getSyllabusDict(indcourseDetailsDict):
    sylDict = indcourseDetailsDict['props']['pageProps']['data']['meta']['curriculum']
    sylList = []
    for sylKey in sylDict:
        sylList.append(dict(sylDict[sylKey]))
    return sylList



