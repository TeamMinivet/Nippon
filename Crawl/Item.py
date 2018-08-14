class Item :

    def __init__(self, method="GET", url="", params="", headers={}) :
        self.method = method
        self.url = url
        self.params = params
        self.headers = headers

    def setMethod(self, method) :
        self.method = method

    def setUrl(self, url) :
        self.url = url
    
    def setParams(self, params) :
        self.params = params

    def setHeaders(self, headers) :
        self.headers = headers

    def getMethod(self) :
        return self.method
    
    def getUrl(self) :
        return self.getUrl
    
    def getParams(self) :
        return self.params
    
    def getHeaders(self) :
        return self.headers
    
    def __str__(self) :
        return "[ %s ] %s"%(self.method, self.url)