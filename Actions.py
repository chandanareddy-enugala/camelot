# This Class is used for sending commands to camelot and receiving messages from camelot
# --------------------------------------------------------------------------------------
class Actions:
    def __init__(self):
        # Constant class variables
        self.startStr = "start "
        self.succeededStr = "succeeded "
        self.failedStr = "failed "
        self.errorStr = "error "
        self.failedCount = 0
    def Check_Command_Status(self, command):
        while True:
            receivedMessage = input()
            if (receivedMessage == self.succeededStr + command):
                return True
            elif receivedMessage.startswith(self.failedStr):
                failedMessage = 'target is blocked'
                if failedMessage in receivedMessage:
                    TF = self.Exception_of_TargetBlocked(command)
                    return TF
            elif receivedMessage.startswith(self.errorStr):
                return False
    def Execute_Command(self, command, wait=False):
        print(self.startStr + command)
        if wait == True:
            return self.Check_Command_Status(command)
        else:
            return True
    def Exception_of_TargetBlocked(self, command):
        TF = self.Execute_Command(command)
        return TF

'''
# This code is used for TESTING purpose.
# It shows all the camelot commands execution using 'print()' as we wanted execution.
# ----------------------------------------------------------------------------------
class Actions:
    def __init__(self):
        # Constant class variables
        self.startStr = "start "

    def Execute_Command(self, command, wait=False):
        print(self.startStr + command)
        return True
'''