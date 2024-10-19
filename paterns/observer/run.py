"""
Observer Pattern.

Adapted From:
https://refactoring.guru/design-patterns/observer/python/example#example-0--main-py



Modify the ConcretePublisher run_business_logic() method:
	Pick a random number 0..3
	If 0, set the state to “Step 0”
	If 1, set the state to “Step 1”
	If 2, set the state to “Fail”
Create three subscribers.
	Subscriber A should only respond to “Step 0”
	Subscriber B should only respond to “Step 1”
	Subscriber C should only respond to “Fail”

"""
from publisher import ConcretePublisher
from subscriber import ConcreteSubscriberA
from subscriber import ConcreteSubscriberB

# The client code.

publisher = ConcretePublisher()

subscriber_a = ConcreteSubscriberA()
publisher.attach(subscriber_a)

subscriber_b = ConcreteSubscriberB()
publisher.attach(subscriber_b)

publisher.run_business_logic()
publisher.run_business_logic()
