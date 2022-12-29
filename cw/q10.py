import re

address = "Tehran, Hemmat Road, Shariati street"
print(re.sub("Road", "Rd.", address))
