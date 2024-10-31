
from abc import ABC, abstractmethod

from search_factory import SearchFactory
from search import GoogleSearch
from search import DuckDuckGoSearch
from search import RedditSearch
import sys
import webbrowser


# Create the Search Factory and Register Search Engines
search_factory = SearchFactory()
search_factory.register("google", GoogleSearch)
search_factory.register("duck", DuckDuckGoSearch)
search_factory.register("reddit", RedditSearch)
…


#And, here is a list of all the classes with important methods that you will need to create:

SearchService(ABC)
def get_search_url(self, q)
GoogleSearch(SearchService)
DuckDuckGoSearch(SearchService)
RedditSearch(SearchService)
SearchFactory
def register(self, site, search_class):
def get_search_engine (self, site)
