"""Example of the Factory Metod Pattern."""

class SearchFactory():

    def __init__(self):
        self._search_engines = {}

    def register(self, search_service_name, class_name):
        """Register a new music service."""
        self._search_engines[search_service_name] = class_name

    def get_search_engine(self, search_service_name):
        """
        Create object, based on the service name.

        This is the factory method.
        Depending on the search_service_name parameter,
        a different object is created and returned.
        """
        if search_service_name in self._search_engines:
            service = self._search_engines[search_service_name]
        
            # Here, we instantiante the object
            return service()
        return None
        
        
    