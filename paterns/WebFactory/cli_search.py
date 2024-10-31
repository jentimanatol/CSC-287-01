
from search_factory import SearchFactory
from search import GoogleSearch, DuckDuckGoSearch, RedditSearch
import sys


# Create the Search Factory and Register Search Engines
search_factory = SearchFactory()
search_factory.register("google", GoogleSearch)
search_factory.register("duck", DuckDuckGoSearch)
search_factory.register("reddit", RedditSearch)


def search(search_factory, site_name="google", query="tesla"):

    if site_name == "all":
        print(site_name, query)
        google = search_factory.get_search_engine("google")
        duck = search_factory.get_search_engine("duck")
        reddit =search_factory.get_search_engine("reddit")
        
        google.search(query)
        duck.search(query)
        reddit.search(query)
    else:
        search_service = search_factory.get_search_engine(site_name)
        search_service.search(query)
        


search(search_factory, sys.argv[1], sys.argv[2])