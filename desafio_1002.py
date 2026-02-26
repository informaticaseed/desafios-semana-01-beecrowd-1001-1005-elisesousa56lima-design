"""
Beecrowd 1002 - Área do Círculo

A fórmula para calcular a área de uma circunferência é: area = π . raio².
Considerando para este problema que π = 3.14159:

- Efetue o cálculo da área, elevando o valor de raio ao quadrado e
 multiplicando por. 

Entrada: O arquivo de entrada contém um valor de ponto flutuante (dupla precisão),
no caso, a variável raio.

Saída: Apresentar a mensagem "A=" seguido pelo valor da variável area, conforme
exemplo abaixo, com 4 casas após o ponto decimal. Utilize variáveis de dupla precisão
(duplo).
"""

# Link do problema: https://judge.beecrowd.com/pt/problems/view/1002

# Escreva sua solução abaixo

# Definição do valor de pi conforme o enunciado
PI = 3.14159

# Leitura do raio (ponto flutuante de dupla precisão)
raio = float(input())

# Cálculo da área: area = pi * raio^2
area = PI * (raio ** 2)

# Exibição do resultado com 4 casas decimais
# O :.4f garante a formatação correta e o arredondamento necessário
print(f"A={area:.4f}")
