#!/usr/bin/python3
"""Using requests"""

if __name__ == "__main__":
    import requests


    response = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("    - type:", response.text.__class__)
    print("    - content:", response.text)
