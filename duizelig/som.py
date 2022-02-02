#Tel de cijfers vanaf 50 totdat hun gezamelijke som groter is dan 1000, print elk cijfer en de totale som per iteratie.

cijfer = 50
som = 0
while som < 1000:
    som += cijfer
    print(cijfer,som)
    cijfer += 1