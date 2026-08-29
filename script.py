def saludo(nombre):
    return f"¡Hola, {nombre}!"

def suma(a, b):
    return a + b

if __name__ == "__main__":
    print(saludo("mundo"))
    print(f"2 + 3 = {suma(2, 3)}")