import logging as log


class LogUtil:

    def basicInfoConfig(self):
        log.basicConfig(filename="test.log", level=log.INFO, format="%(asctime)s %(message)s")
        return log

    def basicDebugConfig(self):
        log.basicConfig(filename="test.log", level=log.DEBUG, format="%(asctime)s %(message)s")
        return log

    def basicWarningConfig(self):
        log.basicConfig(filename="test.log", level=log.WARNING, format="%(asctime)s %(message)s")
        return log

    def basicErrorConfig(self):
        log.basicConfig(filename="test.log", level=log.ERROR, format="%(asctime)s %(message)s")
        return log

    def logInfo(self, inputLog):
        log = self.basicInfoConfig()
        log.info(inputLog)
        pass

    def logDebug(self, inputLog):
        log = self.basicDebugConfig()
        log.info(inputLog)

    def logWarning(self, inputLog):
        log = self.basicWarningConfig()
        log.info(inputLog)

    def logError(self, inputLog):
        log = self.basicErrorConfig()
        log.info(inputLog)
