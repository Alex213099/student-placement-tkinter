import requests
response = requests.request("GET", 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials', headers = { 'Authorization': 'Basic RzNyWWdtNENVWWNNUFMyZFRIelVXMXgwbnhKcm1FY2xxa3hCaGthN0JtZ0x0MFN5Old2YllWZWhuUWJFVG1rSmdkS0J6VEdGYjdpeHlIWk5aNVAyZW5RNzU5YmRKRUdiMzFaRlJlTEwyNTVOVGtZMHo=' })
print(response.text.encode('utf8'))
print(response.text)