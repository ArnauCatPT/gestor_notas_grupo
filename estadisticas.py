def media_notas(dict):
    notas = [fila["nota"] for fila in dict]  
    return sum(notas)/len(dict)


def max_notas(dict):
        notas = [fila["nota"] for fila in dict]  
        return print(f"Nota más alta: {max(notas)}")

def min_notas(dict):
    notas = [fila["nota"] for fila in dict]  
    return print(f"Nota más baja: {min(notas)}")