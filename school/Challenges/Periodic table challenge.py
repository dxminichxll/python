while True:
    symbol = input("Enter a chemical symbol for its information:")

    if symbol == 'Li':
        name = 'Lithium'
        atomicWeight = 7
        group = 'Alkali metals'
    elif symbol == 'Na':
        name = 'Sodium'
        atomicWeight = 23
        group = 'Alkali metals'
    elif symbol == 'K':
        name = 'Potassium'
        atomicWeight = 40
        group = 'Alkali metals'
    elif symbol == 'Rb':
        name = 'Rubidium'
        atomicWeight = 85.5
        group = 'Alkali metals'
    elif symbol == 'Cs':
        name = 'Cesium'
        atomicWeight = 133
        group = 'Alkali metals'
    elif symbol == 'Fr':
        name = 'Francium'
        atomicWeight = 223
        group = 'Alkali metals'

    elif symbol == 'He':
        name = 'Helium'
        atomicWeight = 4
        group = 'Noble gases'
    elif symbol == 'Ne':
        name = 'Neon'
        atomicWeight = 20
        group = 'Noble gases'
    elif symbol == 'Ar':
        name = 'Argon'
        atomicWeight = 40
        group = 'Noble gases'
    elif symbol == 'Kr':
        name = 'Krypton'
        atomicWeight = 84
        group = 'Noble gases'
    elif symbol == 'Xe':
        name = 'Xenon'
        atomicWeight = 131
        group = 'Noble gases'
    elif symbol == 'Rn':
        name = 'Radon'
        atomicWeight = 222
        group = 'Noble gases'

    print("Element:", name, "(", symbol, ")")
    print("Atomic weight:", atomicWeight)
    print("Group:", group, "\n")