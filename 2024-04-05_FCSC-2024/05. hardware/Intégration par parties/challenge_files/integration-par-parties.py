import json
from shared_value import SharedValue

order = 32
bit_size = 256
with open("flag.bin", "rb") as f_flag:
    flag = f_flag.read()

key = SharedValue(bit_size, order)
key.set(int(flag, 16))
key.refresh()

print(json.dumps(key.export(), indent = 4))
