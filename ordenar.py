def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        # Percorre a lista até a penúltima posição não ordenada
        for j in range(0, n-i-1):
            # Troca os elementos se estiverem na ordem errada
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

dados = [64, 34, 25, 12, 22, 11, 90]
print("Bubble Sort:", bubble_sort(dados))

def insertion_sort(lista):
    for i in range(1, len(lista)):
        # Seleciona o elemento atual
        key = lista[i]
        j = i - 1
        # Move os elementos da porção ordenada para criar espaço para o elemento atual
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista

dados = [64, 34, 25, 12, 22, 11, 90]
print("Insertion Sort:", insertion_sort(dados))

def merge_sort(lista):
    if len(lista) > 1:
        # Divide o array no meio
        meio = len(lista) // 2
        parte_esquerda = lista[:meio]
        parte_direita = lista[meio:]

        # Ordena cada metade recursivamente
        merge_sort(parte_esquerda)
        merge_sort(parte_direita)

        # Mescla as metades ordenadas
        indice_esquerda = indice_direita = indice_geral = 0
        while indice_esquerda < len(parte_esquerda) and indice_direita < len(parte_direita):
            if parte_esquerda[indice_esquerda] < parte_direita[indice_direita]:
                lista[indice_geral] = parte_esquerda[indice_esquerda]
                indice_esquerda += 1
            else:
                lista[indice_geral] = parte_direita[indice_direita]
                indice_direita += 1
            indice_geral += 1

        # Copia os elementos restantes da parte esquerda (se houver)
        while indice_esquerda < len(parte_esquerda):
            lista[indice_geral] = parte_esquerda[indice_esquerda]
            indice_esquerda += 1
            indice_geral += 1

        # Copia os elementos restantes da parte direita (se houver)
        while indice_direita < len(parte_direita):
            lista[indice_geral] = parte_direita[indice_direita]
            indice_direita += 1
            indice_geral += 1

dados = [64, 34, 25, 12, 22, 11, 90]
merge_sort(dados)
print("Merge Sort:", dados)


# Exemplo de uso
dados = [64, 34, 25, 12, 22, 11, 90]
merge_sort(dados)
print("Merge Sort:", dados)


# Exemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
merge_sort(lista)
print("Merge Sort:", lista)

# Exemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print("Insertion Sort:", insertion_sort(lista))

# Exemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print("Bubble Sort:", bubble_sort(lista))
import time
import random

# Função para gerar conjuntos de dados
def generate_data(size, data_type="random"):
    if data_type == "ordered":
        return list(range(size))
    elif data_type == "reverse_ordered":
        return list(range(size, 0, -1))
    elif data_type == "random":
        return [random.randint(1, 1000) for _ in range(size)]
    else:
        raise ValueError("Tipo de dado desconhecido")

# Função para medir o tempo de execução
def measure_execution_time(sort_function, data):
    start_time = time.time()
    sort_function(data)
    end_time = time.time()
    return end_time - start_time

# Tamanhos de dados e cenários
sizes = [100, 1000, 10000]
scenarios = ["ordered", "reverse_ordered", "random"]

# Testes de desempenho
results = []
for size in sizes:
    for scenario in scenarios:
        data = generate_data(size, scenario)
        for algo_name, algo_function in [
            ("Bubble Sort", bubble_sort),
            ("Insertion Sort", insertion_sort),
            ("Merge Sort", merge_sort),
        ]:
            # Clona o conjunto de dados para cada teste
            test_data = data[:]
            time_taken = measure_execution_time(algo_function, test_data)
            results.append((algo_name, size, scenario, time_taken))

# Exibir resultados
print("Resultados de Desempenho:")
for result in results:
    print(f"Algoritmo: {result[0]}, Tamanho: {result[1]}, Cenário: {result[2]}, Tempo: {result[3]:.6f} segundos")
