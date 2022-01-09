#!/usr/bin/python3
"""Status module: fetches url"""


if __name__ == "__main__":
    from urllib import request

    with request.urlopen('https://intranet.hbtn.io/status') as response:
        page = response.read()
        print("Body response:")
        print("    - type:", page.__class__)
        print("    - content:", page)
        print("    - utf8 content:", page.decode("utf-8"))
