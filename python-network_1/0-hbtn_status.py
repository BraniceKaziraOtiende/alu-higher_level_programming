#!/usr/bin/python3
"""
A script that fetches status from two URLs using urllib.
"""

import urllib.request
import pycodestyle

def fetch_status(url):
    """
    Fetches status from the given URL and displays the content.
    """
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode("utf-8")
            print("Body response:")
            for line in content.splitlines():
                print(f"\t- {line}")
    except Exception as e:
        print(f"Error fetching data from {url}: {e}")

def main():
    """
    Main function to fetch status from specified URLs.
    """
    url1 = "https://alu-intranet.hbtn.io/status"
    url2 = "http://0.0.0.0:5050/status"

    fetch_status(url1)
    fetch_status(url2)

    # PEP8 validation
    style_checker = pycodestyle.StyleGuide()
    result = style_checker.check_files(["your_script.py"])
    if result.total_errors == 0:
        print("PEP8 validation passed.")
    else:
        print(f"PEP8 validation failed. Found {result.total_errors} issues.")

if __name__ == "__main__":
    main()

