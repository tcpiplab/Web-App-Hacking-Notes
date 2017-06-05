#!/usr/bin/env python
#
# Just for unhiding hidden strings as found in
# my written notes about web app hacking labs
#
# Example:
# $ ./unhide.py IiA7IG5ldHN0YXQgLWFuIDsgRk9PPSIx
# " ; netstat -an ; FOO="1

import base64
import sys

# Help message
if len(sys.argv) == 1:
    print(str(sys.argv[0]) + ' \'your_base64_string\'')
    exit()
else:
    obf_string = sys.argv[1]

#obf_string =  base64.b64encode(raw_string.encode())

print( base64.b64decode(obf_string).decode())
