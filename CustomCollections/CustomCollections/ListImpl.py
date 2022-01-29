from LogUtility.LogUtil import LogUtil


class ListImpl:

    def __init__(self):
        try:
            self.iList = []
            self.log = LogUtil()
        except Exception as e:
            LogUtil.logError(e)

    def __str__(self):
        return "This is a Custume Implementation of List"

    def append(self, input):
        try:
            self.log.logInfo("Request Received for append : " + str(input))
            newlist = [input]
            self.iList = self.iList + newlist
            self.log.logInfo("Request Successful New List post append : " + str(self.iList))

            return self.iList
        except Exception as e:
            self.log.logError(e)

    def clear(self):
        try:
            self.log.logInfo("Request Received for clear : ")
            self.iList = []
            self.log.logInfo("Request Successful New List post clear : " + str(self.iList))
            return self.iList
        except Exception as e:
            self.log.logError(e)

    def copy(self):
        nList = []
        try:
            self.log.logInfo("Request Received for Copy")
            nList = self.iList
            self.log.logInfo("New List After Copy" + nList)
        except Exception as e:
            self.log.logError(e)

        return nList

    def count(self, input):

        self.log.logInfo("Request Received for count : " + str(input))
        counter = 0
        try:
            for i in range(len(self.iList)):
                if self.iList[i] == input:
                    counter = counter + 1
            self.log.logInfo("Total Count of : " + str(input) + " is " + str(counter))
        except Exception as e:
            self.log.logError(e)

        return counter

    def extend(self, input):

        self.log.logInfo("Request Received for extend : " + str(input))

        try:
            for i in input:
                self.iList = self.append(i)
            return self.iList
            self.log.logInfo("List Post Append : " + str(self.iList))
        except Exception as e:
            print(e)
            self.log.logError(e)

    def index(self, input):
        self.log.logInfo("Request Received for index : " + str(input))
        try:

            if input not in self.iList:
                raise Exception(str(input) + " is not in list")
            else:
                for i in range(len(self.iList)):
                    if self.iList[i] == input:
                        return i
                        break

        except Exception as e:
            self.log.logError(e)

    def insert(self, input, position):

        self.log.logInfo("Request received for Insert for input : " + str(input) + " for position : " + str(position))
        try:
            beforeList = self.iList[:position]
            afterList = self.iList[position:]
            newList = [input]
            self.iList = beforeList + newList + afterList
            self.log.logInfo("Final List After insert : " + str(self.iList))
            return self.iList
        except Exception as e:
            self.log.logError(e)

    def pop(self):
        self.log.logInfo("Request Received for pop")
        try:
            self.iList = self.iList[:len(self.iList) - 1]
            self.log.logInfo("List after pop : " + str(self.iList))
        except Exception as e:
            self.log.logError(e)
        return self.iList

    def remove(self, value):

        self.log.logInfo("Request Received for remove : " + str(value))
        index = 0

        try:
            index = self.index(value)

            beforeList = self.iList[:index]
            afterList = self.iList[index+1:]
            self.iList = beforeList + afterList
            self.log.logInfo("List after remove operation : " + str(self.iList))

            return self.iList

        except Exception as e:
            print(e)
            self.log.logError(e)

    def reverse(self):

        reverseList = []
        try:
            self.log.logInfo("Request Received for reverse : ")
            reverseList = self.iList[::-1]
            self.log.logInfo("Reverse List is : " + str(reverseList))
        except Exception as e:
            LogUtil.logError(e)

        return reverseList

    def sort(self):

        self.log.logInfo("Request received for Sort ")
        try:
            self.log.logInfo("List Before Sort : "+str(self.iList))
            self.iList = sorted(self.iList)
            self.log.logInfo("List After Sort : "+str(self.iList))
            return self.iList
        except Exception as e:
            self.log.logError(e)
