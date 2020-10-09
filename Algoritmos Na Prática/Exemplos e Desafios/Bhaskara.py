def bhaskara(a, b, c):
    x1 = (-b + (b**2 - 4 * a * c) ** 0.5) / 2
    x2 = (-b - (b**2 - 4 * a * c) ** 0.5) / 2

    return x1, x2
    
print(bhaskara(1, 4, 5))
