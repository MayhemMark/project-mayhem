import requests
response = requests.get('https://p0mp.com')
print(response)
print(f"""
	Response status:
	{response.status_code}

	Response content:
	{response.content}

	Response encoding:
	{response.encoding}
""")

