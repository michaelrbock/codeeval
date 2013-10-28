import sys
import re

EMAIL_RE = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

input = open(sys.argv[1], 'r')

emails = []

for line in input:
    emails.append(line)
input.close()

for i, email in enumerate(emails):
    if email == "":
            continue
    if re.match(EMAIL_RE, email):
        sys.stdout.write('true')
    else:
        sys.stdout.write('false')
    if i != len(emails)-1:
        sys.stdout.write('\n')
