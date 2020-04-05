import requests
import config


class HttpClient:

    def __init__(self, dataType):
        self.uri = "https://api.hebergnity.com/vps/" + dataType + "/" +config.APIKey
        self.content = None
        self.response = None
        self.callURI()

    def callURI(self):
        self.response = requests.get(url=self.uri)
        return self.response

    """

            :rtype: string
    """
    def readContent(self, content):
        self.content = content.text
        self.content = self.content.replace("%", "")
        self.content = self.content.replace(',', '.')

        return self.content
