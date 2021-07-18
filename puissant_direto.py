import numpy as np

#problema direto

#coordenadas curitiba
phi1 = - (25 + 27 / 60 + 5.19 / 3600) * np.pi / 180
lambda1 = - (49 + 13 / 60 + 41.04 / 3600) * np.pi / 180
h1 = 924

#distância geodésica e azimute
s12 = 74662.35574808183
az12 = 350.6423815395677 * np.pi / 180

#adoção do elipsoide de referência
a = 6378137
f = 1 / 298.257222101

#
sec = np.pi / (3600 * 180)

#grandezas elpsoidicas
equad = 2 * f - f ** 2
M1 = a * (1 - equad) / (1 - equad * np.sin(phi1) ** 2) ** (3 / 2)
N1 = a / (1 - equad * np.sin(phi1) ** 2) ** (1 / 2)

#elementos intermediários
B = 1 / (M1 * np.sin(sec))
C = np.tan(phi1) / (2 * N1 * M1 * np.sin(sec))
D = 3 * equad * np.cos(phi1) * np.sin(phi1) * np.sin(sec) / (2 * (1 - equad * np.sin(phi1) ** 2))
E = (1 + 3 * np.tan(phi1) ** 2) / (6 * N1 ** 2)
h = (s12 + np.cos(az12)) / (M1 * np.sin(sec))

#variação de latitude entre os pontos 1 e 2
dphi = B * s12 * np.cos(az12) + C * s12 ** 2 * np.sin(az12) ** 2 - h * E * s12 ** 2 * np.sin(az12) ** 2
dphi_ = dphi + D * dphi ** 2
dphi__ = (dphi_ * np.pi) / (3600 * 180)

#cálculo da latitude do ponto 2
phi2 = phi1 - dphi__

#variação da longitude entre os pontos 1 e 2
N2 = a / (1 - equad * np.sin(phi2) ** 2) ** (1 / 2)
dlambda = s12 * np.sin(az12) / (N2 * np.cos(phi2) * np.sin(sec))

#cálculo da longitude no ponto 2
lambda2 = lambda1 + (dlambda * np.pi) / (3600 * 180)

#elementos intermediários
phim = (phi1 + phi2) / 2
F = np.sin(phim) * np.cos(phim) ** 2 * np.sin(sec) ** 2 / 12

#convergência meridiana e azimute de 2 para 1
conv = dlambda * np.sin(phim) * (1 / np.cos(dphi__ / 2)) + F * (dlambda) ** 3
conv = (conv * np.pi) / (3600 * 180)
az21 = az12 - np.pi + conv

print('Latitude Curitiba:\nPhi2 = %.5f°' %(phi2*180/np.pi))
print('\nLongitude Curitiba:\nLambda2 = %.5f°' %(lambda2*180/np.pi))
print('\nContra azimute Curitiba-Piên:\nAZ21 = %.5f°' %(az21 * 180 / np.pi))