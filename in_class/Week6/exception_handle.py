import os

import sys

# TODO: Check first that the arguments you were expecting are present
names = os.listdir(sys.argv[1])



for name in names:
	print(name)



