#!/usr/bin/python3
"""Status module: fetches url"""


if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        page = response.read()
        print("Body response:")
        print("\t- type:", page.__class__)
        print("\t- content:", page)
        print("\t- utf8 content:", page.decode("utf-8"))
