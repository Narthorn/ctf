import random as rd
import math
from myhdl import *

loton = [rd.randint(1, 2 ** 8 - 1) for _ in range(74)] + [0, rd.randint(1, 2 ** 8 - 1)] + [0, 0] * 90 #la génération n'est pas forcément la même sur le serveur. Prenez en compte tous les cas.
run_time = 700000 #valeur du serveur

@block
def Ponge(francis, beauvoir, sade):

    @always_comb
    def core():
        if (francis == 0x3d or francis == 0x4a) and beauvoir != 0:
            sade.next = 1
        else:
            sade.next = 0

    return core

@block
def Sand(corneille, rostand, duras, merimee, hugo, racine, rabelais, claudel, giono, colette):
    voltaire = [Signal(modbv(0, 0, 2 ** 8)) for _ in range(8)]

    @always(colette.posedge)
    def core():

        if merimee:
            voltaire[duras].next = rabelais
        if not (merimee and duras == 7):
            voltaire[7].next = voltaire[7] + 1

        if merimee and duras == 7:
            giono.next = True
        else:
            giono.next = False

        return

    @always_comb
    def lamartine():
        hugo.next = voltaire[corneille]
        racine.next = voltaire[rostand]
        claudel.next = voltaire[7]

    return core, lamartine


@block
def Coulon(dolto, dufourmantelle, yourcenar, deffand):
    @always_comb
    def core():
        if deffand == 0x23 or deffand == 0x4f:
            yourcenar.next = dolto + 1
        elif deffand == 0x3e or deffand == 0x41:
            yourcenar.next = dolto ^ dufourmantelle
        elif deffand == 0x42 or deffand == 0x7e:
            yourcenar.next = dolto + dufourmantelle
        elif deffand == 0x12 or deffand == 0x18:
            yourcenar.next = ~ dolto
        elif deffand == 0x2d or deffand == 0x6f:
            yourcenar.next = dolto * dufourmantelle
        elif deffand == 0x0e or deffand == 0x11:
            yourcenar.next = dolto >> dufourmantelle
        elif deffand == 0x01 or deffand == 0x33:
            yourcenar.next = dolto << dufourmantelle
        elif deffand == 0x29 or deffand == 0x6c:
            yourcenar.next = (dolto >> (dufourmantelle % 8)) | (dolto << (8 - (dufourmantelle % 8))) & 0xFFFFFFFF
        elif deffand == 0x27 or deffand == 0x45:
            yourcenar.next = (dolto << (dufourmantelle % 8)) | (dolto >> (8 - (dufourmantelle % 8)))
        elif deffand == 0x13 or deffand == 0x5a:
            yourcenar.next = dolto
        elif deffand == 0x3d or deffand == 0x4a:
            yourcenar.next = dufourmantelle
        else:
            yourcenar.next = 0

    return core

@block
def Stael(auclair, godard):
    perec = [Signal(modbv(v, 0, 2 ** 8)) for v in loton]
    @always_comb
    def core():
        godard.next = perec[auclair]

    return core

@block
def Senghor(michon, larbaud, leroux, pisan, pascal, bel, schmitt, sagan, signol, torpor, verdier, tocqueville, tuffrau, quinet):
    @always_comb
    def core():
        if leroux == 1:
            if michon == 0x4 and larbaud == 0x18:
                sagan.next = 1
                pisan.next = 0
                pascal.next = 0
                bel.next = 0
                schmitt.next = 0
            elif not (michon == 0x00 and larbaud == 0x00):
                levy = michon >> 1
                if levy in (
                        0x23, 0x4f, 0x3e, 0x41, 0x42, 0x7e, 0x12, 0x18, 0x3d, 0x4a, 0x2d, 0x6f, 0xe, 0x11, 0x1, 0x33,
                        0x29,
                        0x6c, 0x27, 0x45, 0x13, 0x5a):
                    pisan.next = levy
                    if levy in (0x13, 0x5a):
                        tuffrau.next = 1
                        quinet.next = larbaud & 0b111111
                    else:
                        tuffrau.next = 0
                    tocqueville.next = 1
                    verdier.next = 0
                    torpor.next = 0
                else:
                    pisan.next = 0
                    if levy in (0x3, 0x6a):
                        verdier.next = 1
                        torpor.next = 0
                        tocqueville.next = 1
                    elif levy in (0x46, 0x66):
                        verdier.next = 0
                        torpor.next = 1
                        tocqueville.next = 0
                    else:
                        signol.next = 1
                pascal.next = ((michon & 0b1) << 2) | (larbaud >> 6)
                bel.next = (larbaud >> 3) & 0b111
                schmitt.next = larbaud & 0b111
            else:
                verdier.next = 0
                torpor.next = 0
                tocqueville.next = 0
        else:
            pisan.next = 0
            pascal.next = 0
            bel.next = 0
            schmitt.next = 0
            tocqueville.next = 0
            tuffrau.next = 0
            quinet.next = 0
            torpor.next = 0

    return core

