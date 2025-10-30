alumnos = [
    {"nombre": "Ana", "edad": 20, "nota": 8.5},
    {"nombre": "Luis", "edad": 22, "nota": 6.9},
    {"nombre": "Juan", "edad": 22, "nota": 6.9},
    {"nombre": "Maria", "edad": 22, "nota": 6.9},
    {"nombre": "Pedro", "edad": 22, "nota": 6.9}
]

def validate(a):
    #La funcion me valida segun sea el dato cadena o numerico
    b = a.replace(" ","")
    correc = False
    c = 0
    if a.isdigit(): c = int(a)
    try:
        #comprueba si la cadena no esta vacio
        if len(a) > 0 or len(b) > 0:
            #si la longitud es mayor que 0, no esta vacia, y hara las siguientes validaciones
            if b.isalpha(): #Si es alfanumerico
                correc = True
            elif a.isdigit() and c > 0: #si el dato enviado es numerico
               correc = True
            else:
               correc = False

        return c, correc                    
    except ValueError:
            return False
    
def operativas(val):
    datos = []
    #Segun el valor introducido 1 para añadir y 2 para buscar
    nom = input('Introduce un nombre de alunmno').lower()
    _, correc = validate(nom)
    if correc == True and len(nom) > 0:
        if val == 1:
            edad = input('Introduce una edad de alunmno')
            num, correc = validate(edad)
            if num > 0 and correc == True:
                nota = input('Introduce una nota de alunmno')
                num, correc = validate(nota)
                if num > 0 and correc == True:
                    datos = {'nombre': nom, 'edad': int(edad), 'nota': float(nota)}
                    alumnos.append(datos)
            else:
                print('el Valor introducido no es correcto')
        elif val == 2:
            for i, alumno in enumerate(alumnos, start=1):
                if alumno["nombre"].lower() == nom.lower():
                    print(f"Alumno {i}: {alumno}")
                    break
    else:
        print('el nombre no es correcto')


def visualizar_alumnos():
    i=0
    # Imprimimos el listado de alumnos y sus notas
    print('Listado de alumnos y notas:')
    for i, alumno in enumerate(alumnos, start=1):
        print(f"Alumno {i}: {alumno}")


# def mostrar_nota_media(diccionario):
#     return sum(diccionario.values()) / len(diccionario)

print(f'Esta es la gran, super, hiper, mega aportación de Óscar al proyecto')

# print(f'La nota media es {mostrar_nota_media(alumnos):.2f}')

def main():
    val = 0
    continuar = True
    while continuar:
        
        print('''          Gestor de Alumhnos
              ============================================
                    1. Ver lista de alumnos
                    2. Añadir un nuevo alumno
                    3. Buscar un alumno por nombre
                    4. Mostrar estadísticas del grupo
                    5. Salir
            ''')

        op = input('Elige una opcion')
        num, correc = validate(op)

        if num > 0 and correc == True:
            num = int(op)

            match num:
                case 1:
                    if not alumnos:
                            print('La lista esta vacia')
                    else:
                        visualizar_alumnos()
                case 2:
                    val = 1
                    operativas(val)
                case 3:
                    val = 2
                    operativas(val)
                case 4:
                    estadisticas.media_notas(alumnos)
                    estadisticas.max_notas(alumnos)
                    estadisticas.min_notas(alumnos)
                case 5:
                    continuar = False
                    break
        else:
            print('Has introducido una opcion incorrecta')

#llamamos al main
if __name__ == '__main__':
    main()
