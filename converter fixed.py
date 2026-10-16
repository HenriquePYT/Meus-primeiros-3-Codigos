

def remove_signal (s):
    # aqui o float vai abraçar o s que é a variavel o replace que vai dar o sinal do python pra tirar o cifrao se tiver apenas
    return float(s.replace ("$", ""))

def converter_dollar_to_real (d, c):
    # as variaveis no parametro nao precisam fzr referencias aos nomes, mas sim as posiçoes do main() 
    return float(d * c)
    
def main():
    print("Welcome to the Currency´s Converter!")
    product = input("What´s the product that you bought")
    product_price = input("What´s was the product´s price in dollar that you bought? ")
    # nao ha nenhum problema dps do def criado dentro dos parenteses ter o mesmo nome da variavel
    product_price= remove_signal(product_price)
    dollar_currently_price = float(input("What´s the currently price of the dollar right now? "))
    #refaça a mesma coisa do def remove_signal mas com o def converter_dollar_to_real
    dollar_currently_price = converter_dollar_to_real(product_price, dollar_currently_price)
    #agora faça o print mostrando o valor total, usando a variavel que vc criou
    print(f"Your converted value will be {dollar_currently_price}")
    print("Thank you so much for use the Currency´s Converter!")
#chamar a função
main()