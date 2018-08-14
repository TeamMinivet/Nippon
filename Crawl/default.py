import Crawl.Interface as Interface
import Crawl.Item as Item

pluginInfo = {
    "type" : "default",
    "description" : "This is default crawler."
}

class Run(Interface.Interface) :

    def crawl(self, url) :
        pass

