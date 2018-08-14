import Crawl.Item as Item
from threading import Thread

"""
    Please use BFS searching with queue object.
"""

class Interface :

    """
        @params : string url, integer threads
        @return : None
    """
    def __init__(self, url, threads=10) :
        self.url = url
        self.queue = [url]
        self.crawled = []
        self.threads = 10

    """
        @params : None
        @return : None
    """
    def run(self) :
        threads = []
        for i in range(0, self.threads) :
            threads.append(Thread(target=self.threadFunc))
        for t in threads:
            t.start()
        for t in threads:
            t.join()
    
    """
        @params : None
        @return : None
    """
    def threadFunc(self) :
        if len(self.queue) == 0 :
            return
        url = self.queue.pop()
        self.crawl(url)
    
    """
        @params : string url
        @return : None
    """
    def crawl(self, url) :
        pass

    """
        @params : None
        @return : Crawl.Item[]
    """
    def getCrawled(self) :
        return self.crawled
