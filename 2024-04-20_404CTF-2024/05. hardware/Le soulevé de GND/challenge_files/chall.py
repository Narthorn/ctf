from myhdl import *

A = 7
B = 1918273
N = 25


@block
def GND(state, clk):
    """
    Le sol il bouge ?
    ça envoie un mauvais signal tout ça...
    """

    @always(clk.posedge)
    def core():
        state.next = A * state + B

    return core


@block
def xor(a, b, z):

    @always_comb
    def core():
        z.next = a ^ b

    return core


@block
def demul(sel, s, z):

    @always_comb
    def core():
        z.next = s[sel]

    return core


@block
def up(a, clk):

    @always(clk.posedge)
    def core():
        a.next += 1

    return core


@block
def checker(s, v, sel, clk):
    data = [
        78,
        114,
        87,
        9,
        245,
        67,
        252,
        90,
        90,
        126,
        120,
        109,
        133,
        78,
        206,
        121,
        52,
        115,
        123,
        102,
        164,
        194,
        170,
        123,
        5,
    ]

    @always(clk.posedge)
    def core():
        s.next &= data[sel] == v

        if sel == N - 1:
            if s.next:
                print("GG ! Le flag est 404CTF{Le mot de passe}")
            else:
                print("uh oh...")

    return core


@block
def main(inp):

    clk_sig = Signal(bool(0))
    state = Signal(modbv(0, 0, 256))
    sel = Signal(modbv(0, 0, N))
    upper = up(sel, clk_sig)
    s = Signal(modbv(0, 0, 256))
    demul_inst = demul(sel, inp, s)
    tc = Signal(modbv(0, 0, 256))
    xor_inst = xor(s, state, tc)
    gnd = GND(state, clk_sig)

    m = Signal(bool(1))
    checker_inst = checker(m, tc, sel, clk_sig)

    @always(delay(10))
    def clk():
        clk_sig.next = not clk_sig

    return clk, upper, demul_inst, gnd, xor_inst, checker_inst


a = input(">>> ")
assert len(a) == N

inp = [Signal(modbv(ord(c), 0, 256)) for c in a]

sim = main(inp)
sim.run_sim(20 * N)
