def binary_search(nums, n, lo=0, hi=None):
    """
    Realiza busca binária em um array ordenado para encontrar um valor alvo.
    
    Args:
        nums: Lista de números inteiros ordenados
        n: Valor alvo a ser encontrado
        lo: Índice inferior (padrão 0)
        hi: Índice superior (padrão len(nums)-1)
    
    Returns:
        Índice do valor alvo se encontrado, -1 caso contrário
    """
    # Inicializa hi se não foi fornecido
    if hi is None:
        hi = len(nums) - 1  # Define o limite superior como último índice
    
    # Loop da busca binária
    while lo <= hi:  # Enquanto houver elementos para buscar
        mid = (lo + hi) // 2  # Calcula o ponto médio (índice central)
        
        if nums[mid] == n:
            return mid  # Valor alvo encontrado no índice mid
        elif nums[mid] < n:
            lo = mid + 1  # Busca na metade direita do array
        else:
            hi = mid - 1  # Busca na metade esquerda do array
    
    return -1  # Valor alvo não encontrado


def exponential_search(arr, target):
    """
    Realiza busca exponencial em um array ordenado para encontrar um valor alvo.
    Combina a técnica de expansão exponencial com busca binária.
    
    Args:
        arr: Lista de números inteiros ordenados
        target: Valor alvo a ser encontrado
    
    Returns:
        Índice do alvo se encontrado, -1 caso contrário
    """
    # Verifica se o array está vazio
    if not arr:
        return -1
    
    # Verifica o primeiro elemento diretamente
    if arr[0] == target:
        return 0
    
    n = len(arr)
    i = 1  # Começa com índice 1
    
    # Expansão exponencial para encontrar o intervalo
    while i < n and arr[i] <= target:
        i *= 2  # Dobra o tamanho do intervalo de busca
    
    # Realiza busca binária no intervalo encontrado
    return binary_search(
        arr, 
        target, 
        i // 2,  # Início do intervalo (metade do último i)
        min(i, n - 1)  # Fim do intervalo (não ultrapassa o array)
    )

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

print(exponential_search(arr, target))  # Output: 6 (index of 7)
print(binary_search(arr, target))      # Output: 6 (index of 7)