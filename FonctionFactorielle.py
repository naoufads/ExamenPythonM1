"""
b) Implémenter la fonction factorielle (Approche récursive ou classique) :
"""

# Fonction factoriel, approche classique, iterative 
def factorielle(n):
  """
  Entrée: param "n" un entier naturelle 
  Role: fonction qui calcule le factorielle d'un entier naturel 
  Sortie: le factoriel d'un entier naturel 
  """
  if n == 0:
      return 1
  else:
    fac = 1
    for i in range(2,n+1):
        fac = fac*i

    return fac
print(factorielle(5))