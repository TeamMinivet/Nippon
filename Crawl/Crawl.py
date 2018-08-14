import requests
import Crawl.default as CrawlDefault
import Crawl.angularjs as CrawlAngularJS
import Crawl.reactjs as CrawlReactJS 
import Crawl.vuejs as CrawlVueJS

class Crawl :

    types = {
        "default" : CrawlDefault,
        "angularjs" : CrawlAngularJS,
        "reactjs" : CrawlReactJS,
        "vuejs" : CrawlVueJS
    }

    def __init__(self, type) :
        self.Crawler = self.types.get(type, self.types['default'])
    
    
