from Crypto.Random.random import randrange

class SharedValue:
    def __init__(self, bit_size, order, shares = None):
        self.order = order
        self.value = []
        self.bit_size = bit_size
        if shares != None:
            for i in range(order + 1):
                self.value.append(shares[i])
        else:
            for i in range(order + 1):
                self.value.append(0)

    def reset(self):
        for i in range(self.order + 1):
            self.value[i] = 0

    def set(self, value):
        self.value[0] = value
        for i in range(1,self.order + 1):
            self.value[i] = 0

    def randomize(self):
        for i in range(self.order + 1):
            self.value[i] = randrange(1 << self.bit_size)

    def refresh(self):
        for i in range(self.order):
            for j in range(i+1, self.order + 1):
                t = randrange(1 << self.bit_size)
                self.value[i] ^= t
                self.value[j] ^= t

    def __xor__(self, other):
        shares = []
        for i in range(self.order + 1):
            shares.append(self.value[i] ^ other.value[i])
        return SharedValue(self.bit_size, self.order, shares)

    def __and__(self, other):
        shares = []
        for i in range(self.order + 1):
            shares.append(self.value[i] & other.value[i])
        for i in range(self.order):
            for j in range(i + 1, self.order + 1):
                t = randrange(1 << self.bit_size)
                shares[i] ^= t ^ (self.value[i] & other.value[j])
                shares[j] ^= t ^ (self.value[j] & other.value[i])
        return SharedValue(self.bit_size, self.order, shares)

    def export(self):
        res = []
        for i in range(self.order + 1):
            res.append(self.value[i])
        return res

if __name__ ==  "__main__":
    order = 32
    bit_size = 128
    key = SharedValue(bit_size, order)
    key.reset()
    key.randomize()
    key.refresh()

    message = 0xFFEEDDCCBBAA99887766554433221100
    msg = SharedValue(bit_size, order)
    msg.set(message)

    x = msg ^ key
    a = msg & key
