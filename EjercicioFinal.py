# Lanzar nuestras propias excepciones
while True:
    def verificandoEdad(edad):

        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
        elif edad < 18:
            print("Eres muy joven")
        elif edad < 30:
            print("Eres joven")
        elif edad < 50:
            print("Eres maduro")


    edad = int(input("Digite su edad: "))
    try:
        verificandoEdad(edad)
    except ValueError as EdadNegativa:
        print(EdadNegativa)
    else:
        print("Programa terminado")






# Carolina EM :)
