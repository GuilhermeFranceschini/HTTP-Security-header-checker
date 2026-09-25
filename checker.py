import requests 
security_headers = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy"
]
def check_website(url):
    url = input("Digite a URL desejada:")
    response = requests.get(url)
    for header in security_headers:
        if header in response.headers:
            print(f"{header} está presente.")
        else:
            print(f"{header} não está presente.")