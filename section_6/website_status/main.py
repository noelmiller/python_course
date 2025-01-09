#! /usr/bin/env python3

import re
import sys
from typing import Pattern

import requests
from requests import Response


def validate_http_or_https_url(url: str) -> bool:
    regex: Pattern[str] = re.compile(
        r'^(?:http)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def get_valid_user_input() -> str:
    while True:
        try:
            user_input: str = input("Enter a website: ")
            if not validate_http_or_https_url(user_input):
                raise ValueError("Invalid URL. Please try again.")
        except ValueError as e:
            print(e)
            continue
        except KeyboardInterrupt:
            print("\nExiting program.")
            sys.exit()
        return user_input

def get_response(url: str) -> Response:
    try:
        return requests.get(url, timeout=5)
    except requests.exceptions.SSLError as e:
        if "certificate verify failed" in str(e):
            print("SSL certificate verification failed. Please enter a URL with a valid SSL certificate.")
        else:
            print(e)
        sys.exit()
    except requests.exceptions.ConnectionError:
        print("Connection error. Please try again.")
        sys.exit()
    except requests.exceptions.Timeout:
        print("Timeout error. Please try again.")
        sys.exit()
    except requests.exceptions.TooManyRedirects:
        print("Too many redirects. Please try again.")
        sys.exit()
    except requests.exceptions.RequestException:
        print("Request exception. Please try again.")
        sys.exit()

def show_response_info(response: Response) -> None:
    print("----")
    print(f"URL: {response.url}")
    print(f"Status code: {response.status_code}")
    print(f"OK: {response.ok}")
    print(f"Links: {response.links}")
    print(f"Encoding: {response.encoding}")
    print(f"Is redirect: {response.is_redirect}")
    print(f"Is permanent redirect: {response.is_permanent_redirect}")
    print("----")


def main() -> int:
    user_input: str = get_valid_user_input()
    response: Response = get_response(user_input)
    show_response_info(response)
    return 0

# Example Code from Tutorial, obviously I expanded on it with the above code
#    website: str = "https://www.indently.io/abc"
#    response: Response = get_response(website)
#    show_response_info(response)

if __name__ == "__main__":
    raise SystemExit(main())
