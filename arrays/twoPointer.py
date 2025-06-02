class Solution:
    def reverseWords(self, s):
        res = ''  # String que armazenará o resultado final
        l, r = 0, 0  # Ponteiros esquerdo (l) e direito (r) para marcar o início e fim de cada palavra
        
        while r < len(s):
            if s[r] != ' ':
                # Se o caractere atual não é espaço, movemos o ponteiro direito para frente
                r += 1
            else:
                # Quando encontramos um espaço, pegamos a palavra (de l até r) e a invertemos
                res += s[l:r+1][::-1]  # Adiciona a palavra invertida + espaço ao resultado
                r += 1  # Move r para o próximo caractere (início da próxima palavra)
                l = r   # Atualiza l para a posição de r (início da nova palavra)
        
        # Após o loop, adiciona a última palavra (que não foi processada no loop)
        res += ' '
        res += s[l:r + 2][::-1]
        return res[1:]  # Retorna o resultado removendo o espaço extra no início