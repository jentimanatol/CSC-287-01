"""Search Services module"""
from abc import ABC, abstractmethod
import webbrowser


class SearchService(ABC):
    """The Search Service Base Class."""

    @abstractmethod
    def search(self, q):
        """Search the service with the specified q parameter."""


class GoogleSearch(SearchService):
    """The Google Search Class."""

    def search(self, q):
        """Search the service with the specified q parameter."""
        webbrowser.open( f"https://www.google.com/search?q={q}&sca_esv=6a685f8a9507fd28&sxsrf=ADLYWIJIPsSv4ntAoGUS0UvaJgjlC3FGAQ%3A1729961158187&source=hp&ei=xhwdZ7vWB-ftptQPmfmssAc&iflsig=AL9hbdgAAAAAZx0q1lunBFiDtqKW67LeKJtozpacZLrH&ved=0ahUKEwi70bjCv6yJAxXntokEHZk8C3YQ4dUDCBg&uact=5&oq=bhcc&gs_lp=Egdnd3Mtd2l6GgIYAiIEYmhjYzIKECMYgAQYJxiKBTIEECMYJzIQEAAYgAQYsQMYQxiDARiKBTINEC4YgAQYsQMYQxiKBTIOEC4YgAQYxwEYjgUYrwEyDhAuGIAEGMcBGI4FGK8BMgoQABiABBhDGIoFMggQABiABBixAzIFEAAYgAQyDhAuGIAEGMcBGI4FGK8BSIMgUPEbWMMecAF4AJABAJgBWqABxQKqAQE0uAEDyAEA-AEBmAIFoALgAqgCCsICDRAjGCcY-AUY6gIYiwPCAgoQIxgnGOoCGIsDwgILEAAYgAQYkQIYigXCAg4QLhiABBixAxiDARiKBcICDhAAGIAEGLEDGIMBGIoFwgIOEC4YgAQYsQMY0QMYxwHCAhAQLhiABBixAxhDGIMBGIoFwgIKEC4YgAQYQxiKBcICDRAAGIAEGLEDGEMYigXCAhAQLhiABBixAxhDGNQCGIoFmAMPkgcBNaAHwTg&sclient=gws-wiz", 
                        1)


class DuckDuckGoSearch(SearchService):
    """The Duck Duck Go Search Class."""

    def search(self, q):
        """Search the service with the specified q parameter."""
        webbrowser.open(f"https://duckduckgo.com/?t=h_&q={q}&ia=web", 1)


class RedditSearch(SearchService):
    """The Reddit Search Class."""

    def search(self, q):
        """Search the service with the specified q parameter."""
        webbrowser.open(f"https://www.reddit.com/search/?q={q}&cId=8efb742b-9de7-406d-9a1c-24f483272883&iId=b37885fe-5938-40fb-948a-ff31fde22e08", 1)
