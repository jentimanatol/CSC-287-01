from search_factory import SearchFactory
from search import GoogleSearch
from search import DuckDuckGoSearch
from search import RedditSearch
import sys
import webbrowser


def search(search_factory: SearchFactory, search_service_name, query):
    search_service = search_factory.get_service(search_service_name)
    if search_service:
        url = search_service.get_search_url(query)
        webbrowser.open_new_tab(url)


def search_all(search_factory: SearchFactory, query):
    search_services = search_factory.get_all_services()

    if search_services:
        for service in search_services:
            url = service.get_search_url(query)
            webbrowser.open_new_tab(url)


def main():
    if len(sys.argv) != 3:
        print("Not enough arguments")
        sys.exit(1)

    search_factory = SearchFactory()
    search_factory.register("google", GoogleSearch)
    search_factory.register("duck", DuckDuckGoSearch)
    search_factory.register("reddit", RedditSearch)

    search_service_name = sys.argv[1]
    query = sys.argv[2]

    if search_service_name == "all":
        search_all(search_factory, query)
    else:
        search(search_factory, search_service_name, query)


if __name__ == "__main__":
    main()
