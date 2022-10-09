import re
import email.utils

pattern = "(<[a-zA-Z]{1,})([\.\-\_A-zA-Z0-9]*)(\@)([a-zA-Z]*)(\.)([a-zA-Z]{1,3}>)"

N = int(input())

for _ in range(N):
    name, email = tuple(input().split())
    
    if bool(re.search(pattern, email)):
        print(name, email)    
