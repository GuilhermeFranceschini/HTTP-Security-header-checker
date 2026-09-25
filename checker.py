import requests 
security_headers = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy"
]
url = input("Digite a URL desejada:")
def check_website(url):
    try:
        response = requests.get(url, timeout = 5)
        for header in security_headers:
            if header in response.headers:
                print(f"{header} está presente.")
            else:
                print(f"{header} não está presente.")
    except requests.RequestException as e:
        print(f"Erro ao acessar o site: {e}")
check_website(url)
