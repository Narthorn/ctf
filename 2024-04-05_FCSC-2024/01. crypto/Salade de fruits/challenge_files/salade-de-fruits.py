from itertools import count
from hashlib import sha256

for pineapple in count(start = 1):
  for strawberry in range(1, pineapple + 1):
    for banana in range(1, pineapple + 1):
      if pineapple ** 3 + strawberry ** 3 == 94 * banana ** 3:
        h = sha256(str(banana).encode()).hexdigest()
        print(f"FCSC{{{h}}}")
        exit(1)
