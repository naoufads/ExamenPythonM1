"""
2 Création de fonction comportant des modules de gestions des exceptions (5 points) :
En utilisant l’une des trois fonctions mathématiques précédentes, implémenter un script permettant de gérer les exceptions pours les cas suivants :

Saisie d'une chaine de caractère dans les arguments de la fonction
Saisie un nombre complexe
Saisie d'un nombre négatif
Saisie d'un très grand nombre
Saisie d'un très petit nombre
"""

#Dans cet exercice, nous allons prendre la fonction fibonacci
def fibonacci(n):
    """
    Entrée: param n, un entier naturel 
    Rôle: il s'agit d'une fonction recusive qui calcul le terme de la suite de Fibonacci connaissant le rang n
    Sortie: Le terme de la suite de Fobonacci au rang n
    """
    ########## Cas 1: l'utilisateur saisie une chaine de caractère 
    if type(n)==str:
      #print("Veillez saisir un nombre entier s'il vous plait !")
      while type(n) == str: #Execute ce code suivant, tant que n est une chaine de caractère
        try:
            n = int(input("Entrer un entier s'il vous plait")) #Saisir une valeur de n et le transformer en entier
        except ValueError:   # Si nous avons cet exception, alors execute le code suivant
            print(n," est une chaine de caractère et non pas un entier.\n")

    ########## Cas 2: l'utilisateur saisie un nombre complexe positif ou negatif
    if type(n)==complex:
       n = int(abs(n.real)) # Nous prenons seulement la partie réel de n et nous le convertissons en entier en valeur absolue
    
    ########## Cas 3: l'utilisateur saisie un nombre réel negatif
    if n<0:
       n = int(abs(n)) #Nous prenons la valeur absolue convertie en entier naturel
    
    ##### Cas 3: L'utilisateur entre un nombre n très grand et dont la longueur est au-dessus de 16 
    while len(str(n)) >16:  #Execute ce code tanque longeur de n variables est > à 16
      n = int(input("Entrer un nombre entier dont le nombre de chiffre est inferieur à 16\n"))

    #### Cas 4: l'utilisateur entre un nombre très petit 
    """
    Ce cas est déjà géré lorsque le nombre entrée est inférieur 0.  
    """
    if(n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

print(fibonacci("iii"))    