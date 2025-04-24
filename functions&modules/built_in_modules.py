import math

import requests
import mymodule

# print(mymodule.sub(6,3))
# print(math.sin(90))

r = requests.get("https://www.instagram.com")
print(r.text)