import re
url = "https://www.youtube.com/watch?v=fS7Hv43EkZw&u=a"
match = re.search(r'(?<=v=)[^&#]+',url)
#match = match or re.search(r'(?<=be/)[^&#]+',url)
id = (match.group(0) if match else None)
print match.group()

"""
[^&#] will stop matching when finding # or &
?<=x will start matching after finding x excluding x
"""