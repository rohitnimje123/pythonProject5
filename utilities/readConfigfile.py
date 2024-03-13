import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\HP\\PycharmProjects\\pythonProject5\\Configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def geturl():
        Url = config.get('common info', 'url')
        return Url
