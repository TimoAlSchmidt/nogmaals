#Vraag een dag van de week op (ma,di,wo,do,vr,za,zo) Print alle dagen tot en met de opgegeven dag.

dagen = {
    "ma" : 1,
    "di" : 2,
    "wo" : 3,
    "do" : 4,
    "vr" : 5,
    "za" : 6,
    "zo" : 7
}

while True:
    print("Welke dag? [ma/di/wo/do/vr/za/zo]")
    dag = input()
    if dag not in dagen:
        print("A.U.B. een dag invullen.")
        continue
    else:
        print()
        for i in range(dagen[dag]):
            print(list(dagen.keys())[i])
        break

