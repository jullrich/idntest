#!/usr/bin/env python3

import sys
import idna
import unicodedata

def idntest(domain):
    oldscript = ''
    try:
        decoded_domain = idna.decode(domain.split('.')[0])
    except idna.IDNAError:
        return "Invalid Punycode"
    for char in decoded_domain:
        if unicodedata.name(char):
            script = unicodedata.name(char).split()[0]
        else:
            script = 'Unknown'
        if oldscript != '':
            if script != oldscript:
                return("Mixed Script")
        oldscript = script
    return("Normal Punycode")

if __name__ == "__main__":
    for line in sys.stdin.readlines():
        if line.startswith('xn--'):
            result = idntest(line)
            print(f"""{line} IDN domain: {result}""")
        else:
            print(f"""{line} is not an IDN domain""")
