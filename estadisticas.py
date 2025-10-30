def media_notas(dict):
    return sum(dict.values())/len(dict)

def max_notas(dict):
    notas = [nota for fila, nota in dict.items()]
    return print(f"Nota más alta: {max(notas)}")

def min_notas(dict):
    notas = [nota for fila, nota in dict.items()]
    return print(f"Nota más baja: {min(notas)}")