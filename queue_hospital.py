import math

def erlang_c(lam, mu, c):
    rho = lam / (c * mu)
    if rho >= 1: return None
    somme = sum((c*rho)**k / math.factorial(k) for k in range(c))
    terme = (c*rho)**c / (math.factorial(c) * (1 - rho))
    P0 = 1.0 / (somme + terme)
    Pw = terme * P0
    Lq = Pw * rho / (1 - rho)
    Wq = (Lq / lam) * 60
    return {'c':c,'rho':rho,'Lq':Lq,'Wq':Wq}

print(erlang_c(12, 5, 4))