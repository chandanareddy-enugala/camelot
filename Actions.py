

# This Class is used for executing any action commands
class Actions:
    def __init__(self):
        # Constant class variables
        self.startStr = "start "
        self.succeededStr = "succeeded "
        self.failedStr = "failed "
        self.errorStr = "error "
        self.failedCount = 0

        #self.quit = Quit()

    def Check_Command_Status(self, command):
        while True:
            receivedMessage = input()  # Python is asking Camelot some Input (here "input()" means the output of Camelot) - [Example: succeeded CreatePlace(BobsHouse, Cottage)]

            if (receivedMessage.upper() == "Y"):
                return True
            elif (receivedMessage == self.succeededStr + command):
                return True
            elif receivedMessage.startswith(self.failedStr):
                failedMessage = 'target is blocked'
                if failedMessage in receivedMessage:                   # f'failed {command} "The path to the target is blocked"'
                    TF = self.Exception_of_TargetBlocked(command)
                    return TF
            elif receivedMessage.startswith(self.errorStr):
                #self.quit.game()
                return False

    def Execute_Command(self, command, wait=False):
        print(self.startStr + command)                                   # Sending command as message to Camelot
        if wait == True:
            return self.Check_Command_Status(command)
        else:
            return True
    def Exception_of_TargetBlocked(self, command):
        TF = self.Execute_Command(command)
        return TF

