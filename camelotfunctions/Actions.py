
# This Class is used for executing any action commands
class Actions:
    def __init__(self):
        # Constant class variables
        self.startStr = "start "
        self.succeededStr = "succeeded "
        self.failedStr = "failed "
        self.errorStr = "error "

    def checkForSuccess(self, command):
        while True:
            receivedMessage = input()  # Python is asking Camelot some Input (here "input()" means the output of Camelot) - [Example: succeeded CreatePlace(BobsHouse, Cottage)]

            if (receivedMessage == self.succeededStr + command):
                return True
            '''elif receivedMessage.startswith(self.failedStr):
                return False
            elif receivedMessage.startswith(self.errorStr):
                return False'''

    def run_command(self, command, wait=False):
        print(self.startStr + command)                                   # Sending command as message to Camelot
        if wait == True:
            return self.checkForSuccess(command)
        else:
            return True
