class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        """
        Encontra o comprimento da maior substring que contém no máximo 
        duas ocorrências de qualquer caractere.
        
        Args:
            s (str): String de entrada a ser analisada
            
        Returns:
            int: Comprimento da maior substring válida
        """
        
        # Inicialização dos ponteiros da janela deslizante
        l, r = 0, 0          # l = ponteiro esquerdo, r = ponteiro direito
        _max = 1              # Armazena o comprimento máximo encontrado (mínimo é 1)
        counter = {}          # Dicionário para contar ocorrências de caracteres na janela atual
        
        # Inicializa o contador com o primeiro caractere da string
        counter[s[0]] = 1     # Exemplo: se s[0] = 'a', counter = {'a': 1}

        # Loop principal para expandir a janela deslizante
        while r < len(s) - 1:
            # Move o ponteiro direito para expandir a janela
            r += 1
            
            # Atualiza o contador para o caractere na posição r
            if counter.get(s[r]):    # Se o caractere já existe no contador
                counter[s[r]] += 1   # Incrementa sua contagem
            else:                    # Se o caractere não existe no contador
                counter[s[r]] = 1    # Inicializa com contagem 1

            # Ajusta a janela quando um caractere aparece 3 vezes
            while counter[s[r]] == 3:
                # Remove o caractere na posição l da janela
                counter[s[l]] -= 1   # Decrementa sua contagem
                l += 1               # Move o ponteiro esquerdo para direita

            # Atualiza o comprimento máximo da substring válida
            # r - l + 1 = comprimento atual da janela
            _max = max(_max, r - l + 1)
        
        # Retorna o comprimento da maior substring encontrada
        return _max



sol = Solution()
print(sol.maximumLengthSubstring("aababcbb"))  # Saída esperada: 5 ("ababc")