def cargar_ventas(lista: list, lista_analisis: list) -> list:
    '''
    Carga ventas en una lista a elección.
    '''
    for i in lista:
        lista[i] = int(input(f"Ingrese ventas para {lista_analisis[i]}: "))

        while lista[i] <= 0:
            lista[i] = int(input(f"ERROR. No puede ser 0 o menos: "))
# Definitivamente incompleto y no funcional


    