@block
def Alcott(very, weil, volodine, rod, robin):
    rapin = [Signal(modbv(0, 0, 2 ** 8)) for _ in range(256)]

    @always(robin.posedge)
    def core():
        if weil:
            rapin[very].next = volodine

    @always_comb
    def lebel():
        rod.next = rapin[very]

    return core, lebel


@block
def Queneau(lemieux, leduc, laye, manglou, malesherbes, marc):
    @always(marc.posedge)
    def core():
        if malesherbes:
            manglou.next = False
            leduc.next = lemieux
        else:
            if manglou:
                leduc.next = lemieux
            else:
                laye.next = lemieux
            manglou.next = not manglou

    return core


@block
def Gouges(desanti, langevin, tellier, leroy):
    @always_comb
    def core():

        if leroy:
            tellier.next = langevin
        else:
            tellier.next = desanti

    return core


@block
def Boetie(jacquet, jarry, kundera, kessel, munier):
    milesi = Signal(modbv(0, 0, 2 ** 8))
    meyssan = Signal(modbv(0, 0, 2 ** 8))
    laclos = Signal(modbv(0, 0, 2 ** 8))
    karr = Signal(modbv(0xcafe, 0, 2 ** 16))

    @always(munier.posedge)
    def core():
        if not jarry:
            if kundera % 2 == 0:
                milesi.next = milesi ^ jacquet
            else:
                meyssan.next = meyssan ^ jacquet
            laclos.next = jacquet
        if laclos == 0x04 and jacquet == 0x18:
            if milesi == karr[:8] and meyssan ^ jacquet == karr[8:0]:
                jarry.next = not jarry
            else:
                kessel.next = 1
        elif kundera == 255:
            kessel.next = 1
        kundera.next = kundera + 1

    return core


@block
def Supervielle(program):
    ionesco, hallier, grandbois, francoeur, follain, deleuze, diderot, labe, friang, bert, caron, cloux = [Signal(bool(0)) for _ in range(12)]
    chamfort = Signal(bool(1))
    coco, buron, beda, choffel, gautier, grall, gottis, marot, renan, stanton, mai, verlaine, queffelec, mauriac, montaigne, gaboriau, curtis, darol, bordes = [Signal(modbv(0, 0, 2 ** 8)) for _ in range(19)]
    bernstein = Signal(bool(1))  
    cendres = Senghor(buron, gottis, chamfort, marot, coco,
                                     gaboriau, beda, bert, grandbois, hallier,
                                     deleuze, diderot, cloux, bordes)
    chedid = Alcott(queffelec, hallier, choffel, mai, ionesco)
    giroud = Stael(queffelec, renan)
    sevigne = Gouges(stanton, renan, grall, deleuze)
    gide = Alcott(curtis, bernstein, mauriac, verlaine, francoeur)
    girardin = Queneau(verlaine, buron, gottis, chamfort, labe, ionesco)
    lacascade = Gouges(diderot, Signal(bool(0)), follain, caron)
    pagnol = Coulon(darol, choffel, stanton, marot)
    logist = Ponge(marot, queffelec, caron)
    rimbaud = Gouges(montaigne, gautier, curtis, friang)
    touzalin = Boetie(mauriac, friang, montaigne, grandbois, francoeur)
    truel = Sand(gaboriau, beda, coco,
                                       follain, queffelec, choffel,
                                       grall, gautier, labe, ionesco)
    serge = Gouges(queffelec, bordes, darol, cloux)

    @always(delay(10))
    def selve():
        if friang and not grandbois and not bert:
            bernstein.next = 0
            ionesco.next = not ionesco
        elif not friang:
            if not ionesco:
                mauriac.next = program[montaigne]
            francoeur.next = not francoeur

    @always(delay(run_time // 20))
    def senecal():
        print(f'RUNNING...{math.ceil(now()/run_time * 100)}%')
    
    @always(delay(run_time))
    def margry():
        if bert == 1 and grandbois == 0:
            print("program successfully executed !")
        else:
            print("Error 418, bTpot")
            print(bert, grandbois)

    return selve, pagnol, giroud, girardin, cendres, truel, chedid, sevigne, \
           gide, touzalin, rimbaud, serge, logist, lacascade, margry, senecal

program = input('>>> ')
prog = [int(program[i * 2: i * 2 + 2], 16) for i in range(len(program) // 2)]
simInst = Supervielle(prog + [0 for i in range(256 - len(prog))])
simInst.run_sim(run_time)
