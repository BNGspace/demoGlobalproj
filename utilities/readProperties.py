import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getURL():
        url=config.get("common info","baseURL")
        return url

    #@staticmethod
    #def getemail():
        #username = config.get("common info", "username")
        #return username

    #@staticmethod
    #def getpassword():
        #password = config.get("common info", "password")
       # return password