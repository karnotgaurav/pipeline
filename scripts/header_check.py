import requests

def check_headers(url):
    headers_to_check = [
        "strict-transport-security",
        "content-security-policy",
        "x-frame-options",
        "x-content-type-options",
    ]

    response = requests.get(url, timeout=10)
    server_headers = {k.lower(): v for k, v in response.headers.items()}

    print(f"Checking: {url}")
    print(f"Status: {response.status_code}")

    for header in headers_to_check:
        if header in server_headers:
            print(f"PRESENT - {header}")
        else:
            print(f"MISSING - {header}")

    print("---")

check_headers("https://google.com")
