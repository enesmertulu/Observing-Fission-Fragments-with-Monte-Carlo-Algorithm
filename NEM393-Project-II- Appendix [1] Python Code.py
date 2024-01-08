#Enes Mert Ulu - NEM393 Project II#
import random
import math
import numpy as np
#Constants
R_f = 0.16     #mm
R_shell = 0.18 #mm
l = 0.1        #mm
d = 0.05       #mm

#Monte Carlo Algorithm
q0 = 0                         #None particle escaped per fission.
q1 = 0                         #One particle escaped per fission.
q2 = 0                         #Two particles escaped per fission.
q1_absorbed = 0                #One particle absorbed per fission.
q2_absorbed = 0                #Two particles absorbed per fission.

#Main Loop
for i in range(1, (10**8+1)):

    r = z = R_f * random.random()
    fissionLocation = np.array([0, 0, z])

    mu1 = (2 * (random.random()**1/3)) - 1 #First Fission Fragment
    mu2 = -mu1                             #Second Fission Fragment

    #S Value 1

    if random.random() < 0.3:
        S1 = d
    else:
        S1 = -l*math.log10(random.random())

    #S Value 2

    if random.random() < 0.3:
        S2 = d
    else:
        S2 = -l*math.log10(random.random())

    #For the first fission fragment:

    a = 1
    b = 2*mu1*z
    cRf = z**2 - R_f**2
    cRs = z**2 - R_shell**2

    rootFuel = [a, b, cRf]
    rootShell = [a, b, cRs]
    d1Fuel = np.roots(rootFuel)
    d1Shell = np.roots(rootShell)

    d1fuelStar = max(d1Fuel)
    d1shellStar = max(d1Shell)

    #For the second fission fragment:

    a = 1
    b2 = 2*mu2*z
    c2Rf = z**2 - R_f**2
    c2Rs = z**2 - R_shell**2

    rootFuel2 = [a, b2, c2Rf]
    rootShell2 = [a, b2, c2Rs]
    d2Fuel2 = np.roots(rootFuel2)
    d2Shell2 = np.roots(rootShell2)

    d2fuelStar = max(d2Fuel2)
    d2shellStar = max(d2Shell2)

    #Counts
    if (S1 > d1fuelStar) and (S2 > d2fuelStar):
        q2 += 1

        if (S1 < d1shellStar) and (S2 < d2shellStar):
            q2_absorbed += 1
        elif (S1 < d1shellStar) and (S2 > d2shellStar):
            q1_absorbed += 1
        elif (S1 > d1shellStar) and (S2 < d2shellStar):
            q1_absorbed += 1

    elif (S1 > d1fuelStar) and (S2 < d2fuelStar):
        q1 += 1
        if S1 < d1shellStar:
            q1_absorbed += 1

    elif (S1 < d1fuelStar) and (S2 > d2fuelStar):
        q1 += 1
        if S2 < d2shellStar:
            q1_absorbed += 1

    else:
        q0 += 1


    if i == 10:
        print("For 10 Fissions\n")
        print(f'None particle escaped per fission number = {q0}')
        print(f'One particle escaped per fission number = {q1}')
        print(f'Two particles escaped per fission number = {q2}')
        print(f'One particle absorbed per fission number = {q1_absorbed}')
        print(f'Two particles absorbed per fission number = {q2_absorbed}')
        escapedFraction1 = ((q1+2*q2)/i)*100
        absorbedFraction1 = ((q1_absorbed+2*q2_absorbed)/i)*100
        print(f'Escape Probability from the Fuel Region = {escapedFraction1}')
        print(f'Absorption Probability in the Shell Region = {absorbedFraction1}\n')

    if i == 10**2:
        print("For 100 Fissions\n")
        print(f'None particle escaped per fission number = {q0}')
        print(f'One particle escaped per fission number = {q1}')
        print(f'Two particles escaped per fission number = {q2}')
        print(f'One particle absorbed per fission number = {q1_absorbed}')
        print(f'Two particles absorbed per fission number = {q2_absorbed}')
        escapedFraction2 = ((q1+2*q2)/i)*100
        absorbedFraction2 = ((q1_absorbed+2*q2_absorbed)/i)*100
        print(f'Escape Probability from the Fuel Region = {escapedFraction2}')
        print(f'Absorption Probability in the Shell Region = {absorbedFraction2}\n')

    if i == 10**3:
        print("For 1 000 Fissions\n")
        print(f'None particle escaped per fission number = {q0}')
        print(f'One particle escaped per fission number = {q1}')
        print(f'Two particles escaped per fission number = {q2}')
        print(f'One particle absorbed per fission number = {q1_absorbed}')
        print(f'Two particles absorbed per fission number = {q2_absorbed}')
        escapedFraction3 = ((q1+2*q2)/i)*100
        absorbedFraction3 = ((q1_absorbed+2*q2_absorbed)/i)*100
        print(f'Escape Probability from the Fuel Region = {escapedFraction3}')
        print(f'Absorption Probability in the Shell Region = {absorbedFraction3}\n')

    if i == 10**4:
        print("For 10 000 Fissions\n")
        print(f'None particle escaped per fission number = {q0}')
        print(f'One particle escaped per fission number = {q1}')
        print(f'Two particles escaped per fission number = {q2}')
        print(f'One particle absorbed per fission number = {q1_absorbed}')
        print(f'Two particles absorbed per fission number = {q2_absorbed}')
        escapedFraction4 = ((q1+2*q2)/i)*100
        absorbedFraction4 = ((q1_absorbed+2*q2_absorbed)/i)*100
        print(f'Escape Probability from the Fuel Region = {escapedFraction4}')
        print(f'Absorption Probability in the Shell Region = {absorbedFraction4}\n')

    if i == 10**5:
        print("For 100 000 Fissions\n")
        print(f'None particle escaped per fission number = {q0}')
        print(f'One particle escaped per fission number = {q1}')
        print(f'Two particles escaped per fission number = {q2}')
        print(f'One particle absorbed per fission number = {q1_absorbed}')
        print(f'Two particles absorbed per fission number = {q2_absorbed}')
        escapedFraction5 = ((q1+2*q2)/i)*100
        absorbedFraction5 = ((q1_absorbed+2*q2_absorbed)/i)*100
        print(f'Escape Probability from the Fuel Region = {escapedFraction5}')
        print(f'Absorption Probability in the Shell Region = {absorbedFraction5}\n')

    if i == 10 ** 6:
        print("For 1 000 000 Fissions\n")
        print(f'None particle escaped per fission number = {q0}')
        print(f'One particle escaped per fission number = {q1}')
        print(f'Two particles escaped per fission number = {q2}')
        print(f'One particle absorbed per fission number = {q1_absorbed}')
        print(f'Two particles absorbed per fission number = {q2_absorbed}')
        escapedFraction6 = ((q1 + 2 * q2) / i) * 100
        absorbedFraction6 = ((q1_absorbed + 2 * q2_absorbed) / i) * 100
        print(f'Escape Probability from the Fuel Region = {escapedFraction6}')
        print(f'Absorption Probability in the Shell Region = {absorbedFraction6}\n')

    if i == 10 ** 7:
        print("For 10 000 000 Fissions\n")
        print(f'None particle escaped per fission number = {q0}')
        print(f'One particle escaped per fission number = {q1}')
        print(f'Two particles escaped per fission number = {q2}')
        print(f'One particle absorbed per fission number = {q1_absorbed}')
        print(f'Two particles absorbed per fission number = {q2_absorbed}')
        escapedFraction7 = ((q1 + 2 * q2) / i) * 100
        absorbedFraction7 = ((q1_absorbed + 2 * q2_absorbed) / i) * 100
        print(f'Escape Probability from the Fuel Region = {escapedFraction7}')
        print(f'Absorption Probability in the Shell Region = {absorbedFraction7}\n')

    if i == 10 ** 8:
        print("For 100 000 000 Fissions\n")
        print(f'None particle escaped per fission number = {q0}')
        print(f'One particle escaped per fission number = {q1}')
        print(f'Two particles escaped per fission number = {q2}')
        print(f'One particle absorbed per fission number = {q1_absorbed}')
        print(f'Two particles absorbed per fission number = {q2_absorbed}')
        escapedFraction8 = ((q1 + 2 * q2) / i) * 100
        absorbedFraction8 = ((q1_absorbed + 2 * q2_absorbed) / i) * 100
        print(f'Escape Probability from the Fuel Region = {escapedFraction8}')
        print(f'Absorption Probability in the Shell Region = {absorbedFraction8}\n')
