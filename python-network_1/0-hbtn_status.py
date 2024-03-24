#!/usr/bin/python3
"""
A Python script that fetches https://alu-intranet.hbtn.io/status using urllib.
"""
import urllib.request

if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    url = "https://alu-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        content = response.read().decode("utf-8")
        print("Body response:")
        for line in content.splitlines():
            print("\t- {}".format(line))

