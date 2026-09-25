import requests 
security_headers = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy"
]
print("------------------------------------------------------")
print("|Bem-vindo ao verificador de cabeçalhos de segurança!|")
print("------------------------------------------------------")
url = input("Digite a URL desejada:")
def check_website(url):
    try:
        print(f"Verificando os cabeçalhos de segurança para {url}...")
        response = requests.get(url, timeout = 5)
        headers_presentes = 0
        for header in security_headers:
            if header in response.headers:
                print(f"{header} [✓] - presente.")
                headers_presentes += 1
            else:
                print(f"{header} [X] - ausente.")
        print(f"Total de cabeçalhos de segurança presentes: {headers_presentes}")
    except requests.RequestException as e:
        print(f"Erro ao acessar o site: {e}")
check_website(url)
