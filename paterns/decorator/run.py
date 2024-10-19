"""Run the example decorator pattern.
Make a new UpperCase Decorator that transforms your message to upper case.
Do a triple nesting example:  Encrypt(Upper(Japanese)))

"""

from component import SecuritySystem
from decorator import EncryptionDecorator
from decorator import JapaneseDecorator
from decorator import UpperCase

def get_message(component):
    """Get the latest component message."""
    print(f"MESSAGE: {component.get_message()}")


# Here we try the original component
simple = SecuritySystem()
get_message(simple)

# Then we wrap the original component with encryption
encrypt_decorator = EncryptionDecorator(simple)
get_message(encrypt_decorator)

# Wrap the original component with Japanese translation
japanese_decorator = JapaneseDecorator(simple)
get_message(japanese_decorator)

# Nesting
nested_decorators = EncryptionDecorator(japanese_decorator)
get_message(nested_decorators)
# get_message(encrypt_decorator)


nested_uppler =  UpperCase(nested_decorators)
get_message(nested_uppler)








"""s
#upper
Upper_Case = UpperCase(simple)
get_message(Upper_Case)


#nested uper


nested_uppler =  EncryptionDecorator(japanese_decorator)

securitySystem = SecuritySystem().get_message()
print(securitySystem)

japanese_decorator = JapaneseDecorator(SecuritySystem)
print(japanese_decorator.get_message())
get_message(nested_uppler)

get_message(Upper_Case)

get_message(encrypt_decorator)
"""