
import time

from abc import ABC, abstractmethod
from random import randrange

class Cryptocurrency(ABC):

    """This class should fetch the real-time prices of a specific cryptocurrency (e.g., Bitcoin) and notify subscribed users when the price changes.

User Class (Observer):
    Users can set thresholds, and when the price crosses the threshold, they will be notified (e.g., “Buy now” or “Sell now”).

Threshold Logic:
    Each user will define a threshold (e.g., buy if the price is lower than $40,000 or sell if the price is higher than $50,000).

"""
    @abstractmethod
    def attach(self, subscriber):
        """Attach a subscriber to the publisher."""

    @abstractmethod
    def detach(self, subscriber):
        """Detach a subscriber from the publisher."""

    @abstractmethod
    def notify(self):
        """Notify all subscribers about an event."""


    @abstractmethod
    def fetch_real_time(self):
        """fetch_real_time Notify all subscribers about an event."""

class ConcreteUser(Cryptocurrency):
    """Concrete Publisher."""

    def __init__(self):
        """Init the Publisher."""
        self.bitcoin = None
        self._bitcoin_users = []


    def get_state(self):
        """Get the Publisher State."""
        return self._state

    def attach(self, subscriber):
        """Attach a new subscriber."""
        print("Publisher: Attached a subscriber.")
        self._subscriber.append(subscriber)

    def detach(self, subscriber):
        """Detach the specified subscriber."""
        self._subscriber.remove(subscriber)

    def notify(self):
        """Notify all subscribers."""
        print("Publisher: Notifying subscribers...")
        for subscriber in self._subscriber:
            subscriber.update(self)

    def run_business_logic(self):
        """Run Business Logic."""


        print("Publisher: I'm doing something important.")
        self._state = randrange(0, 3)

        

        print(f"Publisher: My state has just changed to: {self._state}")
        self.notify()




    def fetch_real_time(self):

      self._state = randrange(0, 3)
"""
        while True:
            Price = self.get_price()

            time.sleep(30)
"""












