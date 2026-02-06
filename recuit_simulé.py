import math 
import random 

""" Exercise: Finding the minimum of a simple function
Objective: To use simulated annealing to find the minimum value of a simple mathematical function.
"""

def function(x):
    return x**2 + 4*x + 4

def random_num(start, end):
    return random.uniform(start, end)

def proba(T, delta): 
    return math.exp(-delta/T)

def algorithm(x, T):
    f_x = function(x)
    voisin_x = x + random_num(-1, 1)
    f_voisinx = function(voisin_x)
    delta = f_voisinx - f_x
    if f_voisinx < f_x:
        return voisin_x, T * 0.99
    else : 
        probability = proba(T, delta)
        num = random.random()  # nombre entre 0 et 1
        if num < probability:
            return voisin_x, T * 0.99
        else : 
          return x, T * 0.99

def execute():
  T = 9
  x = random_num(-10, 10)
  print(f"Point de départ x = {x}, f(x) = {function(x)}")
  while(T > 2):
      x, T = algorithm(x, T)
  print(f"Minimum trouvé: x = {x}, f(x) = {function(x)}")

execute()