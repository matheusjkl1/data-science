# leitura
file = open("main_character.txt", mode="r")
for line in file:
    print(line)
# não esqueça que a quebra de linha também é um caractere da linha
file.close()  # não podemos esquecer de fechar o arquivo
