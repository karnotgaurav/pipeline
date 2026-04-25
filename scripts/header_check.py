import requests

def check_header(URL):
	headers_to_check = [
		"strict-transport-security",
		"content-security-policy",
		"x-frame-option",
		"x-content-type-options",
		]

	response = requests.get(url, timeout=10)
	server_headers={k.lower() : v for k v in response.headers.items()}

	print(f"checking: {url}")
	print(f"status:: {response.status.code}")

for header in headers_to_check:
	if header in server_headers:
		print(f"PRESENT - {header}"
	else:
		print(f"missing - {header}"

	print("---")

check_headers("https://google.com)
