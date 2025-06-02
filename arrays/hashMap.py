class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        Encontra o índice do primeiro caractere não repetido em uma string.
        
        Args:
            s: String de entrada a ser analisada
            
        Returns:
            int: Índice do primeiro caractere único ou -1 se não existir
        """
        
        # Dicionário para armazenar informações dos caracteres:
        # chave: caractere
        # valor: lista [índice_primera_ocorrência, contagem]
        char_info = {}
        
        # Primeira passagem: contar ocorrências e registrar índices
        for idx, ch in enumerate(s):
            if not char_info.get(ch):
                # Se caractere não está no dicionário, registra com:
                # [índice_da_primeira_ocorrência, contagem=1]
                char_info[ch] = [idx, 1]
            else:
                # Se caractere já existe, incrementa a contagem
                char_info[ch][1] += 1
        
        # Segunda passagem: encontrar o primeiro caractere com contagem 1
        for ch, info in char_info.items():
            if info[1] == 1:  # Se a contagem for exatamente 1
                return info[0]  # Retorna o índice da primeira ocorrência
        
        # Se nenhum caractere único for encontrado
        return -1
    
sol = Solution()
print(sol.firstUniqChar("leetcode"))    # Retorna 0 ('l' é o primeiro único)
print(sol.firstUniqChar("loveleetcode")) # Retorna 2 ('v' é o primeiro único)
print(sol.firstUniqChar("aabb"))        # Retorna -1 (não tem caracteres únicos)