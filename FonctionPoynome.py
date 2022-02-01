"""Cet examen consiste à mettre en application les notions de programmation Python et de versionning de code étudié au S1.1. Les supports des cours et la documentation Python sont autorisés. Aucun rendu ne sera corrigé s'il est rendu 3h00 après le début de l'examen. Tout rendu identique où jugé fortement similaire ne sera pas corrigé.

1. Création de fonction mathématique simple en Python (12 points) :

Dans cette partie, vous devrez implémenter en Python les fonctions ci-dessous :
a) Implémenter la fonction polynomiale ci-dessous :
"""
# Fonction polynomiale 

def Polynome(x):
  """
  Entrée: paramettre x
  Role: Fonction qui retourne la valeur d'un polynome 
  Sortie: La valeur d'un polynome f, de type double 
  """
  f=x**3-1.5*x**2-6*x+5
  return f
print(Polynome(5))


