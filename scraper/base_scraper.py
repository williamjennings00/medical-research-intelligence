from abc import ABC, abstractmethod


class BaseScraper(ABC):

    @abstractmethod
    def search(self, query):
        pass


    @abstractmethod
    def collect_results(self):
        pass


    @abstractmethod
    def close(self):
        pass
