import numpy as np
import numpy.fft

FLAG = open("flag.txt", "rb").read()

array = np.array([], dtype=np.complex64)
for c in FLAG:
    array = np.append(array, c)


# Compute inverse FFT
result = np.array(np.fft.ifft(array, n=64), dtype=np.complex64)

result.tofile("challenge")
