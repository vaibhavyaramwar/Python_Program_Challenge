from Library import sub_functionality

def extract_iNeuron_data():
    resultData=[]
    iNeuron_html = sub_functionality.get_ineuron_web_page_html()
    parentDataDict = sub_functionality.get_parent_data_dictionary(iNeuron_html)
    for parentKey, parentValue in parentDataDict.items():
        iNeuronData = {}
        courseTitle = parentDataDict[parentKey]['title']
        coursesubCategory = parentDataDict[parentKey]['subCategories']
        iNeuronData["courseTitle"] = courseTitle
        #iNeuronData["coursesubCategory"] = coursesubCategory
        for categoryName in coursesubCategory:
            courseUrl = sub_functionality.get_parent_course_url(parentDataDict,parentKey,categoryName)
            courseDetailsDict = sub_functionality.getCourseDetailsDict(courseUrl)

            filteredCoursesList = courseDetailsDict['props']['pageProps']['initialState']['filter']['initCourses']

            counter = 0
            for filterResult in range(len(filteredCoursesList)):

                try:
                    filteredCourses = courseDetailsDict['props']['pageProps']['initialState']['filter']['initCourses'][filterResult]['title']

                    indcourseDetailsDict = sub_functionality.getFilteredCources(filteredCourses)
                    courseDescription = indcourseDetailsDict['props']['pageProps']['data']['details']['description']
                    CourseOverview =  indcourseDetailsDict['props']['pageProps']['data']['meta']['overview']['learn']
                    Requirements = indcourseDetailsDict['props']['pageProps']['data']['meta']['overview']['requirements']
                    sylList = sub_functionality.getSyllabusDict(indcourseDetailsDict)

                    iNeuronData["courseDescription"] = courseDescription
                    iNeuronData["CourseOverview"] = CourseOverview
                    iNeuronData["Requirements"] = Requirements
                    iNeuronData["Syllabus"] = sylList

                    resultData.append(iNeuronData)
                    break
                except Exception as e:
                    print(e)
    return resultData



