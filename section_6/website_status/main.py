#! /usr/bin/env python3

import sys

import requests
from requests import Response
import validators


def get_valid_user_input() -> str:
    while True:
        try:
            user_input: str = input("Enter a website: ")
            if not validators.url(user_input):
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
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        print("Connection error. Please try again.")
    except requests.exceptions.Timeout:
        print("Timeout error. Please try again.")
    except requests.exceptions.TooManyRedirects:
        print("Too many redirects. Please try again.")
    except requests.exceptions.RequestException:
        print("Request exception. Please try again.")

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


def main() -> None:
    user_input: str = get_valid_user_input()
    response: Response = get_response(user_input)
    show_response_info(response)
    sys.exit()

# Example Code from Tutorial, obviously I expanded on it with the above code
#    website: str = "https://www.indently.io/abc"
#    response: Response = get_response(website)
#    show_response_info(response)

if __name__ == "__main__":
    main()
