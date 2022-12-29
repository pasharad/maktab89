import re

words = ["Pasha ; mohammad Parsa ali", "Parsa ; Parisa ///// .h,c pedram", "pedram pbjdh Pkdjb sgr;"]
for word in words:
    found = re.match("(P\w+).*(P\w+)", word)
    # print(found)
    if found:
        print(found.groups())
