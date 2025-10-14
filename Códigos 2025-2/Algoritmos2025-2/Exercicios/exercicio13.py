a_str = input("Digite o número: ")
b_str = input("Digite o número a ser encaixado: ")

length_of_b = len(b_str)

if len(a_str) < length_of_b:
    print("Não encaixa")
else:
    ending_of_a = a_str[-length_of_b:]
    if ending_of_a == b_str:
        print("Encaixa")
    else:
        print("Não encaixa")