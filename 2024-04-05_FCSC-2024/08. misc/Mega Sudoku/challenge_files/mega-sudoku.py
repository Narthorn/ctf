import zlib
import base64

def check(X):
	for index in range(3 ** 9):
		S = set()
		for i in range(9):
			M = 3 ** (i + 1)
			index_i =  (index + 3 ** i) % (M) + (index // M) * M
			S.add(X[index_i])
		if len(S) != 9:
			return False
	return True

if __name__ ==  "__main__":

	try:
		print("Input your values as 3**9 contiguous bytes in range(1, 10).")
		print("Your input will first be base64 decoded then decompressed with zlib.")

		X = input()
		X = base64.b64decode(X)
		X = zlib.decompress(X)
		X = list(X)
		assert len(X) == 3 ** 9
		assert all(v in range(1, 10) for v in X)
		assert check(X)
		print(open("flag.txt").read())
	except:
		print("Please check your inputs.")
