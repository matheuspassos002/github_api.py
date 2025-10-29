import requests
import json
from datetime import datetime

class GitHubAPIConsumer:
    """Classe para consumir a API do GitHub e ordenar resultados"""
    
    def __init__(self):
        self.base_url = "https://api.github.com"
        self.headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"
        }
    
    def get_users(self, since=0, per_page=10):
        """
        Busca lista de usuários do GitHub
        
        Args:
            since: ID do último usuário visto (para paginação)
            per_page: Quantidade de usuários por página
        
        Returns:
            Lista de usuários
        """
        url = f"{self.base_url}/users"
        params = {
            "since": since,
            "per_page": per_page
        }
        
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar usuários: {e}")
            return []
    
    def get_user_details(self, username):
        """
        Busca detalhes de um usuário específico
        
        Args:
            username: Nome do usuário
        
        Returns:
            Detalhes do usuário
        """
        url = f"{self.base_url}/users/{username}"
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar detalhes do usuário {username}: {e}")
            return None
    
    # MÉTODOS DE ORDENAÇÃO
    
    def ordenar_por_login(self, usuarios, reverso=False):
        """
        Ordena usuários por login alfabeticamente
        
        Args:
            usuarios: Lista de usuários
            reverso: Se True, ordena em ordem decrescente
        
        Returns:
            Lista ordenada
        """
        return sorted(usuarios, key=lambda x: x['login'].lower(), reverse=reverso)
    
    def ordenar_por_id(self, usuarios, reverso=False):
        """
        Ordena usuários por ID
        
        Args:
            usuarios: Lista de usuários
            reverso: Se True, ordena em ordem decrescente
        
        Returns:
            Lista ordenada
        """
        return sorted(usuarios, key=lambda x: x['id'], reverse=reverso)
    
    def ordenar_por_tipo(self, usuarios, reverso=False):
        """
        Ordena usuários por tipo (User, Organization, etc)
        
        Args:
            usuarios: Lista de usuários
            reverso: Se True, ordena em ordem decrescente
        
        Returns:
            Lista ordenada
        """
        return sorted(usuarios, key=lambda x: x.get('type', ''), reverse=reverso)
    
    def ordenar_multiplo(self, usuarios, criterios):
        """
        Ordena por múltiplos critérios
        
        Args:
            usuarios: Lista de usuários
            criterios: Lista de tuplas (campo, reverso)
                      Ex: [('type', False), ('login', False)]
        
        Returns:
            Lista ordenada
        """
        resultado = usuarios.copy()
        for campo, reverso in reversed(criterios):
            if campo == 'login':
                resultado = sorted(resultado, key=lambda x: x['login'].lower(), reverse=reverso)
            elif campo == 'id':
                resultado = sorted(resultado, key=lambda x: x['id'], reverse=reverso)
            elif campo == 'type':
                resultado = sorted(resultado, key=lambda x: x.get('type', ''), reverse=reverso)
        return resultado
    
    def exibir_usuarios(self, usuarios, campos=['login', 'id', 'type']):
        """
        Exibe lista de usuários formatada
        
        Args:
            usuarios: Lista de usuários
            campos: Campos a serem exibidos
        """
        print(f"\n{'='*60}")
        print(f"Total de usuários: {len(usuarios)}")
        print(f"{'='*60}\n")
        
        for i, usuario in enumerate(usuarios, 1):
            print(f"{i}. ", end="")
            info = " | ".join([f"{campo}: {usuario.get(campo, 'N/A')}" for campo in campos])
            print(info)
        print()


def main():
    """Função principal com exemplos de uso"""
    
    print("=" * 60)
    print("CONSUMIDOR DA API DO GITHUB - TRABALHO")
    print("=" * 60)
    
    # Inicializa o consumidor
    api = GitHubAPIConsumer()
    
    # Busca usuários
    print("\n1. BUSCANDO USUÁRIOS DA API...")
    usuarios = api.get_users(per_page=20)
    
    if not usuarios:
        print("Erro ao buscar usuários!")
        return
    
    print(f"✓ {len(usuarios)} usuários carregados com sucesso!")
    
    # Demonstração dos métodos de ordenação
    
    print("\n" + "="*60)
    print("2. ORDENAÇÃO POR LOGIN (A-Z)")
    print("="*60)
    ordenados_login = api.ordenar_por_login(usuarios)
    api.exibir_usuarios(ordenados_login[:10])
    
    print("\n" + "="*60)
    print("3. ORDENAÇÃO POR LOGIN (Z-A)")
    print("="*60)
    ordenados_login_rev = api.ordenar_por_login(usuarios, reverso=True)
    api.exibir_usuarios(ordenados_login_rev[:10])
    
    print("\n" + "="*60)
    print("4. ORDENAÇÃO POR ID (CRESCENTE)")
    print("="*60)
    ordenados_id = api.ordenar_por_id(usuarios)
    api.exibir_usuarios(ordenados_id[:10])
    
    print("\n" + "="*60)
    print("5. ORDENAÇÃO POR ID (DECRESCENTE)")
    print("="*60)
    ordenados_id_rev = api.ordenar_por_id(usuarios, reverso=True)
    api.exibir_usuarios(ordenados_id_rev[:10])
    
    print("\n" + "="*60)
    print("6. ORDENAÇÃO POR TIPO")
    print("="*60)
    ordenados_tipo = api.ordenar_por_tipo(usuarios)
    api.exibir_usuarios(ordenados_tipo[:10])
    
    print("\n" + "="*60)
    print("7. ORDENAÇÃO MÚLTIPLA (TIPO + LOGIN)")
    print("="*60)
    ordenados_mult = api.ordenar_multiplo(usuarios, [('type', False), ('login', False)])
    api.exibir_usuarios(ordenados_mult[:10])
    
    # Exemplo de detalhes de usuário
    print("\n" + "="*60)
    print("8. EXEMPLO DE DETALHES DE USUÁRIO")
    print("="*60)
    if usuarios:
        primeiro_usuario = usuarios[0]['login']
        print(f"\nBuscando detalhes de: {primeiro_usuario}")
        detalhes = api.get_user_details(primeiro_usuario)
        if detalhes:
            print(f"\nLogin: {detalhes.get('login')}")
            print(f"Nome: {detalhes.get('name', 'N/A')}")
            print(f"Bio: {detalhes.get('bio', 'N/A')}")
            print(f"Repositórios públicos: {detalhes.get('public_repos', 0)}")
            print(f"Seguidores: {detalhes.get('followers', 0)}")
            print(f"Seguindo: {detalhes.get('following', 0)}")
    
    print("\n" + "="*60)
    print("MÉTODOS DE ORDENAÇÃO DISPONÍVEIS:")
    print("="*60)
    print("1. ordenar_por_login(usuarios, reverso=False)")
    print("2. ordenar_por_id(usuarios, reverso=False)")
    print("3. ordenar_por_tipo(usuarios, reverso=False)")
    print("4. ordenar_multiplo(usuarios, criterios)")
    print("="*60)


if __name__ == "__main__":
    main()