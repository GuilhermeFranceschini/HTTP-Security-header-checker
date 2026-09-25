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
    if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
    try:
        print(f"Verificando os cabeçalhos de segurança para {url}...")
        response = requests.get(url, timeout = 5)
        print(f"\nStatus HTTP: {response.status_code}")
        headers_presentes = 0
        for header in security_headers:
            if header in response.headers:
                print(f"{header} [✓] - presente.")
                headers_presentes += 1
            else:
                print(f"{header} [X] - ausente.")
        porcentagem = (headers_presentes / len(security_headers)) * 100
        print(f"Total de cabeçalhos de segurança presentes: {headers_presentes}")
        print(f"Porcentagem de cabeçalhos de segurança presentes: {porcentagem:.2f}%")
        if porcentagem == 100:
             print("- Excelente! Todos os cabeçalhos de segurança estão presentes.")
        elif porcentagem >= 60:
             print("- Bom! A maioria dos cabeçalhos de segurança estão presentes.")
        else:
             print("- Atenção! Muitos cabeçalhos de segurança estão ausentes.")
    except requests.RequestException as e:
        print(f"Erro ao acessar o site: {e}")
check_website(url)
