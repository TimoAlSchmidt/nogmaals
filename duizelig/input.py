#Herhaal een input() tot het resultaat daarvan gelijk is aan ‘quit’. Print het aantal iteraties per iteratie. (Het aantal keren dat de vraag is gesteld)
woord = ""
o = 0
while woord != "quit":
    print("quit?",o)
    woord = input()
    o += 1