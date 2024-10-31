from abc import ABC, abstractmethod


class SearchService(ABC):
    @abstractmethod
    def get_search_url(self, q) -> str:
        """Search the service with the specified q parameter."""


class GoogleSearch(SearchService):
    def get_search_url(self, q) -> str:
        return f"https://www.google.com/search?q={q}"


class DuckDuckGoSearch(SearchService):
    def get_search_url(self, q) -> str:
        return f"https://duckduckgo.com/?t=h_&q={q}"


class RedditSearch(SearchService):
    def get_search_url(self, q) -> str:
        return f"https://www.reddit.com/search/?q={q}"
