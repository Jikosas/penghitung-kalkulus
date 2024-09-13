import sympy as sp

# Mendefinisikan variabel simbolik
x, y = sp.symbols('x y')

# Contoh fungsi
f = x**3 * y + y**3 + sp.sin(x)

# Diferensiasi
derivative_x = sp.diff(f, x)
derivative_y = sp.diff(f, y)

print(f'Derivatif terhadap x: {derivative_x}')
print(f'Derivatif terhadap y: {derivative_y}')

# Integrasi
integral_x = sp.integrate(f, x)
integral_y = sp.integrate(f, y)

print(f'Integral tak tentu terhadap x: {integral_x}')
print(f'Integral tak tentu terhadap y: {integral_y}')

# Integrasi tertentu
definite_integral_x = sp.integrate(f, (x, 0, 1))
definite_integral_y = sp.integrate(f, (y, 0, 1))

print(f'Integral tertentu terhadap x dari 0 hingga 1: {definite_integral_x}')
print(f'Integral tertentu terhadap y dari 0 hingga 1: {definite_integral_y}')
