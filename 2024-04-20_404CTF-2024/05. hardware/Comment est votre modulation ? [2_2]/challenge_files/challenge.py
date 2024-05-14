import numpy as np


def QAM16(symbol):
	return -3+2*(symbol>>2)+1j*(3-2*(symbol&0b11))

def OFDM(T,N,X,t):
	return sum([X[k]*np.exp(2j*np.pi*k*t/T) for k in range(N)])

def map_bytes(bytes_list):
	mapped_symbols = []
	for b in bytes_list:
		mapped_symbols += [QAM16(b>>4),QAM16(b&0b1111)]
	return mapped_symbols

NB_SOUS_PORTEUSES = 8
F_C = 7e3
F_E = int(50*F_C)
T_E = 1/F_E
R = 1000
T = 1/R

data = np.fromfile('flag.png', dtype = "uint8")
modulated = []

for i in range(0,len(data),4):
	mapped = np.array(map_bytes(data[i:i+4]))
	modulated += [OFDM(T,NB_SOUS_PORTEUSES,mapped,t*T_E) for t in range(int(F_E*T))]

np.array(modulated,dtype='complex64').tofile("flag.iq")
