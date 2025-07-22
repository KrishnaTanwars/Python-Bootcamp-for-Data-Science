# Two types of modules in Python:
# - Built-in Modules
# - External Modules

import math
print(math.sqrt(25))

import mymodule
mymodule.hello()

import requests
r = requests.get("https://www.google.com")
print(r.text)