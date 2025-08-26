# Testing IDN Domains

just pass the domains one line at a time on stdin
```
% ./idntest.py < testnames.txt
sans.org
 is not an IDN domain
xn--sans.org
 IDN domain: Invalid Punycode
xn--comindex-634g.jp
 IDN domain: Mixed Script
xn--govindex-634g.biz
 IDN domain: Mixed Script
```

