from LogUtility.LogUtil import LogUtil

class TupleImpl:

    def __init__(self,inputTuple):
        try:
            if type(inputTuple) == tuple:
                self.iTuple = inputTuple
                self.log = LogUtil()
            else:
                raise Exception("Input Must be of Type Tuple")
        except Exception as e:
            print(e)
            self.log = LogUtil()
            self.log.logError(e)

    def count(self, input):

        self.log.logInfo("Request Received for count : " + str(input))
        counter = 0
        try:
            for i in range(len(self.iTuple)):
                if self.iTuple[i] == input:
                    counter = counter + 1
            self.log.logInfo("Total Count of : " + str(input) + " is " + str(counter))
        except Exception as e:
            self.log.logError(e)

        return counter

    def index(self, input):
        self.log.logInfo("Request Received for index : " + str(input))
        try:

            if input not in self.iTuple:
                raise Exception(str(input) + " is not in Tuple")
            else:
                for i in range(len(self.iTuple)):
                    if self.iTuple[i] == input:
                        return i
                        break

        except Exception as e:
            self.log.logError(e)