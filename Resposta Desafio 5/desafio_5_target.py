user_input = input("Digite uma palavra ou texto para ser invertido: ")

i = 0
reversed_string = ""

while len(user_input) > i:
    reversed_string += user_input[-1 - i]
    i += 1

print(reversed_string)