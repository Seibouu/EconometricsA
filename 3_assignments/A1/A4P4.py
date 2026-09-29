import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.pi * x**2 + np.pi * x * np.sqrt(x**2+15**2)-1400

def sekant_metode(a, b, M=100, eps = 1e-7, delta = 1e-10):
    fa = f(a)
    fb = f(b)

    x_value = [a,b]
    fejl_value = [abs(fa),abs(fb)]

    print(f"Iteration 0: x = {a}, f(x)= {fa}")
    print(f"Iteration 1: x = {b}, f(x) = {fb}")

    for k in range (2, M+1):
        if abs(fa)>abs(fb):
            a,b = b,a
            fa, fb = fb,fa

        s = (b-a)/(fb-fa)
        b = a
        fb =fa
        a = a-fa*s
        fa = f(a)

        x_value.append(a)
        fejl_value.append(abs(fa))

        print(f"Iteration {k}: x = {a}, f(x) = {fa}")

        if abs(fa) < eps or abs(b-a)< delta:
            print(f"\nKonvergerede efter {k} iterationer")
            return a, x_value, fejl_value

    print("Advarsel: Nåede max iterationer.")
    return a, x_value, fejl_value

rod, x_historik, fejl_historik = sekant_metode(10.0, 15.0)

dx = np.abs(np.diff(x_historik))
x, y = dx[:-1], dx[1:]

plt.loglog(x, y, 'bo-', label='Sekantmetode')
plt.loglog(x, x**1, 'g--', label='Lineær hældning')
plt.loglog(x, x**2, 'r--', label='Kvadratisk hældning')

plt.xlabel(r'$|x_n - x_{n-1}|$')
plt.ylabel(r'$|x_{n+1} - x_n|$')
plt.legend()
plt.savefig("konvergensplot.png")
plt.show()



def bisektion_metode(a, b, M=100, eps = 1e-7, delta = 1e-10):
    u =f(a)
    v = f(b)
    e = b-a
    if np.sign(u) == np.sign(v):
        print("Stop: f(a) og f(b) har samme fortegn")
        return
    for k in range (1, M+1):
        e = e/2
        c = a+e
        w = f(c)

        print(f"Iteration {k}: c={c:.6f}, w={w:.2e}, e){e:.2e}")

        if abs(e) < delta or abs(w) < eps:
            print(f"\nKonvergerede efter {k} iterationer")
            return c, w
        if np.sign(w) != np.sign(u):
            b = c
            v = w
        else:
            a = c
            u = w
    print("Advarsel: Nåede max iterationer")
    return c, w        

#bisektion_metode(10.0,15.0)

