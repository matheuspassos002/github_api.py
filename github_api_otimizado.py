import requests

# Configuração da API
BASE_URL = "https://api.github.com"
HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

def get_users(qtd=20):
    """Busca usuários do GitHub"""
    response = requests.get(f"{BASE_URL}/users", headers=HEADERS, params={"per_page": qtd})
    return response.json()

# MÉTODOS DE ORDENAÇÃO

def ordenar_por_login(usuarios, reverso=False):
    """Ordena por login (A-Z ou Z-A)"""
    return sorted(usuarios, key=lambda x: x['login'].lower(), reverse=reverso)

def ordenar_por_id(usuarios, reverso=False):
    """Ordena por ID (crescente ou decrescente)"""
    return sorted(usuarios, key=lambda x: x['id'], reverse=reverso)

def ordenar_por_tipo(usuarios, reverso=False):
    """Ordena por tipo de usuário"""
    return sorted(usuarios, key=lambda x: x.get('type', ''), reverse=reverso)

def exibir(usuarios):
    """Exibe usuários formatados"""
    print(f"\nTotal: {len(usuarios)} usuários")
    print("-" * 50)
    for i, u in enumerate(usuarios, 1):
        print(f"{i}. Login: {u['login']} | ID: {u['id']} | Tipo: {u.get('type', 'N/A')}")
    print()

# EXECUÇÃO
print("=" * 50)
print("API DO GITHUB - MÉTODOS DE ORDENAÇÃO")
print("=" * 50)

# Busca usuários
usuarios = get_users(20)
print(f"\n✓ {len(usuarios)} usuários carregados!")

# Demonstração dos métodos
print("\n1. ORDENAÇÃO POR LOGIN (A-Z)")
exibir(ordenar_por_login(usuarios)[:10])

print("2. ORDENAÇÃO POR LOGIN (Z-A)")
exibir(ordenar_por_login(usuarios, reverso=True)[:10])

print("3. ORDENAÇÃO POR ID (CRESCENTE)")
exibir(ordenar_por_id(usuarios)[:10])

print("4. ORDENAÇÃO POR ID (DECRESCENTE)")
exibir(ordenar_por_id(usuarios, reverso=True)[:10])

print("5. ORDENAÇÃO POR TIPO")
exibir(ordenar_por_tipo(usuarios)[:10])

print("=" * 50)
print("MÉTODOS DISPONÍVEIS:")
print("- ordenar_por_login(usuarios, reverso)")
print("- ordenar_por_id(usuarios, reverso)")
print("- ordenar_por_tipo(usuarios, reverso)")
print("=" * 50)
