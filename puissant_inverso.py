import numpy as np

#problema inverso

#coordenadas piên
phi1 = - (26 + 6 / 60 + 58.91 / 3600) * np.pi / 180
lambda1 = - (49 + 20 / 60 + 58 / 3600) * np.pi / 180
h1 = 872

#coordenadas curitiba
phi2 = - (25 + 27 / 60 + 5.19 / 3600) * np.pi / 180
lambda2 = - (49 + 13 / 60 + 41.04 / 3600) * np.pi / 180
h2 = 924

#adoção do elipsoide de referência
a = 6378137
f = 1 / 298.257222101

#
sec = np.pi / (3600 * 180)

#grandezas elpsoidicas
equad = 2 * f - f ** 2
M1 = a * (1 - equad) / (1 - equad * np.sin(phi1) ** 2) ** (3 / 2)
N1 = a / (1 - equad * np.sin(phi1) ** 2) ** (1 / 2)
N2 = a / (1 - equad * np.sin(phi2) ** 2) ** (1 / 2)

#elementos intermediários
B = 1 / (M1 * np.sin(sec))
C = np.tan(phi1) / (2 * N1 * M1 * np.sin(sec))
D = 3 * equad * np.cos(phi1) * np.sin(phi1) * np.sin(sec) / (2 * (1 - equad * np.sin(phi1) ** 2))
E = (1 + 3 * np.tan(phi1) ** 2) / (6 * N1 ** 2)
A_ = 1 / (N2 * np.sin(sec))
dphi = (phi2 - phi1) * 3600 * 180 / np.pi
dlambda = (lambda2 - lambda1) * 3600 * 180 / np.pi

#cálculo de x e y
x = dlambda * np.cos(phi2) / A_
y = - (dphi + C * x ** 2 + dphi * E * x ** 2 + D * dphi ** 2) / B

#cálculo do azimute do p1 para p2
az12 = np.arctan2(x, y)

#cálculo da distância entre os pontos 1 e 2
s12 = y / np.cos(az12)
s12_ = x / np.sin(az12)

#elementos intermediários
phim = (phi1 + phi2) / 2
F = np.sin(phim) * np.cos(phim) ** 2 * np.sin(sec) ** 2 / 12

#convergência meridiana e azimute de 2 para 1
conv = dlambda * np.sin(phim) * (1 / np.cos(dphi / 2)) + F * (dlambda) ** 3
conv = (conv * np.pi) / (3600 * 180)
az21 = az12 + np.pi + conv

print('Distância geodésica Piên-Curitiba:\nS12 = %.5f metros' %s12_)
print('\nAzimute Piên-Curitiba:\nAZ12 = %.5f°' %(az12 * 180 / np.pi))
print('\nContra azimute Piên-Curitiba:\nAZ21 = %.5f°' %(az21 * 180 / np.pi))