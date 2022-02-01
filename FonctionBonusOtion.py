"""
3. Question Bonus : Implémentation de la formule Pricer d’option avec Python
"""
import numpy as np

def d1(S,K,X,T,r,sig):
    """
    Entrée: 
          S = Prix actuel de l’action
          X = Prix d’exercice de l’option 
          T = Temps restant avant l’expiration de l’option, en pourcentage d’une année 
          r = Taux d’intérêt sans risque 
          σ = sig: volatilité implicite du prix de l’action, mesurée par un décimal
    Role: cette fonction sera appelé lors du calcul d'un Call ou Put dans la formule du modèle Black-Scholes-Merton
    Sortie: Paramettre d1 utilisé dans la tarification d'un Call ou Put

    """
    return (np.log(S/K)+(r+sig**2/2)*T)/(sig*np.sqrt(T))

def d2(S,K,T,r,sig):
    """
    Entrée: 
          S = Prix actuel de l’action
          X = Prix d’exercice de l’option 
          T = Temps restant avant l’expiration de l’option, en pourcentage d’une année 
          r = Taux d’intérêt sans risque 
          σ = sig: volatilité implicite du prix de l’action, mesurée par un décimal
    Role: cette fonction sera appelé lors du calcul d'un Call ou Put dans la formule du modèle Black-Scholes-Merton
    Sortie: Paramettre d2 utilisé dans la tarification d'un Call ou Put

    """
    return d1(S,K,T,r,sig)-sig*np.sqrt(T)

def callOption(S,N,X,r,T):
    """
      Entrée: 
            S = Prix actuel de l’action
            X = Prix d’exercice de l’option 
            T = Temps restant avant l’expiration de l’option, en pourcentage d’une année 
            r = Taux d’intérêt sans risque 
            N = Maturité, c'est à dire le moment où on peut effectuer l'achat 
      Role: Il s'agit de la formule du modèle Black-Scholes-Merton utilisé pour le calcul du prix d'une option de type call
      Sortie: Le prix d'une option de type call

      """
    return (S*N(d1)-X*np.exp(-r*T)*N(d2))

def putOption(S,N,X,r,T):
  """
      Entrée: 
            S = Prix actuel de l’action
            X = Prix d’exercice de l’option 
            T = Temps restant avant l’expiration de l’option, en pourcentage d’une année 
            r = Taux d’intérêt sans risque 
            N = Maturité, c'est à dire le moment où on peut effectuer l'exercice
      Role: Il s'agit de la formule du modèle Black-Scholes-Merton utilisé pour le calcul du prix d'une option de type Put 
      Sortie: Le prix d'une option de type Put

      """
  return((X*np.exp(-r*T)*N(-d2)-(S*N(-d1))))