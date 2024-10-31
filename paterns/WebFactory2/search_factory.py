class SearchFactory:
    def __init__(self):
        self._search_services = {}

    def register(self, search_service_name, class_name):
        self._search_services[search_service_name] = class_name

    def get_service(self, search_service_name):
        if search_service_name in self._search_services:
            service = self._search_services[search_service_name]

            return service()
        return None

    def get_all_services(self):
        search_services = []
        if self._search_services:
            for _, service in self._search_services.items():
                search_services.append(service())
            return search_services
        return None
