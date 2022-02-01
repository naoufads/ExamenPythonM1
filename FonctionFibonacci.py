"""
c) Implémenter la suite de Fibonnaci

La suite de Fibonacci est une suite de nombres entiers de 0, 1, 1, 2, 3, 5, 8 ….
Les deux premiers termes sont 0 et 1. Tous les autres termes sont obtenus en ajoutant les deux termes précédents.
 Cela signifie que le nième terme est la somme des (n-1)ème et (n-2)ème terme.
"""
#Suite de fibonacci, approche recursive 
def fibonacci(n):
    """
    Entrée: param n, un entier naturel 
    Rôle: il s'agit d'une fonction recusive qui calcul le terme de la suite de Fibonacci connaissant le rang n
    Sortie: Le terme de la suite de Fobonacci au rang n
    """
    if(n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

#Code qui demande à l'utilisateur d'entrée le rang n
n = int(input("Entrez le nombre :"))

#Code qui affiche les termes d'une suite de fibonacci
print("La suite de Fibonacci est :")
for k in range(n):
    print(fibonacci(k),end=", ")
    