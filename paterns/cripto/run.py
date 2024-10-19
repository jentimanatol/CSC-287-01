    # Create cryptocurrency object
from cryptocurrency import Cryptocurrency
from cryptocurrency import ConcreteUser


bitcoin = Cryptocurrency('bitcoin')

    # Create users with thresholds for buying and selling
alice = ConcreteUser('Alice', buy_threshold=40000, sell_threshold=60000)
bob = ConcreteUser('Bob', buy_threshold=45000, sell_threshold=55000)

    # Subscribe users to Bitcoin updates
bitcoin.add_user(alice)
bitcoin.add_user(bob)

    # Start monitoring Bitcoin price (fetch every 30 seconds)
bitcoin.monitor_price(interval=30)